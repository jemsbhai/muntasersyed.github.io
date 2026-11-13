#!/usr/bin/env python3
"""Validate this static site's crawlable HTML, links, and structured metadata.

Run with Python 3.10+; no dependencies or network access are required.
An optional --root directory can point at a built site instead of the source.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


SITE = "https://muntasersyed.com/"
VOID_TAGS = set("area base br col embed hr img input link meta param source track wbr".split())
BLOCK_TAGS = set("address article aside blockquote div dl fieldset figure footer form h1 h2 h3 h4 h5 h6 header hr main nav ol p pre section table ul".split())
JSONLD_KEYWORDS = set("@base @container @context @direction @graph @id @import @included @index @json @language @list @nest @none @prefix @propagate @protected @reverse @set @type @value @version @vocab".split())
PAGE_TYPES = {"WebPage", "CollectionPage", "ProfilePage"}


@dataclass
class Element:
    tag: str
    attrs: dict[str, str]
    line: int
    content: list = field(default_factory=list)

    def text(self) -> str:
        return "".join(x.text() if isinstance(x, Element) else x for x in self.content)

    def has_class(self, name: str) -> bool:
        return name in self.attrs.get("class", "").split()


class Document(HTMLParser):
    def __init__(self, source: str):
        super().__init__(convert_charrefs=True)
        self.elements: list[Element] = []
        self.stack: list[Element] = []
        self.errors: list[tuple[int, str]] = []
        self.feed(source)
        self.close()
        if self.stack:
            self.errors.append((self.stack[-1].line, "unclosed elements: " + ", ".join(e.tag for e in self.stack)))

    def handle_starttag(self, tag, attrs):
        node = Element(tag, {k: v or "" for k, v in attrs}, self.getpos()[0])
        ancestors = [e.tag for e in self.stack]
        if tag in BLOCK_TAGS and "p" in ancestors:
            self.errors.append((node.line, f"block element <{tag}> must not be nested inside <p>"))
        if tag in {"a", "button", "form"} and tag in ancestors:
            self.errors.append((node.line, f"<{tag}> must not be nested inside another <{tag}>"))
        self.elements.append(node)
        if self.stack:
            self.stack[-1].content.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index].tag == tag:
                if index != len(self.stack) - 1:
                    self.errors.append((self.getpos()[0], f"</{tag}> closes before </{self.stack[-1].tag}>"))
                del self.stack[index:]
                break
        else:
            self.errors.append((self.getpos()[0], f"unexpected closing tag </{tag}>"))

    def handle_data(self, data):
        if self.stack:
            self.stack[-1].content.append(data)

    def find(self, tag=None, **attrs):
        return [e for e in self.elements if (tag is None or e.tag == tag)
                and all(e.attrs.get(k) == v for k, v in attrs.items())]


def walk_json(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_json(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_json(child)


def unique_json_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def canonical_for(path: str) -> str:
    return urljoin(SITE, path[:-10] if path.endswith("index.html") else path)


class Validator:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.errors: list[str] = []
        self.documents: dict[str, Document] = {}
        self.nodes: list[tuple[str, dict]] = []
        self.page_dates: dict[str, str] = {}
        self.internal_links = 0

    def fail(self, location, message):
        self.errors.append(f"{location}: {message}")

    def read(self, path):
        try:
            return (self.root / path).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            self.fail(path, str(error))
            return ""

    def local_reference(self, source, value, location, *, fragment=True):
        target = urlsplit(urljoin(canonical_for(source), value))
        if target.scheme not in {"http", "https"} or target.hostname != urlsplit(SITE).hostname:
            return
        self.internal_links += 1
        relative = unquote(target.path).lstrip("/")
        if not relative or relative.endswith("/"):
            relative += "index.html"
        file = (self.root / relative).resolve()
        if not file.is_relative_to(self.root) or not file.is_file():
            self.fail(location, f"local destination does not exist: {value}")
        elif fragment and target.fragment and relative in self.documents:
            ids = {e.attrs.get("id") for e in self.documents[relative].elements}
            if unquote(target.fragment) not in ids:
                self.fail(location, f"local anchor does not exist: {value}")

    def html(self):
        # Skip maintenance/build directories; the public site may add nested pages.
        for file in sorted(self.root.rglob("*.html")):
            relative = file.relative_to(self.root)
            if any(part.startswith((".", "_")) or part in {"tmp", "scripts", "node_modules"}
                   for part in relative.parts[:-1]):
                continue
            name = relative.as_posix()
            self.documents[name] = Document(self.read(name))
        if not self.documents:
            self.fail(self.root, "no HTML pages found")
        for name, doc in self.documents.items():
            for line, message in doc.errors:
                self.fail(f"{name}:{line}", message)
            html = doc.find("html")
            if len(html) != 1 or not html[0].attrs.get("lang", "").strip():
                self.fail(name, "one html element with a language is required")
            for tag in ("title", "h1"):
                found = doc.find(tag)
                if len(found) != 1 or not found[0].text().strip():
                    self.fail(name, f"exactly one nonempty {tag} is required")
            descriptions = doc.find("meta", name="description")
            if len(descriptions) != 1 or not descriptions[0].attrs.get("content", "").strip():
                self.fail(name, "exactly one nonempty meta description is required")
            canonicals = doc.find("link", rel="canonical")
            canonical = canonical_for(name)
            if len(canonicals) != 1 or canonicals[0].attrs.get("href") != canonical:
                self.fail(name, f"canonical must be {canonical}")
            og_urls = doc.find("meta", property="og:url")
            if len(og_urls) != 1 or og_urls[0].attrs.get("content") != canonical:
                self.fail(name, "og:url must match the canonical URL")
            for meta in doc.find("meta"):
                if meta.attrs.get("name", "").lower() in {"robots", "googlebot", "bingbot"}:
                    directives = re.split(r"[\s,]+", meta.attrs.get("content", "").lower())
                    if "noindex" in directives or "none" in directives:
                        self.fail(f"{name}:{meta.line}", "public page must not be noindex")
            ids = Counter(e.attrs["id"] for e in doc.elements if "id" in e.attrs)
            for ident, count in ids.items():
                if not ident or count > 1:
                    self.fail(name, f"empty or duplicate HTML id: {ident!r}")
            for node in doc.elements:
                for attribute in ("href", "src", "poster"):
                    if attribute in node.attrs:
                        self.local_reference(name, node.attrs[attribute], f"{name}:{node.line}")
            scripts = doc.find("script", type="application/ld+json")
            if not scripts:
                self.fail(name, "missing JSON-LD")
            for script in scripts:
                try:
                    data = json.loads(script.text(), object_pairs_hook=unique_json_keys)
                except (ValueError, TypeError) as error:
                    self.fail(f"{name}:{script.line}", f"invalid JSON-LD: {error}")
                    continue
                if not isinstance(data, dict) or data.get("@context") not in ("https://schema.org", "https://schema.org/"):
                    self.fail(name, "HTML JSON-LD must use the standard Schema.org context")
                for node in walk_json(data):
                    self.nodes.append((name, node))
                    unknown = [key for key in node if key.startswith("@") and key not in JSONLD_KEYWORDS]
                    if unknown:
                        self.fail(name, f"nonstandard JSON-LD keywords in public HTML: {unknown}")
            page_nodes = [node for source, node in self.nodes if source == name
                          and node.get("@id") == canonical + "#webpage"
                          and isinstance(node.get("@type"), str) and node["@type"] in PAGE_TYPES]
            if len(page_nodes) != 1:
                self.fail(name, "exactly one typed #webpage entity is required")
            else:
                page = page_nodes[0]
                if page.get("url") != canonical:
                    self.fail(name, "page entity URL must match its canonical")
                modified = page.get("dateModified", "")
                try:
                    date.fromisoformat(modified)
                except (ValueError, TypeError):
                    self.fail(name, "page dateModified must be an ISO calendar date")
                self.page_dates[canonical] = modified

    def metadata(self):
        definitions = {node["@id"] for _, node in self.nodes if "@id" in node and "@type" in node}
        versions = defaultdict(set)
        for name, node in self.nodes:
            ident = node.get("@id", "")
            if isinstance(ident, str) and ident.startswith(SITE) and ident not in definitions:
                self.fail(name, f"undefined local JSON-LD entity: {ident}")
            version_identity = ident or node.get("url")
            if isinstance(version_identity, str) and "version" in node:
                versions[version_identity].add(str(node["version"]))
            if node.get("@type") == "ItemList":
                items = node.get("itemListElement", [])
                if not isinstance(items, list):
                    self.fail(name, f"{ident}: itemListElement must be a list")
                    continue
                if node.get("numberOfItems") != len(items):
                    self.fail(name, f"{ident}: numberOfItems differs from itemListElement length")
                positions = [item.get("position") if isinstance(item, dict) else None for item in items]
                if positions != list(range(1, len(items) + 1)):
                    self.fail(name, f"{ident}: list positions must be consecutive starting at 1")
                # These catalogs have one visible card for each metadata entry.
                card_class = {"research.html#publications": "catalog-item",
                              "media.html#coverage": "catalog-item",
                              "speaking.html#engagements": "timeline-item",
                              "speaking.html#selected-recordings": "recording-card"}.get(ident.removeprefix(SITE))
                if card_class:
                    count = sum(e.has_class(card_class) for e in self.documents[name].elements)
                    if count != len(items):
                        self.fail(name, f"{ident}: {count} visible cards differ from {len(items)} metadata items")
            if node.get("@type") == "Event" and "startDate" in node:
                try:
                    start = datetime.fromisoformat(node["startDate"].replace("Z", "+00:00"))
                    if "endDate" in node:
                        end = datetime.fromisoformat(node["endDate"].replace("Z", "+00:00"))
                        if end < start:
                            self.fail(name, f"event ends before it starts: {node.get('name', ident)}")
                except (ValueError, TypeError, AttributeError):
                    self.fail(name, f"invalid or inconsistent event dates: {node.get('name', ident)}")
        for ident, values in versions.items():
            if len(values) > 1:
                self.fail(ident, f"conflicting versions across page entities: {sorted(values)}")
        for file in sorted((self.root / "structured-data").glob("*.jsonld")):
            try:
                json.loads(self.read(file.relative_to(self.root)), object_pairs_hook=unique_json_keys)
            except (ValueError, TypeError) as error:
                self.fail(file.name, f"invalid standalone JSON-LD: {error}")

    def discovery(self):
        try:
            sitemap = ET.fromstring(self.read("sitemap.xml"))
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            entries = sitemap.findall("s:url", ns)
            urls = [entry.findtext("s:loc", default="", namespaces=ns) for entry in entries]
            if Counter(urls) != Counter(self.page_dates.keys()):
                missing = sorted(set(self.page_dates) - set(urls))
                extra = sorted(set(urls) - set(self.page_dates))
                duplicates = [url for url, count in Counter(urls).items() if count > 1]
                self.fail("sitemap.xml", f"page coverage differs: missing={missing}, extra={extra}, duplicates={duplicates}")
            for entry, url in zip(entries, urls):
                lastmod = entry.findtext("s:lastmod", default="", namespaces=ns)
                if url in self.page_dates and lastmod != self.page_dates[url]:
                    self.fail("sitemap.xml", f"lastmod differs from page dateModified: {url}")
        except ET.ParseError as error:
            self.fail("sitemap.xml", f"invalid XML: {error}")
        robots = self.read("robots.txt")
        directives = [line.split("#", 1)[0].strip() for line in robots.splitlines()]
        if not any(line.lower() == "user-agent: *" for line in directives):
            self.fail("robots.txt", "missing general crawler group")
        if any(re.fullmatch(r"disallow\s*:\s*/\*?", line, flags=re.I) for line in directives):
            self.fail("robots.txt", "site-wide crawler disallow would block indexing")
        if not any(re.fullmatch(r"sitemap\s*:\s*" + re.escape(SITE + "sitemap.xml"), line, flags=re.I) for line in directives):
            self.fail("robots.txt", "missing canonical sitemap URL")
        cname = self.root / "CNAME"
        if cname.exists() and self.read("CNAME").strip() != urlsplit(SITE).hostname:
            self.fail("CNAME", "custom domain differs from canonical host")
        # Optional agent discovery files are checked when present, including builds.
        for name in ("llms.txt", "llms-full.txt"):
            if (self.root / name).is_file():
                content = self.read(name)
                if not content.strip():
                    self.fail(name, "discovery file is empty")
                for line_number, line in enumerate(content.splitlines(), 1):
                    for link in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", line):
                        self.local_reference(name, link, f"{name}:{line_number}")

    def run(self):
        self.html()
        self.metadata()
        self.discovery()
        if self.errors:
            for error in self.errors:
                print(f"ERROR {error}", file=sys.stderr)
            print(f"Validation failed: {len(self.errors)} issue(s).", file=sys.stderr)
            return 1
        print(f"Validated {len(self.documents)} pages, {self.internal_links} local references, "
              "JSON-LD entities and catalog counts, sitemap dates, and crawler discovery.")
        return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    return Validator(args.root).run()


if __name__ == "__main__":
    raise SystemExit(main())

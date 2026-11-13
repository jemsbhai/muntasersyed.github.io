#!/usr/bin/env python3
"""Generate public Markdown and JSON-LD companions from the HTML source pages."""

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://muntasersyed.com/"


class PageReader(HTMLParser):
    """Keep the main content and links, excluding interactive control chrome."""

    def __init__(self, url):
        super().__init__(convert_charrefs=True)
        self.url = url
        self.main = False
        self.skip = 0
        self.parts = []
        self.links = []
        self.pre = False
        self.schema = []
        self.schema_parts = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.schema_parts = []
        if tag == "main":
            self.main = True
        if not self.main:
            return
        void = tag in {"br", "img", "input", "hr", "source", "wbr"}
        if self.skip:
            if not void:
                self.skip += 1
            return
        if (tag in {"button", "script", "style", "noscript", "form"}
                or "hidden" in attrs or "data-empty-state" in attrs
                or "data-results-status" in attrs or attrs.get("aria-hidden") == "true"):
            if not void:
                self.skip = 1
            return
        if re.fullmatch(r"h[1-6]", tag):
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag in {"section", "article", "p", "blockquote", "figure", "div"}:
            self.parts.append("\n\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "br":
            self.parts.append(" ")
        elif tag == "pre":
            self.pre = True
            self.parts.append("\n\n```text\n")
        elif tag == "code" and not self.pre:
            self.parts.append("`")
        elif tag == "a":
            self.links.append(urljoin(self.url, attrs.get("href", "")))
            self.parts.append("[")
        elif tag == "img" and attrs.get("alt"):
            self.parts.append("![" + attrs["alt"] + "](" + urljoin(self.url, attrs.get("src", "")) + ")")

    def handle_endtag(self, tag):
        if tag == "script" and self.schema_parts is not None:
            self.schema.append(json.loads("".join(self.schema_parts)))
            self.schema_parts = None
        if not self.main:
            return
        if self.skip:
            self.skip -= 1
            return
        if tag == "main":
            self.main = False
        elif re.fullmatch(r"h[1-6]", tag) or tag in {"section", "article", "p", "div", "blockquote", "figure", "ul", "ol"}:
            self.parts.append("\n\n")
        elif tag == "pre":
            self.parts.append("\n```\n\n")
            self.pre = False
        elif tag == "code" and not self.pre:
            self.parts.append("`")
        elif tag == "a" and self.links:
            self.parts.append("](" + self.links.pop() + ") ")
        elif tag in {"span", "time", "cite", "strong", "small"}:
            self.parts.append(" ")

    def handle_data(self, data):
        if self.schema_parts is not None:
            self.schema_parts.append(data)
        if self.main and not self.skip:
            self.parts.append(data if self.pre else re.sub(r"\s+", " ", data))

    def markdown(self):
        text = "".join(self.parts)
        text = re.sub(r"[ \t]*\n[ \t]*", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def generated_files():
    for page in sorted(ROOT.glob("*.html")):
        url = BASE if page.stem == "index" else BASE + page.name
        reader = PageReader(url)
        reader.feed(page.read_text(encoding="utf-8"))
        if len(reader.schema) != 1:
            raise ValueError(f"{page.name}: expected exactly one JSON-LD graph")
        graph = reader.schema[0]
        modified = next(node["dateModified"] for node in graph["@graph"]
                        if node.get("@id") == url + "#webpage")
        markdown = f"Source: [{url}]({url})\n\nUpdated: {modified}\n\n" + reader.markdown()
        yield page.with_suffix(".md"), markdown
        yield ROOT / "structured-data" / f"{page.stem}.jsonld", json.dumps(graph, ensure_ascii=False, indent=2) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are missing or stale")
    args = parser.parse_args()
    stale = []
    count = 0
    for path, content in generated_files():
        count += 1
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if stale:
        raise SystemExit("Stale discovery files: " + ", ".join(stale) + ". Run python scripts/build_discovery.py")
    print(f"{'Checked' if args.check else 'Generated'} {count} discovery files")


if __name__ == "__main__":
    main()

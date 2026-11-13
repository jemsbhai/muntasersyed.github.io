# muntasersyed.com

Personal research portfolio for Muntaser Syed, published with GitHub Pages.

The site includes publications, major open-source software
families, research repositories, both Devpost portfolios, a dated speaking
archive, professional service, selected awards, press, and public profiles.

## Pages

- `index.html`: overview and featured work
- `research.html`: deduplicated papers, preprints, and research artifacts
- `software.html`: major software families and language ports
- `hashrope.html`: focused Hashrope guide, packages, research, and demonstrations
- `pollard.html`: focused Pollard guide, language runtimes, research, and materials
- `projects.html`: research repositories, software, Devpost portfolios, and selected awards
- `speaking.html`: presentation videos, talks, workshops, lectures, podcasts, and teaching materials
- `media.html`: dated media coverage, interviews, university news, and organizer or sponsor reports
- `about.html`: biography, roles, education, professional service, press, milestones, and profile links

## Current catalog - November 13, 2026

The research catalog contains 47 distinct scholarly outputs: 20 published
works and 25 accepted works. Six works also have preprints; these categories
overlap. Beyond FLOPs is published in the ACM AI Leadership Summit proceedings,
with DOI 10.1145/3806096.3844801. CryptEpi was presented at TML4DM on November 12.
KVRM is accepted at COMNETSAT 2026.

The site includes 36 selected project artifacts, 54 speaking engagements and
presentation entries, seven selected recordings, and 48 media entries.
New project entries include qfourierrope and Quantum Optimisation Circuit
Builder, with links to the circuit builder’s interactive demo. The recordings
include qhashrope, ReleaseProof, and swarm-forest demonstrations
alongside Hashrope at DevFest Florida, AASN, CloudCom, and CorpusKit.

The software catalog covers 27 top-level works and 38 package distributions:
25 PyPI packages, six npm packages, six Rust crates, and one Maven artifact.
Registry versions were rechecked on November 13, including Epicormic 0.2.0,
Hashrope Bio 0.3.4, and Hashrope's Python, JavaScript, Rust, and Java 0.3.4
releases. Hashrope links to its interactive demo and related projects.

Upcoming events include the November 14 DevFest Tampa workshop, November 21
IEEE Smart City USA talk, December 3–5 COMNETSAT,
December 5 DevFest Miami workshop, December 14–17 ComComAp, and the FLAIRS-40
call for papers. About includes AAAI-27 AISI program-committee service and
ICML AI4GOOD and ICMLA reviewer service.

The November 5 refresh added 19 presentation decks across Speaking, Research,
Software, and Projects. Conference groups expose individual paper anchors
alongside papers, code, packages, and recordings. SQT-IoT links to its slides.

See `CONTENT_AUDIT.md` for refresh history and source references. `AGENTS.md`
records the standing preference to present the work confidently as papers,
presentations, and talks.

## Structured data

Each HTML page includes a Schema.org JSON-LD graph with stable identifiers for
the site, author, page, and page-specific research or software entities. The
search-engine-facing graphs intentionally use only standard Schema.org terms.

`structured-data/jsonld-ex.jsonld` is a linked JSON-LD Ex representation that
provides extension annotations for compatible research tooling.

Each page also links a standard Schema.org download in `structured-data/`
and a Markdown companion containing its main content. `llms.txt` maps these
resources to the portfolio’s topics. The HTML remains the canonical source.
The sitemap lists only the canonical HTML pages.

## Publishing and maintenance

GitHub Pages builds `main` with Jekyll. `_config.yml` excludes `AGENTS.md`,
`CONTENT_AUDIT.md`, `README.md`, `scripts`, and `tmp` from the published artifact while
keeping maintenance records in this repository.

After editing HTML, regenerate the discovery files and validate before pushing:

```sh
python scripts/build_discovery.py
python scripts/build_discovery.py --check
python scripts/validate_site.py
node --check assets/site.js
```

The validation workflow runs these checks for pushes and pull requests. The
Jekyll configuration disables optional front matter conversion so generated
Markdown files are copied as static companions and cannot replace HTML pages.

The November 10 discovery update gives all 47 research cards stable anchors
and completes catalog entity identifiers and citation references. Preserve
existing anchors and graph identities when updating or moving content.

Keep the Hashrope and Pollard guides consistent with `software.html` when
updating package versions, capabilities, or research status. Their visible
package dates record the registry check; per-language versions stay independent.
Update page metadata and the sitemap together. Verify the Jekyll output,
internal links, structured data, and mobile behavior with and without
JavaScript before publishing shared navigation changes.

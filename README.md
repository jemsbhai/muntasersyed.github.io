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

## Current catalog — November 9, 2026

The research catalog contains 47 distinct scholarly outputs: 19 published
works and 26 accepted works. Six works also have preprints; these categories
overlap. KVRM is accepted at COMNETSAT 2026. CryptEpi's TML4DM presentation
is scheduled for November 12, 11:40–11:55 a.m. in the Paris Room, Shenyang
(UTC+8).

The site includes 34 selected project artifacts, 53 speaking engagements and
presentation entries, seven selected recordings, and 48 media entries.
New project entries cover ReleaseProof, qhashrope, swarm-forest, Tidepath,
and greenroom. The recordings include their three project demonstrations
alongside Hashrope at DevFest Florida, AASN, CloudCom, and CorpusKit.

The software catalog covers 27 top-level works and 38 package distributions:
25 PyPI packages, six npm packages, six Rust crates, and one Maven artifact.
Registry versions were rechecked on November 9, including Epicormic 0.2.0,
Hashrope Bio 0.3.4, and Hashrope's Python, JavaScript, Rust, and Java 0.3.4
releases. Hashrope links to its interactive demo and related projects.

Upcoming events include the November 12 TML4DM workshop, November 14 DevFest
Tampa talk, November 21 IEEE Smart City USA talk, December 3–5 COMNETSAT,
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

## Publishing and maintenance

GitHub Pages builds `main` with Jekyll. `_config.yml` excludes `AGENTS.md`,
`CONTENT_AUDIT.md`, `README.md`, and `tmp` from the published artifact while
keeping maintenance records in this repository.

The November 10 discovery update gives all 47 research cards stable anchors
and completes catalog entity identifiers and citation references. Preserve
existing anchors and graph identities when updating or moving content.

Keep the Hashrope and Pollard guides consistent with `software.html` when
updating package versions, capabilities, or research status. Their visible
package dates record the registry check; per-language versions stay independent.
Update page metadata and the sitemap together. Verify the Jekyll output,
internal links, structured data, and mobile behavior with and without
JavaScript before publishing shared navigation changes.

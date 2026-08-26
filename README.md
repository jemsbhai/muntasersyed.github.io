# muntasersyed.com

Personal research portfolio for Muntaser Syed, published with GitHub Pages.

The site includes a verified publication record, major open-source software
families, research repositories, both Devpost portfolios, a dated speaking
archive, professional service, selected awards, press, and public profiles.

## Pages

- `index.html`: overview and featured work
- `research.html`: deduplicated papers, preprints, and research artifacts
- `software.html`: major software families and language ports
- `projects.html`: research repositories, source-stage builds, Devpost portfolios, and selected awards
- `speaking.html`: verified talks, workshops, lectures, podcasts, and teaching materials
- `about.html`: biography, roles, education, professional service, press, milestones, and profile links

Content and registry records were last reconciled against primary sources on
August 26, 2026. See `CONTENT_AUDIT.md` for counts, evidence boundaries,
deliberate holdbacks, and the next refresh checklist.

## Structured data

Each HTML page includes a Schema.org JSON-LD graph with stable identifiers for
the site, author, page, and page-specific research or software entities. The
search-engine-facing graphs intentionally use only standard Schema.org terms.

`structured-data/jsonld-ex.jsonld` is a separately linked experimental JSON-LD
Ex representation. Keeping it separate lets compatible research tooling inspect
the extension annotations without risking the standard search markup.

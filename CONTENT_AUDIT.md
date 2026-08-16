# Content audit — August 16, 2026

This file records the maintenance boundary behind the public site. The August
2026 review reconciled the repository against DOI/Crossref and publisher
records, arXiv, IEEE Xplore, official conference programs, PyPI, npm,
crates.io, GitHub, Sessionize, organizer event pages, and institutional news.

## Published state

- Research: 13 peer-reviewed full publications, 4 standalone preprints, and 1
  proceedings poster abstract. Earlier versions and duplicate preprint/published
  pairs are counted once.
- Software: 22 featured published PyPI packages, 4 npm packages, and 5 Rust crates.
  `i3cex` is a development release and `facecloak-suite` is a placeholder, so
  neither is included in the featured PyPI total. Package maturity ranges from
  pre-alpha through production/stable and is not implied by this count.
- Projects: public repositories link directly. Private repositories are either
  labeled as private research without a link or omitted from the public index.
- Speaking: dated entries require an organizer, conference, institutional, or
  public scheduling record. Material-only repositories are kept in a separate
  teaching archive.

## Deliberate holdbacks and owner follow-ups

- WVLL 2026 currently publishes conflicting November and December dates and a
  stale NVIDIA/“Dr.” bio. The site identifies the program-listed keynote but
  withholds the date until the organizer confirms the event details.
- Public sources disagree about Ph.D. timing and do not establish conferral.
  The site says “doctoral work” and does not use “Dr.” Pending owner confirmation.
- TraceCoder’s accepted status follows the author-maintained comment on
  [arXiv:2607.26307](https://arxiv.org/abs/2607.26307). Replace or supplement
  that link with the proceedings record when AGENTICS publishes it.
- Fourteen repositories linked by the previous site were private at review time:
  `cryptepi`, `explainiverse-explorer`, `hashrope-paper`,
  `healthSLnetwrokslicer`, `IEEEHealth-pharma`, `imujepa`, `jepa-fhir`,
  `kvrm-paper`, `oneura-ictai2026`, `thermocline`, `TimeCMAPlus`,
  `TOMLSignals`, `trilstm`, and `uhc-visualizer`. Re-add links only after
  confirming public visibility.
- ORCID contains namesake records, duplicates, and misclassified service. Clean
  the profile manually before using its displayed count. OpenAlex also splits
  the author record across two profiles and should be merged.
- Recent awards supported only by social posts were not promoted to the curated
  awards section. Add them when an organizer result page or owner-supplied
  evidence is available.

## Refresh checklist

1. Reconcile Crossref/DOI, arXiv, IEEE Xplore, and conference proceedings;
   deduplicate manuscript and version-of-record pairs.
2. Compare the PyPI, npm, and crates.io profiles; preserve independently
   versioned language ports instead of assigning one family-wide version.
3. Check every linked GitHub repository as a signed-out/public visitor and keep
   pre-alpha, preview, and stable claims aligned with each README.
4. Recheck Sessionize plus official organizer schedules for speaking dates,
   titles, cancellations, and venue changes.
5. Update `sitemap.xml`, structured data, visible review dates, and this audit
   record together.

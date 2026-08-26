# Content audit — August 26, 2026

This file records the maintenance boundary behind the public site. The August
2026 review reconciled the repository against DOI/Crossref and publisher
records, arXiv, IEEE Xplore, official conference programs, PyPI, npm,
crates.io, GitHub, Sessionize, organizer event pages, and institutional news.

## August 26 research delta

- Added the August 25 arXiv preprint [Rules Before Oracles: Auditable,
  User-Configurable Argument Selection for Deliberative
  Polling](https://arxiv.org/abs/2608.23979).
- Added three conference-verified accepted or forthcoming papers: TOML Signals
  at IEEE MLSP 2026, MultiSpecQR at IEEE ICMLA 2026, and Epistemic Edge at
  IEEE IRI 2026. The existing Chronofy preprint is also now linked to its
  official IEEE IRI program listing.
- Added TOML Signals after its repository became public, with the MLSP schedule,
  OpenReview record, reproducibility data, and profiler traces.
- Added the IEEE IRI appearances to the speaking archive. Also added the
  independently reported Fresh Fridge third-place result, the AWE Nite Orlando
  directory listing, and the source-stage Joulehound collaboration.

## Published state

- Research: 13 published peer-reviewed full papers, 3 accepted/forthcoming
  papers without a separate public preprint, 5 public preprints, and 1
  proceedings poster abstract, for 22 scholarly outputs. TraceCoder and
  Chronofy remain counted as public preprints while their conference status is
  recorded separately. Earlier versions and duplicate preprint/published pairs
  are counted once.
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
- The official programs or accepted-paper lists establish the current status of
  Chronofy, Epistemic Edge, MultiSpecQR, and TOML Signals, but no IEEE Xplore
  version-of-record or DOI was found. Replace the program links when proceedings
  records publish.
- The repository linked from the Rules Before Oracles arXiv record (`devfitcs/ABAS`)
  returned 404 for a signed-out visitor, so the site does not expose a code link.
- Thirteen repositories linked by the previous site were private at review time:
  `cryptepi`, `explainiverse-explorer`, `hashrope-paper`,
  `healthSLnetwrokslicer`, `IEEEHealth-pharma`, `imujepa`, `jepa-fhir`,
  `kvrm-paper`, `oneura-ictai2026`, `thermocline`, `TimeCMAPlus`, `trilstm`,
  and `uhc-visualizer`. Re-add links only after
  confirming public visibility.
- The public `jsonld-ex-experiments` README describes the repository as private
  and says it must not be public. Its portfolio link was removed; the owner
  should review the repository’s visibility and contents directly.
- ORCID contains namesake records, duplicates, and misclassified service. Clean
  the profile manually before using its displayed count. OpenAlex also splits
  the author record across two profiles and should be merged.
- Recent awards supported only by social posts remain outside the curated awards
  section. Fresh Fridge was added only after an independent result report named
  the team, placement, and participants.

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

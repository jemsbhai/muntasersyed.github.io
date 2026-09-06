# Content audit — September 6, 2026

This file records the maintenance boundary behind the public site. The August
2026 review reconciled the repository against DOI/Crossref and publisher
records, arXiv, IEEE Xplore, official conference programs, PyPI, npm,
crates.io, GitHub, Sessionize, organizer event pages, and institutional news.

## September 6 refresh

- Rechecked all 22 featured PyPI packages, 4 npm packages, and 5 Rust crates.
  Updated [Explainiverse to 0.15.2](https://pypi.org/project/explainiverse/0.15.2/)
  (September 4) and [Pollard to 1.6.0](https://pypi.org/project/pollard/1.6.0/)
  (September 1). The other featured versions still match their registries.
  Latest-release cards now list Explainiverse, Pollard, and Chronofy in order.
- Represented ctxmaster, Hashrope, and hashrope-bio language ports separately
  in structured data, preserving their independent versions.
- Added MultiSpecQR's October 5, 11:00 presentation slot, Special Session 1A
  (SS1-A), from the [official ICMLA page](https://www.icmla-conference.org/icmla26/ss1regularpapers.html)
  to the research record. The named presenter remains unconfirmed, so this
  does not establish a personal speaking engagement.
- Corrected WVLL's name to International Winter Conference on Vision,
  Language & Learning using its [official homepage](https://wvll.github.io/).
  The conflicting event dates remain unresolved.
- No newer arXiv manuscript or matching proceedings DOI was found for the
  outstanding research records. Scholarly-output and package totals are unchanged.
- Fixed research filtering, added accessible result feedback, and included
  TraceCoder in both Accepted and Preprint filters without duplicating its
  scholarly count. Filters can overlap; the totals below remain deduplicated.
- Made theme persistence optional when browser storage is blocked, exposed
  all homepage software-card links, added responsive offsets for deep links,
  and improved text contrast in both themes.
- Removed nine unsupported Schema.org `EventCompleted` values. Past event
  dates remain recorded; no replacement completion status is invented.

The September refresh checked the site's six pages, shared assets, internal
links, JSON-LD, and responsive behavior. Devpost counts retain their explicit
August 26 observation dates; they were not re-counted in this refresh.

Validation after the approved changes:

- Chromium checked all six pages at 1440, 768, 390, and 320 pixels without
  horizontal overflow or broken images.
- Automated WCAG A/AA checks with axe-core 4.13.0 reported no violations
  across all six pages in light and dark themes at desktop and mobile widths.
  These automated checks are not a substitute for a full accessibility review.
- Browser checks covered filtering and result announcements, blocked storage
  reads and writes, menu behavior, theme persistence, exposed card links, and
  unobscured deep links. Firefox also passed filtering and desktop/mobile
  deep-link checks.
- Internal references resolve, JSON-LD parses, catalog totals agree with the
  visible records, and the changed layouts were inspected in screenshots.

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

- The public [FLAIRS-40 track site](https://jemsbhai.github.io/flairs40-tracks/)
  names Muntaser as co-chair, but approval of the specific track needs owner
  confirmation before inclusion in professional service.
- The new [1-bit IoT router repository](https://github.com/jemsbhai/1bit-llm-iot-router)
  contains only a README. It does not establish a released implementation or
  accepted-paper status; both require further evidence before inclusion.
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

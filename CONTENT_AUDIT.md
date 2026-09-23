# Content audit — September 23, 2026

This file records the maintenance boundary behind the public site. The August
2026 review reconciled the repository against DOI/Crossref and publisher
records, arXiv, IEEE Xplore, official conference programs, PyPI, npm,
crates.io, GitHub, Sessionize, organizer event pages, and institutional news.

## September 23 Opera Map addition

- Added Opera Map to the Projects awards and About milestones for 2019, with
  matching Person award metadata on the homepage and About page.
- San Diego Opera’s [official August 20, 2020 press release](https://sdoperastg.wpengine.com/wp-content/uploads/2022/09/Opera-Hack-Winner-Presentations.pdf)
  names Muntaser Syed on the team and confirms $13,500 in development funding.
  The release describes a July 2019 win; 2020 is the follow-up presentation year.
- The [original event listing](https://opera-hack.devpost.com/) establishes
  July 27–28, 2019 at Microsoft in La Jolla. Project manager Angel Mannion’s
  [event history](https://opera-innovation.squarespace.com/oi-insights/hacking-opera-in-san-diego)
  confirms this was the inaugural Opera Hack.
- Copy credits a team win, one of three selected projects, without claiming
  first place, sole authorship, or a personal $13,500 prize. Removed “recent”
  from the awards introduction to accommodate the historical entry.
- Updated sitemap modification dates only for the three affected HTML pages.
- Validated JSON-LD on all three changed pages and checked both new entries
  at 1440px and 390px: no horizontal overflow, duplicate IDs, or JavaScript
  errors. Reviewed rendered entries and confirmed the official PDF returns 200.

## September 15 refresh

- Added Tim Green's September 2 [SmarterArticles analysis](https://smarterarticles.co.uk/the-exported-thirst-how-ai-drinks-water-india-cannot-spare)
  of the Environmental Cost of Digital Sovereignty paper to the homepage,
  press section, and research record. The author identifies as a UK-based
  independent technology writer; this is coverage of the research, not an
  interview or a claim of coverage by the other outlets his essay cites.
- Promoted [Chronofy](https://doi.org/10.1109/IRI69576.2026.00090) and
  [Epistemic Edge](https://doi.org/10.1109/IRI69576.2026.00017) to published
  IEEE IRI proceedings papers. IEEE registered both DOI records on September 9.
  Their bibliographic publication date is July 2026, with month precision;
  the registration date is not presented as the publication date.
- Reconciled research to 15 published peer-reviewed outputs, 21 accepted
  contributions, four preprints awaiting publication, and 38 distinct outputs.
  Earlier arXiv versions remain linked from published work. The preprint
  filter now explicitly covers work awaiting publication; it does not count
  published work again merely because an earlier manuscript is on arXiv.
- Added the organizer-verified [September 17 HuggingFace session](https://luma.com/uuapbq7w)
  as a scheduled talk at Miami Dade College, 7:30–7:50 p.m. Eastern, with
  corresponding event metadata. The homepage and speaking page feature it.
- Added the new public [HIPAA compliance research repository](https://github.com/jemsbhai/hipaa-compliance-algebra)
  and [Station Steward prototype](https://github.com/jemsbhai/station-steward).
  Also added the [Dreamland controller](https://github.com/jemsbhai/dreamland-rpi)
  with artwork credit to Tec/Tec Fase, and linked CorpusKit's setup/demo docs.
  These source artifacts do not increase package or publication totals.
- Removed Corpusgen's temporary ISCA validation-book link after it began
  returning 404. Accepted Show & Tell status and the paper-specific author
  list are retained; no final ISCA proceedings record was verified.
- Added TOML Signals' October 1, 1–3 p.m. Eastern poster slot to its research
  entry, matching the existing speaking record and the current MLSP schedule.
  A paper schedule alone does not identify the presenting author.
- Rechecked all 22 featured PyPI packages, four npm packages, and five Rust
  crates against current registry APIs; all versions still match. The five
  2026 arXiv manuscripts remain v1. No additional distinct scholarly output
  was established. All 45 previously linked GitHub repositories were public.
- Devpost snapshots still show the existing counts, but fresh direct reads
  were blocked. Their August 26 observation dates are retained.
- Expanded the WVLL follow-up to cover current keynote status as well as
  conflicting dates. FLAIRS-40 track approval and social-only award candidates
  remain outside the confirmed additions.

Validation covered all six pages at 1440, 768, 390, and 320 pixels in both
themes (48 layout checks), with no horizontal overflow or broken images.
All 24 axe-core 4.13.0 page/theme/width checks passed for WCAG 2 A/AA and
WCAG 2.1 AA rules. JSON-LD parses, list totals and positions agree, and all
120 internal page, fragment, and asset references resolve. Research filters
return 15 published, 21 accepted, four pending preprints, and 38 total records.
Search, empty results, new research deep links, mobile navigation, and theme
controls passed; no page JavaScript errors were observed. Desktop and mobile
screenshots were reviewed. Detailed test artifacts remain outside this repo.

## September 7 publication reconciliation

- Added 16 accepted 2026 scholarly records across IEEE CloudCom, ICTAI,
  WF-IoT, HealthCom, UEMCON, GHTC, AICCSA, ACM AI Summit, and Interspeech.
  These include full, regular, short, and main-track papers, one extended
  abstract, and one Show & Tell contribution. None is represented as a
  published version of record merely because it was accepted.
- Author lists follow each accepted manuscript or title-specific author
  record. In particular, Corpusgen's conference contribution has four
  authors; its software artifact has a different author list.
- Updated Chronofy and Epistemic Edge to accepted full and short papers,
  respectively. The official IRI program explicitly maps paper 42 to
  Chronofy and paper 161 to Epistemic Edge. Accessible proceedings previews
  are linked; assigned DOIs were not yet resolving at this review.
- Recorded GHTC acceptance for Environmental Cost and AGENTICS acceptance
  for Alternative-Based Information Systems. TraceCoder is an accepted short
  paper with poster presentation. Existing arXiv citations retain their
  version-specific titles and author order.
- Identified Counting Constraints as a published poster paper and completed
  the Springer Distil-BERT chapter title with “a Fine-Tuned Model.”
- Added the AHFE 2016 accepted abstract and NAECON 2018 accepted poster to
  historical research/speaking records, separate from published papers.
  Acceptance or a program listing does not by itself establish delivery.
- Updated related software/project descriptions, visible totals, filtering
  categories, standard JSON-LD, and sitemap dates. Acceptance evidence was
  approved by the owner; private correspondence and working audits are
  excluded from this public repository.

Validation covered all six pages at 1440, 768, 390, and 320 pixels; internal
links and anchors; catalog/JSON-LD agreement; filtering; and light/dark
accessibility. Three initial contrast flags disappeared when checks waited
for the theme change to render; settled-color checks and screenshots confirmed
readable links. All 67 distinct regression checks passed across the initial
run and focused rechecks, including the 24 page/theme/width axe checks.

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

- Research: 38 distinct scholarly outputs: 15 published peer-reviewed
  papers/chapters (including one poster paper), 21 accepted conference
  contributions, one preprint without conference acceptance, and one
  published 2018 poster abstract. Three accepted works also have public
  preprints, making four preprints awaiting publication in all. These filters
  overlap; earlier versions of published papers remain linked and are counted
  once. Two older presentation acceptances
  and software artifacts remain outside this scholarly total.
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
  names Muntaser as co-chair for Embodied AI Agents, Robotics, and IoT.
  Track notifications were due September 8; approval of this specific track
  still needs confirmation before inclusion in professional service.
- The [1-bit IoT router](https://github.com/jemsbhai/1bit-llm-iot-router)
  is confirmed accepted at IEEE WF-IoT 2026 and now has public source code.
  It is not presented as a stable package release. WF-IoT papers remain
  accepted while final manuscripts are being prepared.
- AASN is excluded from the accepted/forthcoming catalog; no current venue
  is asserted. The unidentified IRI record, NADIM/Chronofy disaster title,
  Universal Translator, and SQT version relationship remain held until
  bibliographic identity or status is established.
- WVLL 2026 currently publishes conflicting November and December dates and a
  stale NVIDIA/“Dr.” bio. Its homepage omits Muntaser from the confirmed and
  tentative invited-speaker lists while the older program lists his keynote.
  The site identifies the program-listed keynote but withholds the date until
  the organizer confirms both the invitation and event details. Omission from
  another page does not by itself establish cancellation.
- Public sources disagree about Ph.D. timing and do not establish conferral.
  The site says “doctoral work” and does not use “Dr.” Pending owner confirmation.
- TraceCoder’s accepted short-paper/poster status is confirmed by the owner’s
  acceptance record and the author-maintained comment on
  [arXiv:2607.26307](https://arxiv.org/abs/2607.26307). Replace or supplement
  that link with the proceedings record when AGENTICS publishes it.
- MultiSpecQR and TOML Signals retain their official accepted-paper/program
  sources pending final proceedings records. The two IRI DOI holdbacks were
  resolved on September 15 as documented above.
- Corpusgen retains its accepted Show & Tell status while a stable official
  paper record is awaited. Its temporary ISCA validation PDF now returns 404;
  the software Zenodo DOI is not a conference-paper DOI.
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

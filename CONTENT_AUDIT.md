# Content audit — October 9, 2026

This file records the maintenance boundary behind the public site. The August
2026 review reconciled the repository against DOI/Crossref and publisher
records, arXiv, IEEE Xplore, official conference programs, PyPI, npm,
crates.io, GitHub, Sessionize, organizer event pages, and institutional news.

## October 9 GHTC award recognition

- Added the Reviewers Choice Award at IEEE GHTC 2026 to the Projects awards
  section and the existing Environmental Cost of Digital Sovereignty paper
  entry on Research, with the exact Research on the Broader Impacts of
  Engineering Efforts track attribution and all five coauthors preserved.
- The award name, track, paper title, and author list were checked against the
  owner's conference certificate. The certificate image is not published.
- This is a track-specific Reviewers Choice Award, not an overall best-paper
  award. No award is attributed to the other GHTC ergonomics paper.
- The homepage is unchanged. The paper remains accepted/forthcoming pending
  a proceedings record; publication counts are unchanged. Matching standard
  Schema.org award metadata and the two affected sitemap dates were updated.

## October 6 media archive

- Added `media.html` with 20 distinct stories and interviews from 2018–2026:
  seven reporting/interview records, eight university news records, and five
  guest reports, announcements, or organizer/sponsor records. The five existing
  press stories remain represented; 15 records expand the dedicated archive.
- Added Media to all seven primary navigation menus and a direct archive link
  on the homepage. About retains its existing highlights, adds Pittsburgh's
  ZeroDK feature, and links to the complete media archive.
- Added three selected highlights and a searchable chronological archive with
  category filters. All 20 records remain readable without JavaScript.
- Preserved original publication dates and coarse date precision: Brevard Live
  is January 2021, Florida Tech Magazine is Spring 2020, and Stantec is 2020.
  Stantec's March 9–10 dates identify the event, not a publication day.
- The Hechinger Report original and Washington Post syndication are one story,
  with two source links and the original publisher identified in metadata.
  Publisher reprints of the Florida Tech stories do not add to the story count.
- Penn State is a brief collaboration mention, without an Imagine Cup finalist
  claim. Fresh Fridge is labeled a guest report by organizer Grant Kurz;
  BroadwayWorld is an industry announcement, and Pi Network/Redis/Stantec are
  labeled sponsor or organizer coverage.
- Robot Love coverage describes art/technology collaboration without repeating
  an inaccurate professor title. Dreamland coverage establishes inclusion in
  the collaborator list, without assigning an individual software contribution.
- Recovered working original-publisher archives for the two Brevard Business
  News stories: [Robot Love, January 25, 2021](https://brevardbusinessnews.com/wp-content/uploads/2022/12/BBN-012521.pdf#page=19)
  and [Dreamland, May 23, 2022](https://brevardbusinessnews.com/wp-content/uploads/2022/11/BBN-052322.pdf#page=21).
  Relevant PDF pages were rendered and visually checked.
- Added CollectionPage, BreadcrumbList, and a 20-entry ItemList using standard
  Schema.org terms. Updated the sitemap, README, stylesheet cache key, and
  navigation breakpoint to accommodate the seventh menu item.

Validation covered all seven pages at 1440, 1101, 1024, 768, 390, and 320 pixels
in both themes: 84 layout checks passed with no horizontal overflow, broken
images, or header collisions. Twelve automated axe-core WCAG A/AA checks passed
on Home, About, and Media. Archive filters, combined search, empty/reset states,
deep links, mobile navigation, Escape, theme switching, and the no-JavaScript
archive passed without page errors. Rendered desktop/mobile archive and About
highlights were reviewed. All 144 local references resolve; structured lists,
positions, dates, titles, and archive counts agree. Nineteen primary source URLs
returned HTTP 200 in the generic link check; Stetson returned 403 to that checker
and was separately verified through the web reader.

## October 5 software refresh

- Checked all 26 owned PyPI projects, four npm packages, and five Rust crates
  against live registry APIs and ownership inventories. Only pollard-jev changed
  since September 28; the other 34 registry versions are unchanged, and no new
  owned packages were found.
- Updated [pollard-jev to 0.13](https://pypi.org/project/pollard-jev/0.13/),
  published October 5. The release adds optional inputs for numerical boundaries
  and action priority; JSON remains the default input. Updated the homepage,
  software cards, release date/link, structured version, and modification date.
- Preserved Alpha status and the hardware-integration and recorded-sensor
  limitations. Development-case results do not establish fresh held-out
  validation or physical-device performance.
- Counts remain 24 featured PyPI packages, four npm packages, five Rust crates,
  eight software families, and 26 top-level structured software works. The
  existing i3cex prerelease and facecloak-suite placeholder remain excluded.
  Eight source-stage repositories still have no published GitHub releases;
  experiment and camera-ready tags remain source snapshots.
- Advanced the registry review date and sitemap dates for Home and Software.
  The September 28 audit below retains its historical release versions.

Validation confirmed all six pages' JSON-LD list counts and positions and all
121 internal references. Home and Software passed browser checks at 1440px,
390px, and 320px with no horizontal overflow, broken images, or page errors.
The updated release cards were visually reviewed at mobile width.

## October 5 speaking refresh

- Added 11 dated archive entries: Tampa Devs' Machine Learning 101
  (September 20, 2022), the IEEE Cruise Conference Chat GPT talk
  (October 2023), four NOAA/NASA events and Princeton Open Hackathon
  (2024), AI Revolution and the Melbourne, Florida ACM lecture (2025),
  and the Google Ecosystem workshop and April 30 AI Masterclass (2026).
- The owner confirms both NOAA/NCAR/NREL events: the February 6–7 AI for
  Science Bootcamp and February 21–29 Open Hackathon. The owner also
  confirms both NASA events: the June 5–7 End-to-End LLM Bootcamp and
  September 10 / September 17–19 GPU Hackathon. Organizer records establish
  event dates; personal participation is confirmed by the speaker. Individual
  session titles and times are not inferred from whole-event programs.
- Princeton is described as technical moderation and mentoring for several
  teams. Added the same contribution to About's community-service record;
  the archive does not assign an invented lecture title to that role.
- The Google workshop was delivered at Miami Dade College on February 11,
  2026. The owner links delivery to the last substantial commit. The
  [latest notebook update](https://github.com/jemsbhai/google-agentic-workshop/commit/f986a3122e0d69141feda1f3467df5b8276c6005)
  and preceding bugfix both have February 11 author and committer dates.
  Linked the curriculum from the dated archive and a new materials card.
- The ACM lecture's November 7 date is documented in its repository; the
  owner confirms an ACM chapter in Melbourne, Florida. No specific campus
  or official chapter name is assumed. The cruise date retains month
  precision. The Tampa 2022 entry describes an announced speaker listing,
  with no claim that an independent delivery recap was found.
- Added AI Revolution's organizer session record and the April 30
  masterclass's event page and delivery recap. Added the firsthand Vibe Days
  recap to its existing entry. Changed the expired MLSP wording to a past
  program listing without asserting who personally presented the poster.
- Expanded standard speaking metadata to all 39 visible archive entries,
  retaining existing session times and featured-work records. Multi-date
  NASA and Princeton events have explicit subevent dates. Princeton uses
  contributor metadata; month-only records do not invent a day. This count
  includes mentoring, announced/program-listed entries, and grouped author
  sessions, so it is not a delivered-talk total.
- Added a 2024 archive link from Projects and updated sitemap modification
  dates for the three changed HTML pages. Research, publication records,
  and the project catalog retain their September 28 review date.

Validation matched all 39 visible entries to structured titles, dates, sources,
and anchors; all six pages' JSON-LD lists parse with consistent counts and
positions. All 121 internal references resolve. Reviewed the speaking archive
at 1280px and 390px, including the new multi-date rows and Google workshop;
About and Projects also have no horizontal overflow at 390px. The Projects
link opens the new 2024 section. Official NOAA/NASA date records were rechecked.

## September 28 refresh

- Added [pollard-jev 0.12](https://pypi.org/project/pollard-jev/0.12/) and
  [epicormic 0.1.0](https://pypi.org/project/epicormic/0.1.0/), both functional
  alpha releases published September 27. Updated
  [StegaQR to 0.2.0](https://pypi.org/project/stegaQR/0.2.0/) (September 25),
  including its default interleaved placement and native decoding for older images.
- Checked all 26 owned PyPI projects, four npm packages, and five Rust crates.
  The other 30 previously featured registry entries are unchanged. With the
  existing prerelease/placeholder exclusions, the catalog now features 24 PyPI
  packages in eight software families. Software JSON-LD has 26 top-level works;
  that count is distinct from package-registry entries and language ports.
- Added the organizer-confirmed [October 8 AiSalon Miami keynote](https://luma.com/AI-Salon-October-Miami-2026),
  “The Power of No.” The 6–9 p.m. Eastern window belongs to the overall event,
  not the individual keynote. It replaces the expired September 17 feature.
- Marked the September 17 Hugging Face session as delivered. The speaker
  confirmed a standing-room-only audience. DeepStation's
  [September 21 recap](https://www.linkedin.com/posts/deepstationai_deepstation-is-excited-to-share-the-post-event-activity-7507809905546821632-UT_f)
  independently describes the live demonstration. Linked the recap, slides,
  Colab exercise, and [materials](https://github.com/jemsbhai/bringing-the-heat).
- Added the August 26 CBOR-LD Ex demonstration at the fifth Miami Hardware
  Meetup using the organizer event and post-event recap.
- Added FLAIRS-40 special-track co-chair service after the
  [official conference roster](https://www.flairs-40.info/special-tracks)
  linked the [canonical track site](https://embodiedaicfp.github.io/).
  The prior approval holdback is resolved. Added the independently credited
  [Deco Portals volunteer contribution](https://lincolnroad.com/deco-portals/).
- Promoted Corpusgen's existing Show & Tell record to a published proceedings
  contribution using the [official ISCA page](https://www.isca-archive.org/interspeech_2026/syed26_interspeech.html)
  and PDF, pp. 5916–5917. Preserved the four conference-paper authors and the
  separate software DOI. The paper page supplies no individual DOI and only
  year-precision publication metadata. ISCA currently has a certificate issue;
  the page and PDF were inspected with that access limitation recorded.
- Research remains 38 distinct outputs: 16 published contributions, 20 accepted
  contributions, one standalone preprint, and one published poster abstract.
  Four preprints await publication, including three accepted works. Renamed the
  published filter to make the two-page Show & Tell contribution explicit
  without implying that every published item is a full paper or chapter.
- Restored public Hashrope experiment links, added mlpowermeter and the
  Epicormic research workspace as source-stage projects, and kept unpublished
  drafts outside publication totals. Linked all four MultiSpecQR model
  repositories and both datasets on Hugging Face. Added the verified publication
  name variant and Hugging Face identity link to Person metadata across the site.
- Live OpenAlex searches now return one matching ORCID-linked profile. The
  earlier author split was not reproduced; the follow-up is coverage and
  deduplication rather than an assumed unresolved merge.
- Refreshed the public GitHub biography, website, pinned projects, and profile
  README. Updated the Hashrope paper README to its accepted title and status.
  Refreshed Sessionize's biography and employer link, preserved the separately
  labeled Florida Tech link, and published the Hugging Face and Pollard offerings.
- Labeled the old Hugging Face DistilBERT Space as an archived demo, preserving
  its app code and runtime configuration. The main Hugging Face profile biography
  and website update still require the owner's password confirmation.
- Cleaned the ORCID record using verified publisher metadata: added missing
  proceedings, preprints, the 2018 poster abstract, and the current Corpusgen
  software release; corrected work types, dates, identifiers, and truncated
  contributor lists; grouped duplicate sources while preserving provenance.
  Moved FLAIRS-39 committee service into professional activities. Six confirmed
  misattributions and the replaced service-as-paper row were set to Only me,
  retaining reversibility. The website's scholarly count remains independent
  of ORCID's record, version, and software totals.

Validation covered all six pages at 1440, 768, 390, and 320 pixels in both
themes: 48 layout checks with no horizontal overflow or broken images. All
24 automated axe-core WCAG A/AA checks passed. JSON-LD list counts and
positions agree, all 129 internal references resolve, and the research filters
return 38 total, 16 published, 20 accepted, and four pending preprints.
Search, empty results, deep links, mobile navigation, and theme controls passed
without page JavaScript errors. Updated sections were visually reviewed.

## September 23 Opera Map addition

- Added Opera Map to the Projects awards and About milestones for 2019, with
  matching Person award metadata on the homepage and About page.
- San Diego Opera’s [official August 20, 2020 press release](https://sdoperastg.wpengine.com/wp-content/uploads/2022/09/Opera-Hack-Winner-Presentations.pdf)
  names Muntaser Syed on the winning team and describes the project.
  The release describes a July 2019 win; 2020 is the follow-up presentation year.
- The [original event listing](https://opera-hack.devpost.com/) establishes
  July 27–28, 2019 at Microsoft in La Jolla. Project manager Angel Mannion’s
  [event history](https://opera-innovation.squarespace.com/oi-insights/hacking-opera-in-san-diego)
  confirms this was the inaugural Opera Hack.
- Copy credits a team win, one of three selected projects, without claiming
  first place or sole authorship. Removed “recent”
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

- Research: 38 distinct scholarly outputs: 16 published contributions
  (papers, chapters, a poster paper, and a two-page Show & Tell contribution),
  20 accepted conference contributions, one preprint without conference
  acceptance, and one published 2018 poster abstract. Three accepted works also have public
  preprints, making four preprints awaiting publication in all. These filters
  overlap; earlier versions of published papers remain linked and are counted
  once. Two older presentation acceptances
  and software artifacts remain outside this scholarly total.
- Software: 24 featured published PyPI packages, 4 npm packages, and 5 Rust crates.
  `i3cex` is a development release and `facecloak-suite` is a placeholder, so
  neither is included in the featured PyPI total. Package maturity ranges from
  pre-alpha through production/stable and is not implied by this count.
- Projects: public repositories link directly. Private repositories are either
  labeled as private research without a link or omitted from the public index.
- Speaking: dated entries require an organizer, conference, institutional, or
  public scheduling record. Material-only repositories are kept in a separate
  teaching archive.

## Deliberate holdbacks and owner follow-ups

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
- The repository linked from the Rules Before Oracles arXiv record (`devfitcs/ABAS`)
  returned 404 for a signed-out visitor, so the site does not expose a code link.
- Twelve repositories linked by the previous site remain held from the earlier review:
  `cryptepi`, `explainiverse-explorer`,
  `healthSLnetwrokslicer`, `IEEEHealth-pharma`, `imujepa`, `jepa-fhir`,
  `kvrm-paper`, `oneura-ictai2026`, `thermocline`, `TimeCMAPlus`, `trilstm`,
  and `uhc-visualizer`. Re-add links only after
  confirming public visibility.
- The public `jsonld-ex-experiments` README describes the repository as private
  and says it must not be public. Its portfolio link was removed; the owner
  should review the repository’s visibility and contents directly.
- The main ORCID cleanup was applied on September 28. The sinonasal-masses
  authorship, Universal Translator identity, and conflicting SQT author/version
  metadata remain unresolved. Some organization-owned source records retain
  their imported types; corrected owner copies are preferred where available.
  Do not use ORCID's displayed count as the website's scholarly-output count.
  Recheck OpenAlex coverage and deduplication; the previously observed author
  split was not reproduced on September 28.
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

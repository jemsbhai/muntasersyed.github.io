Source: [https://muntasersyed.com/software.html](https://muntasersyed.com/software.html)

Updated: 2026-11-13

Open source  / Python · Rust · TypeScript · JavaScript · Java

# Software and research code.

Related packages, language ports, papers, demos, and installation links are grouped on this page.

Explore the software.  Packages, research repositories, and tools for building trustworthy, efficient AI systems.

25 Featured PyPI packages

6 npm packages

6 Rust crates

8 Major software families

Registry sync / November 13, 2026

## Latest package releases.

The newest releases across the public package profile, with direct links to install details and source.

LATEST · OCT 28, 2026

### epicormic Python 0.2.0

Updates sequential drift detection to use an exact baseline interval, correcting false alarms for constant baseline observations.

[PyPI](https://pypi.org/project/epicormic/0.2.0/) [Release notes](https://github.com/jemsbhai/epicormic/releases/tag/v0.2.0) [Details](https://muntasersyed.com/software.html#epicormic)

OCT 24, 2026

### Hashrope 0.3.4 · Python · JavaScript · Rust · Java

Synchronized core libraries for persistent editing, substring hashing, exact comparison, and compact repetition encoding.

[PyPI](https://pypi.org/project/hashrope/0.3.4/) [Release notes](https://github.com/jemsbhai/hashrope/blob/master/releases/0.3.4/README.md) [Details](https://muntasersyed.com/software.html#hashrope)

OCT 24, 2026

### hashrope-bio Python 0.3.4 · Rust 0.3.4

Synchronizes the Python and Rust biology libraries with Hashrope 0.3.4 for exact genomic comparison and mutation analysis.

[PyPI](https://pypi.org/project/hashrope-bio/0.3.4/) [crate](https://crates.io/crates/hashrope-bio/0.3.4) [Details](https://muntasersyed.com/software.html#hashrope-bio)

Major software

## Major software families.

Each section describes the project and lists its implementations, papers, demos, and package releases.

01 / TRUSTWORTHY DATA

## JSON-LD Ex

Created by Muntaser Syed, JSON-LD Ex is an AI/ML extension framework for representing confidence, provenance, temporal validity, embeddings, privacy rights, validation, and context integrity while preserving compatibility with linked-data workflows.

`pip install jsonld-ex`

### jsonld-ex · Python reference

v0.7.4

The full reference implementation, including Subjective Logic, FHIR interoperability, security hardening, temporal operations, and AI/ML metadata.

[PyPI](https://pypi.org/project/jsonld-ex/) [GitHub](https://github.com/jemsbhai/jsonld-ex) [Docs](https://jsonld-ex.github.io/ns) [Companion site](https://jsonldex.lovable.app/)

### @jsonld-ex/core · TypeScript port

v0.1.2 · npm

A feature-complete JavaScript/TypeScript implementation with built-in type declarations and an MCP server.

[npm](https://www.npmjs.com/package/@jsonld-ex/core) [Source](https://github.com/jemsbhai/jsonld-ex/tree/main/packages/js) [Interactive lab](https://jsonld-playtime.lovable.app/)

### Research paper

FLAIRS-39

The formal gap analysis and extension proposal behind the framework.

[DOI](https://doi.org/10.32473/flairs.39.1.141786)

### Veracity and compliance research

IEEE CIC · IEEE WF-IoT 2026

Subjective Logic grounds veracity-aware data exchange and compliance algebra for IoT energy-data governance. The CIC paper includes a dedicated experiment repository.

[Veracity paper](https://muntasersyed.com/research.html#veracity-cic) [CIC experiments](https://github.com/jemsbhai/jsonld-ex-experiments) [CIC slides](https://docs.google.com/presentation/d/1Ar6e4PSd9q5L9WwBUrVKpodg0hSV7Obx/edit?usp=sharing) [Compliance paper](https://muntasersyed.com/research.html#compliance-algebra-iot) [WF-IoT slides](https://docs.google.com/presentation/d/1YvYY_Qu6DYu9FgPplnCg08RpYsm75pWo/edit?usp=sharing)

02 / AGENT CONTEXT

## Tokenmaster + ctxmaster

A two-layer toolkit for measuring LLM context budgets, estimating exhaustion, choosing compaction or handoff actions, and rendering a live context gauge.

`pip install tokenmaster ctxmaster`

### tokenmaster · Core decision engine

v0.2.0 · Python · Rust · npm

Normalized token accounting, effective-budget gauges, turns-to-exhaustion prediction, and compaction/handoff policies.

[PyPI](https://pypi.org/project/tokenmaster/) [crate](https://crates.io/crates/tokenmaster) [npm](https://www.npmjs.com/package/tokenmaster)

### ctxmaster · Visualization layer

Python 0.1.2 · Rust/npm 0.1.1

Terminal gauges and renderers that present context-budget telemetry.

[PyPI](https://pypi.org/project/ctxmaster/) [crate](https://crates.io/crates/ctxmaster) [npm](https://www.npmjs.com/package/ctxmaster)

### Shared repository

Monorepo

Language-parity implementations and a unified handoff-fidelity protocol are developed together.

[GitHub](https://github.com/jemsbhai/tokenmaster) [Open-source packaging talk](https://docs.google.com/presentation/d/1H8mMlLhTkxyCuWazhVCCiSH1fCxlTna2/edit?usp=sharing)

03 / DATA STRUCTURES

## Hashrope

A balanced rope with polynomial-hash metadata for efficient concatenation, splitting, substring hashing, exact comparison, and compact repetition encoding.

`pip install hashrope`

### hashrope · Core library

v0.3.4 · Python · JavaScript · Rust · Java

Python, JavaScript, Rust, and Java implementations of the BB[2/7] hash-augmented tree for persistent editing, substring hashing, exact comparison, and compact repetition encoding.

[Hashrope overview](https://muntasersyed.com/hashrope.html) [PyPI](https://pypi.org/project/hashrope/) [npm](https://www.npmjs.com/package/hashrope) [Maven Central](https://central.sonatype.com/artifact/io.github.jemsbhai/hashrope) [Interactive demo](https://hashrope.lovable.app/) [crate](https://crates.io/crates/hashrope) [GitHub](https://github.com/jemsbhai/hashrope) [Live visualizer](https://uhc-visualizer.lovable.app/) [DevFest Florida talk](https://muntasersyed.com/speaking.html#recording-hashrope-devfest) [Quantum verification project](https://muntasersyed.com/projects.html#qhashrope)

### hashrope-bio · Computational biology

Python 0.3.4 · Rust 0.3.4

Genomic region comparison, mutation localization, tandem-repeat analysis, and drug-resistance screening.

[PyPI](https://pypi.org/project/hashrope-bio/) [crate](https://crates.io/crates/hashrope-bio) [GitHub](https://github.com/jemsbhai/hashrope-bio)

### Agentic context research

Research experiments

Experiments for the accepted IEEE ICTAI 2026 paper on persistent editing, branching, prefix identification, and repetition encoding for LLM context management.

[Preprint](https://arxiv.org/abs/2610.16144) [Accepted paper](https://muntasersyed.com/research.html#hashrope-ictai) [Experiments](https://github.com/jemsbhai/hashrope-paper) [ICTAI slides](https://docs.google.com/presentation/d/11_hXF6CMn1XsgLwPHNToE_GW6xnUA1KB/edit?usp=sharing)

04 / TEMPORAL TRUST

## Epistemic & temporal stack

Packages for representing belief, tracking validity over time, and updating confidence through chains of evidence or agents.

`pip install chronofy trustandverify xrag-temporal`

### Chronofy

IRI 2026 · Python 0.1.9 · npm JS 0.1.8

The reference implementation of the Temporal-Logical Decay Architecture: temporal embeddings, decay-weighted retrieval, STL knowledge-validity checks, and data re-acquisition triggers for time-aware RAG. The paper is published in the IEEE IRI 2026 proceedings.

[PyPI](https://pypi.org/project/chronofy/) [Published paper](https://doi.org/10.1109/IRI69576.2026.00090) [Preprint](https://arxiv.org/abs/2607.20560) [IRI program](https://ieee-iri.github.io/resources/documents/IEEE_IRI2026_Detailed_Program_Jul31.pdf) [GitHub](https://github.com/jemsbhai/chronofy) [npm](https://www.npmjs.com/package/chronofy)

### TrustAndVerify + TrustGraph Jac

0.2.1 · 0.2.0

Subjective-Logic confidence algebra and a Jac/Jaseci agent walker for verifiable knowledge workflows.

[PyPI](https://pypi.org/project/trustandverify/) [Jac port](https://pypi.org/project/trustgraph-jac/) [GitHub](https://github.com/jemsbhai/trustandverify)

### X-RAG Temporal

v0.1.0

Time-decayed uncertainty and evidence confidence for retrieval systems.

[PyPI](https://pypi.org/project/xrag-temporal/) [GitHub](https://github.com/jemsbhai/subjective-logic-rag)

### Epistemic Edge

v0.1.0 · IEEE IRI 2026

Air-gapped neuro-symbolic cognition over verified edge state, with Subjective Logic guardrails for LLM-driven IoT actuation. The paper is published in the IEEE IRI 2026 proceedings.

[PyPI](https://pypi.org/project/epistemic-edge/) [GitHub](https://github.com/jemsbhai/epistemic-edge) [Published paper](https://doi.org/10.1109/IRI69576.2026.00017) [IRI program](https://ieee-iri.github.io/resources/documents/IEEE_IRI2026_Detailed_Program_Jul31.pdf)

05 / AGENT INFRASTRUCTURE

## Governed agents & edge systems

Pollard provides governed and replayable execution trees for agents. Its companions add typed robotics decisions and provider-drift monitoring; MCP-Edge connects constrained devices. The [Station Steward hackathon project](https://muntasersyed.com/projects.html#station-steward)  combines Pollard and MCP-Edge with Chronofy, Arduino telemetry, and human task handoffs. [ReleaseProof](https://muntasersyed.com/projects.html#releaseproof)  brings Pollard, Epicormic, and Hashrope into an agent-release workbench; [swarm-forest](https://muntasersyed.com/projects.html#swarm-forest)  studies governed execution across agent teams.

`pip install pollard mcp-edge`

`pip install pollard-jev epicormic`

### Pollard · Python

v1.6.2

A runtime for budgeting agent work, enforcing versioned action gates, auditing execution trees, and replaying decisions. Python 1.6.2 adds optional Codex CLI integration with bounded task execution, recorded usage, duplicate refusal, and strict replay. Agent teams retain inherited budgets, permissions, checkpoints, and durable approvals.

[Pollard overview](https://muntasersyed.com/pollard.html) [PyPI](https://pypi.org/project/pollard/) [GitHub](https://github.com/jemsbhai/pollard) [Team guide](https://github.com/jemsbhai/pollard/blob/v1.6.2/docs/teams.md) [Codex integration](https://github.com/jemsbhai/pollard/blob/v1.6.2/docs/codex-cli.md) [Preprint](https://arxiv.org/abs/2610.16145) [Accepted paper](https://muntasersyed.com/research.html#pollard-ictai) [ICTAI slides](https://docs.google.com/presentation/d/1e604yMBf24acaQI1UIJw_0B_Fq7zc_IuAh1ELziU-94/edit?usp=sharing) [Slides PDF](https://docs.google.com/presentation/d/1e604yMBf24acaQI1UIJw_0B_Fq7zc_IuAh1ELziU-94/export/pdf) [DevFest Tampa talk](https://muntasersyed.com/speaking.html#devfest-tampa-2026) [DevFest Miami workshop](https://muntasersyed.com/speaking.html#devfest-miami-2026) [Open-source packaging talk](https://docs.google.com/presentation/d/1H8mMlLhTkxyCuWazhVCCiSH1fCxlTna2/edit?usp=sharing) [Applied AI Summit slides](https://docs.google.com/presentation/d/1A6ballogWGr02m26VCoruYbfccPy5oDp/edit?usp=sharing)

### pollardai · TypeScript

v0.2.0

A native Node.js/TypeScript runtime with streaming, replay, persistent stores, shared budgets, provider adapters, and audit tools. Its independent release line targets Python Pollard 1.6.0 behavior.

[npm](https://www.npmjs.com/package/pollardai) [Source](https://github.com/jemsbhai/pollard/tree/main/packages/npm) [Compatibility](https://github.com/jemsbhai/pollard/blob/pollardai-v0.2.0/docs/npm-parity.md)

### pollardai · Rust

v0.2.1

A native Rust runtime with eight storage backends, shared budgets, async streaming, replay, and audit tools. Its independent release line targets Python Pollard 1.6.0 behavior.

[crate](https://crates.io/crates/pollardai) [Source](https://github.com/jemsbhai/pollard/tree/main/crates/pollardai) [Release notes](https://github.com/jemsbhai/pollard/releases/tag/pollardai-rust-v0.2.1)

### pollard-jev

v0.13

A Pollard companion for typed robotics and IoT decisions, with observation-validity checks, bounded simulated actions, audit records, and reproducible local OpenJev benchmarks.

[PyPI](https://pypi.org/project/pollard-jev/) [GitHub](https://github.com/jemsbhai/pollard-jev) [Benchmarks](https://github.com/jemsbhai/pollard-jev/blob/main/docs/BENCHMARKING.md) [Applied AI Summit slides](https://docs.google.com/presentation/d/1A6ballogWGr02m26VCoruYbfccPy5oDp/edit?usp=sharing)

### epicormic

v0.2.0

Statistical provider-drift monitoring for Pollard-governed AI systems, with reproducible evidence records and controls that gate subsequent model and tool calls. Its verdicts distinguish stable, warning, drift, and unknown states.

[PyPI](https://pypi.org/project/epicormic/) [GitHub](https://github.com/jemsbhai/epicormic) [Technical details](https://github.com/jemsbhai/epicormic/blob/main/docs/limitations.md) [Applied AI Summit slides](https://docs.google.com/presentation/d/1A6ballogWGr02m26VCoruYbfccPy5oDp/edit?usp=sharing)

### MCP-Edge

v0.2.0 · Edge · IoT

A bridging gateway, MCP-Lite server, and four-tier taxonomy for extending the Model Context Protocol to constrained devices.

[PyPI](https://pypi.org/project/mcp-edge/) [GitHub](https://github.com/jemsbhai/mcp-edge) [Paper](https://doi.org/10.1109/CLOUDSUMMIT68932.2026.00020)

### Securing MCP Workflows for Agentic AI

AgentCon Miami · Jun 12, 2026

An interactive talk and security lab covering MCP, autonomous agents, AI pipelines, attack surfaces, and defensive patterns.

[Event](https://globalai.community/e/q7qdn1cp) [Open lab](https://agentic-defense-lab.lovable.app/) [Speaking record](https://muntasersyed.com/speaking.html)

06 / SEMANTIC IOT

## CBOR-LD Ex

A reasoning-carrying binary linked-data protocol for constrained IoT networks. It combines compact CBOR-LD documents with bit-packed Subjective Logic annotations while preserving on-wire semantics.

`pip install cbor-ld-ex`

`cargo add cborld-ex`

### cbor-ld-ex · Python reference

v0.2.1 · Python 3.10+

The full protocol implementation: CBOR Tag 60000 annotations, constrained opinion quantization, temporal decay, cumulative fusion, MQTT and CoAP transport, security metadata, provenance chains, streaming, and batch compression.

[PyPI](https://pypi.org/project/cbor-ld-ex/) [GitHub](https://github.com/jemsbhai/cbor-ld-ex)

### cborld-ex · Rust implementation

v0.1.0 · no_std

A byte-compatible implementation for embedded, bare-metal, WASM, and ESP32 targets. Its feature tiers support full standard-library use, allocator-only environments, digest verification, or a heap-free core wire format.

[crate](https://crates.io/crates/cborld-ex) [GitHub](https://github.com/jemsbhai/cborld-ex)

### Protocol architecture & evaluation

IEEE WF-IoT 2026 · Accepted paper

Tier 1 sensors add a 4-byte opinion; Tier 2 gateways fuse and temporally decay evidence; Tier 3 services append tamper-evident provenance. Across four real IoT datasets, the accepted study reports 4.1× compression over JSON-LD for Intel telemetry and 100% IEEE 802.15.4 frame fit while retaining self-description.

[Accepted paper](https://muntasersyed.com/research.html#cborld-ex-paper) [WF-IoT slides](https://docs.google.com/presentation/d/1pmijmsdqrK8woen5Jj5jXGf1NapFw7NZ/edit?usp=sharing)

### Related compact-data tools

CDXF 0.1.3 · UHC 0.1.6

CDXF provides universal binary interchange across JSON, YAML, XML, and TOML; its paper is accepted at IEEE ComComAp 2026. UHC hashes directly over LZ77 streams for compressed-domain processing.

[CDXF](https://pypi.org/project/cdxf/) [CDXF code](https://github.com/jemsbhai/cdxf) [Accepted CDXF paper](https://muntasersyed.com/research.html#cdxf-paper) [UHC](https://pypi.org/project/uhc/) [UHC code](https://github.com/jemsbhai/uhc)

07 / RESEARCH TOOLS

## Research toolkits

Reusable research frameworks for understanding model decisions, constructing speech corpora, harmonizing clinicogenomic cohorts, measuring energy, and building efficient edge architectures.

### geniekit

v0.1.0

Python tools for harmonizing six GENIE BPC clinicogenomic cohorts, deriving lines of therapy, and producing aggregate summaries with disclosure controls. Includes metadata and synthetic-data tools.

[PyPI](https://pypi.org/project/geniekit/) [GitHub](https://github.com/jemsbhai/geniekit) [Data provenance](https://github.com/jemsbhai/geniekit/blob/main/NOTICE.md)

### Explainiverse

v0.15.2 · audited registry

A unified explainability framework with an audited registry of methods and capabilities.

[PyPI](https://pypi.org/project/explainiverse/) [GitHub](https://github.com/jemsbhai/explainiverse) [Live explorer](https://explainiverse-explorer.lovable.app/)

### Corpusgen

v0.1.7 · Speech

A language-agnostic generator and evaluator for speech corpora with maximal phoneme coverage. Its paper is published in the Interspeech 2026 proceedings, pp. 5916–5917.

[PyPI](https://pypi.org/project/corpusgen/) [GitHub](https://github.com/jemsbhai/corpusgen) [Software version DOI](https://doi.org/10.5281/zenodo.21891821) [ISCA Archive](https://www.isca-archive.org/interspeech_2026/syed26_interspeech.html) [Paper PDF](https://www.isca-archive.org/interspeech_2026/syed26_interspeech.pdf) [Published paper](https://muntasersyed.com/research.html#corpusgen-interspeech) [CorpusKit demo](https://www.youtube.com/watch?v=m1guE38mbIo)

### NEXUS + ArcMind

0.0.1 · 0.2.0

Physics-grounded energy metrics paired with a causal, dual-rate sequence backbone for streaming sensor policies.

[NEXUS](https://pypi.org/project/nexus-ml-metrics/) [ArcMind](https://pypi.org/project/arcmind/)

### TOML Signals

Accepted · IEEE MLSP 2026

Reproducible transistor-level energy analysis for 37 signal-processing algorithms on RTX 4090 and A100 GPUs, including data and profiler traces.

[GitHub](https://github.com/jemsbhai/TOMLSignals) [OpenReview](https://openreview.net/forum?id=jYBcP44EDn) [Conference schedule](https://neuroneural.net/mlsp2026schedule/)

08 / APPLIED ML

## Practical ML tooling

Focused packages for machine-learning environment repair, multi-spectral codes, and neural data embedding.

### Compatibillabuddy

v0.2.1 · ML environments

A hardware-aware agent that diagnoses and repairs incompatible Python machine-learning stacks.

[PyPI](https://pypi.org/project/compatibillabuddy/) [GitHub](https://github.com/jemsbhai/compatibillabuddy)

### MultispecQR

v0.4.1 · IEEE ICMLA 2026

RGB channel multiplexing for three independent QR payloads, with neural-assisted decoding and a palette mode supporting up to nine layers. Its paper is published in the IEEE ICMLA 2026 proceedings.

[PyPI](https://pypi.org/project/multispecqr/) [GitHub](https://github.com/jemsbhai/multispecqr) [Published paper](https://doi.org/10.1109/ICMLA69890.2026.00221) [ICMLA slides](https://docs.google.com/presentation/d/1LwrP67_kbdc-FbjcnuCFlhDdBX7yY5Kr/edit?usp=sharing)

### MultiSpecQR models & datasets

Hugging Face

Published model checkpoints for RGB and palette modes, plus RGB and palette-6 datasets.

[RGB model](https://huggingface.co/Jemsbhai/multispecqr-rgb) [Palette 6 model](https://huggingface.co/Jemsbhai/multispecqr-palette6) [Palette 8 model](https://huggingface.co/Jemsbhai/multispecqr-palette8) [Palette 9 model](https://huggingface.co/Jemsbhai/multispecqr-palette9) [RGB dataset](https://huggingface.co/datasets/Jemsbhai/multispecqr-rgb-dataset) [Palette 6 dataset](https://huggingface.co/datasets/Jemsbhai/multispecqr-palette6-dataset)

### stegaQR

v0.2.0

Neural private-payload embedding in standard-decodable QR codes, with a bundled model, error correction, and interleaved bit placement. Decode images created with 0.1.0 using `--placement native`. The robust operating point has a visible color tint.

[PyPI](https://pypi.org/project/stegaQR/) [GitHub](https://github.com/jemsbhai/stegaQR) [Paper](https://muntasersyed.com/research.html#stegaqr-ictai) [ICTAI slides](https://docs.google.com/presentation/d/1H5sl9ycs7kndZJUwMABVxFdzbmrtMzXP/edit?usp=sharing)

Live materials

## Interactive demos and talk materials.

These companion sites demonstrate the software and provide material from technical talks.

EXPLAINABILITY

### Explainiverse Explorer

Browse the Explainiverse framework and its model-explanation methods.

[Launch explorer](https://explainiverse-explorer.lovable.app/) [Code](https://github.com/jemsbhai/explainiverse)

JSON-LD EX

### Project companion

Read about the JSON-LD 1.2 extension framework and its FLAIRS-39 paper.

[Open site](https://jsonldex.lovable.app/) [Paper](https://doi.org/10.32473/flairs.39.1.141786)

JSON-LD EX

### JSON-LD Playtime

Test security, validation, Subjective Logic, resource limits, and agent integrations.

[Open lab](https://jsonld-playtime.lovable.app/)

AGENTCON MIAMI

### Agentic Defense Lab

Interactive material from the AgentCon Miami talk on securing MCP, agents, and AI pipelines.

[Open lab](https://agentic-defense-lab.lovable.app/)

HASHROPE

### Hashrope interactive demo

Explore concatenation, splitting, substring hashing, insertion, repetition, and exact comparison with live tree diagrams and in-browser benchmarks.

[Launch interactive demo](https://hashrope.lovable.app/) [Library and packages](https://muntasersyed.com/software.html#hashrope)

HASHROPE + UHC

### UHC Visualizer

View unified hash compression and hash-rope structures.

[Launch visualizer](https://uhc-visualizer.lovable.app/) [UHC code](https://github.com/jemsbhai/uhc)

POLLARD · EPICORMIC · HASHROPE

### ReleaseProof

Explore an agent-release workbench that combines configuration approval, measured behavior, execution controls, and drift monitoring.

[Open workbench](https://jemsbhai-releaseproof.hf.space/) [Project and code](https://muntasersyed.com/projects.html#releaseproof) [Watch the demo](https://muntasersyed.com/speaking.html#recording-releaseproof)

QUANTUM OPTIMISATION

### Quantum Optimisation Circuit Builder

Build QAOA circuits from MaxCut graphs or QUBO matrices, explore algorithm recommendations, and compare simulations with exact solutions for small instances.

[Open builder](https://qopt-builder.vercel.app/) [Guided demo](https://qopt-builder.vercel.app/demo.html) [Project and code](https://muntasersyed.com/projects.html#qopt-builder)

MORE MATERIALS

### Talks & workshops

Lecture notebooks, workshop repositories, and public teaching materials for agentic AI and MCP.

[View speaking archive](https://muntasersyed.com/speaking.html)

Registry profiles

## Package registries.

Use these profiles for current versions, release history, and installation files.

[PyPI profile](https://pypi.org/user/jemsbhai/)  [npm profile](https://www.npmjs.com/~jemsbhai)  [crates.io profile](https://crates.io/users/jemsbhai)  [GitHub](https://github.com/jemsbhai)  [Hugging Face](https://huggingface.co/Jemsbhai)  [Zenodo](https://doi.org/10.5281/zenodo.18881479)  [Related papers](https://muntasersyed.com/research.html)

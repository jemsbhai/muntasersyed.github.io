Source: [https://muntasersyed.com/pollard.html](https://muntasersyed.com/pollard.html)

Updated: 2026-11-13

[Software](https://muntasersyed.com/software.html)  / Pollard

# Pollard.

A runtime for agent work with explicit resource limits, approval gates, inspectable execution trees, and replay.

Build on your agent loop.

Explore the runtime, integration guides, and local examples.

[GitHub repository](https://github.com/jemsbhai/pollard)

Agent infrastructure

## Govern each step of agent work.

Pollard records model and tool calls in a content-addressed execution tree. Keep your application’s model clients and agent loop while adding explicit controls at the call boundary.

LIMIT

### Bound the work

Set token and step allowances, refuse work that exceeds known limits, and share resource scopes across workers. Branches and delegated assignments carry their inherited constraints.

[Teams and shared limits](https://github.com/jemsbhai/pollard/blob/v1.6.2/docs/teams.md)

GATE

### Control actions before execution

Resolve tool calls against versioned action definitions. Policies can allow, refuse, or require approval; delegated permissions can narrow as tasks pass between agents.

[Permissions and durable approvals](https://github.com/jemsbhai/pollard/blob/v1.6.2/docs/teams.md)

REPLAY

### Inspect a recorded run

Use stored semantic steps to audit a run and replay recorded results in tests. Branch and rollback operations preserve the recorded history while you explore alternatives.

[Runtime documentation](https://github.com/jemsbhai/pollard)

Packages / November 13, 2026

## Choose a language runtime.

Python, TypeScript, and Rust have independent release versions. The native TypeScript and Rust releases target Python 1.6.0 runtime behavior; Python 1.6.2 includes the optional Codex CLI adapter.

PYTHON · 1.6.2

### pollard

Install with `pip install pollard`. Includes agent teams, inherited scopes, checkpoints, durable approvals, and optional Codex CLI task integration. Python 3.10 or newer.

[PyPI](https://pypi.org/project/pollard/) [Quick start](https://github.com/jemsbhai/pollard/blob/v1.6.2/README.md)

TYPESCRIPT · 0.2.0

### pollardai

Install with `npm install pollardai`. The native Node.js runtime supports streaming, replay, persistent stores, shared resource limits, provider adapters, and audit tools.

[npm](https://www.npmjs.com/package/pollardai) [TypeScript documentation](https://github.com/jemsbhai/pollard/tree/main/packages/npm)

RUST · 0.2.1

### pollardai

Install with `cargo add pollardai`. The native Rust runtime includes eight storage backends, async streaming, shared resource limits, replay, and audit tools.

[crates.io](https://crates.io/crates/pollardai) [Rust documentation](https://github.com/jemsbhai/pollard/tree/main/crates/pollardai)

Build with Pollard

## Begin locally, then connect your tools.

The Python quick start uses an ordinary local function, so you can inspect a governed run before connecting a model provider.

FIRST RUN

### A small execution tree

Install the Python package and follow the credential-free example. Create a runtime, set a token and step allowance, invoke a local model callable, and inspect the resulting node and usage report.

[Follow the quick start](https://pypi.org/project/pollard/)

DELEGATION

### Give each agent a scope

Build a team with recorded task identities and separate cursors. Delegate work with inherited resource limits and narrowed tool permissions, then inspect dependencies and results together.

[Team guide](https://github.com/jemsbhai/pollard/blob/v1.6.2/docs/teams.md)

CODEX CLI

### Record and replay a coding task

Python 1.6.2 adds an optional adapter for Codex CLI tasks. Record the task inputs and returned answer, apply execution controls, and reuse the stored result through strict replay.

[Codex integration guide](https://github.com/jemsbhai/pollard/blob/v1.6.2/docs/codex-cli.md)

Research and materials

## Governed semantic execution trees.

The paper connects agent control, audit records, and replay across frameworks.

IEEE ICTAI 2026 · ACCEPTED PAPER

### Pollard: Governed Semantic Execution Trees for Framework-Independent AI Agent Control and Replay

Muntaser Syed and Marius Silaghi. Presented November 3, 2026 at IEEE ICTAI in Boca Raton. Preprint: arXiv:2610.16145.

[Paper details](https://muntasersyed.com/research.html#pollard-ictai) [Read preprint](https://arxiv.org/abs/2610.16145) [Presentation slides](https://docs.google.com/presentation/d/1e604yMBf24acaQI1UIJw_0B_Fq7zc_IuAh1ELziU-94/edit?usp=sharing) [Slides as PDF](https://docs.google.com/presentation/d/1e604yMBf24acaQI1UIJw_0B_Fq7zc_IuAh1ELziU-94/export/pdf)

WORKING EXAMPLES

### Swarm Forest and ReleaseProof

Swarm Forest explores governed agent teams with shared limits and drift detection. ReleaseProof connects evaluation results, approval, execution controls, and drift holds in an agent-release workbench.

[Swarm Forest](https://muntasersyed.com/projects.html#swarm-forest) [ReleaseProof](https://muntasersyed.com/projects.html#releaseproof) [Watch the walkthrough](https://muntasersyed.com/speaking.html#recording-swarm-forest)

Talks and workshops

## Learn through practical sessions.

Conference sessions connect the runtime to governed agent workflows and open-source development.

DEVFEST TAMPA · NOVEMBER 14, 2026

### Govern Your Agents: Budgets, Approval Gates, and Exact Replay with Pollard

A hands-on workshop at DevFest Tampa 2026: Build, Secure, Scale, at USF Tampa Campus, Engineering Building II. Exercises cover resource limits, action approval, evidence verification, and strict replay.

[Workshop and event details](https://muntasersyed.com/speaking.html#devfest-tampa-2026) [Workshop materials](https://github.com/jemsbhai/devfestTampaPollard2026)

DEVFEST MIAMI · DECEMBER 5, 2026

### Build a Creative AI Agent You Can Budget, Inspect, and Replay

An accepted hands-on Python workshop at DevFest Miami 2026: AI + Art Edition, at Mana Tech Loft 10.

[Workshop and event details](https://muntasersyed.com/speaking.html#devfest-miami-2026)

HACKTOBERFEST ORLANDO · OCTOBER 22, 2026

### Shipping the Pollard Ecosystem

A practical session on packaging, testing, documenting, and releasing Python, JavaScript, and Rust libraries, illustrated with tokenmaster and Pollard.

[Talk details](https://muntasersyed.com/speaking.html#hacktoberfest-orlando-2026) [Slides](https://docs.google.com/presentation/d/1H8mMlLhTkxyCuWazhVCCiSH1fCxlTna2/edit?usp=sharing)

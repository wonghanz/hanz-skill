# Hanz Skill Vault

**45 agent skills** for coding assistants — 35 original, 10 vendored from MIT
upstreams. Built for **Google Antigravity**, **Claude Code**, **OpenCode**,
**Codex**, and anything else that reads the Agent Skill spec.

> **This repo is private.** The skills are working tools carried through real
> job searches and security work, not a showcase. Where a skill states a rule
> below, the rule is quoted from its own `SKILL.md`.

---

## Find what you need

Start here. Pick the row closest to your situation.

| I want to… | Go to |
| :--- | :--- |
| **Get a job** — start anywhere in the pipeline | [`resume`](skills/resume/) (coordinator) or [`technical-job-search`](skills/technical-job-search/) |
| Analyze one job posting before applying | [`job-description-analyzer`](skills/job-description-analyzer/) |
| Rewrite weak resume bullets into measured ones | [`resume-bullet-writer`](skills/resume-bullet-writer/), [`resume-quantifier`](skills/resume-quantifier/) |
| Prove resume claims from code I actually wrote | [`repo-to-resume`](skills/repo-to-resume/) |
| Prepare for a specific interview, or debrief one | [`interview-coach`](skills/interview-coach/), [`interview-prep-generator`](skills/interview-prep-generator/) |
| Compare offers or negotiate pay | [`offer-comparison-analyzer`](skills/offer-comparison-analyzer/), [`salary-negotiation-prep`](skills/salary-negotiation-prep/) |
| Change industry and translate what I have | [`career-changer-translator`](skills/career-changer-translator/) |
| Audit a codebase for vulnerabilities | [`security-audit`](skills/security-audit/) |
| Contribute a security fix upstream, safely | [`open-source-security-contribution`](skills/open-source-security-contribution/) |
| Stop an agent leaking secrets or running blind destructive commands | [`aegis-guard`](skills/aegis-guard/), [`nodiguard`](skills/nodiguard/) |
| Write or review production code more carefully | [Engineering suite](#engineering-suite) — 8 vendored practice skills |
| Draw a system / sequence / data-flow diagram | [`archify`](skills/archify/) |
| Build a frontend that doesn't look templated | [`design-taste-frontend`](skills/design-taste-frontend/), [`apple-design`](skills/apple-design/) |
| Render furniture CAD into photoreal previews | [`furniture-cad-render`](skills/furniture-cad-render/) |
| Check a Chinese rental contract for unfair clauses | [`rentguard-ai`](skills/rentguard-ai/) |
| Produce video with React | [`remotion-best-practices`](skills/remotion-best-practices/) |
| Install these into my own agent | [Installation](#install) |
| See what was evaluated and *rejected* | [VENDORED.md](VENDORED.md) |

---

## The thinking behind the vault

The bet underneath all of this: **an agent's competence is not the bottleneck —
its accountability is.** Models will happily produce a resume bullet, a
vulnerability rating, or a `rm -rf` that *sounds* right. What they don't do by
default is show the evidence, flag the guess, or stop before an action you can't
undo. Every skill here is an attempt to bolt one of those three things onto a
workflow. Four patterns carry most of the weight:

**1. Irreversible decisions stay with the human.**
[`open-source-security-contribution`](skills/open-source-security-contribution/)
defines three explicit gates, and the last one has no exceptions:

> **Before `git commit`, `git push`, or opening a PR** — always. No exceptions,
> even if earlier gates passed.

The same shape recurs: [`security-and-hardening`](skills/security-and-hardening/)
has an *Ask First (Requires Human Approval)* tier;
[`security-audit`](skills/security-audit/) prohibits ungated destructive
operations by autonomous tools; `aegis-guard` and `nodiguard` demand a blast
radius count — "how many files, processes, systems does this touch" — before a
risky command executes.

**2. Claims need a boundary and a result.**
`security-audit` won't accept a theoretical finding; it asks for reachable
input, a violated boundary, and an observable outcome, and it insists on
*separating priority from certainty* so "probably fine" can't masquerade as
"verified". `repo-to-resume` extracts achievement evidence from commits and
code that exist rather than inventing plausible-sounding work.
[`interview-coach`](skills/interview-coach/) scores answers against a written
rubric and counts sessions from log rows instead of remembering vaguely.

**3. An honest guess beats a confident lie.**
Where a real number is missing, `resume-quantifier` makes you emit
`[Metric]: Conservative estimate using [method]` — the estimate is labelled, not
laundered into fact. `application-form-filler` says *"rate honestly — inflated
ratings create problems in technical interviews."*
[`code-review-and-quality`](skills/code-review-and-quality/) goes the other way
on politeness: *"Don't soften real issues. 'This might be a minor concern' when
it's a bug that will hit production is dishonest."*

**4. Scope should be defined by what a skill refuses to do.**
This one is the vault's weakest discipline, and it's worth stating exactly how
weak: only **2 of 45** descriptions carry an explicit do-not-trigger clause —
[`technical-job-search`](skills/technical-job-search/), which declines "general
career advice unrelated to an active search", and the vendored
[`design-taste-frontend`](skills/design-taste-frontend/). It matters
disproportionately anyway, because every installed skill's description sits in
the model's context permanently and each one competes to be selected, so a loose
trigger quietly degrades all the others. The burden is instead carried
structurally: [`resume`](skills/resume/) exists purely to route, orchestrating
sub-skills by workflow phase rather than letting fifteen fire on their own — and
it's why the [vendoring bar is high](VENDORED.md), with ~200 rejected candidates
documented rather than quietly dropped.

### What you can take from it

If you're building your own skills, the reusable parts are the patterns, not the
career content:

- **Gate tables** — name the actions that require a human, and say which gate is
  unconditional. Cheaper to write once than to recover from a bad push.
- **Conservative-estimate labels** — a syntax for "this is a guess" that still
  lets the output be useful.
- **Negative triggers in descriptions** — tell a skill what it is *not* for; it's
  the main lever against over-firing.
- **A coordinator skill per domain** — one router that knows the phases beats
  fifteen skills competing for the same prompt.
- **State files with staleness checks** — `interview-coach` keeps
  `coaching_state.md` with archival rules and schema migration, so long-horizon
  coaching survives a fresh context window.
- **Provenance as a first-class file** — [VENDORED.md](VENDORED.md) records
  upstream commits, retained `LICENSE`s, and the rejection reasons. A vault that
  can't say where its parts came from isn't maintainable.

### Honest shape of the collection

27 of the 45 skills are the career/resume suite, because that's the problem this
vault was built against — a full technical job search, end to end, with fewer
invented facts. Security is four skills driven by a deliberate study of real
application-security fixes. Design and multi-modal is four. The engineering
suite is entirely borrowed, and says so.

---

## Package anatomy

Every skill follows the modern Agent Skill specification:

- **`SKILL.md`** — frontmatter (`name`, `description` with triggers and negative
  triggers) plus the execution procedure.
- **`references/`** — schemas, rulebooks, templates, and stage detail, pulled in
  on demand so `SKILL.md` stays short.
- **`scripts/`** — runnable automation where the task is mechanical enough to
  deserve it (CAD render pipeline, security inspection, archify's renderers).

---

## Skills catalog

### 🛡️ Security & Cyber-Defense Suite

| Skill | Description | Key Capabilities |
| :--- | :--- | :--- |
| [`aegis-guard`](skills/aegis-guard/) | AI cybersecurity sentinel | Adversarial prompt-injection defense, Zero-Leak DLP policy, blast-radius verification before destructive commands. |
| [`open-source-security-contribution`](skills/open-source-security-contribution/) | Open-source security fix contribution pipeline | Issue discovery ranked by learning value, isolated local reproduction, failing regression test, minimal fix, three human approval gates before commit/push/PR. |
| [`nodiguard`](skills/nodiguard/) | Zero-trust local AI security proxy | Hardcoded secret neutralization, tokenized prompt isolation, memory safety enforcement. |
| [`security-audit`](skills/security-audit/) | Multi-phase codebase security audit | 13 attack classes, machine-readable finding ledgers, Cloudflare edge rule validation, automated reporting. |

---

### 💼 Career, Resume & Job Search Suite

| Skill | Description | Highlights |
| :--- | :--- | :--- |
| [`academic-cv-builder`](skills/academic-cv-builder/) | Academic CV formatting & builder | Publications, grant proposals, teaching dossier, and tenure-track CV structuring. |
| [`application-form-filler`](skills/application-form-filler/) | Intelligent job application field filler | Context-aware, tailored answers mapped directly from candidate profile and JD. |
| [`career-changer-translator`](skills/career-changer-translator/) | Cross-industry skill translator | Identifies transferable competencies, reframes prior achievements for new target domains. |
| [`cold-email-writer`](skills/cold-email-writer/) | High-conversion cold outreach writer | Crafts concise, human, personalized outreach to founders and hiring managers. |
| [`cover-letter-generator`](skills/cover-letter-generator/) | Targeted cover letter generator | Compelling narrative bridge between resume achievements and job descriptions. |
| [`creative-portfolio-resume`](skills/creative-portfolio-resume/) | Creative resume builder | Balances visual design flair with strict ATS parseability for designers and artists. |
| [`executive-resume-writer`](skills/executive-resume-writer/) | C-suite & VP executive resume writer | Emphasizes P&L ownership, board-level communication, and enterprise vision. |
| [`interview-coach`](skills/interview-coach/) | Full-cycle high-rigor interview coach | Rubric scoring, storybank manager, session state with staleness checks, mock drills across PM, Eng, Design, Data, and Ops. |
| [`interview-prep-generator`](skills/interview-prep-generator/) | Targeted interview preparation | Formulates STAR stories, expected technical/behavioral questions, and talking points. |
| [`job-description-analyzer`](skills/job-description-analyzer/) | Deep job posting analyzer | Calculates match score, uncovers unspoken requirements, and flags critical qualification gaps. |
| [`linkedin-profile-optimizer`](skills/linkedin-profile-optimizer/) | LinkedIn profile optimization | Recruiter SEO keywords, headline hooks, punchy "About" copy, and featured work curation. |
| [`offer-comparison-analyzer`](skills/offer-comparison-analyzer/) | Total compensation & offer evaluator | Side-by-side equity, base, bonus, vesting cliffs, tax implications, and benefits comparison. |
| [`portfolio-case-study-writer`](skills/portfolio-case-study-writer/) | Portfolio deep-dive case study writer | Expands bullet points into full narrative case studies (Problem, Discovery, Solution, Impact). |
| [`reference-list-builder`](skills/reference-list-builder/) | Professional reference manager | Formats professional references and equips referees with prep kits and talking points. |
| [`repo-to-resume`](skills/repo-to-resume/) | Codebase-to-Resume extractor | Mines GitHub repositories for evidence-based bullet points; compiles live LaTeX resumes. |
| [`resume`](skills/resume/) | Master career & resume coordinator | Orchestrates all resume lifecycle sub-skills based on user goals and workflow phase. |
| [`resume-ats-optimizer`](skills/resume-ats-optimizer/) | ATS scanner & keyword optimization | Keyword frequency scoring, ATS parser compatibility checks, format sanitization. |
| [`resume-bullet-writer`](skills/resume-bullet-writer/) | Impact-driven bullet point writer | Transforms passive job duties into metric-anchored achievement bullets (X-Y-Z formula). |
| [`resume-formatter`](skills/resume-formatter/) | Layout & visual hierarchy formatter | Clean scannable layouts, ATS compliance, font hierarchy, and whitespace balance. |
| [`resume-quantifier`](skills/resume-quantifier/) | Metric & impact quantification | Discovers hidden opportunities for metrics; labels estimates as conservative estimates with their method. |
| [`resume-section-builder`](skills/resume-section-builder/) | Modular resume section builder | Customizes Education, Skills, Experience, and Project sections by seniority level. |
| [`resume-tailor`](skills/resume-tailor/) | Job-specific resume tailoring | Aligns existing experience with target job postings without inventing experience. |
| [`resume-version-manager`](skills/resume-version-manager/) | Resume version tracking & control | Maintains master source-of-truth resume while managing specialized variant branches. |
| [`resumecraftr`](skills/resumecraftr/) | Modular JSON-driven resume engine | JSON-first CV architecture, instant schema validation, and exportable modern templates. |
| [`salary-negotiation-prep`](skills/salary-negotiation-prep/) | Salary & compensation negotiation | Market compensation research, negotiation strategy playbooks, and counter-offer scripts. |
| [`tech-resume-optimizer`](skills/tech-resume-optimizer/) | Tech industry resume optimizer | Tailored for Software Engineers, Tech Leads, Engineering Managers, and PMs. |
| [`technical-job-search`](skills/technical-job-search/) | Full technical job search copilot | End-to-end guidance from initial application to final offer negotiation. |

---

### 🎨 Design, Video & Multi-Modal Suite

| Skill | Description | Key Capabilities |
| :--- | :--- | :--- |
| [`apple-design`](skills/apple-design/) | Apple design system & fluid motion | Physical spring animations, gesture-driven UI, translucent materials, and Apple typography. |
| [`furniture-cad-render`](skills/furniture-cad-render/) | Furniture CAD photorealistic render pipeline | Multi-angle CAD analysis, Qwen-VL/Image pipeline, automated consistency verification. |
| [`remotion-best-practices`](skills/remotion-best-practices/) | Remotion React video production standards | 30+ production rules covering composition, animations, audio, captions, and rendering. |
| [`rentguard-ai`](skills/rentguard-ai/) | RentGuard AI 租房合同霸王条款透视镜 | Multi-modal OCR contract scanner, PRC Civil Code compliance, risk scoring, and counter-tactics. |

---

<a id="engineering-suite"></a>

### ⚙️ Engineering Practice & Diagramming Suite (vendored)

Not original work — 10 skills copied from upstream MIT projects, each keeping its
own `LICENSE`. See [VENDORED.md](VENDORED.md) for exact commits and for the repos
that were evaluated and deliberately rejected.

| Skill | Upstream | Purpose |
| :--- | :--- | :--- |
| [`security-and-hardening`](skills/security-and-hardening/) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Hardens code against OWASP-class vulnerabilities; input handling, auth, storage. |
| [`code-review-and-quality`](skills/code-review-and-quality/) | addyosmani/agent-skills | Multi-axis review before a change reaches main; honest about severity. |
| [`debugging-and-error-recovery`](skills/debugging-and-error-recovery/) | addyosmani/agent-skills | Root-cause discipline for unexpected failures. |
| [`test-driven-development`](skills/test-driven-development/) | addyosmani/agent-skills | Red-green-refactor loop for logic and behaviour changes. |
| [`api-and-interface-design`](skills/api-and-interface-design/) | addyosmani/agent-skills | Stable contracts across modules and services. |
| [`performance-optimization`](skills/performance-optimization/) | addyosmani/agent-skills | Regressions, Core Web Vitals, N+1 patterns, profiling. |
| [`observability-and-instrumentation`](skills/observability-and-instrumentation/) | addyosmani/agent-skills | Logging, metrics, tracing, alerting for production paths. |
| [`git-workflow-and-versioning`](skills/git-workflow-and-versioning/) | addyosmani/agent-skills | Atomic commits, branching, conflict resolution, PR hygiene. |
| [`design-taste-frontend`](skills/design-taste-frontend/) | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Audit-first, non-templated frontend work; installed under its frontmatter name. |
| [`archify`](skills/archify/) | [tt-a1i/archify](https://github.com/tt-a1i/archify) | Architecture, sequence, data-flow and lifecycle diagrams as standalone HTML. Attribution to Cocoon-AI travels with it. |

`archify` is trimmed for this vault: its `test/` suite and rendered HTML demos
are dropped, keeping only the 14 JSON schema examples that `SKILL.md` reads at
runtime (8.6 MB → 2.6 MB). No runtime npm dependencies; requires Node >= 18.

---

<a id="install"></a>

## 🛠️ Installation & Quick Start

Install a few skills, not all 45. Every installed skill's name and description
enters your agent's context permanently, and each one competes with the others
to be selected — a bloated skill directory measurably degrades which skill
actually fires.

### Google Antigravity

```bash
git clone https://github.com/wonghanz/hanz-skill.git

# One skill:
cp -r hanz-skill/skills/security-audit ~/.gemini/config/skills/

# Or all of them, accepting the context cost:
cp -r hanz-skill/skills/* ~/.gemini/config/skills/
```

### Claude Code / OpenCode / Codex

```bash
cp -r hanz-skill/skills/<skill-name> ~/.claude/skills/
# or
cp -r hanz-skill/skills/<skill-name> ~/.codex/skills/
```

### Workspace-specific

```bash
mkdir -p my-project/.gemini/skills
cp -r hanz-skill/skills/security-audit my-project/.gemini/skills/
```

Qoder uses `<workspace>/.qoder/skills/<skill-name>/`.

### Verifying an install

If a skill registers but never triggers, check for a **UTF-8 BOM** before the
opening `---` of its frontmatter. It parses as description text instead of a
delimiter, so the skill loads with `---` as its description and becomes
unselectable:

```bash
head -c3 skills/<skill-name>/SKILL.md | xxd   # efbbbf means BOM is present
```

---

## 📁 Repository Structure

```
hanz-skill/
├── .gitignore
├── README.md
├── VENDORED.md
└── skills/
    ├── academic-cv-builder/
    ├── aegis-guard/
    ├── api-and-interface-design/
    ├── apple-design/
    ├── application-form-filler/
    ├── archify/
    ├── career-changer-translator/
    ├── code-review-and-quality/
    ├── cold-email-writer/
    ├── cover-letter-generator/
    ├── creative-portfolio-resume/
    ├── debugging-and-error-recovery/
    ├── design-taste-frontend/
    ├── executive-resume-writer/
    ├── furniture-cad-render/
    ├── git-workflow-and-versioning/
    ├── interview-coach/
    ├── interview-prep-generator/
    ├── job-description-analyzer/
    ├── linkedin-profile-optimizer/
    ├── nodiguard/
    ├── observability-and-instrumentation/
    ├── offer-comparison-analyzer/
    ├── open-source-security-contribution/
    ├── performance-optimization/
    ├── portfolio-case-study-writer/
    ├── reference-list-builder/
    ├── remotion-best-practices/
    ├── rentguard-ai/
    ├── repo-to-resume/
    ├── resume/
    ├── resume-ats-optimizer/
    ├── resume-bullet-writer/
    ├── resume-formatter/
    ├── resume-quantifier/
    ├── resume-section-builder/
    ├── resume-tailor/
    ├── resume-version-manager/
    ├── resumecraftr/
    ├── salary-negotiation-prep/
    ├── security-and-hardening/
    ├── security-audit/
    ├── tech-resume-optimizer/
    ├── technical-job-search/
    └── test-driven-development/
```

---

## 🔒 Security & DLP Compliance

Adheres to **NodiGuard Zero-Leak Data Loss Prevention (DLP)** standards:

- **No hardcoded secrets** — API keys, passwords, bearer tokens, and private credentials are excluded.
- **Environment decoupled** — scripts read credentials from environment variables supplied at runtime (`os.environ.get(...)`).
- **Strict `.gitignore`** — local `.env`, credential files, logs, and dev artifacts are filtered.
- **Vendored code is scanned too** — the 10 third-party skills were checked against AWS/GitHub/Anthropic/OpenAI/Slack/Google key formats, PEM private keys and JWTs; zero matches. The only hits repo-wide are detection-rule *text* in `aegis-guard`/`nodiguard` and base64-embedded fonts in `resumecraftr` templates.

---

## 📄 License

The 35 original skills in `skills/` are private work curated for personal and
team agent orchestration.

10 skills are **not** original: they are vendored from upstream MIT projects and
remain under those terms. Each vendored directory keeps its upstream `LICENSE`;
`archify` additionally keeps `THIRD_PARTY_NOTICES.md` and the OFL text for its
bundled JetBrains Mono font. Sources, commits, and rejected candidates are
recorded in [VENDORED.md](VENDORED.md).

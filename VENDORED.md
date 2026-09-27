# Vendored skills — provenance and license

Skills in this directory come from three sources. Anything below "vendored" is
third-party work; each skill directory carries its upstream `LICENSE` file.

## Original (hanz-skill)

35 skills authored here and maintained in this vault as the source of truth.
Re-installed into `<workspace>/.qoder/skills/` from `skills/*`.

## Vendored — MIT

`github.com/addyosmani/agent-skills` @ `main`, shallow clone 2026-09-27:

- api-and-interface-design
- code-review-and-quality
- debugging-and-error-recovery
- git-workflow-and-versioning
- observability-and-instrumentation
- performance-optimization
- security-and-hardening
- test-driven-development

`github.com/Leonxlnx/taste-skill` @ `main` — directory `skills/taste-skill`,
installed under its frontmatter name `design-taste-frontend`.

## Vendored — MIT, itself a derivative

`github.com/tt-a1i/archify` @ `main`, installed as `archify`. Upstream
`SKILL.md` declares MIT and credits `Cocoon-AI/architecture-diagram-generator`
(MIT, v1.0) as its base; that attribution travels with the copy, as do
`THIRD_PARTY_NOTICES.md` and the SIL OFL text for the bundled JetBrains Mono
font in `assets/`. The skill shells out to Node under `bin/` (plain `.mjs`, no
compiled binaries, zero runtime npm dependencies, Node >= 18). Trimmed for this
vault: `test/` and the rendered `examples/*.html` demos were dropped, keeping
the 14 JSON schema examples that `SKILL.md` reads at runtime (8.6 MB -> 2.6 MB).

## Deliberately not vendored

- `K-Dense-AI/scientific-agent-skills` (166 skills) — domain bindings for
  bio/chem/physics instrument and SaaS APIs, most requiring paid credentials.
  No overlap with the work these skills serve.
- 12 of 13 `taste-skill` variants (`brutalist-`, `minimalist-`, `soft-`,
  `output-`, `gpt-tasteskill`, `taste-skill-v1`, ...) — style-persona
  duplicates of the flagship, plus overlap with `apple-design`.
- `JetBrains/go-modern-guidelines` — the skill's whole premise is invoking a
  "Modern Go Guidelines CLI" that self-installs from the network on first use,
  and it only applies to Go.
- `Graphify-Labs/graphify` — a tool that *generates* skills, shipping
  lowercase `skill.md` plus aider/devin-specific variants. Not a loadable
  Agent Skill.
- `google/artemis` — contains zero `SKILL.md` files. It is an agent platform,
  not a skill pack.
- 15 remaining `addyosmani/agent-skills` entries — either self-referential
  once the vault is installed (`using-agent-skills`) or duplicative of
  existing planning behaviour (`planning-and-task-breakdown`,
  `spec-driven-development`, `incremental-implementation`).

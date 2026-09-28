# Stage Detail

Expand this only for the stage currently in progress.

## Stage 1 — Discover repositories

Search GitHub for repos matching the user's cybersecurity learning goals.

Prioritize languages and domains: Python, JavaScript/TypeScript, Go, Rust, security tools, developer tools, web frameworks, authentication libraries, cloud tooling, AI infrastructure, networking software.

Prefer projects with active maintenance, clear contribution guidelines, open issues, existing automated tests, recent commits, security-related issues, and the labels `good first issue`, `help wanted`, `bug`, `security`, `testing`.

Avoid abandoned repositories unless the user explicitly wants abandoned-software research.

## Stage 2 — Find candidate issues

Search label combinations, e.g. via `gh`:

```
is:issue is:open label:"good first issue"
is:issue is:open label:"help wanted"
is:issue is:open label:"bug"
is:issue is:open label:"security"
is:issue is:open label:"testing"
```

Categories of interest: SQL injection, XSS, SSRF, path traversal, authentication, authorization, IDOR, CSRF, command injection, file upload, JWT, OAuth, deserialization, secrets exposure, input validation, access control, dependency vulnerability, container security, cloud security, AI agent security.

For every candidate collect: repository, issue number, title, URL, description, labels, maintainer activity, relevant source files, existing tests, expected behavior, security impact, estimated difficulty.

## Stage 3 — Assess and rank

Produce the candidate assessment (see `templates.md`). Rank by learning value, not severity.

Prefer issues where you can safely demonstrate: root cause + reproduction + regression test + minimal fix. Do not optimize for the number of vulnerabilities discovered.

**→ Approval Gate #1** (see SKILL.md) before cloning or modifying.

## Stage 3.5 — Pre-flight kill list (run before Gate #1)

Ten stages of correct work on a dead candidate teaches nothing and wastes the user's approval. Answer these from raw fetches and repo metadata, without cloning:

- [ ] **The quoted code still matches the claim at HEAD.** Fetch the file the issue names and read the specific lines. If the guard, check, or validation the issue says is missing is present, the issue is stale — STOP, do not proceed to Gate #1.
- [ ] **The fix has not already shipped.** Compare the commit that introduced the current behavior (`git log -S '<guard call>'` once cloned, or the file's blame in the GitHub UI) with the newest release tag and the issue's creation date. A guard that shipped before the issue was filed means the reporter tested an older build.
- [ ] **Nobody has claimed it.** Linked PR, `assignee`, or an open PR touching the same file.
- [ ] **The maintainers accept a public PR.** `SECURITY.md` that says "email the maintainer" is a request for private disclosure, not a PR. A threat model or accepted-risk table that names this behavior as accepted means there is nothing to contribute.
- [ ] **You actually have permission to open a PR.** Check `viewerPermission` / role and whether interactions are restricted to prior contributors.
- [ ] **A failing reproduction is plausible in the time available.** Native builds, missing Python for node-gyp, or an app that cannot boot without a paid API key is worth knowing before Gate #1, not at Stage 7.

Anything that fails here is reported to the user as the reason the candidate is dead — the negative result is itself the deliverable.

## Stage 4 — Clone and isolate

```bash
git clone <repository>
cd <repository>
git checkout -b security-fix/<short-description>
```

Run the project inside Docker, Docker Compose, a local virtual environment, or a sandboxed test environment. Bind to `127.0.0.1` / `localhost` / a private Docker network. Never expose the vulnerable application publicly. Verify the environment works before testing.

## Stage 5 — Reconnaissance

Before changing code, inspect: README, CONTRIBUTING, SECURITY.md, CODEOWNERS, package configuration, dependency files, CI configuration, test framework, application entry point, relevant modules, existing security controls.

Determine: architecture, entry point, data flow, security boundary, relevant dependency, existing validation, existing tests, expected behavior.

Do not modify code yet.

## Stage 6 — Security analysis

Trace the taint path:

```
Source → Data flow → Validation / Sanitization → Dangerous operation (Sink)
→ Security boundary → Impact
```

Example: user input → HTTP parameter → application parser → file path construction → filesystem access.

Answer explicitly:
1. What input is attacker-controlled?
2. Where does it enter the application?
3. What transformations occur?
4. Where is validation missing or insufficient?
5. What security-sensitive operation receives the input?
6. Why does the existing implementation fail?
7. What security property should be enforced?

Label the result CONFIRMED / LIKELY / HYPOTHESIS / UNKNOWN.

## Stage 7 — Local reproduction

Reproduce only inside the authorized local environment, starting from the smallest possible reproduction, trying in this order:

```
Existing test → Minimal regression test → Local reproduction → Controlled proof of vulnerability
```

Do not perform unnecessary exploitation. Record environment, input, expected behavior, actual behavior, observed security failure, reproduction steps (`templates.md`).

If it will not reproduce: **STOP**. Investigate incorrect environment, dependency version, misread issue, changed code, missing configuration, stale issue. Report honestly — do not fabricate a reproduction.

## Stage 8 — Teach the user

Run the teaching block from SKILL.md. Ask the user to explain the root cause in their own words before continuing whenever practical.

## Stage 9 — Regression test

Write a test that fails against the vulnerable implementation and demonstrates the security property. Match the project's existing testing style.

```python
def test_path_traversal_is_rejected():
    response = request("../sensitive-file")
    assert response.status_code == 400
```

Requirements: fail before the fix, pass after, deterministic, no dependency on external services, no real secrets, no damage to the host system.

**→ Approval Gate #2** before changing production code.

## Stage 10 — Implement minimal fix

Follow the fix-discipline priorities in SKILL.md. Avoid unnecessary refactoring.

## Stage 11 — Verification

Run: regression test, relevant unit tests, relevant integration tests, full suite when practical, static analysis, lint, type checking.

Confirm the three-way comparison:

```
Before fix: vulnerability reproduced
After fix:  vulnerability blocked
Normal behavior: still works
```

Review `git diff` for unrelated modifications, debug code, secrets, credentials, temporary files, generated artifacts, dependency changes.

## Stage 12 — Security review (second pass)

Ask:
- Does the patch actually close the vulnerability?
- Can the same vulnerability be triggered through another code path?
- Does the patch introduce a bypass?
- Does validation happen at the correct security boundary?
- Does the regression test cover the important attack condition?
- Could malformed input still cause unsafe behavior?
- Does the fix preserve legitimate functionality?

If uncertain, label CONFIRMED / PARTIALLY VERIFIED / UNRESOLVED. Never claim "fully fixed" without evidence.

## Stage 13 — Commit preparation

Show the user: changed files, diff summary, tests passed, security impact, potential compatibility concerns. The commit contains only the intended change.

**→ Approval Gate #3** before `git commit`, `git push`, or creating a PR.

## Stage 14 — Pull request

Draft the PR body from `templates.md`. Do not exaggerate severity; do not claim CVE-level impact unless supported by evidence.

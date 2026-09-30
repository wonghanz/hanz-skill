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

Ten stages of correct work on a dead candidate teaches nothing and wastes the user's approval. Answer these from raw fetches and repo metadata, without cloning. **Check governance before code**: a repo policy that forbids the contribution voids every line of code analysis spent on it, and the read costs three files instead of an afternoon.

- [ ] **Does this project have a contribution path you qualify for?** Read `AGENTS.md`, `.github/copilot-instructions.md`, `SECURITY.md` and `CONTRIBUTING.md` before any code. Repos increasingly gate agent-assisted work: some require a maintainer-approved Proposal *and* Design issue before implementation — under higress's policy, confirming a defect and choosing a verification approach already counts as "material participation", so the gate binds before a line is written; some run an issue-*claim* protocol where another agent may already hold it; some bar public issues and PRs for vulnerabilities outright. Confirm `gh api repos/<r> --jq .permissions` too — if their exception demands `maintain`/`admin` and you have `pull:true, push:false`, there is no path and the bug is somebody else's to fix.
- [ ] **Match policy wording by intent, not literal phrase.** A filter hunting `do not create a public` returned `public-ok` for a repo whose SECURITY.md says "Please do NOT report security vulnerabilities through public GitHub issues, discussions, or pull requests". Read the file yourself for whatever candidate reaches the shortlist; never trust the automation's verdict on the disclosure channel.
- [ ] **The quoted code still matches the claim at HEAD.** Fetch the file the issue names and read the specific lines. If the guard, check, or validation the issue says is missing is present, the issue is stale — STOP, do not proceed to Gate #1.
- [ ] **The fix has not already shipped.** Compare the commit that introduced the current behavior (`git log -S '<guard call>'` once cloned, or the file's blame in the GitHub UI) with the newest release tag and the issue's creation date. A guard that shipped before the issue was filed means the reporter tested an older build. Re-fetch the issue's own `state` immediately before Gate #1 — search indexes lag, and smithers#2936 was claimed, fixed and closed between my scan and my reading of it.
- [ ] **Nobody has claimed it.** Linked PR, `assignee`, or an open PR touching the same file.
- [ ] **Do the maintainers treat this as a bug at all?** A `SECURITY.md` that says "email the maintainer" is a request for private disclosure, not a PR — Questarr's #1081 had a tested fix sitting on a fork by the time that line was read. An accepted-risk table or threat model that names this behavior accepted means there is nothing to contribute. The positive signal is equally worth looking for: sibling issues carrying a `security` label show the project does not consider the behavior by-design.
- [ ] **You actually have permission to open a PR.** Check `viewerPermission` / role and whether interactions are restricted to prior contributors.
- [ ] **Who filed the issue?** An issue self-filed by an active maintainer is usually their own todo list, not an open invitation — compare the author against the recent commit list and their activity that day. Not a kill on its own, but a Gate #1 caveat: the acceptance window can close in hours while you are still writing tests.
- [ ] **Is the fix the issue proposes even expressible here?** Read the actual interface you are told to use (the vendored `.d.ts`, the type stubs, the SDK docs) and list its members. If the API has no way to distinguish what the issue wants distinguished, that half is unimplementable — plan to ship the verified part and name the rest as open rather than inventing a mechanism.
- [ ] **A failing reproduction is plausible in the time available.** Native builds, missing Python for node-gyp, an app that cannot boot without a paid API key, or a fix that lives in a submodule of a different repository are all worth knowing before Gate #1, not at Stage 7.

Anything that fails here is reported to the user as the reason the candidate is dead — the negative result is itself the deliverable. A confirmed, well-described, genuinely exploitable bug with no contribution path you qualify for is still a dead candidate: do not let the quality of the analysis talk you into proposing the PR anyway, and do not let a user's "make sure you actually fix a bug" pressure turn a blocked path into an end-run around a project's stated policy.

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

Read the project's contribution policy **as written** before the first push: does it require `git commit -s` / a `Signed-off-by` trailer (DCO), a GPG signature, an issue link in the body, a PR template, or a label? A missing trailer fails the DCO check and forces an amend plus a force-push to your own PR branch.

Do not infer the requirement from recent commit history — squash-merging and bot commits hide trailers that human contributors are still required to write. Read `CONTRIBUTING.md`.

Draft the PR body from `templates.md`. Do not exaggerate severity; do not claim CVE-level impact unless supported by evidence.

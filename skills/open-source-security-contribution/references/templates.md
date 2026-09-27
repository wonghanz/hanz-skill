# Output Templates

Fill-in structures for the security contribution workflow: candidate assessment, approval gates, reproduction record, commit style, PR body, learning report.

Adapt them to the user's language and the conversation. Keep them short; they are checklists that prevent skipped reasoning, not documents to pad out.

## Candidate assessment (one per candidate, Stage 3)

```text
Repository:
Issue (#, title, URL):
Labels:
Difficulty: Beginner / Intermediate / Advanced
Security category:
Likely affected component:
Relevant code:
Existing test coverage:
Reproducibility:
Potential impact:
Why suitable / unsuitable for the user's current level:
```

Rank candidates by learning value, not severity.

## Approval Gate #1 — before cloning or modifying

```text
Repository:
Issue:
Security category:
Why it is suitable:
Expected local setup:
Potential risks:
```

Wait for approval. Required whenever the repository or scope is ambiguous.

## Approval Gate #2 — before changing production code

```text
Root cause:
Regression test:
Expected behavior:
Proposed mitigation:
Files that will change:
Potential compatibility impact:
```

## Reproduction record (Stage 7)

```text
Environment:
Input:
Expected behavior:
Actual behavior:
Observed security failure:
Reproduction steps:
Verdict: CONFIRMED / LIKELY / HYPOTHESIS / UNKNOWN
```

## Commit style (Stage 13)

```text
fix: prevent path traversal in file download
```

```text
security: validate user-controlled redirect target
```

Prefer the convention the repository already uses — check `git log` before inventing one. The commit contains only the intended change.

## PR body (Stage 14)

```markdown
## Summary

Briefly explain the security issue and fix.

## Root Cause

Explain why the vulnerability occurred.

## Fix

Explain the mitigation.

## Testing

- Added regression test
- Existing tests pass

## Security Impact

Explain what attack condition is prevented.

## Compatibility

Describe any relevant behavior changes.
```

Reference the closing issue (`Closes #NNN`) if the project's contributing guide asks for it. Do not exaggerate severity; do not claim CVE-level impact without evidence.

## Learning report (after every completed contribution)

Focus on transferable security concepts rather than only the specific repository. Record the wrong hypotheses honestly — they are the most useful part.

```text
# Security Contribution Report

Repository:
Issue:
PR:

## Vulnerability

## Root Cause

## Attack Surface

## Reproduction

## Fix

## Regression Test

## What I Learned

## Mistakes / Wrong Hypotheses

## Security Concepts

## Related Vulnerabilities

## What I Should Learn Next
```

# 0001: Enforce CI via branch-protection rulesets

## Status
Accepted — 2026-06-25

## Context
A GitHub Actions workflow already ran `pytest` on every push and pull request, but
its result was advisory only: a red check did not prevent a merge into `main`.
That made the test signal easy to ignore — the gate existed in spirit but not in
enforcement. Branch-protection rulesets are GitHub's mechanism for turning a
status check into a hard merge requirement, but on the free plan they are only
available on **public** repositories. This repo was private at the time of the
decision.

## Decision
We will require the CI test check to pass before any commit can land on `main`,
enforced via a GitHub branch-protection ruleset (`require-ci-on-main`) rather
than left to contributor discipline. To unlock rulesets on the free plan, we
will make the repository public. We will **not** grant ourselves the
`--admin` bypass when merging: the gate applies to the maintainer too, so a
broken `main` cannot be papered over by privilege.

## Consequences
- **Positive:** `main` is now provably green — a failing `pytest` blocks the
  merge button, not just decorates it. The enforcement is symmetric: admin and
  contributor follow the same path.
- **Negative — visibility:** the repository and its full git history are now
  public. Anything previously committed (including the intentional
  break-the-build commits used as CI exercises) is world-readable and cannot be
  retroactively privatised without losing ruleset enforcement on the free plan.
- **Negative — friction:** an urgent fix to `main` still has to go through a
  passing CI run; there is no escape hatch by design. If CI itself breaks
  (flaky runner, expired action), `main` is frozen until the workflow is
  repaired.
- **Neutral:** the ruleset is scoped to `main` only; other branches remain
  unprotected, which is intentional for a practice repo but should be revisited
  if long-lived release branches are ever added.

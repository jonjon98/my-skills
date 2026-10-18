# State machine

One row per phase. The supervisor runs the phases in this order and never skips one. A phase's **pass check** is something it can read from a file or from git, never an agent's claim.

| Phase | Owner | Tier | Writes | Pass check | On failure |
|---|---|---|---|---|---|
| Config | supervisor | none | `config.env` | file holds every key | ask the user for the missing values |
| Preflight | `ship-preflight` agent | cheap | `context.md` repo facts, `reports/preflight-1.md` | report status `done` | blocked report |
| Plan | supervisor, using `ship-plan` | session model, cheap context-pull agent | `context.md`, `spec.md`, `plan.md` | user said "go" | none: the user is present |
| Branch | `ship-branch` agent | cheap | branch and worktree, `spec.md` logistics | worktree on the branch | blocked report |
| Build | one `ship-build` agent per task | cheap, then standard | commits, `artifacts/build-<task>.*`, `reports/build-<task>-<n>.md` | commit on branch and `.exit` holds `0` | attempt ladder below |
| Final run | `ship-review` final-run agent | cheap | `artifacts/gate-*`, `reports/final-run-<n>.md` | every gate `.exit` exists and holds `0` | fix work, verify cap |
| Review | `ship-review` reviewer agents, parallel | strong | `reports/review-<lens>-<n>.md` | no blocking finding | fix work, review cap |
| Publish | `ship-publish` agent | cheap | push, PR or MR, `artifacts/pr-body.md`, report | URL in report | blocked report |
| CI check | `ship-ci-check` agent | cheap | `artifacts/ci-*`, report | checks passed or none | draft PR, blocked report |
| Handoff | supervisor | session model | `summary.md` at `done` | message sent | none |

## Attempt ladder

Each build task, and each fix pass, gets this ladder from the config caps:

1. Cheap tier, attempt one.
2. Cheap tier, attempt two.
3. Standard tier, one attempt.
4. Stop with a blocked report: trigger `retry cap`, rule hit `per-task attempts`.

A failed attempt is a report with status `failed`, no commit, a nonzero `.exit`, or no report at all.

## Fix work

Fix work is a `ship-build` agent in fix mode. Its brief points at the failing `.out` files or the review reports that block. The verify cap counts rounds of final run then fix. The review cap counts rounds of review then fix. After any fix, rerun the final run before the next review round.

When the review cap is hit, continue to publish. The PR carries the open findings and is not marked ready.

## Ready to mark ready

Publish always opens a draft. `ship-ci-check` marks it ready only when all of these hold:

- Every gate `.exit` file holds `0`.
- No blocking review finding is open and no cap was hit.
- Checks passed or none exist.

Otherwise it stays a draft and the handoff says why.

## Brief format

A brief is a short text block of pointers. Spawn each subagent on the tier named in the table, mapped to a real model through the config tier keys. A harness that cannot choose a model runs the default and the supervisor notes it in `log.md`.

```
Follow the skill `<skill-name>`. Its file is ~/.agents/skills/<skill-name>/SKILL.md; read it if you cannot load skills by name.
Repo: <absolute path to the main checkout>
Task folder: <absolute path>
Worktree: <absolute path>            (omit before the Branch phase)
Role: <task id, fix, final-run, reviewer lens, or none>
Tier: <cheap | standard | strong>
Attempt: <n>
Write your report to: <task folder>/reports/<phase>-<n>.md
```

Add nothing else. The skill and the task folder hold everything the agent needs.

## Resume order

On resume, test the pass checks from the top of the table and re-enter at the first one that fails.

---
name: ship-ci-check
description: "Ship phase: read PR checks, mark ready if all pass or none exist. Used by the ship supervisor."
---

Read the checks on the open PR or MR, and mark it ready only if everything holds. You fix nothing. Your brief names the task folder and where to write the report. Read `config.env` in the `ship` skill folder (`~/.agents/skills/ship/config.env`) and the command table for `FORGE` in `~/.agents/skills/ship/references/forge-<forge>.md`. Get the PR number from the publish report.

## Read the checks

1. Poll the "Read checks" row. If nothing appears within `CI_GRACE_SECONDS`, no checks exist. Treat that as passed. When `context.md` repo facts say there is no CI config, wait only fifteen seconds instead, because third-party checks are the only thing left to see.
2. When checks exist, keep polling until none is `pending`, up to `CI_WAIT_MINUTES`.

## Decide

- **All passed, or none exist.** Read the publish report. When it says `Ready eligible: yes`, mark the PR ready with the forge table's row and confirm the state. When `no`, leave it a draft and put the reasons in the report. Status `done`.
- **Any failed.** Leave the draft. For each failed check, save its log with the "Failed job logs" row to `artifacts/ci-<check>.out`. Status `blocked`, trigger `ci failure`, naming the failed checks and the log paths.
- **Still pending at the limit.** Leave the draft. Status `blocked`, trigger `ci failure`, saying which checks never finished.

Write the report in the format in `~/.agents/skills/task-memory/RUN-FILES.md`. Done when the PR state is ready or a draft with its reason written down.

To stop, follow "How a phase agent stops" in `~/.agents/skills/ship/references/escalation.md`.

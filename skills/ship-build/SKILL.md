---
name: ship-build
description: "Ship phase: build one task, or fix named failures, test first, then commit. Used by the ship supervisor."
---

Build one task from the plan, or fix named failures. You are one agent on one job. Your brief names the task folder, the worktree, the role (a task id such as `T2`, or `fix`), the attempt number, and where to write the report.

Work only inside the worktree. First run `git branch --show-current` there and confirm it matches the branch in `spec.md`.

## Read first

- `spec.md`: goal, acceptance criteria, out of scope, off limits, verify commands.
- Your task line in `plan.md`, and the acceptance criteria it names.
- `context.md`: the repo facts and convention files. Read the convention files.
- The user's global `~/.agents/AGENTS.md` for the commit format and attribution rules.
- For a fix: the failing `.out` files in `artifacts/` or the review reports your brief names. Fix exactly what they say.

## Build

1. **Test first.** When the repo has a test runner, write a failing test for each criterion your task covers. Run it and confirm it fails for the right reason. When no runner exists, skip this and say so in the report. Never add a test framework.
2. **Implement** the least that makes the tests pass. Follow the repo's conventions.
3. **Check.** Run your task's tests, the typecheck, and the lint for what you touched. Save the output with the artifacts pattern in `~/.agents/skills/task-memory/RUN-FILES.md`, as `artifacts/build-<role>.out` and `.exit`.
4. **Commit** once, with a message in the user's format from `AGENTS.md`. Stage only the files you changed. Run `git status` and confirm nothing of yours is left unstaged.

Done when the commit exists and the `.exit` file holds `0`. A fix with no code to change ends with status `blocked` and an explanation.

## Stay in scope

- Touch only what your task needs. When you spot a bug or cleanup outside it, append a line `Noticed: <what and where>` to `noticed.md` in the task folder and leave the code alone.
- Stop with status `blocked` and the matching trigger, from `~/.agents/skills/ship/references/escalation.md`, when the task needs a credential or service you lack, a destructive or irreversible step, a decision the spec does not settle, or more than twice the files your task line expected.

## Report

Write the report in the format in `~/.agents/skills/task-memory/RUN-FILES.md`: status `done`, `failed`, or `blocked`, a one-paragraph summary, the commit hash, and the artifact paths. Do not tick the task in `plan.md`; the supervisor does that after checking your commit and `.exit` file.

To stop, follow "How a phase agent stops" in `~/.agents/skills/ship/references/escalation.md`.

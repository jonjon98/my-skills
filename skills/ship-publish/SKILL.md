---
name: ship-publish
description: "Ship phase: push the branch, open a draft PR/MR, comment on the ticket. Used by the ship supervisor."
---

Publish the finished branch. Your brief names the task folder, the worktree, and where to write the report. Work inside the worktree. Read `config.env` in the `ship` skill folder (`~/.agents/skills/ship/config.env`) and the command table for `FORGE` in `~/.agents/skills/ship/references/forge-<forge>.md`.

## 1. Check before pushing

Run these in the worktree and stop on a hit, with the trigger from `~/.agents/skills/ship/references/escalation.md`.

- `git status` is clean.
- Read `git diff --stat origin/<target>...HEAD`. Files that do not belong, such as `.env`, logs, build output, `.DS_Store`, or large binaries, stop the run with trigger `security`.
- Scan the diff for secrets: private key blocks, `token=`, `password=`, `api_key=` with a literal value, and long random strings assigned to a name. A hit stops the run with trigger `security`. Write the file and line, never the value.

## 2. Rebase

Run `git fetch origin <target>` then `git rebase origin/<target>`. On a conflict, run `git rebase --abort` and stop with trigger `collision`. If the rebase pulled in new commits, say so in the report, so the supervisor reruns the final run.

## 3. Push

Run `git push -u origin <branch>`. Never force push. A rejected push stops the run with trigger `collision`.

## 4. Write the body

Write `artifacts/pr-body.md` in the task folder. When the repo has a PR or MR template (listed in `context.md`), fill that template. Otherwise use these sections, in this order, and omit any that would be empty:

- **Summary**: what changed and why, in a few lines. A diagram or a short call tree when it makes the change clearer.
- **Decisions made with you**: from `spec.md` Decisions.
- **Evidence**: the gates and criteria with their pass results, from the final-run report.
- **Needs your eyes**: from the final-run report.
- **Advisory**: every review finding the run did not fix. List blocking findings still open when the review cap was hit first, marked as blocking. Then list the non-blocking ones. Give each one's file, line, and why it matters, so the reviewer can accept or reject it.
- **Noticed but out of scope**: `noticed.md`.
- **Merge danger**: whether the change is a one-way door, such as a migration, a deletion, or a public contract change, or a two-way door, plus the blast radius in a few words.
- **Linked ticket**: the key and URL. Add `Closes #<n>` only when the tracker is the forge's own issues.

Write the evidence results into the body itself. The reader cannot open the task folder, so never point at its paths. Write no AI attribution anywhere in the body.

## 5. Open it

Open a **draft** PR or MR with the forge table's open command. The title follows the user's commit format from `~/.agents/AGENTS.md`: `<type>(<ticket key>): <summary>`, or `<type>: <summary>` with no ticket. Record the number and URL.

## 6. Tell the ticket

When `TRACKER_ACCESS` is configured and there is a ticket, comment the PR URL on it. Move the ticket's status only when `TICKET_STATUS_AFTER_PR` is set. Never close the ticket. A failed comment goes in the report and does not fail the phase.

## Report

Write the report in the format in `~/.agents/skills/task-memory/RUN-FILES.md`. Include the PR number and URL and whether the rebase pulled new commits. Add a line of exactly this form, because the next phase reads it: `Ready eligible: yes`, or `Ready eligible: no (<reasons>)`. Ready is eligible only when no blocking review finding is open and no cap was hit.

Done when the PR URL is in the report.

To stop, follow "How a phase agent stops" in `~/.agents/skills/ship/references/escalation.md`.

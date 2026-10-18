# Escalation

A run is unattended after "go". It stops for the user only on one of these triggers. Anything else the supervisor decides and logs.

| Trigger | Fires when |
|---|---|
| ambiguity | Two readings of the request give materially different work, and the code and docs cannot settle it. |
| retry cap | An attempt ladder, the verify cap, or the review cap is exhausted without a pass (a review cap stop opens a draft instead; see state-machine.md). |
| security | A reviewer reports a high-severity finding, or the diff holds a secret or a stray credential file. Medium findings go to the fix loop. |
| credentials | The work needs a credential or service the agent does not have. |
| destructive step | A step deletes data, migrates a schema, rewrites history, or cannot be undone. |
| scope growth | The work needs more than twice the files or tasks the plan expected. |
| subagent failure | A subagent keeps erroring or hanging until its ladder is exhausted. |
| collision | A branch, worktree, or open PR for this ticket already exists, or the target branch moved in a way a rebase cannot resolve. |
| ci failure | Checks failed, or stayed pending past the wait limit. |

## How a phase agent stops

A phase agent that cannot continue writes its report with status `blocked`, fills in the report's `Trigger` line with one trigger name from the table above, and states the single fix or answer needed under Blockers. It writes no `blocked.md`, edits no `summary.md`, and does nothing else. The supervisor does the rest, below.

## How to stop

1. Stop all delegation. Let nothing else run.
2. Write `blocked.md` in the task folder in the format of `~/.agents/skills/task-memory/RUN-FILES.md`.
3. Set `summary.md` Status to `blocked` and point its Next step at `blocked.md`.
4. Tell the user in chat, in three lines: which phase and position, which rule and its value (for example "per-task attempts: 3, in build, task 2 of 5"), and the path to `blocked.md`.
5. Wait. When the user answers, apply it, delete `blocked.md`, set Status back to `active`, and continue from the phase that stopped.

During the interview the user is present, so ask there and write no blocked report.

# Forge: GitHub

Commands for `FORGE=github` with `FORGE_ACCESS=cli`. With an MCP, use that server's equivalent tool for each row. When it lacks one, say so in the report instead of improvising.

| Need | Command |
|---|---|
| Logged in | `gh auth status` |
| Your username | `gh api user --jq .login` |
| Default branch | `git symbolic-ref --short refs/remotes/origin/HEAD` |
| Read an issue | `gh issue view <n> --comments` |
| Find open PRs for a ticket | `gh pr list --state open --search "<KEY>" --json number,title,headRefName,url` |
| Open a draft PR | `gh pr create --draft --base <target> --head <branch> --title "<title>" --body-file <file>` |
| Mark ready | `gh pr ready <n>` |
| Read checks | `gh pr checks <n> --json name,state,bucket,link` |
| Failed job logs | `gh run view <run-id> --log-failed`, with the run id taken from the check's `link` |
| Comment on the PR | `gh pr comment <n> --body-file <file>` |

`bucket` is one of `pass`, `fail`, `pending`, `skipping`, `cancel`. The exit code is nonzero when a check failed (and `8` while checks are pending), so decide from the output, never from the exit code. A repo with no workflows gives an empty list or a "no checks reported" message. Both mean no checks exist.

PR templates: `.github/pull_request_template.md`, `.github/PULL_REQUEST_TEMPLATE.md`, or a `PULL_REQUEST_TEMPLATE` folder.

Link an issue with `Closes #<n>` in the body, only when the tracker is GitHub issues.

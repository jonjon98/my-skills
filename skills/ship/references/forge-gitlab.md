# Forge: GitLab

Commands for `FORGE=gitlab` with `FORGE_ACCESS=cli`. With an MCP, use that server's equivalent tool for each row.

**Unverified.** This table was written from the `glab` docs and has never been run. Test each row where `glab` is installed, and correct the row here.

| Need | Command |
|---|---|
| Logged in | `glab auth status` |
| Your username | `glab api user`, read the `username` field |
| Default branch | `git symbolic-ref --short refs/remotes/origin/HEAD` |
| Read an issue | `glab issue view <n> --comments` |
| Find open MRs for a ticket | `glab mr list --search "<KEY>"` |
| Open a draft MR | `glab mr create --draft --target-branch <target> --source-branch <branch> --title "<title>" --description "$(cat <file>)" --yes` |
| Mark ready | `glab mr update <n> --ready` |
| Read checks | `glab mr view <n>` for the head pipeline, then `glab ci status --branch <branch>` |
| Failed job logs | `glab ci trace <job-id>` |
| Comment on the MR | `glab mr note <n> --message "<text>"` |

GitLab calls a PR a merge request. An MR with no pipeline means no checks exist.

MR templates live in `.gitlab/merge_request_templates/`.

Link an issue with `Closes #<n>` in the description, only when the tracker is GitLab issues.

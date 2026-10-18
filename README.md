# my-skills

Personal agent skills, plus the record of every third-party skill installed on this machine.

Skills install globally the same way for both sources:

```
~/.agents/skills/<name>            real folder (downloaded) or symlink into this repo (mine)
~/.claude/skills/<name>  ->  ../../.agents/skills/<name>
```

Claude Code reads `~/.claude/skills`. Other agents that follow the `~/.agents` convention read `~/.agents/skills`.

## Fresh install

Requires git and Node.js (for `npx`).

1. **Clone this repo** to its usual place:
   ```bash
   git clone <this-repo-url> ~/Developer/my-skills
   ```
2. **Link my skills** into both global skill folders. The script is safe to re-run and skips any real folder already in the way. It also asks where task-memory should store tasks and saves the answer to `skills/task-memory/config.env` (git-ignored, kept on re-runs). Set `TASK_MEMORY_DIR` to skip the prompt:
   ```bash
   TASK_MEMORY_DIR=~/Developer/task-memory ~/Developer/my-skills/install.sh
   ```
3. **Install the downloaded skills** from [mattpocock/skills](https://github.com/mattpocock/skills) with the [skills CLI](https://github.com/vercel-labs/skills). Pick the skills listed below when it prompts:
   ```bash
   npx skills add mattpocock/skills -g
   ```
4. **Link global agent instructions** so Claude Code reads the shared `AGENTS.md`:
   ```bash
   ln -s ~/.agents/AGENTS.md ~/.claude/CLAUDE.md
   ```
5. **Restart** Claude Code so it picks up the new skills.

To update the downloaded skills later:

```bash
npx skills update -g
```

The ship suite also needs `grill-me` and `grilling` from the downloaded set below. Its `config.env` files are git-ignored like task-memory's.

Adding a new skill of my own: create `skills/<name>/SKILL.md` in this repo, run `./install.sh`, and add a row to the table below.

## Skills

### Mine (this repo)

| Skill | What it does |
| --- | --- |
| [task-memory](skills/task-memory/SKILL.md) | Save and resume task progress in `<root>/<repo>/<task>/`, as a summary, a plan, and a log. The root is chosen at install time (`config.env`). Say "remember this" or "read from task memory". Also defines the run files an orchestrator adds (spec, context, reports, blocked report) in `RUN-FILES.md`. |
| [ship](skills/ship/SKILL.md) | Supervisor: take a request or ticket from interview to an open draft PR/MR. Plans, delegates to fresh subagents, gates on exit codes, stops only on a real problem. User-invoked: `/ship PROJ-108`. Needs `config.env`, created on first run. |
| [ship-preflight](skills/ship-preflight/SKILL.md) | Check forge, tracker and repo access, and collisions, before the interview. |
| [ship-branch](skills/ship-branch/SKILL.md) | Create `{username}/{type}/{ticket}-{slug}` in its own worktree. Naming template in its own `config.env`. |
| [ship-plan](skills/ship-plan/SKILL.md) | Pull context, interview on the gaps with `grilling`, write the spec and task list, wait for go. |
| [ship-build](skills/ship-build/SKILL.md) | One agent, one task: test first, implement, commit. Also fixes named failures. |
| [ship-review](skills/ship-review/SKILL.md) | Final run of all gates and acceptance checks, and parallel code reviewers by lens. |
| [ship-publish](skills/ship-publish/SKILL.md) | Check, rebase, push, open a draft PR/MR, comment on the ticket. |
| [ship-ci-check](skills/ship-ci-check/SKILL.md) | Read PR checks, mark ready when all pass or none exist. |

### Downloaded from [mattpocock/skills](https://github.com/mattpocock/skills)

Installed with the skills CLI. The install record lives in `~/.agents/.skill-lock.json`.

#### engineering

| Skill | What it does |
| --- | --- |
| [ask-matt](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt) | Ask which skill or flow fits your situation. |
| [code-review](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review) | Review changes since a commit or branch against the repo's standards and the originating spec. |
| [codebase-design](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design) | Shared vocabulary for designing deep modules. |
| [diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) | Diagnosis loop for hard bugs and performance regressions. |
| [domain-modeling](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling) | Build and sharpen a project's domain model. |
| [grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| [implement](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement) | Implement a piece of work based on a spec or set of tickets. |
| [implement-spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement-spec) | Implement the result of /to-spec and /to-tickets in code. |
| [improve-codebase-architecture](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| [pr](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) | Write a PR body. |
| [prototype](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) | Build a throwaway prototype to answer a design question. |
| [research](https://github.com/mattpocock/skills/tree/main/skills/engineering/research) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. |
| [retro](https://github.com/mattpocock/skills/tree/main/skills/engineering/retro) | Conduct a retrospective on a coding session. |
| [setup-matt-pocock-skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills) | Configure a repo for the engineering skills: issue tracker, triage labels, and domain doc layout. |
| [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) | Test-driven development. |
| [to-spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec) | Turn the current conversation into a spec and publish it to the issue tracker. |
| [to-tickets](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets) | Break a plan or spec into tracer-bullet tickets with blocking edges, published to the tracker. |
| [triage](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage) | Move issues and external PRs through triage and write agent-ready briefs. |
| [wayfinder](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder) | Plan work too big for one session as a map of decision tickets, resolved one at a time. |
| [wizard](https://github.com/mattpocock/skills/tree/main/skills/engineering/wizard) | Generate an interactive bash wizard that walks a human through steps only they can perform. |

#### productivity

| Skill | What it does |
| --- | --- |
| [grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) | A relentless interview to sharpen a plan or design. |
| [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) | Grill the user relentlessly about a plan, decision, or idea. |
| [handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) | Compact the current conversation into a handoff document for another agent to pick up. |
| [teach](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) | Teach the user a new skill or concept, within this workspace. |
| [to-questionnaire](https://github.com/mattpocock/skills/tree/main/skills/productivity/to-questionnaire) | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| [wait-what](https://github.com/mattpocock/skills/tree/main/skills/productivity/wait-what) | Re-pitch a last message that did not land. |
| [writing-for-agents](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents) | Writing documents for agents. |

#### misc

| Skill | What it does |
| --- | --- |
| [git-guardrails-claude-code](https://github.com/mattpocock/skills/tree/main/skills/misc/git-guardrails-claude-code) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. |
| [migrate-to-shoehorn](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn) | Migrate test files from `as` type assertions to @total-typescript/shoehorn. |
| [scaffold-exercises](https://github.com/mattpocock/skills/tree/main/skills/misc/scaffold-exercises) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. |
| [setup-pre-commit](https://github.com/mattpocock/skills/tree/main/skills/misc/setup-pre-commit) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. |

#### in-progress

| Skill | What it does |
| --- | --- |
| [chief-of-staff](https://github.com/mattpocock/skills/tree/main/skills/in-progress/chief-of-staff) | Pursue a long-running goal in a single session by co-ordinating subagents. |
| [claude-handoff](https://github.com/mattpocock/skills/tree/main/skills/in-progress/claude-handoff) | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| [loop-me](https://github.com/mattpocock/skills/tree/main/skills/in-progress/loop-me) | Grill me about specs for the workflows I want to build, within this workspace. |
| [setup-ts-deep-modules](https://github.com/mattpocock/skills/tree/main/skills/in-progress/setup-ts-deep-modules) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module. |
| [writing-beats](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-beats) | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| [writing-fragments](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-fragments) | Writing, explore: mine raw fragments, no structure yet. |
| [writing-shape](https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-shape) | Writing, exploit: shape raw material into an article, paragraph by paragraph. |

### Synced from claude.ai

Anthropic's built-in skills sync automatically into `~/.claude/skills/synced` when signed in to Claude. They need no install step: built-in-browser, chrome-browser, computer-use, deep-research, docs, docx, google-workspace, import-memory, morning, pdf, pptx, skill-creator, xlsx.

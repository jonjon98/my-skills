"""Rebuild the Skills section of README.md from each skill's frontmatter.

Mine: every folder in skills/ that holds a SKILL.md.
Downloaded: the install record in ~/.agents/.skill-lock.json, grouped by folder.
Everything above the "## Skills" heading is left as written.
"""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
LOCK = pathlib.Path.home() / ".agents" / ".skill-lock.json"
HEADING = "## Skills"


def description(text):
    match = re.search(r"^description:\s*(.+)$", text, re.M)
    if not match:
        return ""
    line = match.group(1).strip().strip('"')
    return re.split(r"(?<=\.)\s", line, maxsplit=1)[0].replace("|", "\\|")


def mine_rows():
    rows = []
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        name = skill.parent.name
        text = skill.read_text()
        name_match = re.search(r"^name:\s*(\S+)", text, re.M)
        label = name_match.group(1) if name_match else name
        link = f"skills/{name}/SKILL.md"
        rows.append(f"| [{label}]({link}) | {description(text)} |")
    return rows


def downloaded_sections():
    skills = json.loads(LOCK.read_text())["skills"]
    groups = {}
    for name, info in sorted(skills.items()):
        path = info["skillPath"].rsplit("/SKILL.md", 1)[0]
        category = path.split("/")[1]
        text = (pathlib.Path.home() / ".agents" / "skills" / name / "SKILL.md").read_text()
        url = f"https://github.com/{info['source']}/tree/main/{path}"
        groups.setdefault(category, []).append(f"| [{name}]({url}) | {description(text)} |")
    out = []
    for category in sorted(groups):
        out.append(f"#### {category}\n\n| Skill | What it does |\n| --- | --- |\n" + "\n".join(groups[category]))
    return "\n\n".join(out)


def build():
    return "\n".join([
        HEADING,
        "",
        "### Mine (this repo)",
        "",
        "| Skill | What it does |",
        "| --- | --- |",
        *mine_rows(),
        "",
        "### Downloaded from [mattpocock/skills](https://github.com/mattpocock/skills)",
        "",
        "Installed with the skills CLI. The install record lives in `~/.agents/.skill-lock.json`.",
        "",
        downloaded_sections(),
        "",
        "### Synced from claude.ai",
        "",
        "Anthropic's built-in skills sync automatically into `~/.claude/skills/synced` when signed in to Claude. They need no install step: built-in-browser, chrome-browser, computer-use, deep-research, docs, docx, google-workspace, import-memory, morning, pdf, pptx, skill-creator, xlsx.",
        "",
    ])


text = README.read_text()
head = text.split(HEADING, 1)[0]
README.write_text(head + build())
print("README skills section rebuilt")

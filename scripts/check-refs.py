"""Fail if any skill points at a ~/.agents/skills path that the repo does not provide.

Checks every reference of the form ~/.agents/skills/<name>/<path> in the repo.
A name that is not in this repo is looked up in the installed folder, for downloaded skills.
A path with a <placeholder> is checked up to its parent folder.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
REF = re.compile(r"~/\.agents/skills/([A-Za-z0-9_-]+)/([A-Za-z0-9_./<>-]*)")
INSTALLED = pathlib.Path.home() / ".agents" / "skills"

failures = []
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or "evals" in path.parts:
        continue
    if path.suffix not in {".md", ".sh", ".py", ".json", ".example", ""} and path.name != "config.env.example":
        continue
    for match in REF.finditer(path.read_text(errors="ignore")):
        name, rel = match.group(1), match.group(2).rstrip(".")
        target = SKILLS / name if (SKILLS / name).is_dir() else INSTALLED / name
        if not target.is_dir():
            failures.append(f"{path.relative_to(ROOT)}: no skill folder '{name}'")
            continue
        if not rel:
            continue
        if "<" in rel:
            rel = rel.split("<", 1)[0].rsplit("/", 1)[0] if "/" in rel.split("<", 1)[0] else ""
        if rel and not (target / rel.rstrip("/")).exists():
            failures.append(f"{path.relative_to(ROOT)}: missing {name}/{rel}")

if failures:
    print("\n".join(failures))
    sys.exit(1)
print("all ~/.agents/skills references resolve")

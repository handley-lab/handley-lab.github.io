"""Build assets/papers/people.json for the people panel on /papers/.

Merges assets/group/group.yaml (names, photos, role dates) with
assets/group/focus.yaml (what current members work on), and notes who has a
card on the group page (assets/group/group.html) so their face can link to it.
The page works out who is current from the role dates and counts papers from
papers.json, so this only needs re-running when group.yaml, focus.yaml or
group.html changes. No network access.

    python script/people.py
"""
import datetime as dt
import json
import re
from html import unescape
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
GROUP = ROOT / "assets" / "group" / "group.yaml"
FOCUS = ROOT / "assets" / "group" / "focus.yaml"
CARDS = ROOT / "assets" / "group" / "group.html"
OUT = ROOT / "assets" / "papers" / "people.json"

# Most senior first; the page shows the most senior current (or last) role.
ROLES = {
    "pi": "PI",
    "coi": "Co-I",
    "postdoc": "Postdoc",
    "phd": "PhD student",
    "mphil": "MPhil student",
    "partiii": "Part III student",
    "summer": "Summer student",
}


def iso(value):
    return value.isoformat() if isinstance(value, dt.date) else None


def main():
    group = yaml.safe_load(GROUP.read_text())
    focus = yaml.safe_load(FOCUS.read_text()) or {}
    cards = {unescape(n) for n in re.findall(r"<h3>([^<]+)</h3>", CARDS.read_text())}
    people = []
    for name, data in group.items():
        data = data or {}
        roles = [
            {"role": ROLES[r], "start": iso(data[r].get("start")), "end": iso(data[r].get("end"))}
            for r in ROLES
            if isinstance(data.get(r), dict) and iso(data[r].get("start"))
        ]
        if not roles:
            continue
        image = data.get("image")
        if image and image.startswith("images/"):
            image = "/assets/group/" + image
        f = focus.get(name) or {}
        people.append({
            "name": name,
            "image": image,
            "card": name in cards,
            "roles": roles,
            "themes": f.get("themes") or [],
            "tags": f.get("tags") or [],
        })
    unknown = set(focus) - {p["name"] for p in people}
    if unknown:
        raise SystemExit(f"focus.yaml names not in group.yaml: {', '.join(sorted(unknown))}")
    OUT.write_text(json.dumps({"people": people}, indent=1, ensure_ascii=False) + "\n")
    print(f"Wrote {len(people)} people to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

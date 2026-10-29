"""Find the group's papers on arXiv and build assets/papers/papers.json for the
paper map on /papers/.

A paper is a group paper when Will Handley, or a PhD student or postdoc listed
in assets/group/group.yaml, wrote it while in the group (plus a year's grace
after leaving, for papers that land late). Large collaboration papers only
count when a group member is first author. _data/paper_overrides.yml can force
papers in or out and fix themes; everything else is automatic.

Each paper gets Semantic Scholar citation counts, group-author photos and a
broad theme. No API keys needed.

    python script/papers.py                    # full live run (~5 min, arXiv is slow)
    python script/papers.py --summary out.md   # also write a change summary for a PR
    python script/papers.py --feed feed.atom   # reuse a downloaded copy of Will's feed
"""
import argparse
import datetime as dt
import json
import re
import time
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "papers" / "papers.json"
GROUP = ROOT / "assets" / "group" / "group.yaml"
OVERRIDES = ROOT / "_data" / "paper_overrides.yml"

PI = "Will Handley"
PI_FEED = "https://arxiv.org/a/handley_w_1.atom"
ARXIV_API = "https://export.arxiv.org/api/query"
S2_URL = "https://api.semanticscholar.org/graph/v1/paper/batch"
SEARCHED_ROLES = ("pi", "postdoc", "phd")
GRACE = dt.timedelta(days=365)
COLLABORATION_SIZE = 15
CATEGORIES = ("astro-ph", "gr-qc", "hep-", "physics.", "stat.", "cs.LG", "cs.AI", "math.ST", "quant-ph")
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

# Display order. Classification order is RULES below.
THEMES = [
    ("methods", "Bayesian methods & software"),
    ("cosmo", "Cosmology & dark energy"),
    ("21cm", "21-cm & radio cosmology"),
    ("astro", "Gravitational waves & astrophysics"),
    ("other", "Particle physics & beyond"),
]
OTHER = "other"

# (theme, patterns). Tried against the title first, then the abstract; first
# match wins. Methods sit after the application areas but before the broad
# cosmology terms, so "PolyChord: nested sampling for cosmology" is a methods
# paper while "Bayesian evidence for evolving dark energy" is cosmology.
METHODS = [r"nested sampl", r"sampler", r"sampling algorithm", r"simulation[- ]based", r"emulat",
           r"neural", r"machine learning", r"autoregressive flow", r"gaussian process",
           r"oscillatory", r"numerical", r"anomaly detection", r"data curation", r"foundation model"]
RULES = [
    ("cosmo", [r"^Planck (19|20)\d\d", r"^Planck intermediate", r"Exploring Cosmic Origins with CORE"]),
    ("21cm", [r"21[- ]?cm", r"\bREACH\b", r"\bSARAS", r"global signal", r"radiometer", r"antenna",
              r"cosmic dawn", r"reioni[sz]ation", r"\bEoR\b", r"global sky model"]),
    ("astro", [r"gravitational[- ]wave", r"\bLIGO\b", r"\bLISA\b", r"black[- ]hole", r"neutron star",
               r"transient", r"quasar", r"exoplanet", r"galax", r"satellite"]),
    ("other", [r"dark matter", r"\bWIMP", r"Higgs", r"neutrino", r"axion", r"\bGAMBIT\b", r"global fit",
               r"new physics", r"physical theories", r"materials", r"torsion"]),
    ("methods", METHODS),
    ("cosmo", [r"dark energy", r"inflat", r"curvature", r"primordial", r"\bCMB\b", r"tension",
               r"Hubble", r"H_0", r"\bDESI\b", r"recombination", r"universe", r"large[- ]scale structure",
               r"lensing", r"cluster", r"cosmolog", r"conformal boundary"]),
]
ABSTRACT_FALLBACK = [("methods", [r"bayesian", r"inference", r"evidence", r"likelihood"])]


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z ]", "", s.lower()).split()


def key(name):
    parts = norm(name)
    return (parts[-1], parts[0][0]) if len(parts) > 1 else None


def to_date(value):
    return value if isinstance(value, dt.date) else None


def load_group():
    """Members keyed by (surname, first initial), with their searchable tenures."""
    group = yaml.safe_load(GROUP.read_text())
    members = {}
    for name, data in group.items():
        data = data or {}
        image = data.get("image")
        if image and image.startswith("images/"):
            image = "/assets/group/" + image
        tenures = []
        for role in SEARCHED_ROLES:
            if isinstance(data.get(role), dict) and to_date(data[role].get("start")):
                end = to_date(data[role].get("end"))
                tenures.append((to_date(data[role]["start"]), end + GRACE if end else None))
        if key(name):
            members[key(name)] = {"name": name, "image": image, "tenures": tenures}
    return members


def group_start(members):
    """The group began when the PI's first student or postdoc arrived."""
    return min(s for m in members.values() if m["name"] != PI for s, _ in m["tenures"])


def in_tenure(member, date, start):
    if member["name"] == PI:
        return date >= start
    return any(s <= date and (e is None or date <= e) for s, e in member["tenures"])


def arxiv_get(params):
    for attempt in range(4):
        try:
            r = requests.get(ARXIV_API, params=params, timeout=180)
            r.raise_for_status()
            return r.content
        except requests.RequestException:
            time.sleep(10 * (attempt + 1))
    raise RuntimeError(f"arXiv request failed: {params}")


def arxiv_query(name, start, end):
    """arXiv search for one surname over a date range, following pagination.

    arXiv's au:Surname_I form silently misses many papers (it finds 74 of
    Will's ~170), so search on surname alone and match initials locally.
    """
    surname = " ".join(name.split()[1:])
    au = f'"{surname}"' if " " in surname else surname
    window = f"{start:%Y%m%d}0000 TO {(end or dt.date.today()):%Y%m%d}2359"
    papers, offset = [], 0
    while True:
        batch = parse_feed(arxiv_get({"search_query": f"au:{au} AND submittedDate:[{window}]",
                                      "start": offset, "max_results": 200}))
        papers += batch
        time.sleep(3)  # arXiv asks for at most one request every three seconds
        if len(batch) < 200:
            return papers
        offset += 200


def parse_feed(xml):
    root = ET.fromstring(xml)
    papers = []
    for e in root.findall("a:entry", NS):
        arxiv = re.sub(r"v\d+$", "", e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1])
        if not e.findtext("a:published", "", NS):
            continue
        primary = e.find("arxiv:primary_category", NS)
        papers.append({
            "arxiv": arxiv,
            "title": " ".join(e.findtext("a:title", "", NS).split()),
            "abstract": " ".join(e.findtext("a:summary", "", NS).split()),
            "date": e.findtext("a:published", "", NS)[:10],
            "authors": [a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)],
            "category": primary.get("term") if primary is not None else "",
            "categories": [c.get("term") for c in e.findall("a:category", NS)],
        })
    return papers


def classify(title, abstract):
    for text, rules in ((title, RULES), (abstract, RULES + ABSTRACT_FALLBACK)):
        for theme, patterns in rules:
            if any(re.search(p, text, re.IGNORECASE) for p in patterns):
                return theme
    return OTHER


def citations(ids):
    counts = {}
    for i in range(0, len(ids), 100):
        chunk = ids[i:i + 100]
        for attempt in range(5):
            r = requests.post(S2_URL, params={"fields": "citationCount"},
                              json={"ids": [f"ARXIV:{a}" for a in chunk]}, timeout=60)
            if r.status_code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            r.raise_for_status()
            break
        for arxiv, hit in zip(chunk, r.json()):
            counts[arxiv] = (hit or {}).get("citationCount") or 0
    return counts


def is_group_paper(paper, members, start):
    """Return the group authors who make this a group paper, or [] if it isn't."""
    date = dt.date.fromisoformat(paper["date"])
    if not any(c.startswith(CATEGORIES) for c in paper["categories"]):
        return []
    authors = [members.get(key(a)) for a in paper["authors"]]
    active = [m for m in authors if m and m["tenures"] and in_tenure(m, date, start)]
    if not active:
        return []
    # Surname search pulls in strangers who share a surname and initial, so
    # require a second link to the group: Will, or another group member.
    if not any(m["name"] == PI for m in active) and len({m["name"] for m in authors if m}) < 2:
        return []
    # Collaboration author lists are often alphabetical, so only first
    # authorship says anything about who led the work.
    if len(paper["authors"]) > COLLABORATION_SIZE and authors[0] not in active:
        return []
    return active


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", help="write a markdown summary of changes to this path")
    parser.add_argument("--feed", help="reuse a downloaded copy of the PI's arXiv feed")
    args = parser.parse_args()

    members = load_group()
    start = group_start(members)
    overrides = yaml.safe_load(OVERRIDES.read_text()) if OVERRIDES.exists() else {}
    overrides = overrides or {}
    include = {str(i) for i in overrides.get("include") or []}
    exclude = {str(i) for i in overrides.get("exclude") or []}
    theme_fix = {str(k): v for k, v in (overrides.get("theme") or {}).items()}

    # Will's claimed-papers feed is the most complete record of his work.
    feed = Path(args.feed).read_bytes() if args.feed else requests.get(PI_FEED, timeout=900).content
    candidates = {p["arxiv"]: p for p in parse_feed(feed)}
    print(f"{PI} arXiv feed: {len(candidates)} papers")
    searched = [m for m in members.values() if m["tenures"]]
    for i, m in enumerate(searched, 1):
        first = min(s for s, _ in m["tenures"])
        if m["name"] == PI:
            first, last = start, None
        else:
            ends = [e for _, e in m["tenures"]]
            last = None if None in ends else max(ends)
        found = arxiv_query(m["name"], first, last)
        print(f"[{i}/{len(searched)}] {m['name']}: {len(found)} arXiv hits")
        for p in found:
            candidates[p["arxiv"]] = p
    for arxiv in include - candidates.keys():
        hits = parse_feed(arxiv_get({"id_list": arxiv}))
        candidates.update({p["arxiv"]: p for p in hits})

    papers = []
    for arxiv, p in candidates.items():
        if arxiv in exclude:
            continue
        active = is_group_paper(p, members, start)
        if not active and arxiv not in include:
            continue
        everyone = [members.get(key(a)) for a in p["authors"]]
        p["group"] = [{"name": m["name"], "image": m["image"]} for m in everyone if m]
        p["theme"] = theme_fix.get(arxiv) or classify(p["title"], p["abstract"])
        papers.append(p)

    counts = citations([p["arxiv"] for p in papers])
    for p in papers:
        p["citations"] = counts.get(p["arxiv"], 0)
        del p["categories"]
    papers.sort(key=lambda p: p["date"], reverse=True)

    previous = set()
    if OUT.exists():
        previous = {p["arxiv"] for p in json.loads(OUT.read_text())["papers"]}
    themes = [{"key": k, "label": l} for k, l in THEMES]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"themes": themes, "papers": papers}, indent=1, ensure_ascii=False))

    added = [p for p in papers if p["arxiv"] not in previous]
    removed = previous - {p["arxiv"] for p in papers}
    print(f"Wrote {len(papers)} group papers to {OUT.relative_to(ROOT)} "
          f"(+{len(added)} / -{len(removed)} since last run)")
    for t in themes:
        print(f"  {t['label']}: {sum(p['theme'] == t['key'] for p in papers)}")

    if args.summary:
        lines = [f"Paper map refresh: {len(papers)} group papers, {len(added)} added, {len(removed)} removed.", ""]
        if added:
            lines += ["## Added", "", "Check each is really a group paper; add false matches to "
                      "`exclude` in `_data/paper_overrides.yml`.", ""]
            lines += [f"- [{p['title']}](https://arxiv.org/abs/{p['arxiv']}) ({p['date']}), "
                      f"group authors: {', '.join(m['name'] for m in p['group'])}" for p in added]
        if removed:
            lines += ["", "## Removed", ""] + [f"- arXiv:{a}" for a in sorted(removed)]
        Path(args.summary).write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

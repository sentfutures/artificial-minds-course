#!/usr/bin/env python3
"""Rebuild 09-concept-atlas.md from atlas.json.

atlas.json is the source. Edit it, then run this. Do not hand-edit the
Markdown outline: the next run overwrites it.

    python3 tools/regenerate-atlas.py           # dry run, prints the diff size
    python3 tools/regenerate-atlas.py --write   # rewrite 09-concept-atlas.md

Everything above "## I." and from "## Earlier map terminology corrections"
onward is kept from the existing Markdown and is edited by hand.
"""

import difflib
import html as _html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
JSON = ROOT / "atlas.json"
MD = ROOT / "09-concept-atlas.md"

BODY_START = "## I. "
BODY_END = "## Earlier map terminology corrections"


def split_md(txt):
    lines = txt.splitlines(keepends=True)
    start = next(i for i, l in enumerate(lines) if l.startswith(BODY_START))
    end = next(i for i, l in enumerate(lines) if l.startswith(BODY_END))
    return "".join(lines[:start]), "".join(lines[end:])


def md(s):
    """JSON's inline HTML to Markdown."""
    s = re.sub(r'<a href="([^"]+)">(.*?)</a>', r"[\2](\1)", s)
    s = re.sub(r"</?b>", "**", s)
    s = re.sub(r"</?em>", "*", s)
    s = re.sub(r"</?i>", "*", s)
    return _html.unescape(s)


def marker(node, overlay):
    """The week and assessment tags after a concept's name."""
    o = overlay.get(node.get("id", "")) or {}
    if node.get("addition") is True:
        wk = o.get("week")
        return f" [extra, {wk}]" if wk else " [extra]"
    s = ""
    if o.get("graded"):
        s += " ★"
    wk = o.get("week")
    if wk:
        s += f" [{wk}]"
    gw = list(o.get("gradedWeeks") or [])
    if gw and gw != [wk]:
        s += f" (assessed {', '.join(gw)})"
    return s


def render_concept(node, overlay, depth, out):
    pad = "  " * depth
    out.append(f"{pad}- **{md(node['term'])}**{marker(node, overlay)}: {md(node['definition'])}")
    sub = "  " * (depth + 1)
    if node.get("origin"):
        out.append(f"{sub}- *Origin.* {md(node['origin'])}")
    if node.get("bearsOn"):
        out.append(f"{sub}- *Bears on.* {md(node['bearsOn'])}")
    if node.get("correction"):
        out.append(f"{sub}- *⚑ Corrected.* {md(node['correction'])}")
    for child in node.get("children") or []:
        render_concept(child, overlay, depth + 1, out)


def render(data):
    overlay = (data.get("syllabusOverlay") or {}).get("terms") or {}
    out = []
    for i, branch in enumerate(data["branches"]):
        if i:
            out.append("---")
            out.append("")
        out.append(f"## {branch['numeral']}. {md(branch['term'])}")
        out.append("")
        if branch.get("summary"):
            out.append(md(branch["summary"]))
            out.append("")
        for group in branch.get("children") or []:
            out.append(f"- **{md(group['term'])}**")
            if group.get("summary"):
                out.append(f"  - {md(group['summary'])}")
            for concept in group.get("children") or []:
                render_concept(concept, overlay, 1, out)
        out.append("")
    out.append("---")
    out.append("")
    return "\n".join(out)


def main():
    data = json.loads(JSON.read_text(encoding="utf-8"))
    head, tail = split_md(MD.read_text(encoding="utf-8"))
    new = head + render(data) + tail

    old = MD.read_text(encoding="utf-8")
    diff = [l for l in difflib.unified_diff(old.splitlines(), new.splitlines(), lineterm="", n=0)
            if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]

    concepts = 0
    def count(n):
        nonlocal concepts
        if n.get("kind") == "concept":
            concepts += 1
        for c in n.get("children") or []:
            count(c)
    for b in data["branches"]:
        count(b)

    if "--write" in sys.argv:
        MD.write_text(new, encoding="utf-8")
        print(f"wrote {MD.name}: {concepts} concepts, {len(diff)} changed lines")
    else:
        print(f"dry run: {concepts} concepts, {len(diff)} changed lines")
        for l in diff[:40]:
            print("   ", l[:160])


if __name__ == "__main__":
    main()

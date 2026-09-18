#!/usr/bin/env python3
"""Build atlas/atlas.data.js from atlas.json for the interactive map.

atlas.json is the source. The syllabusOverlay terms (week chips and graded
marks) are merged into each node for display, which is what atlas/index.html
expects. Run after any atlas.json edit, alongside regenerate-atlas.py:

    python3 tools/build-atlas-data.py
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "atlas.json").read_text())
terms = (data.get("syllabusOverlay") or {}).get("terms") or {}


def merge(node):
    o = terms.get(node.get("id", ""))
    if o:
        if o.get("graded"):
            node["graded"] = True
        if o.get("week"):
            node["week"] = o["week"]
    for child in node.get("children") or []:
        merge(child)


for branch in data["branches"]:
    merge(branch)

out = ROOT / "atlas" / "atlas.data.js"
out.write_text(
    "/* %s: generated from atlas.json by tools/build-atlas-data.py."
    " Edit the JSON, not this file. */\nwindow.ATLAS=%s;\n"
    % (data["name"], json.dumps(data, ensure_ascii=False, separators=(",", ":")))
)
print("wrote %s (%d bytes)" % (out, out.stat().st_size))

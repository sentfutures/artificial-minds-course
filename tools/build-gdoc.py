#!/usr/bin/env python3
"""Build Google-Docs-ready HTML from the course Markdown files.

The Markdown files stay the source of truth; this emits one HTML file per
review tab into gdoc-build/. Import each into Google Drive (upload, then
"Open with > Google Docs") and paste the converted Doc into its tab of the
shared review document.

Link rules (verified against Drive's HTML-to-Doc conversion, 2026-09-18):
- Every heading gets an inner <a name="github-slug"></a>; same-file links
  keep their #fragment and convert to NATIVE Google Docs heading links.
- Footnote refs/bodies get <a name> anchors, converting to native bookmarks.
- Cross-file links are rewritten to the live GitHub Pages URL, so they work
  from any tab immediately. (They can later be upgraded to native tab links.)
- <a name> values keep the same GitHub-style slugs the Markdown links use,
  so the sources need no edits.

Run:  <venv>/bin/python tools/build-gdoc.py
"""

import html as _html
import pathlib
import re
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "gdoc-build"
PAGES = "https://sentfutures.github.io/artificial-minds-course/"
VERSION_LINE = "Artificial Minds Research Course · version 4.4 review copy"

TABS = {
    "01-syllabus.md": "Syllabus v4.4",
    "02-course-companion.md": "Course Companion v4.4",
    "03-glossary.md": "Glossary v4.4",
    "04-facilitator-guide.md": "Facilitator Guide v4.4",
    "05-facilitator-appendices.md": "Facilitator Appendices v4.4",
    "09-concept-atlas.md": "Concept Atlas v4.4",
}


def github_slug(text, seen):
    """GitHub's heading-anchor algorithm, with -N dedupe."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    s = s.replace(" ", "-")
    n = seen.get(s, 0)
    seen[s] = n + 1
    return s if n == 0 else f"{s}-{n}"


def heading_text(inner_html):
    return _html.unescape(re.sub(r"<[^>]+>", "", inner_html))


def convert(md_text):
    return markdown.markdown(
        md_text,
        extensions=["tables", "footnotes", "fenced_code", "sane_lists"],
    )


def anchor_headings(body):
    """Insert <a name> into every heading; return (body, slug set)."""
    seen, slugs = {}, set()

    def repl(m):
        level, inner = m.group(1), m.group(2)
        slug = github_slug(heading_text(inner), seen)
        slugs.add(slug)
        return f'<h{level}><a name="{slug}"></a>{inner}</h{level}>'

    body = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", repl, body, flags=re.S)
    return body, slugs


def anchor_footnotes(body, slugs):
    """Turn footnote ids into <a name> anchors (colons become hyphens)."""
    body = re.sub(
        r'<sup id="fnref:([^"]+)">',
        lambda m: f'<sup><a name="fnref-{m.group(1)}"></a>',
        body,
    )
    body = re.sub(
        r'<li id="fn:([^"]+)">',
        lambda m: f'<li><a name="fn-{m.group(1)}"></a>',
        body,
    )
    body = body.replace('href="#fn:', 'href="#fn-')
    body = body.replace('href="#fnref:', 'href="#fnref-')
    slugs |= set(re.findall(r'<a name="(fn(?:ref)?-[^"]+)"></a>', body))
    return body, slugs


def rewrite_links(body, warnings):
    """Cross-file links -> Pages URLs; flag unknown relative links."""

    def repl(m):
        href = m.group(1)
        if href.startswith(("#", "http://", "https://", "mailto:")):
            return m.group(0)
        fm = re.match(r"^([0-9]{2}-[a-z0-9-]+\.md)(#(.+))?$", href)
        if fm and fm.group(1) in TABS:
            url = PAGES + fm.group(1)[:-3] + ".html"
            if fm.group(3):
                url += "#" + fm.group(3)
            return f'href="{url}"'
        warnings.append(f"unhandled relative link: {href}")
        return m.group(0)

    return re.sub(r'href="([^"]+)"', repl, body)


def collect_refs(body):
    same = set(re.findall(r'href="#([^"]+)"', body))
    cross = re.findall(r'href="([0-9]{2}-[a-z0-9-]+\.md)#([^"]+)"', body)
    return same, cross


def main():
    OUT.mkdir(exist_ok=True)
    built, all_slugs, all_cross, problems = {}, {}, [], []

    for fname, tab in TABS.items():
        md_text = (ROOT / fname).read_text()
        body = convert(md_text)
        _, cross_refs = collect_refs(body)
        all_cross.extend((fname, t, a) for t, a in cross_refs)
        body, slugs = anchor_headings(body)
        body, slugs = anchor_footnotes(body, slugs)
        warnings = []
        body = rewrite_links(body, warnings)
        problems.extend(f"{fname}: {w}" for w in warnings)
        for ref in set(re.findall(r'href="#([^"]+)"', body)):
            if ref not in slugs:
                problems.append(f"{fname}: same-file link #​{ref} has no matching anchor")
        all_slugs[fname] = slugs
        built[fname] = (tab, body)

    for src, target_file, anchor in all_cross:
        if anchor not in all_slugs.get(target_file, set()):
            problems.append(f"{src}: cross link {target_file}#{anchor} missing in target")

    for fname, (tab, body) in built.items():
        page = (
            "<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\">"
            f"<title>{tab}</title></head><body>\n"
            f"<p><em>{VERSION_LINE} · compiled from <code>{fname}</code> · "
            f'<a href="{PAGES}{fname[:-3]}.html">live web version</a></em></p>\n'
            f"{body}\n</body></html>\n"
        )
        out = OUT / (fname[:-3] + ".html")
        out.write_text(page)
        print(f"wrote {out.name}  ({out.stat().st_size:,} bytes, {len(all_slugs[fname])} anchors)")

    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print("\nAll same-file and cross-file link targets verified.")


if __name__ == "__main__":
    main()

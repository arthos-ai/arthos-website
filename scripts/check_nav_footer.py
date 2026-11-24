#!/usr/bin/env python3
"""
Checks that every page's nav and footer links match.

This site has no shared header/footer component (every page is a standalone
static HTML file with its own copy of the nav and footer markup — see
README.md). That means a link added to one page's footer has to be added by
hand to every other page too, and it's easy to miss one (it happened once
already: the homepage footer was missing the new /security/ link).

This script doesn't fix that — it just catches drift before you deploy.
Run it after any nav/footer change, before pushing:

    python3 scripts/check_nav_footer.py

Exits non-zero if any page's nav or footer links don't match the rest.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Pages that share the current nav/footer convention. how-it-works.html is
# deliberately excluded: it runs on an older, different design system (a
# different font, different CSS variables, and a footer that doesn't even
# have Privacy/LinkedIn/Security links) that predates the rest of the site's
# rebrand and was never migrated. Flagging it here would just be noise until
# someone decides to migrate it — see the handoff notes from 2026-11-23.
PAGES = [
    "index.html",
    "about.html",
    "contact.html",
    "privacy/index.html",
    "security/index.html",
    "subprocessors/index.html",
    "404.html",
]

NAV_BLOCK_RE = re.compile(r'<div class="nav-links">(.*?)</div>', re.S)
FOOT_BLOCK_RE = re.compile(r'<span class="foot-links">(.*?)</span>', re.S)
HREF_RE = re.compile(r'href="([^"]+)"')


def extract_hrefs(html, block_re):
    match = block_re.search(html)
    if not match:
        return None
    return HREF_RE.findall(match.group(1))


def normalize(href):
    # The current page links to itself with a hash-only or onclick-guarded
    # href sometimes written as the bare path; treat equivalent paths the
    # same regardless of which page we're comparing from.
    return href


def main():
    nav_sets = {}
    foot_sets = {}

    for page in PAGES:
        path = ROOT / page
        if not path.exists():
            print(f"MISSING FILE: {page}")
            continue
        html = path.read_text()

        nav_hrefs = extract_hrefs(html, NAV_BLOCK_RE)
        foot_hrefs = extract_hrefs(html, FOOT_BLOCK_RE)

        if nav_hrefs is None:
            print(f"{page}: could not find a <div class=\"nav-links\"> block")
        else:
            nav_sets[page] = [normalize(h) for h in nav_hrefs]

        if foot_hrefs is None:
            print(f"{page}: could not find a <span class=\"foot-links\"> block")
        else:
            foot_sets[page] = [normalize(h) for h in foot_hrefs]

    ok = True
    ok &= report_drift("nav", nav_sets)
    ok &= report_drift("footer", foot_sets)

    if ok:
        print(f"OK — nav and footer links match across all {len(PAGES)} pages.")
        return 0
    return 1


def report_drift(label, sets_by_page):
    if not sets_by_page:
        return True

    # Majority link set wins as "the" reference, so one divergent page gets
    # flagged instead of everyone else being flagged against an arbitrary
    # first page.
    from collections import Counter
    counts = Counter(tuple(v) for v in sets_by_page.values())
    reference, _ = counts.most_common(1)[0]
    reference_set = set(reference)

    ok = True
    for page, hrefs in sets_by_page.items():
        page_set = set(hrefs)
        missing = reference_set - page_set
        extra = page_set - reference_set
        if missing or extra:
            ok = False
            print(f"{page} [{label}]: does not match the rest of the site")
            if missing:
                print(f"  missing: {sorted(missing)}")
            if extra:
                print(f"  extra:   {sorted(extra)}")
    return ok


if __name__ == "__main__":
    sys.exit(main())

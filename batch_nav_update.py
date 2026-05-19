#!/usr/bin/env python3
"""
Adds Case Studies to Commercial dropdown nav + mobile nav across all HTML files.
Also updates privacy-policy.html footer-bottom to standard format.
"""
import os
import re
import glob

BASE = "/Users/kel/Documents/projects/american-glass-experts"

# ── Desktop nav: add Case Studies after Commercial Areas in the dropdown ──
OLD_COMMERCIAL_NAV = '<li><a href="/service-areas">Commercial Areas</a></li></ul></li>'
NEW_COMMERCIAL_NAV = '<li><a href="/service-areas">Commercial Areas</a></li><li><a href="/case-studies">Case Studies</a></li></ul></li>'

# ── Mobile nav: add Case Studies link after Commercial Areas link ──
OLD_MOBILE_NAV = 'style="padding-left:28px;font-size:.85rem;opacity:.85;">Commercial Areas <span>→</span></a>'
NEW_MOBILE_NAV = 'style="padding-left:28px;font-size:.85rem;opacity:.85;">Commercial Areas <span>→</span></a>\n  <a href="/case-studies" style="padding-left:28px;font-size:.85rem;opacity:.85;">Case Studies <span>→</span></a>'

html_files = glob.glob(os.path.join(BASE, "**/*.html"), recursive=True) + \
             glob.glob(os.path.join(BASE, "*.html"))
html_files = list(set(html_files))

# skip the new files we just created (they already have the updated nav)
SKIP_NAMES = {
    "terms-of-service.html",
    "case-studies.html",
    "batch_footer_update.py",
    "batch_nav_update.py",
}

matched_desktop = []
matched_mobile = []
for f in sorted(html_files):
    fname = os.path.basename(f)
    if fname in SKIP_NAMES:
        continue
    # also skip case-studies/ directory files (new)
    if "/case-studies/" in f:
        continue
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    has_desktop = OLD_COMMERCIAL_NAV in content
    has_mobile = OLD_MOBILE_NAV in content
    if has_desktop or has_mobile:
        matched_desktop.append(f) if has_desktop else None
        matched_mobile.append(f) if has_mobile else None

all_matched = list(set(matched_desktop + matched_mobile))
print(f"DRY RUN: {len(all_matched)} files need nav update")
print(f"  Desktop dropdown matches: {len(matched_desktop)}")
print(f"  Mobile nav matches:       {len(matched_mobile)}")
for f in sorted(all_matched)[:8]:
    print(f"  {os.path.relpath(f, BASE)}")
if len(all_matched) > 8:
    print(f"  ... and {len(all_matched)-8} more")

confirm = input("\nProceed with nav update? (yes/no): ").strip().lower()
if confirm != "yes":
    print("Aborted.")
    exit(0)

changed = 0
errors = []
for f in all_matched:
    try:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
        new_content = content
        new_content = new_content.replace(OLD_COMMERCIAL_NAV, NEW_COMMERCIAL_NAV)
        new_content = new_content.replace(OLD_MOBILE_NAV, NEW_MOBILE_NAV)
        if new_content != content:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new_content)
            changed += 1
    except Exception as e:
        errors.append((f, str(e)))

print(f"\nDone: {changed} files updated")
if errors:
    print(f"Errors ({len(errors)}):")
    for f, e in errors:
        print(f"  {f}: {e}")

# ── Special fix: privacy-policy.html footer-bottom ──
pp = os.path.join(BASE, "privacy-policy.html")
OLD_PP_FOOTER = '<div><a href="/privacy-policy">Privacy Policy</a></div></div>'
NEW_PP_FOOTER = '<div style="display:flex;gap:20px;"><a href="/terms-of-service">Terms</a><a href="/privacy-policy">Privacy</a><a href="sitemap.xml">Sitemap</a><a href="/service-areas">Service Areas</a></div></div>'
with open(pp, "r", encoding="utf-8") as fh:
    pp_content = fh.read()
if OLD_PP_FOOTER in pp_content:
    pp_new = pp_content.replace(OLD_PP_FOOTER, NEW_PP_FOOTER)
    with open(pp, "w", encoding="utf-8") as fh:
        fh.write(pp_new)
    print("\nprivacy-policy.html footer-bottom updated")
else:
    print("\nprivacy-policy.html: old footer pattern not found — check manually")

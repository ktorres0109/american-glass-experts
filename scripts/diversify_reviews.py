#!/usr/bin/env python3
"""
Review diversification — assigns a different set of 6 reviews to each page.
Uses page path as deterministic seed so each page always gets the same reviews.

Usage:
  python scripts/diversify_reviews.py --dry-run
  python scripts/diversify_reviews.py
"""

import json
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
REVIEWS_FILE = Path(__file__).parent / "reviews.json"
DRY_RUN = "--dry-run" in sys.argv


def load_reviews():
    with open(REVIEWS_FILE) as f:
        return json.load(f)


def pick_six(reviews, seed_str):
    """Deterministic shuffle by seed, pick first 6."""
    h = int(hashlib.md5(seed_str.encode()).hexdigest(), 16)
    lst = list(range(len(reviews)))
    for i in range(len(lst) - 1, 0, -1):
        j = (h % (i + 1))
        h = h >> 1 or h  # prevent h going to 0
        lst[i], lst[j] = lst[j], lst[i]
    return [reviews[i] for i in lst[:6]]


def card_html(review, delay):
    stars = "<div class=\"review-stars\"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>"
    text = f"<p class=\"review-text\">{review['text']}</p>"
    footer = (
        f"<div class=\"review-footer\">"
        f"<div class=\"review-author\"><strong>{review['name']}</strong>"
        f"<span>{review['service']}</span></div>"
        f"<div class=\"yelp-badge\"><svg viewBox=\"0 0 24 24\">"
        f"<circle cx=\"12\" cy=\"12\" r=\"10\"/></svg>Yelp</div></div>"
    )
    return (
        f"        <div class=\"review-card reveal {delay}\">\n"
        f"          {stars}\n"
        f"          {text}\n"
        f"          {footer}\n"
        f"        </div>"
    )


def build_grid_content(reviews_for_page):
    delays = ["d1", "d2", "d3", "d1", "d2", "d3"]
    return "\n".join(card_html(r, delays[i]) for i, r in enumerate(reviews_for_page))


def find_grid_bounds(html):
    """Return (start, end) char positions of the reviews-grid div content (between opening and closing tags)."""
    marker = '<div class="reviews-grid">'
    start = html.find(marker)
    if start == -1:
        return None, None

    # Walk forward counting div depth to find matching close
    pos = start + len(marker)
    depth = 1
    while pos < len(html) and depth > 0:
        open_tag = html.find("<div", pos)
        close_tag = html.find("</div>", pos)
        if close_tag == -1:
            break
        if open_tag != -1 and open_tag < close_tag:
            depth += 1
            pos = open_tag + 4
        else:
            depth -= 1
            if depth == 0:
                # close_tag points to the closing </div> of the grid
                content_start = start + len(marker)
                content_end = close_tag
                return content_start, content_end
            pos = close_tag + 6
    return None, None


def process(filepath, reviews):
    html = filepath.read_text()
    content_start, content_end = find_grid_bounds(html)

    if content_start is None:
        return "skip"

    seed = filepath.name  # use filename as seed for consistency
    six = pick_six(reviews, seed)
    new_content = "\n" + build_grid_content(six) + "\n      "

    if DRY_RUN:
        names = [r["name"] for r in six]
        return f"would set: {names}"

    new_html = html[:content_start] + new_content + html[content_end:]
    filepath.write_text(new_html)
    return "updated"


def main():
    reviews = load_reviews()
    print(f"Loaded {len(reviews)} reviews")
    if DRY_RUN:
        print("DRY RUN — no files modified\n")

    patterns = ["*.html", "blog/*.html", "commercial/*.html"]
    files = []
    for p in patterns:
        files.extend(ROOT.glob(p))
    files = sorted(set(files))

    updated = skipped = 0
    for f in files:
        result = process(f, reviews)
        if result == "skip":
            skipped += 1
        else:
            updated += 1
            if DRY_RUN:
                print(f"  {f.name}: {result}")

    action = "Would update" if DRY_RUN else "Updated"
    print(f"\n{action}: {updated} pages | Skipped (no reviews section): {skipped}")


if __name__ == "__main__":
    main()

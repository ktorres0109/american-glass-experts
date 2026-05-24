#!/usr/bin/env python3
"""
Review diversification script — assigns different sets of 6 reviews to each page.

Usage:
  python scripts/diversify_reviews.py --dry-run   # count pages, show plan
  python scripts/diversify_reviews.py             # apply changes

Reviews source: scripts/reviews.json
"""

import json
import os
import re
import sys
import hashlib
from pathlib import Path

ROOT = Path(__file__).parent.parent
REVIEWS_FILE = Path(__file__).parent / "reviews.json"


def load_reviews():
    if not REVIEWS_FILE.exists():
        print("ERROR: scripts/reviews.json not found.")
        print("Create it with the format shown in scripts/reviews.json.example")
        sys.exit(1)
    with open(REVIEWS_FILE) as f:
        return json.load(f)


def pick_reviews(reviews, page_path, count=6):
    """Deterministically pick `count` reviews for a page using page path as seed."""
    # Use hash of path to get consistent but varied selection per page
    h = int(hashlib.md5(page_path.encode()).hexdigest(), 16)
    indices = list(range(len(reviews)))
    # Fisher-Yates shuffle seeded by hash
    for i in range(len(indices) - 1, 0, -1):
        j = (h >> i) % (i + 1)
        indices[i], indices[j] = indices[j], indices[i]
    return [reviews[i] for i in indices[:count]]


def build_review_html(review):
    """Build a single .review-card div from a review dict."""
    stars = '<div class="review-stars">' + '<span>★</span>' * 5 + '</div>'
    text = f'<p class="review-text">{review["text"]}</p>'
    footer = (
        f'<div class="review-footer">'
        f'<div class="review-author"><strong>{review["name"]}</strong>'
        f'<span>{review["service"]}</span></div>'
        f'<div class="yelp-badge">'
        f'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg>'
        f'Yelp</div></div>'
    )
    return f'<div class="review-card reveal d{{d}}">\n        {stars}\n        {text}\n        {footer}\n      </div>'


def build_reviews_grid(reviews_for_page):
    """Build the full 6-card reviews grid HTML."""
    cards = []
    delay_classes = ['d1', 'd2', 'd3', 'd1', 'd2', 'd3']
    for i, review in enumerate(reviews_for_page[:6]):
        d = delay_classes[i]
        stars = '<div class="review-stars"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>'
        text = f'<p class="review-text">{review["text"]}</p>'
        footer = (
            f'<div class="review-footer"><div class="review-author">'
            f'<strong>{review["name"]}</strong><span>{review["service"]}</span></div>'
            f'<div class="yelp-badge"><svg viewBox="0 0 24 24">'
            f'<circle cx="12" cy="12" r="10"/></svg>Yelp</div></div>'
        )
        card = (
            f'<div class="review-card reveal {d}">\n'
            f'        {stars}\n'
            f'        {text}\n'
            f'        {footer}\n'
            f'      </div>'
        )
        cards.append(card)
    return '\n      '.join(cards)


# Regex to match the reviews grid block
# Matches from first review-card to last closing </div> of the grid
GRID_PATTERN = re.compile(
    r'(<div class="reviews-grid"[^>]*>)'  # opening grid div
    r'(\s*<div class="review-card.*?</div>\s*){6}'  # exactly 6 cards
    r'(\s*</div>)',  # closing grid div
    re.DOTALL
)


def find_and_replace_reviews(html, new_cards_html):
    """Replace the 6 review cards inside .reviews-grid."""
    # Find the reviews-grid div and replace its contents
    pattern = re.compile(
        r'(<div class="reviews-grid"[^>]*>)(.*?)(</div>\s*</div>\s*</section)',
        re.DOTALL
    )

    def replacer(m):
        before = m.group(1)
        after = m.group(3)
        return f'{before}\n      {new_cards_html}\n    {after}'

    result, count = pattern.subn(replacer, html, count=1)
    return result, count


def process_file(filepath, reviews, dry_run=False):
    with open(filepath) as f:
        html = f.read()

    if 'class="reviews-grid"' not in html:
        return False, "no reviews-grid"

    page_path = str(filepath.relative_to(ROOT))
    page_reviews = pick_reviews(reviews, page_path, 6)
    new_cards = build_reviews_grid(page_reviews)

    if dry_run:
        return True, f"would update with reviews from: {[r['name'] for r in page_reviews]}"

    new_html, count = find_and_replace_reviews(html, new_cards)
    if count == 0:
        return False, "pattern not matched"

    with open(filepath, 'w') as f:
        f.write(new_html)
    return True, "updated"


def main():
    dry_run = '--dry-run' in sys.argv
    reviews = load_reviews()
    print(f"Loaded {len(reviews)} reviews from reviews.json")

    if dry_run:
        print("DRY RUN — no files will be changed\n")

    # Find all HTML files with reviews-grid
    html_files = []
    for pattern in ['*.html', 'blog/*.html', 'commercial/*.html']:
        html_files.extend(ROOT.glob(pattern))

    updated = 0
    skipped = 0
    errors = 0

    for filepath in sorted(html_files):
        success, msg = process_file(filepath, reviews, dry_run=dry_run)
        if success:
            updated += 1
            if dry_run:
                print(f"  {filepath.name}: {msg}")
        elif "no reviews-grid" in msg:
            skipped += 1
        else:
            errors += 1
            print(f"  WARN {filepath.name}: {msg}")

    print(f"\n{'Would update' if dry_run else 'Updated'}: {updated} pages")
    print(f"Skipped (no reviews section): {skipped}")
    if errors:
        print(f"Errors: {errors}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Diversify city page content using Claude Opus to pass Google's uniqueness threshold.
Updates 2 sections per page:
  - Service card <p> descriptions (6 per page)
  - "Why Choose Us" bullets (4 per page, when section exists)

Does NOT touch: HTML structure, attributes, styles, <h3> titles, phone numbers,
canonical tags, meta tags, or the About/d4 card (handled by generate_city_content.py).

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...   # or edit default in script
  python3 diversify_city_content.py --city burbank           # test one city
  python3 diversify_city_content.py --dry-run --city burbank # preview, no writes
  python3 diversify_city_content.py --chunk 1                # pages 1-50
  python3 diversify_city_content.py --chunk 2                # pages 51-100
  python3 diversify_city_content.py --chunk 3                # pages 101+
  python3 diversify_city_content.py --force --city burbank   # rerun even if logged
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

# ─── Config ─────────────────────────────────────────────────────────────────

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
if not ANTHROPIC_API_KEY:
    sys.exit("Error: set ANTHROPIC_API_KEY env var before running")
API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-opus-4-6"
LOG_FILE = Path(__file__).parent / "diversify_log.json"
CHUNK_SIZE = 50

# Non-city pages — skip these
SKIP_STEMS = {
    "about", "blog", "contact", "custom-mirrors", "emergency-glass",
    "gallery", "index", "privacy-policy", "review", "service-areas",
    "services", "shower-enclosures", "storefront-glass", "window-repair",
}

# Map normalized <h3> text → JSON key
H3_TO_KEY = {
    "shower enclosures": "shower",
    "window repair & replacement": "windows",
    "window repair &amp; replacement": "windows",
    "storefronts & commercial glass": "storefronts",
    "storefronts &amp; commercial glass": "storefronts",
    "mirrors": "mirrors",
    "glass partitions": "partitions",
    "emergency repairs & board-up": "emergency",
    "emergency repairs &amp; board-up": "emergency",
}

# ─── City data (from generate_city_content.py) ───────────────────────────────
# slug → (county, area_type, housing_notes)

CITY_DATA = {
    "adelanto": ("San Bernardino County", "desert city", "high desert single-family tracts"),
    "agoura-hills": ("Los Angeles County", "upscale suburb", "luxury hillside homes and ranch properties"),
    "alhambra": ("Los Angeles County", "urban suburb", "dense residential and busy commercial storefronts"),
    "apple-valley": ("San Bernardino County", "high desert town", "sprawling single-family homes on large lots"),
    "arleta": ("Los Angeles County", "working-class neighborhood", "older single-family homes and small commercial strips"),
    "azusa": ("Los Angeles County", "foothill city", "mix of bungalows and newer developments near the mountains"),
    "baldwin-park": ("Los Angeles County", "urban suburb", "dense residential and commercial corridors"),
    "banning": ("Riverside County", "pass city", "retirement communities and transit-corridor commercial properties"),
    "beaumont": ("Riverside County", "fast-growing suburb", "new master-planned communities with modern open-plan homes"),
    "bell-canyon": ("Los Angeles County", "gated community", "exclusive private residences with high-end finishes"),
    "big-bear-lake": ("San Bernardino County", "mountain resort town", "vacation cabins, chalets, and lakefront properties"),
    "burbank": ("Los Angeles County", "media industry hub", "bungalows, entertainment studios, and commercial storefronts"),
    "calabasas": ("Los Angeles County", "affluent gated enclave", "luxury estates, high-end condos, and upscale retail"),
    "calimesa": ("Riverside County", "small foothill city", "quiet residential neighborhoods and senior communities"),
    "camarillo": ("Ventura County", "planned suburban city", "master-planned neighborhoods with modern tract homes"),
    "canoga-park": ("Los Angeles County", "west Valley neighborhood", "dense residential and Warner Center office towers"),
    "canyon-lake": ("Riverside County", "private lake community", "waterfront and hillside homes inside a gated community"),
    "carson": ("Los Angeles County", "industrial suburb", "residential neighborhoods alongside industrial parks near the port"),
    "cathedral-city": ("Riverside County", "desert city", "resort condos and permanent residences near Palm Springs"),
    "chatsworth": ("Los Angeles County", "west Valley neighborhood", "upscale hillside homes, horse properties, and industrial parks"),
    "chino": ("San Bernardino County", "inland suburb", "newer tract developments amid agricultural-to-residential transitions"),
    "chino-hills": ("San Bernardino County", "affluent suburb", "hillside executive homes with panoramic valley views"),
    "claremont": ("Los Angeles County", "college town", "craftsman bungalows, academic buildings, and tree-lined streets"),
    "coachella": ("Riverside County", "desert city", "agricultural community with growing residential development"),
    "colton": ("San Bernardino County", "inland city", "older homes, light industrial, and commercial strips"),
    "compton": ("Los Angeles County", "urban city", "dense residential neighborhoods undergoing revitalization"),
    "corona": ("Riverside County", "master-planned city", "large suburban tracts, retail corridors, and business parks"),
    "covina": ("Los Angeles County", "east San Gabriel Valley", "post-war neighborhoods and established commercial strips"),
    "culver-city": ("Los Angeles County", "tech and media hub", "renovated mid-century homes and modern commercial lofts"),
    "desert-hot-springs": ("Riverside County", "desert spa town", "mid-century motels, spa resorts, and desert residential"),
    "diamond-bar": ("Los Angeles County", "upscale east San Gabriel Valley", "executive homes in gated communities on rolling hills"),
    "downey": ("Los Angeles County", "south San Gabriel Valley", "post-war suburban homes and active commercial main streets"),
    "duarte": ("Los Angeles County", "foothill suburb", "quiet residential near the Angeles National Forest"),
    "eastvale": ("Riverside County", "new master-planned city", "large modern homes with open floor plans and oversized windows"),
    "el-monte": ("Los Angeles County", "San Gabriel Valley", "dense urban neighborhood with older residential and commercial stock"),
    "el-segundo": ("Los Angeles County", "coastal industrial city", "beachside homes, aerospace campuses, and retail corridors"),
    "encino": ("Los Angeles County", "upscale Valley neighborhood", "mid-century homes on large lots and luxury estate properties"),
    "fillmore": ("Ventura County", "small agricultural town", "quaint historic downtown and modest residential neighborhoods"),
    "fontana": ("San Bernardino County", "large inland city", "sprawling new residential developments and big-box commercial"),
    "gardena": ("Los Angeles County", "south Bay suburb", "dense post-war residential with active commercial strips"),
    "glendale": ("Los Angeles County", "urban suburb", "high-density condos, historic homes, and Americana at Brand retail"),
    "glendora": ("Los Angeles County", "foothill suburb", "historic downtown and executive hillside neighborhoods"),
    "granada-hills": ("Los Angeles County", "north Valley suburb", "established single-family neighborhoods with ranch-style homes"),
    "grand-terrace": ("San Bernardino County", "small inland city", "quiet residential between Colton and Loma Linda"),
    "hawthorne": ("Los Angeles County", "south Bay city", "dense urban neighborhoods near LAX and aerospace campuses"),
    "hemet": ("Riverside County", "inland valley city", "retirement communities, mobile home parks, and older residential"),
    "hesperia": ("San Bernardino County", "high desert city", "sprawling suburban development in the Victor Valley"),
    "hidden-hills": ("Los Angeles County", "exclusive gated city", "celebrity estates and luxury ranch properties on equestrian lots"),
    "indian-wells": ("Riverside County", "resort city", "luxury golf course communities and upscale resort hotels"),
    "indio": ("Riverside County", "desert city", "date farms, resort communities, and festival venues"),
    "inglewood": ("Los Angeles County", "urban city", "dense residential and commercial near SoFi Stadium"),
    "jurupa-valley": ("Riverside County", "newer incorporated city", "industrial warehouses alongside residential neighborhoods"),
    "la-puente": ("Los Angeles County", "San Gabriel Valley suburb", "dense working-class residential and commercial corridors"),
    "la-quinta": ("Riverside County", "desert resort city", "luxury golf communities, spas, and executive homes"),
    "la-verne": ("Los Angeles County", "foothill college town", "craftsman homes and upscale residential"),
    "lake-elsinore": ("Riverside County", "inland lake city", "lakefront homes, new hillside developments, and outdoor recreation areas"),
    "lakewood": ("Los Angeles County", "post-war planned city", "uniform mid-century tract homes and suburban retail"),
    "loma-linda": ("San Bernardino County", "university medical city", "medical campus buildings and modest residential neighborhoods"),
    "long-beach": ("Los Angeles County", "coastal port city", "beach bungalows, high-rise condos, and port commercial"),
    "los-angeles": ("Los Angeles County", "metropolis", "every housing type from historic Craftsmans to glass-curtain-wall high-rises"),
    "malibu": ("Los Angeles County", "coastal celebrity enclave", "beachfront compounds, cliffside estates, and glass-heavy modern architecture"),
    "menifee": ("Riverside County", "fast-growing new city", "master-planned communities with modern suburban homes"),
    "mission-hills": ("Los Angeles County", "north Valley neighborhood", "established single-family residential along the 118 corridor"),
    "monrovia": ("Los Angeles County", "foothill suburb", "historic Victorian downtown and craftsman neighborhoods"),
    "montclair": ("San Bernardino County", "inland suburb", "dense residential and Ontario Mills shopping corridor"),
    "montebello": ("Los Angeles County", "east LA suburb", "established residential near Montebello Town Center"),
    "monterey-park": ("Los Angeles County", "San Gabriel Valley", "diverse urban suburb with dense residential and active commercial"),
    "moorpark": ("Ventura County", "semi-rural suburb", "tract homes, equestrian properties, and country club communities"),
    "moreno-valley": ("Riverside County", "large inland city", "expansive suburban tracts and growing warehouse corridors"),
    "murrieta": ("Riverside County", "upscale south IE suburb", "master-planned communities with newer executive homes"),
    "newbury-park": ("Ventura County", "Conejo Valley suburb", "established suburban neighborhood near open space preserves"),
    "norco": ("Riverside County", "Horsetown USA", "equestrian estates with horse trails throughout the city"),
    "north-hills": ("Los Angeles County", "mid-Valley neighborhood", "dense residential with older single-family and apartment stock"),
    "north-hollywood": ("Los Angeles County", "NoHo Arts District", "arts district lofts, mid-century homes, and commercial on Lankershim"),
    "northridge": ("Los Angeles County", "north Valley suburb", "CSUN campus area with large residential lots and commercial corridors"),
    "oak-park": ("Ventura County", "planned community", "upscale residential bordering the Santa Monica Mountains"),
    "ontario": ("San Bernardino County", "inland hub city", "suburban residential, logistics warehouses, and Ontario Airport corridor"),
    "oxnard": ("Ventura County", "coastal agricultural city", "strawberry fields, harbor-front condos, and residential neighborhoods"),
    "pacific-palisades": ("Los Angeles County", "coastal affluent enclave", "post-fire rebuild zone with glass-heavy modern homes on canyon lots"),
    "pacoima": ("Los Angeles County", "north Valley neighborhood", "working-class residential and industrial pockets near Hansen Dam"),
    "palm-desert": ("Riverside County", "desert resort city", "upscale El Paseo shopping, golf communities, and resort hotels"),
    "palm-springs": ("Riverside County", "desert resort city", "iconic mid-century modern architecture and glass-wall vacation homes"),
    "panorama-city": ("Los Angeles County", "central Valley neighborhood", "dense multi-family residential and large commercial centers"),
    "pasadena": ("Los Angeles County", "historic academic city", "Victorian and craftsman estates near Caltech and the Rose Bowl"),
    "perris": ("Riverside County", "fast-growing inland city", "new large-lot subdivisions and logistics warehouse parks"),
    "pico-rivera": ("Los Angeles County", "east LA suburb", "dense post-war residential along active commercial corridors"),
    "pomona": ("Los Angeles County", "inland hub city", "Cal Poly campus, historic Victorian neighborhoods, and arts district"),
    "port-hueneme": ("Ventura County", "naval city", "Naval Base, beach condos, and working waterfront properties"),
    "rancho-cucamonga": ("San Bernardino County", "affluent IE suburb", "planned communities at the base of the mountains with luxury retail"),
    "rancho-mirage": ("Riverside County", "desert enclave", "gated country clubs and luxury resort communities"),
    "redlands": ("San Bernardino County", "historic inland city", "Victorian mansions, university campus, and established residential"),
    "reseda": ("Los Angeles County", "central Valley neighborhood", "our home base with post-war bungalows and apartments along Reseda Blvd"),
    "rialto": ("San Bernardino County", "inland city", "post-war residential and growing logistics developments"),
    "riverside": ("Riverside County", "county seat", "historic Mission Inn area, UC Riverside campus, and diverse residential"),
    "rubidoux": ("Riverside County", "unincorporated community", "working-class residential along the Santa Ana River"),
    "san-bernardino": ("San Bernardino County", "county seat", "diverse urban neighborhoods and commercial corridors on E Street"),
    "san-dimas": ("Los Angeles County", "foothill suburb", "historic downtown, equestrian properties, and family neighborhoods"),
    "san-fernando": ("Los Angeles County", "small city in the Valley", "dense working-class neighborhood with commercial strips on Brand Blvd"),
    "san-gabriel": ("Los Angeles County", "San Gabriel Valley", "historic Craftsman homes and active San Gabriel Square"),
    "san-jacinto": ("Riverside County", "inland valley city", "college area, retirement communities, and rural residential"),
    "san-marino": ("Los Angeles County", "exclusive residential city", "only large estate homes on wide tree-lined streets, no commercial zoning"),
    "santa-clarita": ("Los Angeles County", "north LA suburb", "master-planned communities and newer tract developments"),
    "santa-monica": ("Los Angeles County", "beachfront city", "upscale condos, boutique hotels, and beach bungalows"),
    "santa-paula": ("Ventura County", "small citrus town", "historic oil heritage, citrus groves, and quaint Victorian downtown"),
    "sherman-oaks": ("Los Angeles County", "upscale Valley neighborhood", "renovated mid-century homes, Ventura Blvd boutiques, and luxury condos"),
    "simi-valley": ("Ventura County", "suburban commuter city", "large planned residential tracts and suburban commercial"),
    "south-pasadena": ("Los Angeles County", "small walkable city", "historic craftsman homes and charming Mission St commercial"),
    "studio-city": ("Los Angeles County", "foothills neighborhood", "TV studios, celebrity homes in Fryman Canyon, and Ventura Blvd dining"),
    "sun-city": ("Riverside County", "active-adult community", "55-plus retirement communities with golf courses and clubhouses"),
    "sylmar": ("Los Angeles County", "north Valley neighborhood", "horse properties, older single-family homes, and industrial near I-5"),
    "tarzana": ("Los Angeles County", "west Valley suburb", "upscale hillside homes, Ventura Blvd commercial, and dense residential"),
    "temecula": ("Riverside County", "wine country suburb", "wine country estates, master-planned communities, and Old Town retail"),
    "temple-city": ("Los Angeles County", "San Gabriel Valley", "dense residential with active commercial on Las Tunas and Cherry Ave"),
    "thousand-oaks": ("Ventura County", "affluent Conejo Valley city", "master-planned communities, biotech corridor, and civic arts center"),
    "topanga-canyon": ("Los Angeles County", "arts enclave", "off-grid cabins, artist studios, and canyon estates in the Santa Monica Mountains"),
    "torrance": ("Los Angeles County", "south Bay suburb", "beach-adjacent residential, Honda campus, and Del Amo Fashion Center"),
    "upland": ("San Bernardino County", "foothill city", "historic downtown, craftsman bungalows, and executive hillside homes"),
    "valley-village": ("Los Angeles County", "east Valley neighborhood", "quiet craftsman and colonial revival homes near North Hollywood"),
    "van-nuys": ("Los Angeles County", "central Valley hub", "dense urban residential, Van Nuys Airport, and active commercial"),
    "ventura": ("Ventura County", "coastal county seat", "historic downtown, harbor, Mission-era architecture, and beach residential"),
    "victorville": ("San Bernardino County", "high desert city", "Route 66 heritage and fast-growing suburban development"),
    "walnut": ("Los Angeles County", "San Gabriel Valley suburb", "upscale planned residential near Mt. San Antonio College"),
    "west-covina": ("Los Angeles County", "east San Gabriel Valley", "post-war suburban tracts and Eastland Center commercial corridor"),
    "west-hills": ("Los Angeles County", "west Valley suburb", "upscale residential at the western edge of the Valley near the 101"),
    "westlake-village": ("Los Angeles County", "master-planned lake community", "luxury lake-view homes, country clubs, and high-end retail"),
    "whittier": ("Los Angeles County", "south San Gabriel Valley", "historic Uptown district and established craftsman residential"),
    "wildomar": ("Riverside County", "new south IE city", "newer residential subdivisions and rural horse properties"),
    "winchester": ("Riverside County", "rural community", "horse ranches, large-lot residential, and new master-planned subdivisions"),
    "winnetka": ("Los Angeles County", "west Valley neighborhood", "dense apartment corridors and single-family residential pockets"),
    "woodland-hills": ("Los Angeles County", "upscale west Valley", "Warner Center high-rises, luxury residential, and Westfield Topanga mall"),
    "yucaipa": ("San Bernardino County", "foothill city", "cherry orchards, mountain-view estates, and suburban residential"),
}


# ─── API ─────────────────────────────────────────────────────────────────────

def call_claude(prompt: str, max_retries: int = 3) -> str:
    data = json.dumps({
        "model": MODEL,
        "max_tokens": 1500,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(
                API_URL,
                data=data,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": ANTHROPIC_API_KEY,
                    "anthropic-version": "2023-06-01",
                },
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = json.loads(resp.read())
            return result["content"][0]["text"].strip()
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"    retry {attempt + 1}: {e}")
                time.sleep(2 ** attempt)
            else:
                raise


def build_prompt(city_name: str, county: str, area_type: str, housing_notes: str) -> str:
    return f"""You're updating the website of American Glass Experts — a family-run C-17 licensed glazing contractor out of Reseda, CA. They do residential and commercial glass work across Southern California. The owner has been doing this for years and knows every part of the region.

You're writing content for their {city_name}, CA page. About this city:
- County: {county}
- Character: {area_type}
- Local stock: {housing_notes}

Write like someone who actually drives to {city_name} and does glass work there. Not a marketer. Short sentences. Reference what's real about the local housing and commercial mix. Use trade terms naturally when they fit (dual-pane, IGU, tempered, frameless, storefront aluminum, etc.). Sound like a contractor, not a content writer.

AVOID COMPLETELY: premier, exceptional, comprehensive, tailored, seamlessly, leverage, top-notch, cutting-edge, state-of-the-art, unparalleled, ensure, facilitate, utilize, moreover, furthermore, diverse range, wide variety, dedicated team, committed to excellence, look no further, your needs.

Return ONLY a valid JSON object — no markdown fences, no explanation, no text before or after the JSON:

{{
  "service_cards": {{
    "shower": "Up to 25 words. Mention {city_name}. What makes shower glass installs specific to the housing here — material, config, or why people call.",
    "windows": "Up to 25 words. Mention {city_name}. What window repair looks like given local building age or type.",
    "storefronts": "Up to 25 words. Mention {city_name}. What commercial glass needs look like — what kind of businesses, what problems they have.",
    "mirrors": "Up to 20 words. Mention {city_name}. Custom mirror context — bathrooms, gyms, closets — relevant to who lives/works there.",
    "partitions": "Up to 20 words. Glass partition context relevant to {city_name} — residential or commercial use case.",
    "emergency": "Up to 20 words. Mention {city_name}. Emergency glass — what situations come up, how fast we get there."
  }},
  "why_choose_us": [
    {{"title": "3–5 word phrase", "detail": "Up to 20 words. A concrete reason specific to serving {city_name} — geography, housing type, or local business patterns."}},
    {{"title": "3–5 word phrase", "detail": "Up to 20 words. Different angle — maybe drive time, project type, or something about how the city's buildings behave."}},
    {{"title": "3–5 word phrase", "detail": "Up to 20 words. Something about our license, process, or crew that matters specifically in {city_name}."}},
    {{"title": "3–5 word phrase", "detail": "Up to 20 words. A practical differentiator — permits, same-day response, commercial work, or something else concrete."}}
  ]
}}"""


# ─── JSON Parsing ─────────────────────────────────────────────────────────────

def parse_json_response(text: str) -> dict:
    """Extract JSON from Claude's response even if it includes extra text."""
    # Strip markdown fences
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\s*```$", "", text, flags=re.MULTILINE)
    text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try to extract a JSON object from the middle of the response
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())

    raise ValueError(f"No valid JSON in response:\n{text[:400]}")


# ─── HTML Patching ────────────────────────────────────────────────────────────

def html_escape(text: str) -> str:
    """Escape & < > for safe injection into HTML text nodes."""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )


def strip_tags(text: str) -> str:
    """Remove any HTML tags Claude might have included in its output."""
    return re.sub(r"<[^>]+>", "", text).strip()


def patch_service_cards(html: str, service_cards: dict) -> tuple:
    """
    Replace <p> text inside each service-card-body, matched by <h3> title.
    Returns (patched_html, count_of_cards_replaced).
    """
    patched = 0

    def replacer(m):
        nonlocal patched
        h3_raw = m.group(2).strip()
        key = H3_TO_KEY.get(h3_raw.lower())
        if key and key in service_cards:
            new_text = html_escape(strip_tags(service_cards[key]))
            patched += 1
            # Keep group 1 (open tag + span + h3 open), group 2 (h3 text), group 3 (h3 close + p open)
            return m.group(1) + h3_raw + m.group(3) + new_text + m.group(5)
        return m.group(0)

    # Match: service-card-body > span > h3 > p
    pattern = (
        r'(<div class="service-card-body">\s*<span[^<]*</span>\s*<h3>)'
        r'(.*?)'
        r'(</h3>\s*<p>)'
        r'(.*?)'
        r'(</p>)'
    )
    html = re.sub(pattern, replacer, html, flags=re.DOTALL)
    return html, patched


def patch_why_choose_us(html: str, bullets: list) -> tuple:
    """
    Replace all <li> items in the Why Choose Us <ul>.
    Preserves the <ul> opening tag (and its style attribute) exactly.
    Returns (patched_html, was_patched).
    """
    # Find the section by its label span
    label_pos = html.find(">Why Choose Us</span>")
    if label_pos < 0:
        return html, False

    # Find the <ul> that follows the label
    ul_start = html.find("<ul", label_pos)
    if ul_start < 0:
        return html, False

    ul_end_pos = html.find("</ul>", ul_start)
    if ul_end_pos < 0:
        return html, False

    ul_close = ul_end_pos + len("</ul>")

    # Preserve the original <ul> opening tag exactly (keep its style attribute)
    ul_open_end = html.find(">", ul_start) + 1
    ul_open_tag = html[ul_start:ul_open_end]

    # Build replacement <li> items with the same inline style as original
    li_style = "margin-bottom:14px;padding-left:8px;border-left:3px solid var(--blue);"
    items = []
    for b in bullets:
        title = html_escape(strip_tags(b.get("title", "")))
        detail = html_escape(strip_tags(b.get("detail", "")))
        if title and detail:
            items.append(
                f'      <li style="{li_style}"><strong>{title}</strong> — {detail}</li>'
            )

    if not items:
        return html, False

    new_ul = ul_open_tag + "\n" + "\n".join(items) + "\n    </ul>"
    html = html[:ul_start] + new_ul + html[ul_close:]
    return html, True


# ─── Log ─────────────────────────────────────────────────────────────────────

def load_log() -> dict:
    if LOG_FILE.exists():
        try:
            return json.loads(LOG_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_log(log: dict):
    LOG_FILE.write_text(json.dumps(log, indent=2), encoding="utf-8")


# ─── Per-city processing ─────────────────────────────────────────────────────

def process_city(page: Path, dry_run: bool = False) -> dict:
    slug = page.stem
    data = CITY_DATA.get(slug)
    if not data:
        return {"status": "skip", "reason": "no city data"}

    county, area_type, housing_notes = data
    city_name = " ".join(
        w.capitalize() if w.lower() not in ("de", "del") else w.lower()
        for w in slug.replace("-", " ").split()
    )

    prompt = build_prompt(city_name, county, area_type, housing_notes)
    raw = call_claude(prompt)
    content = parse_json_response(raw)

    service_cards = content.get("service_cards", {})
    why_bullets = content.get("why_choose_us", [])

    if dry_run:
        print(f"\n  [DRY RUN] {city_name}")
        print("  service_cards:")
        for k, v in service_cards.items():
            print(f"    {k}: {v}")
        print("  why_choose_us:")
        for b in why_bullets:
            print(f"    [{b.get('title')}] {b.get('detail')}")
        return {"status": "dry_run"}

    html = page.read_text(encoding="utf-8")

    # Create backup (only on first run — don't overwrite existing backup)
    backup = page.with_suffix(".html.bak")
    if not backup.exists():
        backup.write_text(html, encoding="utf-8")

    html, cards_patched = patch_service_cards(html, service_cards)
    html, wcu_patched = patch_why_choose_us(html, why_bullets)

    page.write_text(html, encoding="utf-8")

    return {
        "status": "ok",
        "cards_patched": cards_patched,
        "wcu_patched": wcu_patched,
    }


# ─── Entry point ─────────────────────────────────────────────────────────────

def get_city_pages(repo_dir: Path) -> list:
    return sorted([f for f in repo_dir.glob("*.html") if f.stem not in SKIP_STEMS])


def main():
    parser = argparse.ArgumentParser(description="Diversify city page content via Claude Opus.")
    parser.add_argument("--city", help="Process a single city slug (e.g. burbank)")
    parser.add_argument("--chunk", type=int, choices=[1, 2, 3], help="Process 50-page chunk (1, 2, or 3)")
    parser.add_argument("--dry-run", action="store_true", help="Preview generated content without writing files")
    parser.add_argument("--force", action="store_true", help="Reprocess cities already in the log")
    args = parser.parse_args()

    repo_dir = Path(__file__).parent
    log = load_log()

    if args.city:
        page = repo_dir / f"{args.city}.html"
        if not page.exists():
            sys.exit(f"Error: {page} not found")
        pages = [page]
    else:
        all_pages = get_city_pages(repo_dir)
        if args.chunk:
            start = (args.chunk - 1) * CHUNK_SIZE
            pages = all_pages[start : start + CHUNK_SIZE]
        else:
            pages = all_pages

    print(f"Processing {len(pages)} page(s) with {MODEL}...")
    if args.dry_run:
        print("  (DRY RUN — no files will be written)\n")

    success, skipped, failed = 0, 0, []

    for page in pages:
        slug = page.stem

        if not args.force and not args.dry_run and log.get(slug, {}).get("status") == "ok":
            print(f"  SKIP {slug} — already done (--force to rerun)")
            skipped += 1
            continue

        print(f"  {slug}...", end=" ", flush=True)
        try:
            result = process_city(page, dry_run=args.dry_run)
            status = result.get("status", "?")
            if status == "ok":
                cards = result.get("cards_patched", 0)
                wcu = result.get("wcu_patched", False)
                print(f"OK ({cards} cards, wcu={'yes' if wcu else 'no'})")
                success += 1
            elif status == "dry_run":
                pass  # output already printed in process_city
            else:
                print(status)
                skipped += 1

            log[slug] = result
            if not args.dry_run:
                save_log(log)

            time.sleep(0.5)

        except Exception as e:
            print(f"ERROR: {e}")
            failed.append(slug)
            log[slug] = {"status": "error", "error": str(e)}
            if not args.dry_run:
                save_log(log)
            time.sleep(2)

    print(f"\nDone: {success} updated, {skipped} skipped, {len(failed)} failed")
    if failed:
        print("Failed cities:", failed)
        print("Re-run with --force to retry failed cities.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate unique city-specific content for each location page using Gemini.
Replaces the About card (d4) in each city page.
Run again to regenerate: existing d4 cards are replaced.
"""

import re
import json
import time
import urllib.request
from pathlib import Path

GEMINI_API_KEY = "AIzaSyBSVDvudMVGPnV1ABzMeFL5On19qFO7P0g"
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent?key=" + GEMINI_API_KEY
)

# slug → (county, area type, housing / building notes)
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


def call_gemini(prompt: str) -> str:
    data = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024,
            "thinkingConfig": {"thinkingBudget": 0}
        }
    }).encode("utf-8")
    req = urllib.request.Request(
        GEMINI_URL, data=data,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
    return result["candidates"][0]["content"]["parts"][0]["text"].strip()


def generate_blurb(city_name: str, county: str, area_type: str, housing_notes: str) -> str:
    prompt = (
        f"Write exactly 2 complete sentences (50-60 words total) of unique, factual local context "
        f"for a glass contractor's location page targeting {city_name}, {county}, California. "
        f"The area is a {area_type} with {housing_notes}. "
        f"Mention the specific type of glass work most relevant to the local housing/building stock "
        f"(e.g. frameless showers for luxury estates, storefront glass for commercial corridors, "
        f"dual-pane window replacement for older homes). Be concrete and location-specific. "
        f"Output ONLY the 2 sentences. No HTML. No markdown. No quotes."
    )
    return call_gemini(prompt)


def patch_city_page(filepath: Path, city_name: str, blurb: str) -> bool:
    html = filepath.read_text(encoding="utf-8")

    new_card = (
        f'<div class="city-highlight-card reveal d4">\n'
        f'          <h4>\U0001f3d9\ufe0f About {city_name}</h4>\n'
        f'          <p>{blurb}</p>\n'
        f'        </div>'
    )

    # If d4 already exists, replace it
    if 'class="city-highlight-card reveal d4"' in html:
        html = re.sub(
            r'<div class="city-highlight-card reveal d4">.*?</div>',
            new_card,
            html,
            flags=re.S
        )
        filepath.write_text(html, encoding="utf-8")
        return True

    # Otherwise insert d4 inside the city-highlights div, before its closing tag
    # Target: the closing </div> of the city-highlights container (after d3)
    match = re.search(
        r'(<div class="city-highlight-card reveal d3">.*?</div>)(\s*</div>)',
        html, re.S
    )
    if not match:
        print(f"  SKIP {city_name}: d3 card not found")
        return False

    insert_at = match.start(2)  # position of the closing </div> of city-highlights
    html = html[:insert_at] + "\n        " + new_card + html[insert_at:]
    filepath.write_text(html, encoding="utf-8")
    return True


def main():
    repo_dir = Path(__file__).parent
    city_pages = sorted([
        f for f in repo_dir.glob("*.html")
        if f.stem not in ("index", "contact", "services", "gallery", "service-areas")
    ])

    print(f"Processing {len(city_pages)} city pages...")
    success, failed = 0, []

    for page in city_pages:
        slug = page.stem
        data = CITY_DATA.get(slug)
        if not data:
            print(f"  NO DATA: {slug}")
            continue

        county, area_type, housing_notes = data
        # Proper title case for display
        city_name = " ".join(
            w if w.lower() in ("de", "del") else w.capitalize()
            for w in slug.replace("-", " ").split()
        )

        print(f"  {city_name}...", end=" ", flush=True)
        try:
            blurb = generate_blurb(city_name, county, area_type, housing_notes)
            # Sanitize: strip any HTML tags Gemini might have snuck in
            blurb = re.sub(r"<[^>]+>", "", blurb).strip()
            patched = patch_city_page(page, city_name, blurb)
            status = "OK" if patched else "skipped"
            print(status)
            if patched:
                success += 1
            time.sleep(0.25)
        except Exception as e:
            print(f"ERROR: {e}")
            failed.append(slug)
            time.sleep(1)

    print(f"\nDone: {success} updated, {len(failed)} failed")
    if failed:
        print("Failed:", failed)


if __name__ == "__main__":
    main()

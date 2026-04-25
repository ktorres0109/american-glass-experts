#!/usr/bin/env python3
"""
Add FAQPage JSON-LD schema to all 5 service pages.
Extract Q&A from the HTML and emit structured data.
"""
import re, json, os

SERVICE_FAQS = {
    "shower-enclosures": [
        ("What is the primary benefit of a frameless shower door installation?",
         "A frameless shower door offers a modern, minimalist aesthetic, making your bathroom feel more spacious and open. It is also easier to clean due to fewer metal frames trapping grime, enhancing both style and hygiene."),
        ("How long does a custom shower glass installation take?",
         "Fabrication takes 3–5 business days. The actual installation typically takes one full day. Most projects go from measurement to installed enclosure in 5–7 business days."),
        ("Can you install a semi-frameless shower enclosure in an uneven space?",
         "Yes. We field-measure every job and custom-cut to actual dimensions. Uneven walls and floors are accommodated with precise fitting techniques."),
        ("What maintenance is required for a new shower enclosure?",
         "Use a squeegee after each use and clean monthly with a non-abrasive glass cleaner. Avoid harsh chemicals that can damage hardware or glass coatings. Rubber seals and wipes need replacement every 3–5 years."),
        ("What is the difference between 3/8 inch and 1/2 inch shower glass?",
         "Both are tempered safety glass. 3/8 inch (9.5mm) is the standard for most frameless installations. 1/2 inch (12mm) is premium — noticeably heavier and more rigid, preferred for large panels or spa-quality installations. We stock both."),
        ("How long does frameless shower glass last?",
         "The glass itself lasts indefinitely. Hardware (hinges, handles, seals) is the wear item — quality hardware lasts 10–20 years. Rubber seals need replacement every 3–5 years and cost under $50."),
        ("Can you install shower glass over existing tile?",
         "Yes — this is the normal sequence. Tile goes in first, then we measure and install. We mount into tile using anchors rated for wet-area applications and waterproof all penetration points."),
        ("Do I need a permit for shower glass installation in California?",
         "A permit is not typically required for shower enclosure replacement when plumbing and structure are not being altered. We will advise at the estimate if your job requires permit coordination."),
    ],
    "window-repair": [
        ("Can foggy windows be fixed without replacing the whole window?",
         "Yes — in most cases. If only the sealed glass unit has failed (fogging between the panes), we replace the IGU without touching your frame, sash, or trim. This costs $250–$550 per unit, versus $500–$1,200 or more for a full window replacement."),
        ("How do I know if I need IGU replacement or full window replacement?",
         "If the glass is foggy between panes but the frame and operation are fine, you need IGU replacement only. If the frame is cracked, rotted, or will not seal properly — or if you want to change the window style — full replacement is the right move."),
        ("Do you repair sliding glass doors?",
         "Yes — sliding glass door glass panel replacement, track replacement, and roller replacement are all services we provide. Rollers are the most common failure on sliding doors."),
        ("Are there rebates for Low-E window replacement in Southern California?",
         "Yes. LADWP and SCE offer rebates for qualifying dual-pane Low-E window replacements. We can tell you at the estimate whether your project qualifies."),
        ("How long does window seal replacement take?",
         "We typically measure on Monday and schedule replacement within the same week. Each IGU takes 1–3 hours to swap depending on window size and accessibility."),
        ("What causes foggy windows?",
         "Fogging between dual-pane glass is caused by a failed insulating seal. The argon or krypton gas that provides insulation escapes, moisture enters, and condensation forms on the interior glass surfaces. The fix is replacing the IGU — the sealed glass unit — not the entire window."),
    ],
    "storefront-glass": [
        ("Do you handle emergency storefront board-up at night?",
         "For commercial break-ins and urgent situations, call (805) 750-6471 directly. We monitor until 10pm and can dispatch for genuine emergencies. After-hours emergency board-up is available."),
        ("Does commercial storefront glass replacement require a permit?",
         "Replacing broken glass in-kind typically does not require a permit. Changing the framing system, size, or adding new openings does require a permit. As C-17 licensed contractors, we coordinate permit filing when required."),
        ("What glass type should I use for my storefront?",
         "Standard storefronts use 1/4 inch annealed glass in aluminum systems. Any glass in or adjacent to a commercial door must be safety glazing — tempered or laminated — per California code. We will recommend the right specification for your situation."),
        ("Can you install glass office partitions?",
         "Yes. We install full-height frameless glass partitions, aluminum-framed partition systems with glass lites, and partial-height dividers. All commercial partition work is permitted where required."),
        ("How quickly can you replace storefront glass after a break-in?",
         "We do board-up same day to secure the premises. Permanent glass replacement follows within 3–5 business days for standard commercial panel sizes, which we stock. Custom or oversized panels may take 5–10 business days to fabricate."),
    ],
    "custom-mirrors": [
        ("How do you mount large mirrors safely?",
         "We anchor large mirrors — over 20 pounds — to studs or use toggle anchors rated 3–4 times the mirror weight. We never rely on adhesive alone for large installations. For very large pieces, we use a French cleat system."),
        ("What causes mirrors to develop black spots at the edges?",
         "This is called desilvering or foxing — the silver backing layer is degrading, usually from moisture penetrating the edge seal. The fix is replacement with a moisture-resistant mirror with sealed edges. There is no restoration for desilvered spots."),
        ("Can you replace just one sliding closet door mirror?",
         "Yes — but we recommend replacing both panels at the same time if they are the same age, since the second one is likely to desilver within a year or two of the first."),
        ("Do you cut mirrors to irregular shapes?",
         "Yes — arched tops, oval cuts, and custom shapes are available with a template or detailed dimensions. Custom shapes have a 5–10 business day lead time. Bring a cardboard template for best results."),
        ("How long does custom mirror fabrication take?",
         "Standard rectangular cuts are typically ready in 3–5 business days. Custom shapes take 5–10 business days. Most bathroom mirror replacements and closet door mirrors are done as a single visit."),
    ],
    "emergency-glass": [
        ("How fast can you respond to an emergency glass call?",
         "For the San Fernando Valley, we typically respond within 1–2 hours. Outlying areas take longer — we will give you an honest ETA on the call. Call (805) 750-6471 directly for the fastest response."),
        ("Do you do emergency glass repair at night?",
         "We monitor our phone until 10pm and dispatch for genuine emergencies — break-ins, storm damage, situations creating safety or weather exposure risk. Call directly; the website contact form is not monitored after hours."),
        ("Can you provide documentation for an insurance claim?",
         "Yes. We provide detailed itemized estimates and invoices that meet insurance adjuster requirements — glass type, dimensions, quantity, and labor itemized separately."),
        ("What should I do immediately after a window break-in?",
         "Keep people away from the broken glass. Do not remove shards yourself. Call police if it is a break-in and wait for documentation. Then call us — we will walk you through the situation and dispatch for board-up."),
        ("What is the difference between board-up and glass replacement?",
         "Board-up uses plywood or polycarbonate sheeting to secure the opening immediately — it is fast (same day or night) and temporary. Permanent glass replacement follows within 3–5 business days for standard sizes."),
    ],
}

def make_faq_schema(faqs, page_url):
    entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        }
        for q, a in faqs
    ]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }

INSERT_BEFORE = '</script>\n<body>'

for slug, faqs in SERVICE_FAQS.items():
    path = f"{slug}.html"
    if not os.path.exists(path):
        print(f"  MISSING {path}")
        continue
    with open(path) as f:
        content = f.read()
    if '"FAQPage"' in content:
        print(f"  SKIP {slug} — already has FAQPage schema")
        continue
    schema = json.dumps(make_faq_schema(faqs, f"https://www.americanglassexperts.us/{slug}"), indent=2)
    injection = f'\n<script type="application/ld+json">{schema}</script>\n'
    new_content = content.replace(INSERT_BEFORE, injection + INSERT_BEFORE, 1)
    if new_content == content:
        print(f"  WARN {slug} — insertion point not found")
        continue
    with open(path, "w") as f:
        f.write(new_content)
    print(f"  FAQPage schema added: {slug} ({len(faqs)} questions)")

print("\nDone.")

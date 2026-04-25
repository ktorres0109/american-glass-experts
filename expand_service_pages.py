#!/usr/bin/env python3
"""
Replace thin "About This Service" sections on service pages with deep content.
Also add pricing tables and expanded FAQs.
"""
import re, os

# ── Helpers ────────────────────────────────────────────────────────

def make_pricing_table(rows):
    tr = "".join(
        f'<tr><td style="padding:10px 14px;border-bottom:1px solid var(--border);font-weight:500;">{item}</td>'
        f'<td style="padding:10px 14px;border-bottom:1px solid var(--border);color:var(--text-mid);">{price}</td></tr>'
        for item, price in rows
    )
    return f"""<div style="margin-top:28px;overflow-x:auto;">
      <table style="width:100%;border-collapse:collapse;background:var(--bg-soft);border-radius:var(--r-lg);overflow:hidden;">
        <thead><tr style="background:var(--surface);">
          <th style="padding:12px 14px;text-align:left;font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;color:var(--text-mid);">Service</th>
          <th style="padding:12px 14px;text-align:left;font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;color:var(--text-mid);">Typical Range</th>
        </tr></thead>
        <tbody>{tr}</tbody>
      </table>
      <p style="font-size:.8rem;color:var(--text-dim);margin-top:8px;">Prices are estimates. Free on-site quotes for exact pricing — no obligation.</p>
    </div>"""

def make_faq_items(items, start_idx=5):
    return "".join(
        f"""<div class="faq-item reveal d{start_idx+i}">
  <button class="faq-q">{q}<span class="faq-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></span></button>
  <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
</div>"""
        for i, (q, a) in enumerate(items)
    )

# ── Service content ────────────────────────────────────────────────

SERVICE_DATA = {
    "shower-enclosures": {
        "about_replacement": """
        <p>Frameless shower enclosures are the most-requested glass upgrade we install across Southern California — and for good reason. A frameless enclosure removes the heavy aluminum channel frame from around your shower opening, leaving only the glass, hinges, and handle. The result is a bathroom that reads as significantly larger, is dramatically easier to clean, and holds up longer without the hardware corrosion that degrades framed doors over time.</p>
        <p>We install four main shower enclosure types depending on your bathroom layout and budget:</p>
        <ul style="margin:16px 0 16px 20px;line-height:1.9;color:var(--text-mid);">
          <li><strong>Frameless pivot or hinged:</strong> Single panel that swings open on a pivot hinge. Best for alcove and three-wall showers. Most popular style in Southern California remodels.</li>
          <li><strong>Semi-frameless bypass:</strong> Two panels that slide past each other in a minimal track. Good option when a swinging door would interfere with toilet or vanity placement.</li>
          <li><strong>Frameless sliding (barn-style):</strong> One or two panels on an exposed roller track mounted above the opening. Popular for modern and spa-style bathrooms.</li>
          <li><strong>Neo-angle:</strong> Five-sided enclosure for corner shower footprints. Requires precise angular cuts — a job where field measurement matters.</li>
        </ul>
        <p>Glass thickness matters more than most homeowners realize. Standard framed shower doors use 3/16" glass — thin enough to flex and wobble. Our frameless installations use either 3/8" (9.5mm) or 1/2" (12mm) tempered safety glass. The difference is noticeable: 1/2" glass feels solid and premium, 3/8" is the practical standard for most projects. Both are tempered to ANSI Z97.1 requirements — if they break, they shatter into small blunt pieces rather than dangerous shards.</p>
        <p>Hardware finish is the last major decision. We stock brushed nickel, matte black, chrome, and oil-rubbed bronze in standard configurations. Specialty finishes (brushed gold, satin brass, champagne bronze) are available to order with a 1–2 week lead time. For most projects, we can go from initial measurement to installed enclosure in 5–7 business days.</p>
        """,
        "pricing": make_pricing_table([
            ("Frameless pivot door — alcove (standard)", "$1,200 – $2,200"),
            ("Frameless pivot door — custom size or neo-angle", "$1,800 – $3,500"),
            ("Semi-frameless bypass (two-panel)", "$800 – $1,800"),
            ("Frameless sliding (barn-style)", "$1,400 – $2,800"),
            ("Full walk-in frameless enclosure", "$2,500 – $4,500"),
            ("Hardware upgrade (specialty finish)", "+ $200 – $600"),
        ]),
        "extra_faqs": [
            ("What's the difference between 3/8\" and 1/2\" shower glass?",
             "Both are tempered safety glass. 3/8\" (9.5mm) is the standard for most frameless installations — solid, stable, and meets code. 1/2\" (12mm) is premium: noticeably heavier and more rigid, preferred for large panels or spa-quality installations. We stock both and can show you samples at your measurement appointment."),
            ("How long does frameless shower glass last?",
             "The glass itself doesn't wear out — tempered glass is nearly impervious to household chemicals and normal wear. Hardware (hinges, handles, seals) is the wear item. Quality brushed nickel or matte black hardware typically lasts 10–20 years. Rubber seals and wipes need replacement every 3–5 years and cost under $50 to swap yourself."),
            ("Can you install over tile that's already in place?",
             "Yes — and this is the normal sequence. We mount into tile walls using anchors rated for wet-area applications. We always waterproof the penetration points. The tile goes in first, then we come in to measure and install once it's set."),
            ("Do I need a permit for shower glass installation in California?",
             "A permit is not typically required for shower enclosure replacement if the plumbing and structure aren't being altered. If you're changing the shower footprint or moving drains, a permit is needed. We'll tell you at the estimate if your job requires permit coordination."),
        ],
    },

    "window-repair": {
        "about_replacement": """
        <p>Window repair and replacement covers a spectrum of issues — and knowing which fix applies to your situation saves you money. We handle everything from IGU seal replacement (the most common repair) to full sash replacement to complete window unit removal and reinstall. Here's how we think about it:</p>
        <p><strong>Foggy or cloudy glass between panes</strong> is almost always a failed IGU (insulating glass unit) seal. The two panes of glass are factory-sealed with argon or krypton gas between them. When the seal fails, moisture enters and creates the clouding you see. The fix is IGU replacement — we remove the glass unit from your existing frame, install a new factory-sealed unit, and re-glaze. You keep your frame; only the glass changes. This is the right repair for 80% of window calls we get, and it's dramatically cheaper than full window replacement.</p>
        <p><strong>Cracked or broken glass</strong> (single impact or thermal crack) is repaired by replacing just the affected pane or IGU. We stock common dual-pane sizes and can often do same-week replacement. If your window has been boarded after a break-in, we prioritize these.</p>
        <p><strong>Full window replacement</strong> makes sense when: the frame itself is rotted or damaged, the window style is obsolete (single-hung when you want double-hung), you're upgrading to Low-E coatings for LADWP rebates, or the frame is an older aluminum type with significant condensation on the frame (indicating frame thermal transfer, not just glass failure).</p>
        <p>Low-E glass is worth understanding before any window project. Low-E (low emissivity) coating is a microscopically thin metallic layer applied to the glass that reflects radiant heat. In Southern California's climate, this means your AC works less hard in summer — heat doesn't radiate in through the glass. LADWP and SCE both offer rebates for Low-E window replacements in eligible homes. We can tell you at the estimate whether your job qualifies.</p>
        <p>We handle residential and commercial window repair across all window types: aluminum, vinyl, wood, clad, and steel frame. We also do sliding glass door repair — including track replacements, roller replacements, and glass panel swaps — which is a common call we get from apartment managers and homeowners alike.</p>
        """,
        "pricing": make_pricing_table([
            ("IGU replacement (seal failure / foggy glass) — per unit", "$250 – $550"),
            ("Single-pane glass replacement", "$150 – $350"),
            ("Sliding glass door panel replacement", "$400 – $900"),
            ("Sliding door track + roller replacement", "$200 – $450"),
            ("Full window unit replacement (per window)", "$350 – $1,200"),
            ("Emergency board-up (broken pane)", "$150 – $400"),
        ]),
        "extra_faqs": [
            ("Can foggy windows be fixed without replacing the whole window?",
             "Yes — in most cases. If only the sealed glass unit has failed (you see fogging between the panes), we replace the IGU without touching your frame, sash, or trim. This is called IGU replacement and costs $250–$550 per unit, versus $500–$1,200+ for a full window replacement."),
            ("How do I know if I need IGU replacement or full window replacement?",
             "If the glass is foggy between panes but the frame and operation are fine, you need IGU replacement only. If the frame is cracked, rotted, or won't seal properly — or if you want to change the window style — full replacement is the right move. We'll tell you which applies at the free estimate."),
            ("Do you repair sliding glass doors?",
             "Yes — sliding glass door glass panel replacement, track replacement, and roller replacement are all services we provide. Rollers are the most common failure on sliding doors: they wear out and the door becomes difficult to open. We stock replacement rollers for common Milgard, Andersen, and generic patio door systems."),
            ("Are there rebates for Low-E window replacement in Southern California?",
             "Yes. LADWP and SCE offer rebates for qualifying dual-pane Low-E window replacements. The rebate amount varies by program year and unit count. We can tell you at the estimate whether your project qualifies and what the current rebate schedule is."),
        ],
    },

    "storefront-glass": {
        "about_replacement": """
        <p>Commercial storefront glass is one of the most specialized areas of glazing work — and one where contractor licensing matters most. As C-17 licensed glazing contractors, we can legally pull permits, work on commercial properties, and certify installations to California building code. This matters for business owners who need their work documented for insurance claims, tenant improvement buildouts, or commercial lease compliance.</p>
        <p>Storefront glass systems use different glass types than residential work. Standard storefronts use 1/4" annealed or tempered glass in aluminum framing systems. High-traffic entries, glass doors, and sidelites adjacent to doors must use safety glazing (tempered or laminated) per CBC Section 2406. If your storefront glass was installed before 1977, there's a reasonable chance it doesn't meet current safety glazing requirements — something to know if you're doing any renovation work that would trigger a permit inspection.</p>
        <p>The most common commercial calls we get fall into two categories:</p>
        <ul style="margin:16px 0 16px 20px;line-height:1.9;color:var(--text-mid);">
          <li><strong>Emergency break-in board-up and replacement:</strong> A break-in typically happens overnight. We offer same-day board-up to secure the premises and follow-up glass replacement within 3–5 business days for standard sizes, faster for common commercial panel sizes we stock.</li>
          <li><strong>Planned renovation and upgrade:</strong> Updating an older aluminum framing system, replacing scratched or etched panels, installing glass partitions for office buildouts, or upgrading entry doors to a more modern aluminum profile.</li>
        </ul>
        <p>Glass partitions are a growing category as businesses convert warehouse and open-plan space into functional offices. We install full-height frameless glass partitions, aluminum-framed partition systems, and partial-height dividers with glass lites. All commercial partition work is done under permit when required by the building department.</p>
        <p>For property managers: we work with management companies and commercial landlords on ongoing glazing maintenance and emergency response agreements. If you manage multiple storefronts or commercial properties in Southern California, ask about our commercial account setup.</p>
        """,
        "pricing": make_pricing_table([
            ("Emergency board-up (single storefront panel)", "$150 – $400"),
            ("Standard storefront glass panel replacement", "$350 – $900"),
            ("Commercial glass door replacement", "$600 – $1,800"),
            ("Glass partition — per linear foot (framed)", "$120 – $250 / LF"),
            ("Glass partition — frameless full-height", "$250 – $500 / LF"),
            ("Full storefront system (framing + glass)", "Custom quote"),
        ]),
        "extra_faqs": [
            ("Do you handle emergency storefront board-up at night?",
             "For commercial break-ins and urgent situations, call (805) 750-6471 directly. We monitor until 10pm and can dispatch for genuine emergencies. After-hours emergency board-up is available — call to confirm availability and ETA."),
            ("Does commercial storefront glass replacement require a permit?",
             "Replacing broken glass in-kind (same size, same type) typically doesn't require a permit. Changing the framing system, size, or adding new openings does require a permit. As C-17 licensed contractors, we coordinate permit filing when required."),
            ("What glass type should I use for my storefront?",
             "Standard storefronts use 1/4\" annealed glass in aluminum systems. Any glass in or adjacent to a commercial door must be safety glazing (tempered or laminated) per California code. Locations prone to vandalism or break-ins sometimes use laminated glass (holds together when broken) rather than tempered (which shatters out of the frame). We'll recommend the right spec for your situation."),
            ("Can you install glass office partitions?",
             "Yes. We install full-height frameless glass partitions, aluminum-framed partition systems with glass lites, and partial-height dividers. All commercial partition work is permitted where required. We work with business owners and interior contractors on TI (tenant improvement) projects."),
        ],
    },

    "custom-mirrors": {
        "about_replacement": """
        <p>Custom mirrors are one of the most versatile glass products we install — and one of the most impactful visual upgrades you can make to a room. Unlike stock mirror sizes from hardware stores, custom-cut mirrors are fabricated to fit your exact wall, frame, or opening dimensions. This matters in older Southern California homes where wall dimensions rarely match standard sizes, and in bathrooms where you want the mirror to run full-width between tile edges.</p>
        <p>We cut custom mirrors in the following configurations:</p>
        <ul style="margin:16px 0 16px 20px;line-height:1.9;color:var(--text-mid);">
          <li><strong>Bathroom vanity mirrors:</strong> Cut to width and height, with polished or beveled edges. Can be mounted with clips, adhesive, or frame. Commonly sized 24"–72" wide for single and double vanities.</li>
          <li><strong>Full-length and wall mirrors:</strong> Bedroom and dressing room mirrors, gym and dance studio wall mirrors, formal room decorative mirrors. We install mirrors up to full wall height.</li>
          <li><strong>Closet door mirrors:</strong> Bypass sliding closet door mirror panels are one of our most common residential installs. We replace broken or delaminated panels and install new mirror door systems.</li>
          <li><strong>Decorative and architectural:</strong> Mirrored backsplashes, fireplace surround mirrors, custom shapes (arched, round, irregular) cut to template.</li>
        </ul>
        <p>Mirror quality varies more than most people realize. Standard float glass mirrors use silver backing sealed with copper and paint — the silver layer is what degrades first, starting at the edges as black spots or "foxing." Premium mirrors use thicker silver and better edge sealing. For bathroom installations where moisture is a factor, we always use moisture-resistant mirror with sealed edges.</p>
        <p>Installation method depends on the mounting surface and mirror size. Small mirrors (under 20 lbs) can be mounted with J-clips or mirror adhesive. Larger mirrors require French cleats, back-mounted clips, or in some cases wall blocking if the stud layout doesn't align. We always anchor to studs or use toggle anchors rated for the mirror weight — never just adhesive alone for large pieces.</p>
        <p>Lead time for custom mirrors is typically 3–5 business days from order to installation. Most bathroom mirror replacements and closet door mirrors are done as a single visit.</p>
        """,
        "pricing": make_pricing_table([
            ("Bathroom vanity mirror (custom cut + clips)", "$150 – $450"),
            ("Full-length wall mirror (6' tall)", "$250 – $600"),
            ("Gym / studio wall mirror (per sq ft)", "$12 – $22 / sq ft"),
            ("Closet bypass door mirror panels (pair)", "$300 – $700"),
            ("Beveled edge upgrade (per linear foot)", "$4 – $8 / LF"),
            ("Custom shape (arch, oval, irregular)", "Custom quote"),
        ]),
        "extra_faqs": [
            ("How do you mount large mirrors safely?",
             "We anchor large mirrors (over 20 lbs) to studs or use toggle anchors rated 3–4x the mirror weight. We never rely on adhesive alone for large installations. For very large pieces, we use a French cleat system — a hidden wall-mounted strip that the mirror hangs from, which also allows minor leveling adjustment after installation."),
            ("What causes mirrors to develop black spots at the edges?",
             "This is called 'desilvering' or foxing — the silver backing layer is degrading, usually from moisture penetrating the edge seal. It's more common on older mirrors and in bathrooms with poor ventilation. The fix is replacement with a moisture-resistant mirror with sealed edges. There's no restoration for desilvered spots."),
            ("Can you replace just one sliding closet door mirror?",
             "Yes — but we recommend replacing both panels at the same time if they're the same age, since the second one is likely to desilver within a year or two of the first. We can match the thickness and tint of existing panels if you prefer to replace only the damaged one."),
            ("Do you cut mirrors to irregular shapes?",
             "Yes — arched tops, oval cuts, and custom shapes are available with a template or detailed dimensions. Custom shapes have a 5–10 business day lead time and are priced by complexity and size. Bring a template cut from cardboard for best results."),
        ],
    },

    "emergency-glass": {
        "about_replacement": """
        <p>Emergency glass repair means different things to different callers — a break-in at 11pm, a baseball through a living room window, a car backing into a sliding door, a shattered storefront after a collision. Whatever the situation, the immediate priority is securing the opening to protect the property from weather, further damage, and unauthorized entry.</p>
        <p>Our emergency response process works in two stages:</p>
        <p><strong>Stage 1 — Board-up (same day/night):</strong> We secure the opening with plywood or polycarbonate sheeting fastened to the frame or surrounding structure. Board-up protects against weather, insects, and opportunistic entry. It's not pretty, but it's fast and it works. We carry boarding materials on our vehicles and can respond to most of the San Fernando Valley and surrounding areas within 1–3 hours of your call.</p>
        <p><strong>Stage 2 — Permanent glass replacement (same week):</strong> Once the board-up is in place, we schedule the permanent glass replacement. For standard residential windows, sliding doors, and common commercial panel sizes, we typically complete replacement within 3–5 business days. Custom or specialty glass (tempered commercial panels, large picture windows, specific Low-E configurations) may take 5–10 business days to fabricate.</p>
        <p>For insurance claims: we can provide detailed written estimates with glass type, size, and installation labor itemized — the format insurance adjusters require. We're familiar with the major home insurance carriers and know what documentation they need. If the break-in resulted in a police report, your deductible may be waived under a separate property crime clause — ask your agent.</p>
        <p>What to do before we arrive: if glass is broken in a frame, don't try to remove the remaining shards yourself — broken tempered glass is safer than annealed glass because it crumbles into small pieces, but both can cause serious lacerations. Keep people (especially children and pets) away from the area. If the break-in is fresh, don't touch anything until police have documented the scene.</p>
        <p>We handle emergency glass for residential homes, apartment buildings, commercial storefronts, office buildings, and auto dealerships throughout Los Angeles, Ventura, San Bernardino, and Riverside Counties. For the fastest response, call us directly — the contact form is not monitored after business hours.</p>
        """,
        "pricing": make_pricing_table([
            ("Emergency board-up (residential window)", "$150 – $350"),
            ("Emergency board-up (commercial storefront panel)", "$200 – $500"),
            ("After-hours surcharge", "$75 – $150"),
            ("Standard window glass replacement (after board-up)", "$200 – $600"),
            ("Sliding glass door panel replacement", "$400 – $900"),
            ("Commercial storefront glass replacement", "$350 – $1,200"),
        ]),
        "extra_faqs": [
            ("How fast can you respond to an emergency glass call?",
             "For the San Fernando Valley (Reseda, Northridge, Woodland Hills, Van Nuys, Sherman Oaks, Encino, Burbank, Glendale), we typically respond within 1–2 hours. Outlying areas take longer — we'll give you an honest ETA on the call. Call (805) 750-6471 directly for the fastest response."),
            ("Do you do emergency glass repair at night?",
             "We monitor our phone until 10pm and dispatch for genuine emergencies (break-ins, storm damage, situations creating safety or weather exposure risk). Call directly — the website contact form is not monitored after hours."),
            ("Can you provide documentation for an insurance claim?",
             "Yes. We provide detailed itemized estimates and invoices that meet insurance adjuster requirements — glass type, dimensions, quantity, and labor itemized separately. We're familiar with major home insurance carriers and can often communicate directly with adjusters."),
            ("What should I do immediately after a window break-in?",
             "Keep people away from the broken glass area. Don't remove shards yourself. Call police if it's a break-in and wait for documentation before touching anything. Then call us — we'll walk you through the situation on the phone and dispatch for board-up. Don't wait until morning if the opening is weather-exposed."),
        ],
    },
}

# ── Process service pages ──────────────────────────────────────────
ABOUT_PATTERN = re.compile(
    r'(<h2>About This Service</h2>\s*<p>).*?(</p>)',
    re.DOTALL
)
FAQ_END_PATTERN = re.compile(
    r'(</div>\s*</section>\s*\n\s*<section class="content-section reveal" style="background:var\(--bg-soft\);">)',
    re.DOTALL
)

for slug, data in SERVICE_DATA.items():
    path = f"{slug}.html"
    if not os.path.exists(path):
        print(f"  MISSING {path}")
        continue
    with open(path) as f:
        content = f.read()
    if 'frameless shower glass lasts' in content or 'failed IGU' in content or 'two stages' in content or 'silver backing' in content or 'Stage 1' in content:
        print(f"  SKIP {slug} — already expanded")
        continue

    # Replace About This Service paragraph
    new_content = ABOUT_PATTERN.sub(
        r'\1' + data["about_replacement"].strip() + r'</p>',
        content, count=1
    )

    # Inject pricing table before the "Our Process" h2
    pricing_injection = f'\n      {data["pricing"]}\n      '
    new_content = new_content.replace(
        '<h2>Our Process</h2>',
        f'<h2>Pricing Guide</h2>{pricing_injection}<h2 style="margin-top:36px;">Our Process</h2>',
        1
    )

    # Append extra FAQs before the closing </div></section> of the FAQ section
    faq_close = new_content.rfind('</div>\n    </div>\n  </section>\n\n  <section class="content-section reveal" style="background:var(--bg-soft);">')
    if faq_close != -1:
        extra = make_faq_items(data["extra_faqs"])
        new_content = new_content[:faq_close] + extra + new_content[faq_close:]
    else:
        # fallback: find Cities We Serve section and insert before it
        cities_idx = new_content.find('<span class="section-label">Service Area</span>')
        if cities_idx > 0:
            section_start = new_content.rfind('<section', 0, cities_idx)
            extra = make_faq_items(data["extra_faqs"])
            new_content = new_content[:section_start] + extra + '\n' + new_content[section_start:]

    with open(path, "w") as f:
        f.write(new_content)
    print(f"  EXPANDED {path}")

print("\nService pages done.")

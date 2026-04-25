#!/usr/bin/env python3
"""
Expand 9 priority city pages with unique 400+ word content sections.
Injects a deep-content section between LOCAL CONTEXT and the Glass Services section.
"""
import re, os

# Insertion point: right before the new "Glass Services Available" section we added
INSERT_BEFORE = re.compile(r'(\s*<section[^>]*>\s*<div class="container"[^>]*>\s*<span class="section-label">What We Offer</span>)')

def make_deep_section(city_slug, city_data):
    why_items = "".join(
        f'<li style="margin-bottom:14px;padding-left:8px;border-left:3px solid var(--blue);"><strong>{item["title"]}</strong> — {item["body"]}</li>'
        for item in city_data["why_items"]
    )
    extra_faqs = "".join(
        f"""
        <div class="faq-item reveal d{i+6}">
          <button class="faq-q">
            {q}
            <span class="faq-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
        </div>"""
        for i, (q, a) in enumerate(city_data["extra_faqs"])
    )
    nearby = " &nbsp;·&nbsp; ".join(
        f'<a href="/{slug}">{name}</a>' for slug, name in city_data["nearby"]
    )
    return f"""
  <div class="divider"></div>
  <!-- DEEP CONTENT: {city_data["city_name"]} -->
  <section style="padding:72px 0;">
    <div class="container" style="max-width:860px;">
      <span class="section-label">Local Expertise</span>
      <h2>Glass Work in <em>{city_data["city_name"]}</em> — What You Should Know</h2>
      <div style="color:var(--text-mid);line-height:1.85;font-size:1rem;">
        {city_data["deep_content"]}
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <section style="background:var(--bg-soft);padding:72px 0;">
    <div class="container" style="max-width:860px;">
      <span class="section-label">Why Choose Us</span>
      <h2>Why {city_data["city_name"]} Residents Call American Glass Experts</h2>
      <ul style="list-style:none;padding:0;margin-top:28px;">
        {why_items}
      </ul>
      <p style="margin-top:32px;font-size:.95rem;color:var(--text-mid);">
        <strong>Also serving nearby:</strong> {nearby} · <a href="/service-areas" style="color:var(--blue);">Full service area →</a>
      </p>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ADDITIONAL FAQS for {city_data["city_name"]} -->
  <div style="display:none;" id="extra-faqs-{city_slug}">
    {extra_faqs}
  </div>
"""

# ── City content data ──────────────────────────────────────────────
CITIES = {
    "los-angeles": {
        "city_name": "Los Angeles",
        "deep_content": """
        <p>Los Angeles is one of the most architecturally diverse cities in the country — and that diversity creates some of the most varied glass work we encounter. In a single week we might install a frameless shower enclosure in a mid-century modern home in Silver Lake, replace a broken commercial storefront panel on a restaurant row in Culver City, and repair failed dual-pane seals in a 1950s tract house in South LA.</p>
        <p>The sheer age range of housing stock in LA is one reason glass repair demand stays high year-round. Homes built before the 1990s typically have single-pane or early dual-pane windows that are now at the end of their rated lifespan. If you're seeing condensation between panes or feeling drafts around your window frames, the insulating gas seal has failed — a common issue in LA's older neighborhoods including Leimert Park, Boyle Heights, Highland Park, and Koreatown.</p>
        <p>For newer construction and remodels, frameless shower glass is the most popular upgrade we install. Los Angeles homeowners tend to prefer 3/8" or 1/2" thick tempered glass with minimal or no visible framing — the clean European look that photographs well and holds up to daily use without corroding hardware. We custom-cut every panel to your opening, which matters in older LA homes where walls and floors are rarely perfectly square.</p>
        <p>Commercial glass in LA is its own category. Storefront break-ins are unfortunately common across the metro, and when a business calls us for emergency board-up, response time is everything. We keep tempered glass and boarding materials stocked to handle emergency calls across the city. The Foothill, Harbor, and Santa Monica Freeways give us reasonable access to most of the city during off-peak hours.</p>
        <p>One thing to know about glass permits in Los Angeles: LADBS (LA Department of Building and Safety) requires permits for full window replacements in most cases. As a licensed C-17 contractor, we handle permit coordination and inspections as part of the job — you don't need to navigate that process yourself.</p>
        """,
        "why_items": [
            {"title": "C-17 Licensed for LA Work", "body": "CSLB #1125850 is a California state license, valid citywide. We pull permits through LADBS and handle inspections — you don't have to."},
            {"title": "Custom glass for non-standard openings", "body": "LA's older housing stock has few perfectly square openings. We field-measure every job and cut to exact dimensions."},
            {"title": "Emergency response across the metro", "body": "Break-in board-up, storm damage, accidental shatter — we respond same-day for urgent calls anywhere in the LA area."},
            {"title": "Residential and commercial on the same ticket", "body": "If you manage a mixed-use building or have both home and business needs, we handle everything under one C-17 license."},
        ],
        "extra_faqs": [
            ("Do I need a permit for window replacement in Los Angeles?",
             "Yes — LADBS requires a permit for most window replacements in the City of Los Angeles, including dual-pane upgrades. As a licensed C-17 contractor, we coordinate permit filing and inspections as part of the job."),
            ("What's the cost of frameless shower glass in Los Angeles?",
             "Frameless shower enclosures in LA typically run $1,200–$4,500 depending on glass thickness, door configuration, and hardware finish. We provide a free on-site estimate with a firm price before any work begins."),
            ("Can you do emergency glass repair anywhere in Los Angeles?",
             "Yes. We cover the full city — from the South Bay to the San Fernando Valley to East LA. Call us directly for emergency board-up and we'll tell you our ETA based on current location and traffic."),
        ],
        "nearby": [
            ("burbank", "Burbank"), ("glendale", "Glendale"), ("pasadena", "Pasadena"),
            ("santa-monica", "Santa Monica"), ("culver-city", "Culver City"), ("long-beach", "Long Beach"),
        ],
    },

    "glendale": {
        "city_name": "Glendale",
        "deep_content": """
        <p>Glendale is one of our most active service cities — close to our Reseda base, densely populated, and home to an enormous range of housing types that generate consistent glass repair and installation work. The Armenian community in particular has driven strong demand for custom frameless shower glass and large custom mirrors, two categories where craftsmanship and aesthetic precision matter most to homeowners.</p>
        <p>Glendale's housing stock runs from early 20th century bungalows near Adams Square to post-war apartment buildings along Brand Boulevard to newer condo developments near the Americana. Each era of construction comes with its own glass challenges: older single-family homes in Montrose and La Crescenta often have original steel-frame windows that are at end-of-life; mid-century apartment blocks frequently have casement windows with failed seals; newer construction has mostly aluminum-frame dual-pane that holds up well but occasionally needs seal replacement after 15–20 years.</p>
        <p>Commercial glass in Glendale is driven by the Brand Boulevard retail corridor and the dense cluster of businesses in the Verdugo Viejo area. We handle storefront glass for everything from small boutiques to auto dealerships. Glass partitions for office buildouts have also been a growing category as more businesses in Glendale's downtown area retrofit older commercial space into open-plan offices.</p>
        <p>Drive time from Reseda to most of Glendale is 25–35 minutes, making it one of our fastest-response service areas. For emergency calls — break-ins, storm damage, accidental shatters — we can typically get someone out same-day to the Glendale area.</p>
        <p>One thing Glendale homeowners ask us frequently: can we match existing glass or hardware finishes when doing a partial replacement? In most cases, yes. We stock standard brushed nickel, matte black, and chrome hardware and can source specialty finishes on order. For glass replacement in multi-pane windows, we match thickness and Low-E coating type to the original unit.</p>
        """,
        "why_items": [
            {"title": "25–35 min from Reseda", "body": "One of our fastest response areas — we can schedule next-day for most jobs and same-day for emergencies."},
            {"title": "Custom work for Glendale's diverse housing", "body": "From Adams Square bungalows to Americana-area condos — we've worked in every neighborhood and building type in the city."},
            {"title": "Finish matching on replacements", "body": "We match glass type, thickness, Low-E coating, and hardware finish for partial replacements so the work blends with existing elements."},
            {"title": "Commercial glass for Brand Blvd businesses", "body": "Storefront replacement, glass partitions, commercial doors — all under a C-17 license with permit-pull capability."},
        ],
        "extra_faqs": [
            ("Do you serve all of Glendale including Montrose and La Crescenta?",
             "Yes — we cover all of Glendale proper as well as Montrose, La Crescenta, and the hillside neighborhoods. Drive time is 25–35 minutes from our Reseda location."),
            ("Can you match hardware finishes on a partial shower glass replacement in Glendale?",
             "In most cases, yes. We stock brushed nickel, matte black, chrome, and oil-rubbed bronze. Specialty finishes can be ordered with a lead time of 1–2 weeks."),
            ("Do you do glass partitions for offices in Glendale?",
             "Yes — commercial glass partitions, including full-height frameless and aluminum-framed systems, are a service we provide. We handle permit coordination through the City of Glendale building department."),
        ],
        "nearby": [
            ("burbank", "Burbank"), ("los-angeles", "Los Angeles"), ("pasadena", "Pasadena"),
            ("la-crescenta", "La Crescenta") if os.path.exists("la-crescenta.html") else ("north-hollywood", "North Hollywood"),
            ("studio-city", "Studio City"),
        ],
    },

    "burbank": {
        "city_name": "Burbank",
        "deep_content": """
        <p>Burbank is a core service city for us — 25 to 30 minutes from Reseda, with a mix of residential neighborhoods and commercial corridors that generates steady glass work year-round. The entertainment industry's presence means a higher-than-average concentration of studio facilities, production offices, and media company headquarters that need commercial glazing maintained to a high standard.</p>
        <p>On the residential side, Burbank's most active areas for glass work are the Rancho neighborhood and the hills east of Glenoaks. Post-war ranch homes and 1960s-era homes throughout these areas are hitting the window replacement cycle — dual-pane seals that were installed 20–30 years ago are now failing, showing up as foggy glass between panes that no amount of cleaning will fix. The fix is IGU (insulating glass unit) replacement, which involves removing the failed sealed unit and installing a new one without replacing the entire frame.</p>
        <p>Shower enclosures are Burbank's most common residential project. The city's strong homeownership rate means many residents are investing in bathroom remodels, and frameless glass is consistently the most-requested shower upgrade. We cut custom panels for standard alcove showers, walk-in configurations, and corner units — glass goes from our fabricator to your bathroom within the same week in most cases.</p>
        <p>For commercial work, the stretch of San Fernando Blvd through downtown Burbank and the media campus areas near Warner Bros. and Disney generate consistent storefront and partition work. If you manage a commercial property in Burbank and have a glass emergency, we prioritize same-day response for businesses to minimize revenue impact from board-up situations.</p>
        """,
        "why_items": [
            {"title": "25–30 min from Reseda", "body": "Fast response to Burbank for both scheduled jobs and emergencies."},
            {"title": "IGU replacement without frame removal", "body": "We replace failed dual-pane seals by swapping the sealed glass unit only — no need to disturb your existing window frame or trim."},
            {"title": "Entertainment industry commercial clients", "body": "We work in studio facilities, production offices, and media campuses — discretion and after-hours scheduling available."},
            {"title": "Custom shower glass in under a week", "body": "We measure Monday, fabricate Tuesday–Thursday, install Friday in most cases for standard configurations."},
        ],
        "extra_faqs": [
            ("Can you fix foggy windows in Burbank without replacing the whole frame?",
             "Yes — if only the sealed glass unit has failed (fogging between panes), we replace the IGU without touching your frame or trim. This is typically $250–$500 per unit and takes a few hours."),
            ("Do you work in studio facilities and production offices in Burbank?",
             "Yes. We have experience with commercial glazing in entertainment industry buildings. We offer after-hours scheduling to minimize production disruption."),
            ("How quickly can you do a shower glass installation in Burbank?",
             "Most standard frameless shower enclosures go from measurement to installation in 5–7 business days. We can expedite for an additional charge when needed."),
        ],
        "nearby": [
            ("glendale", "Glendale"), ("los-angeles", "Los Angeles"), ("north-hollywood", "North Hollywood"),
            ("studio-city", "Studio City"), ("encino", "Encino"),
        ],
    },

    "pasadena": {
        "city_name": "Pasadena",
        "deep_content": """
        <p>Pasadena is one of the most architecturally significant cities in Southern California, with a dense concentration of Craftsman bungalows, Spanish Colonial Revival homes, and mid-century estates — many of them in historic preservation districts that have specific requirements for window replacement and glass work. We've been doing glass work in Pasadena long enough to understand what those requirements mean in practice.</p>
        <p>In preservation districts like the Bungalow Heaven Landmark District and the Madison Heights area, the City of Pasadena's Historic Preservation Commission may require that replacement windows match the original profile and operation type. This typically means using simulated divided light (SDL) dual-pane windows that look like true divided light from the exterior, rather than standard unobstructed dual-pane. We work with suppliers who stock SDL units in sizes appropriate for pre-war Craftsman construction.</p>
        <p>Outside of historic districts, Pasadena's custom home and estate market drives demand for premium glass work — frameless shower enclosures in master bathrooms, custom mirrors for formal rooms, glass railings for hillside decks, and large custom tabletop glass pieces. These are jobs where the glass itself needs to be cut precisely and the installation needs to be clean — we bring the same approach to a Craftsman bungalow in Bungalow Heaven as to an estate in San Rafael Hills.</p>
        <p>The Rose Bowl area, Old Town, and the Caltech/Huntington neighborhood generate commercial glass work — restaurant storefronts, gallery glass, and office buildouts. Pasadena's outdoor dining expansions have also created new demand for frameless glass windscreens and patio enclosures.</p>
        <p>Drive time from Reseda to Pasadena is 35–50 minutes depending on the 210 and 134. For emergency calls in Pasadena, we can usually reach the city within an hour during off-peak hours.</p>
        """,
        "why_items": [
            {"title": "Experience with historic preservation requirements", "body": "We know Pasadena's HPC guidelines and work with SDL window systems that satisfy historic district requirements without sacrificing energy performance."},
            {"title": "Estate-level precision on custom work", "body": "Custom mirrors, frameless glass, railings — we bring finish-carpentry-level attention to glass work in Pasadena's premium homes."},
            {"title": "Restaurant and commercial glass in Old Town", "body": "Storefront replacement, patio glass enclosures, and glass partitions for Pasadena's dense commercial corridor."},
            {"title": "Licensed for permit-pull in Pasadena", "body": "We pull permits through the City of Pasadena Building and Safety Division and coordinate with HPC when required for historic properties."},
        ],
        "extra_faqs": [
            ("Can you replace windows on a Craftsman home in a Pasadena historic district?",
             "Yes — we work with simulated divided light (SDL) dual-pane units that meet Pasadena Historic Preservation Commission guidelines while providing modern insulation performance. We handle HPC permit coordination."),
            ("Do you install glass railings in Pasadena?",
             "Yes. We install frameless glass railing systems for decks, stairs, and balconies. Pasadena's hillside neighborhoods are a common location for this type of work."),
            ("How far is Pasadena from your Reseda location?",
             "About 35–50 minutes depending on freeway conditions. We schedule Pasadena jobs routinely and can reach the city within an hour for emergency calls."),
        ],
        "nearby": [
            ("arcadia", "Arcadia") if os.path.exists("arcadia.html") else ("monrovia", "Monrovia"),
            ("glendale", "Glendale"), ("los-angeles", "Los Angeles"),
            ("temple-city", "Temple City"), ("san-marino", "San Marino"),
        ],
    },

    "thousand-oaks": {
        "city_name": "Thousand Oaks",
        "deep_content": """
        <p>Thousand Oaks is the largest city in Ventura County and one of the most consistently active markets for residential glass work in our service area. The combination of high homeownership rates, newer construction, and a demographic that invests heavily in home upgrades makes it a strong market for shower enclosures, window maintenance, and custom glass features.</p>
        <p>The majority of Thousand Oaks was built between the 1960s and 1990s, which means a substantial portion of the housing stock is now in the window replacement window. Dual-pane units installed in the 1980s and early 1990s typically have a 20–25 year lifespan for the insulating seal. If you're seeing condensation or cloudiness between your window panes in a Thousand Oaks home built before 2000, the seal has likely failed — and this will only get worse over time, eventually causing glass staining that's difficult to remove even after seal repair.</p>
        <p>Shower enclosure upgrades are the most common request we get from Thousand Oaks homeowners. The city's track-home bathroom layouts from the 70s and 80s typically have older framed or bypass shower doors that homeowners are replacing with frameless or semi-frameless glass. Custom-cut frameless shower glass dramatically changes how a bathroom feels — and in Thousand Oaks' competitive real estate market, it's one of the better-returning bathroom investments before a sale.</p>
        <p>The Conejo Valley business park corridors along Thousand Oaks Blvd and Moorpark Rd generate commercial glass work — we handle storefront glass, office partition glass, and commercial door systems throughout the area. For emergency board-up in Thousand Oaks, call us directly: drive time from Reseda is typically 30–40 minutes via the 101.</p>
        """,
        "why_items": [
            {"title": "30–40 min from Reseda via 101", "body": "Thousand Oaks is one of our primary Ventura County markets — fast access for both scheduled and emergency calls."},
            {"title": "Shower enclosure specialists for Conejo Valley homes", "body": "We've replaced hundreds of framed bypass shower doors with frameless glass in Thousand Oaks' track home stock. We know the standard bathroom sizes."},
            {"title": "IGU replacement for 1980s–1990s era homes", "body": "Most Thousand Oaks homes from this era are hitting dual-pane seal failure now. We replace sealed units without removing your frames."},
            {"title": "Conejo Valley commercial glass", "body": "Storefront glass, office partitions, and commercial door systems for the business parks and retail corridors throughout Thousand Oaks and Newbury Park."},
        ],
        "extra_faqs": [
            ("Is frameless shower glass worth the cost for a Thousand Oaks home?",
             "In Thousand Oaks' real estate market, yes — frameless shower glass typically returns well at resale and makes the bathroom feel significantly larger. Our standard frameless enclosures start around $1,200 for a simple alcove configuration."),
            ("Do you serve Newbury Park and Westlake Village from your Thousand Oaks coverage?",
             "Yes — Newbury Park is part of Thousand Oaks and we serve it routinely. Westlake Village is covered as a separate service area and is also 30–35 minutes from Reseda."),
            ("How long does a window seal replacement take in Thousand Oaks?",
             "We typically measure on Monday and schedule replacement within the same week. Each IGU takes 1–3 hours to swap depending on window size and accessibility."),
        ],
        "nearby": [
            ("westlake-village", "Westlake Village"), ("newbury-park", "Newbury Park"),
            ("moorpark", "Moorpark"), ("simi-valley", "Simi Valley"), ("camarillo", "Camarillo"),
        ],
    },

    "simi-valley": {
        "city_name": "Simi Valley",
        "deep_content": """
        <p>Simi Valley is a natural extension of the San Fernando Valley and one of our most consistent service markets. The city's family-oriented neighborhoods and high homeownership rate, combined with an aging housing stock from the 1970s–1990s, create steady demand for window repair, shower glass upgrades, and residential glass services across the board.</p>
        <p>Simi Valley experienced most of its residential development in three waves: the 1960s–70s (tract homes in Wood Ranch and Royal Highlands), the 1980s (larger developments in the East end), and the 1990s (newer estates near the hills). The 70s–80s-era homes are now hitting the dual-pane window replacement cycle most actively — seals from that era don't last forever, and Simi Valley's climate swings (hot summers, cooler winters than coastal LA) stress window seals faster than they would in more temperate areas.</p>
        <p>Shower enclosures are consistently the top residential project in Simi Valley. Many homes built in the 80s and 90s still have the original framed or bypass shower doors — functional but dated. Homeowners replacing these with frameless glass consistently mention the same two benefits: the bathroom looks twice as large, and cleaning is dramatically easier without metal channels trapping soap scum.</p>
        <p>Commercial glass work in Simi Valley is concentrated along the First Street corridor and the Simi Valley Town Center area. We handle storefront glass replacement, emergency board-up, and commercial door systems for this corridor. Break-in board-up is unfortunately a common call — we're typically 25–30 minutes from central Simi Valley for emergency response.</p>
        <p>One note on Simi Valley emergency service: if you need glass board-up late in the evening, call us at (805) 750-6471 directly rather than using the contact form. We monitor the phone line until 10pm and can dispatch for genuine emergencies after business hours.</p>
        """,
        "why_items": [
            {"title": "25–30 min from Reseda via 118", "body": "Simi Valley is close — one of our fastest response markets for emergencies and same-day scheduling."},
            {"title": "Specialists in 1970s–1990s track home glass", "body": "We've worked in virtually every Simi Valley neighborhood and know the common window and shower configurations in homes from each era."},
            {"title": "Climate-appropriate recommendations", "body": "Simi Valley's temperature swings are harder on window seals than the coast. We recommend appropriate Low-E coatings and glass specs for the local climate."},
            {"title": "After-hours emergency line", "body": "For genuine emergencies, call (805) 750-6471 directly until 10pm — we dispatch for urgent board-up situations."},
        ],
        "extra_faqs": [
            ("Does the Simi Valley climate damage window seals faster than coastal areas?",
             "Yes — the larger temperature differential in Simi Valley (hot summers, cooler winters) accelerates seal degradation compared to coastal LA. If your dual-pane windows are 20+ years old, have them inspected before the fogging stage sets in."),
            ("Can you do emergency board-up in Simi Valley late at night?",
             "For genuine emergencies (break-in, storm damage), call us directly at (805) 750-6471 until 10pm. We assess and dispatch based on urgency."),
            ("What's the most popular shower enclosure type in Simi Valley homes?",
             "Frameless pivot or hinged doors for alcove showers are most common. Semi-frameless is a popular cost-saving option. We measure and custom-cut to your exact opening."),
        ],
        "nearby": [
            ("thousand-oaks", "Thousand Oaks"), ("moorpark", "Moorpark"),
            ("chatsworth", "Chatsworth"), ("northridge", "Northridge"), ("west-hills", "West Hills"),
        ],
    },

    "riverside": {
        "city_name": "Riverside",
        "deep_content": """
        <p>Riverside is the largest city in the Inland Empire and the seat of Riverside County — a sprawling, diverse city with architecture ranging from late Victorian and Craftsman homes in the Wood Streets historic district to post-war tract neighborhoods to new construction developments on the city's expanding edges. Each building type comes with its own glass needs, and we handle all of them.</p>
        <p>The historic neighborhoods north of the 91 Freeway — including the Wood Streets, Magnolia Center, and the downtown core — have some of Riverside's most architecturally significant older homes. Many of these were built in the 1900s–1930s with original single-pane windows that have survived for decades but are increasingly being replaced with dual-pane units that reduce utility costs without altering the exterior appearance. We work with window styles appropriate for older Craftsman and bungalow construction.</p>
        <p>In Riverside's post-war and tract neighborhoods — Highgrove, Orangecrest, Hunter Park — dual-pane seal failure is the most common issue we're called for. Homes built between 1975 and 2000 with original dual-pane are reaching the end of their insulating glass unit lifespan. IGU replacement is a cost-effective fix that restores clarity and insulation without full window replacement.</p>
        <p>Shower glass is growing in Riverside as homeowners invest in master bathroom remodels. Frameless enclosures were historically a premium product concentrated in upscale markets — but pricing has come down and the installation is now accessible to the broader Riverside market. Our drive time is about 60–70 minutes, so we typically batch Riverside jobs and schedule 1–2 day blocks in the area to make the drive worthwhile for smaller jobs.</p>
        <p>Commercial glass in Riverside is anchored by the University Avenue corridor, the downtown Riverside area around the Fox Performing Arts Center, and the industrial/warehouse corridor near the 215. We handle storefront glass, office partitions, and emergency board-up for commercial clients throughout the city.</p>
        """,
        "why_items": [
            {"title": "Experience with historic Riverside architecture", "body": "We work with window styles appropriate for the Wood Streets and Magnolia Center historic districts — including dual-pane units that preserve original sash profiles."},
            {"title": "IGU replacement for Inland Empire's aging stock", "body": "Homes built 1975–2000 in Riverside are hitting seal failure now. We replace the glass unit without frame removal."},
            {"title": "Scheduled Riverside job blocks", "body": "To make the drive worthwhile for smaller jobs, we batch Riverside appointments. We can often pair your job with nearby work for faster scheduling."},
            {"title": "University corridor commercial glass", "body": "Storefront glass, office buildout partitions, and emergency board-up for Riverside's commercial and campus-adjacent districts."},
        ],
        "extra_faqs": [
            ("How far is Riverside from your Reseda location?",
             "About 60–70 minutes via the 60 or 91 freeway. We batch Riverside appointments to make scheduling efficient — call to check if we have a Riverside day coming up soon."),
            ("Do you serve the historic Wood Streets neighborhood in Riverside?",
             "Yes. We're familiar with the architectural requirements of Riverside's historic districts and work with window styles appropriate for pre-war Craftsman and bungalow construction."),
            ("Can you handle emergency glass board-up in Riverside?",
             "Yes — for genuine emergencies (break-in, storm damage), call us directly at (805) 750-6471. Response time to Riverside is 60–90 minutes depending on traffic. We'll tell you our ETA on the call."),
        ],
        "nearby": [
            ("corona", "Corona"), ("moreno-valley", "Moreno Valley"),
            ("jurupa-valley", "Jurupa Valley"), ("colton", "Colton"), ("san-bernardino", "San Bernardino"),
        ],
    },

    "corona": {
        "city_name": "Corona",
        "deep_content": """
        <p>Corona sits at the junction of Los Angeles, San Bernardino, and Riverside Counties — and its rapid residential growth over the past 30 years means a high concentration of homes from the 1990s and 2000s that are entering their first major glass maintenance cycle. Dual-pane seals from this era are failing across the city, and homeowners are also taking the opportunity to upgrade showers, add custom mirrors, and make other glass improvements as they maintain or prepare homes for sale.</p>
        <p>The master-planned neighborhoods of South Corona — Sycamore Creek, Dos Lagos, Sierra del Oro — have a high proportion of custom and semi-custom homes where premium glass work is common. Frameless shower enclosures in 3/8" and 1/2" tempered glass are the standard for these homes. Many also feature large mirrors in master baths, home gyms, and formal rooms — all areas where we do custom-cut glass work.</p>
        <p>North Corona and the older neighborhoods near downtown have a different profile — mid-century homes with original single-pane or early dual-pane, where the priority is often functional repair (broken panes, failed seals) rather than upgrade work. We handle both ends of the market and price accordingly.</p>
        <p>Drive time from Reseda to Corona is about 55–65 minutes via the 91. We typically schedule Corona along with nearby Ontario, Rancho Cucamonga, and Chino Hills to make efficient use of the drive. If you're in Corona and have a neighbor or property manager who also needs glass work, call us — we frequently do multi-job Inland Empire days.</p>
        <p>Commercial glass in Corona includes the Crossings at Corona and the business parks along the 15 Freeway corridor. Storefront glass replacement, glass partitions, and emergency board-up are the most common commercial calls we get from the area.</p>
        """,
        "why_items": [
            {"title": "Specialists in 1990s–2000s tract home glass", "body": "Corona's most common residential profile — and we've done seal replacement, shower upgrades, and custom mirrors in hundreds of these homes."},
            {"title": "Premium glass for South Corona estates", "body": "Custom frameless enclosures in 1/2\" glass, large custom mirrors, and finish-quality installation for Sycamore Creek and Sierra del Oro area homes."},
            {"title": "Inland Empire batching for efficiency", "body": "We run Inland Empire days combining Corona with nearby Ontario, Rancho Cucamonga, and Chino Hills — call to get added to the next available run."},
            {"title": "15 Freeway corridor commercial", "body": "Storefront glass, office buildouts, emergency board-up for the business park and retail developments along Corona's commercial corridors."},
        ],
        "extra_faqs": [
            ("Do you serve South Corona neighborhoods like Sycamore Creek?",
             "Yes — South Corona's premium neighborhoods are a regular service area for us. We install frameless shower glass, custom mirrors, and custom glass features for homes in these communities."),
            ("Can I schedule Corona glass work on the same day as nearby Rancho Cucamonga?",
             "Often yes. We batch Inland Empire appointments to minimize drive time. Call and mention you're near Rancho Cucamonga — we'll try to pair you with existing IE work."),
            ("What's the drive time for emergency glass repair in Corona?",
             "About 55–65 minutes from Reseda under normal conditions. Call us directly at (805) 750-6471 for emergency response — we'll give you an honest ETA based on current traffic."),
        ],
        "nearby": [
            ("riverside", "Riverside"), ("rancho-cucamonga", "Rancho Cucamonga"),
            ("ontario", "Ontario"), ("chino-hills", "Chino Hills"), ("norco", "Norco"),
        ],
    },

    "rancho-cucamonga": {
        "city_name": "Rancho Cucamonga",
        "deep_content": """
        <p>Rancho Cucamonga is one of the most affluent cities in the Inland Empire — and that prosperity shows up in the type of glass work we do here. The city's planned communities, upscale retail around Victoria Gardens, and newer luxury home developments consistently generate demand for premium glass work: frameless shower enclosures in 1/2" glass, large custom wall mirrors, glass railings, and high-specification storefront glass for the city's commercial corridors.</p>
        <p>The neighborhoods clustered north of Foothill Boulevard — particularly the hillside communities with views of the San Gabriel Mountains — have some of Rancho Cucamonga's most active custom glass markets. Homes in this area tend to have large windows and open floor plans that require precise glass measurement and careful installation to maintain the architectural intent. We field-measure every job rather than working from drawings, which matters on hillside lots where level and plumb can't be assumed.</p>
        <p>Rancho Cucamonga's master-planned communities — Etiwanda, Alta Loma, the areas around Victoria Gardens — were largely built between 1985 and 2005. This means a large portion of the housing stock is now in the prime window seal replacement zone. If your home was built before 2000 and you're seeing condensation between window panes, the insulating gas seal has failed — a common issue across this era of construction in the Inland Empire's climate.</p>
        <p>The Victoria Gardens shopping and entertainment district and the Foothill Boulevard commercial corridor generate consistent commercial glass demand. We handle storefront glass replacement (including emergency board-up for break-ins), commercial glass doors, and glass partitions for offices and retail spaces throughout Rancho Cucamonga. Drive time from Reseda is about 55 minutes — we batch Rancho Cucamonga appointments with nearby work in Ontario and Fontana to make efficient use of the day.</p>
        """,
        "why_items": [
            {"title": "Premium glass for hillside and estate homes", "body": "We field-measure on hillside lots where level and plumb can't be assumed — every panel cut to actual field dimensions."},
            {"title": "IGU seal replacement for 1985–2005 homes", "body": "Rancho Cucamonga's prime housing era is hitting seal failure now. We swap the glass unit without removing your frame or trim."},
            {"title": "Victoria Gardens area commercial glass", "body": "Storefront replacement, emergency board-up, and commercial glass partitions for the Victoria Gardens corridor and Foothill Blvd businesses."},
            {"title": "Inland Empire batching", "body": "We run IE days combining Rancho Cucamonga with Ontario, Fontana, and Chino Hills — call to get on the next available run for faster scheduling."},
        ],
        "extra_faqs": [
            ("Why does Rancho Cucamonga rank high for window seal failures?",
             "The city's prime construction era (1985–2005) means a large share of homes are now 20–40 years old — right in the window where dual-pane seals typically fail. The Inland Empire's hotter climate also accelerates seal degradation relative to coastal areas."),
            ("Do you do custom glass work for homes in the Etiwanda or Alta Loma neighborhoods?",
             "Yes — Etiwanda, Alta Loma, and the hillside communities north of Foothill are areas we serve regularly. Call to schedule or request a free estimate online."),
            ("Can you handle storefront glass for businesses near Victoria Gardens?",
             "Yes — we handle storefront glass replacement, emergency board-up, and commercial glass systems for the Victoria Gardens area and throughout Rancho Cucamonga's commercial corridors."),
        ],
        "nearby": [
            ("ontario", "Ontario"), ("fontana", "Fontana"), ("upland", "Upland"),
            ("chino-hills", "Chino Hills"), ("corona", "Corona"),
        ],
    },
}

# ── Process each city ──────────────────────────────────────────────
processed = 0
for slug, data in CITIES.items():
    path = f"{slug}.html"
    if not os.path.exists(path):
        print(f"  MISSING {path}")
        continue

    with open(path) as f:
        content = f.read()

    if f'id="extra-faqs-{slug}"' in content:
        print(f"  SKIP {slug} — already expanded")
        continue

    section_html = make_deep_section(slug, data)
    new_content = INSERT_BEFORE.sub(section_html + r'\1', content, count=1)

    if new_content == content:
        print(f"  WARN {slug} — insertion point not found")
        continue

    # Also inject the extra FAQs into the existing FAQ list
    faq_end = new_content.find('</div>\n      </div>\n    </div>\n  </section>\n\n  <div class="divider"></div>')
    if faq_end == -1:
        # Try to find end of faq-list
        faq_list_end = new_content.rfind('</div>\n      </div>\n    </div>\n  </section>\n\n  <section style="background:var(--bg-soft);padding:72px 0;">')
        if faq_list_end != -1:
            # Insert extra FAQs before the section
            pass

    with open(path, "w") as f:
        f.write(new_content)

    print(f"  EXPANDED {slug} ({data['city_name']})")
    processed += 1

print(f"\nDone: {processed} city pages expanded")

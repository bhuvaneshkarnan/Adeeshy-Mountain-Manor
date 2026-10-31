import os
import re
from pathlib import Path
from datetime import date

DOMAIN = "https://adeeshymanor.com"
TODAY = date.today().isoformat()

# Mapping of file paths to specific optimized metadata
PAGE_METADATA = {
    "index.html": {
        "title": "Adeeshy Mountain Manor | Luxury Tropical Estate in Sirumalai",
        "desc": "Experience luxury mountain living at Adeeshy Mountain Manor in Sirumalai Hills, Tamil Nadu. Book private stone cabins, cloud suites & panoramic retreats.",
        "canonical": f"{DOMAIN}/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "resort_home",
        "priority": "1.0",
        "changefreq": "daily"
    },
    "en/index.html": {
        "title": "Adeeshy Mountain Manor | Luxury Tropical Estate in Sirumalai",
        "desc": "Experience luxury mountain living at Adeeshy Mountain Manor in Sirumalai Hills, Tamil Nadu. Book private stone cabins, cloud suites & panoramic retreats.",
        "canonical": f"{DOMAIN}/en/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "resort_home",
        "priority": "1.0",
        "changefreq": "daily"
    },
    "en/about/index.html": {
        "title": "About Adeeshy Mountain Manor | Luxury Retreat in Sirumalai",
        "desc": "Discover Adeeshy Mountain Manor — an exclusive luxury tropical estate nestled among serene pine forests in Sirumalai Hills, Tamil Nadu. Handcrafted stone sanctuaries.",
        "canonical": f"{DOMAIN}/en/about/",
        "image": f"{DOMAIN}/assets/images/about/sirumalai-peaks.webp",
        "type": "about",
        "priority": "0.9",
        "changefreq": "weekly"
    },
    "en/accommodation/index.html": {
        "title": "Luxury Rooms & Private Suites | Adeeshy Mountain Manor",
        "desc": "Explore handcrafted luxury suites in Sirumalai: Shyadé Stone Cabin, Advé Cloud Suite, DEE’ DAWN Sunrise Room & The Royal’e Suite with 360° views.",
        "canonical": f"{DOMAIN}/en/accommodation/",
        "image": f"{DOMAIN}/assets/images/rooms/shyade-stone-cabin/photo-1.webp",
        "type": "accommodation_collection",
        "priority": "0.95",
        "changefreq": "weekly"
    },
    "en/accommodation/shyade-stone-cabin/index.html": {
        "title": "Shyadé Stone Cabin | Misty Valley Retreat at Adeeshy Manor",
        "desc": "Discover rustic charm and refined luxury in the Shyadé Stone Cabin at Adeeshy Mountain Manor, Sirumalai. Handcrafted stone architecture & mist valley vistas.",
        "canonical": f"{DOMAIN}/en/accommodation/shyade-stone-cabin/",
        "image": f"{DOMAIN}/assets/images/rooms/shyade-stone-cabin/photo-1.webp",
        "type": "room_shyade",
        "priority": "0.9",
        "changefreq": "weekly"
    },
    "en/accommodation/adve-cloud-suite/index.html": {
        "title": "Advé Cloud Suite | 360° Cloudview Room at Adeeshy Manor",
        "desc": "Surround yourself with 360° panoramic mountain views where floating clouds kiss the peak. Book the signature Advé Cloud Suite in Sirumalai Hills.",
        "canonical": f"{DOMAIN}/en/accommodation/adve-cloud-suite/",
        "image": f"{DOMAIN}/assets/images/rooms/adve-cloud-suite/photo-1.webp",
        "type": "room_adve",
        "priority": "0.9",
        "changefreq": "weekly"
    },
    "en/accommodation/dee-dawn/index.html": {
        "title": "DEE’ DAWN Sunrise Room | Luxury Stay at Adeeshy Manor",
        "desc": "Wake up to breathtaking sunrises in Sirumalai Hills. DEE’ DAWN Sunrise Room blends nature, golden morning vistas, and luxurious boutique comfort.",
        "canonical": f"{DOMAIN}/en/accommodation/dee-dawn/",
        "image": f"{DOMAIN}/assets/images/rooms/dee-dawn/photo-1.webp",
        "type": "room_dee_dawn",
        "priority": "0.9",
        "changefreq": "weekly"
    },
    "en/accommodation/the-royale-suite/index.html": {
        "title": "The Royal’e Suite | Mountain Living & Hall at Adeeshy Manor",
        "desc": "Indulge in spacious mountain luxury with a private living hall, elegant dining area, and dedicated kitchen facilities at Adeeshy Mountain Manor.",
        "canonical": f"{DOMAIN}/en/accommodation/the-royale-suite/",
        "image": f"{DOMAIN}/assets/images/rooms/the-royale-suite/photo-1.webp",
        "type": "room_royale",
        "priority": "0.9",
        "changefreq": "weekly"
    },
    "en/contact/index.html": {
        "title": "Contact & Reservations | Adeeshy Mountain Manor Sirumalai",
        "desc": "Get in touch with Adeeshy Mountain Manor in Sirumalai Hills, Dindigul, Tamil Nadu. Book your private retreat, inquire about events, or get directions.",
        "canonical": f"{DOMAIN}/en/contact/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "contact",
        "priority": "0.9",
        "changefreq": "weekly"
    },
    "en/amenities/index.html": {
        "title": "Estate Amenities & Facilities | Adeeshy Mountain Manor",
        "desc": "Discover our premium estate amenities in Sirumalai: panoramic viewing decks, bonfire lounges, curated nature trails, gourmet dining, and spa wellness.",
        "canonical": f"{DOMAIN}/en/amenities/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "amenities",
        "priority": "0.85",
        "changefreq": "monthly"
    },
    "en/facilities/index.html": {
        "title": "Facilities & Experiences | Adeeshy Mountain Manor Sirumalai",
        "desc": "Explore world-class facilities at Adeeshy Mountain Manor in Sirumalai Hills: scenic outdoor spaces, leisure hall, dining pavilion, and tranquility gardens.",
        "canonical": f"{DOMAIN}/en/facilities/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "facilities",
        "priority": "0.85",
        "changefreq": "monthly"
    },
    "en/gallery/index.html": {
        "title": "Estate Photo Gallery | Adeeshy Mountain Manor Sirumalai",
        "desc": "View high-resolution photography of Adeeshy Mountain Manor: stone cabins, cloud view suites, lush pine forests, and misty mountain horizons in Sirumalai.",
        "canonical": f"{DOMAIN}/en/gallery/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "gallery",
        "priority": "0.85",
        "changefreq": "monthly"
    },
    "en/activities/index.html": {
        "title": "Estate Activities & Experiences | Adeeshy Mountain Manor",
        "desc": "Immerse in nature walks, birdwatching, mountain trekking, and private outdoor dining in the tranquil hill station of Sirumalai at Adeeshy Manor.",
        "canonical": f"{DOMAIN}/en/activities/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "activities",
        "priority": "0.8",
        "changefreq": "monthly"
    },
    "en/booking/index.html": {
        "title": "Reserve Your Stay | Adeeshy Mountain Manor Sirumalai",
        "desc": "Book your luxury stay at Adeeshy Mountain Manor, Sirumalai Hills. Select from stone cabins, cloudview suites, and private mountain living quarters.",
        "canonical": f"{DOMAIN}/en/booking/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "booking",
        "priority": "0.95",
        "changefreq": "daily"
    },
    "en/events/index.html": {
        "title": "Private Events & Celebrations | Adeeshy Mountain Manor",
        "desc": "Host intimate weddings, executive retreats, and memorable family gatherings surrounded by cloud-kissed peaks at Adeeshy Mountain Manor in Sirumalai.",
        "canonical": f"{DOMAIN}/en/events/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "events",
        "priority": "0.8",
        "changefreq": "monthly"
    },
    "en/restaurants-and-bars/index.html": {
        "title": "Estate Dining & Gourmet Cuisine | Adeeshy Mountain Manor",
        "desc": "Savor authentic regional delicacies and customized multi-course dining prepared with fresh estate produce amidst the crisp air of Sirumalai Hills.",
        "canonical": f"{DOMAIN}/en/restaurants-and-bars/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "dining",
        "priority": "0.8",
        "changefreq": "monthly"
    },
    "en/spa-center/index.html": {
        "title": "Wellness & Spa Sanctuary | Adeeshy Mountain Manor",
        "desc": "Rejuvenate your senses with herbal therapies, deep relaxation, and holistic wellness amidst the pure mountain air of Sirumalai Hills, Tamil Nadu.",
        "canonical": f"{DOMAIN}/en/spa-center/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "spa",
        "priority": "0.8",
        "changefreq": "monthly"
    },
    "en/getting-here/index.html": {
        "title": "Location & Directions | Adeeshy Mountain Manor Sirumalai",
        "desc": "How to reach Adeeshy Mountain Manor in Sirumalai Hills from Madurai Airport (85 km) and Dindigul Junction (25 km). Driving directions and travel advice.",
        "canonical": f"{DOMAIN}/en/getting-here/",
        "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
        "type": "getting_here",
        "priority": "0.8",
        "changefreq": "monthly"
    }
}

# Standardized JSON-LD Schemas
RESORT_SCHEMA = {
    "@context": "https://schema.org",
    "@type": ["Resort", "Hotel", "LodgingBusiness"],
    "@id": f"{DOMAIN}/#resort",
    "name": "Adeeshy Mountain Manor",
    "alternateName": ["Adeeshy Manor", "Adeeshy Sirumalai"],
    "description": "A luxury private tropical estate retreat nestled in the pristine misty peaks of Sirumalai Hills, Dindigul District, Tamil Nadu, India.",
    "url": DOMAIN,
    "telephone": "+91 98765 43210",
    "email": "info@adeeshymanor.com",
    "image": f"{DOMAIN}/assets/images/drone-video-poster.webp",
    "priceRange": "₹₹₹₹",
    "currenciesAccepted": "INR",
    "paymentAccepted": "Cash, Credit Card, UPI, Net Banking",
    "checkinTime": "14:00",
    "checkoutTime": "11:00",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Sirumalai Hills",
        "addressLocality": "Dindigul",
        "addressRegion": "Tamil Nadu",
        "postalCode": "624314",
        "addressCountry": "IN"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": 10.2078,
        "longitude": 77.9972
    },
    "starRating": {
        "@type": "Rating",
        "ratingValue": "5"
    },
    "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "360 Panoramic Mountain Views", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Handcrafted Stone Architecture", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Private Mountain Living Hall & Dining", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "High-Speed Wi-Fi", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Organic Estate Dining", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Evening Bonfire Experience", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Curated Pine Forest Nature Trails", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "24/7 Concierge Service", "value": True}
    ]
}

FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Where is Adeeshy Mountain Manor located?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Adeeshy Mountain Manor is located atop the tranquil Sirumalai Hills in Dindigul District, Tamil Nadu (PIN: 624314), approximately 25 km from Dindigul Railway Station and 85 km from Madurai International Airport."
            }
        },
        {
            "@type": "Question",
            "name": "What room types and suites are available at Adeeshy Mountain Manor?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "We offer four distinct handcrafted estate sanctuaries: Shyadé Stone Cabin (rustic charm & misty valley retreat), Advé Cloud Suite (360° panoramic cloudview room), DEE’ DAWN (the sunrise room with golden mountain views), and The Royal’e Suite (spacious mountain living hall and dining)."
            }
        },
        {
            "@type": "Question",
            "name": "What are the check-in and check-out timings?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Standard check-in is at 2:00 PM and check-out is at 11:00 AM. Early check-in or late check-out can be requested upon booking subject to estate availability."
            }
        },
        {
            "@type": "Question",
            "name": "How can I book a stay or reserve the entire estate?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Reservations can be made directly through our website booking form, by calling +91 98765 43210, or by emailing info@adeeshymanor.com. We also offer exclusive full-estate private buyouts for families and intimate celebrations."
            }
        },
        {
            "@type": "Question",
            "name": "What is the best time to visit Sirumalai Hills?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Sirumalai enjoys pleasant, refreshing hill weather throughout the year (18°C to 26°C). The monsoon and post-monsoon months (September to February) feature spectacular rolling mist, cloud valleys, and lush green scenery."
            }
        }
    ]
}

def get_room_schema(name, description, beds=1, max_guests=3):
    return {
        "@context": "https://schema.org",
        "@type": "HotelRoom",
        "name": name,
        "description": description,
        "bed": {
            "@type": "BedDetails",
            "numberOfBeds": beds,
            "typeOfBed": "King Bed"
        },
        "occupancy": {
            "@type": "QuantitativeValue",
            "maxValue": max_guests,
            "minValue": 1
        },
        "amenityFeature": [
            {"@type": "LocationFeatureSpecification", "name": "Mountain & Valley Views", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "En-suite Luxury Bathroom", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Dedicated Room Service", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Private Balcony / Veranda", "value": True}
        ]
    }

def get_breadcrumb_schema(items):
    entity_list = []
    for idx, (name, url) in enumerate(items, start=1):
        entity_list.append({
            "@type": "ListItem",
            "position": idx,
            "name": name,
            "item": url
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": entity_list
    }

import json

def build_schema_block(schemas):
    blocks = []
    for s in schemas:
        blocks.append(f'<script type="application/ld+json">\n{json.dumps(s, indent=2, ensure_ascii=False)}\n</script>')
    return "\n".join(blocks)

def process_file(rel_path):
    p = Path(rel_path)
    if not p.exists():
        return False, "File does not exist"
    
    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()
    
    original = html
    norm_path = rel_path.replace('\\', '/')
    
    # 1. Clean legacy Webflow data domain
    html = re.sub(r'data-wf-domain="[^"]*"', 'data-wf-domain="adeeshymanor.com"', html)
    
    # 2. Remove legacy Bulgarian hreflang & x-default links
    html = re.sub(r'<link[^>]*hreflang="x-default"[^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<link[^>]*hreflang="bg"[^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<link[^>]*hreflang="en"[^>]*>', '', html, flags=re.IGNORECASE)
    
    # 3. Safe string removal of json-ld
    while '<script type="application/ld+json">' in html:
        s_idx = html.find('<script type="application/ld+json">')
        e_idx = html.find('</script>', s_idx)
        if e_idx != -1:
            html = html[:s_idx] + html[e_idx + len('</script>'):]
        else:
            break
    
    # 6. Preconnect fonts for speed
    preconnect_block = '''  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link rel="preconnect" href="https://cdn.prod.website-files.com"/>'''
    
    # Replace old preconnect or insert
    html = re.sub(r'<link href="https://cdn\.prod\.website-files\.com" rel="preconnect"/>', preconnect_block, html)
    
    # Determine metadata for this page
    meta = PAGE_METADATA.get(norm_path)
    if not meta:
        # Generate default clean metadata for secondary pages
        # Convert path to title
        slug = norm_path.replace('index.html', '').strip('/').split('/')[-1]
        readable = slug.replace('-', ' ').title() if slug else "Home"
        title = f"{readable} | Adeeshy Mountain Manor Sirumalai"
        desc = f"Discover {readable} at Adeeshy Mountain Manor — a luxury tropical retreat nestled in the pristine misty peaks of Sirumalai Hills, Tamil Nadu."
        canonical = f"{DOMAIN}/{norm_path.replace('index.html', '')}"
        image = f"{DOMAIN}/assets/images/drone-video-poster.webp"
        page_type = "generic"
    else:
        title = meta["title"]
        desc = meta["desc"]
        canonical = meta["canonical"]
        image = meta["image"]
        page_type = meta["type"]
    
    # 7. Update <title>
    if re.search(r'<title>.*?</title>', html, flags=re.IGNORECASE):
        html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1, flags=re.IGNORECASE)
    else:
        html = html.replace('<head>', f'<head>\n<title>{title}</title>', 1)
        
    # 8. Update meta description
    if re.search(r'<meta[^>]*name="description"[^>]*>', html, flags=re.IGNORECASE):
        html = re.sub(r'<meta[^>]*name="description"[^>]*content="[^"]*"[^>]*>', f'<meta name="description" content="{desc}"/>', html, count=1, flags=re.IGNORECASE)
        html = re.sub(r'<meta[^>]*content="[^"]*"[^>]*name="description"[^>]*>', f'<meta name="description" content="{desc}"/>', html, count=1, flags=re.IGNORECASE)
    else:
        html = re.sub(r'(<title>.*?</title>)', f'\\1\n  <meta name="description" content="{desc}"/>', html, count=1, flags=re.IGNORECASE)

    # 9. Canonical link
    canonical_tag = f'  <link rel="canonical" href="{canonical}"/>'
    html = re.sub(r'(<title>.*?</title>)', f'\\1\n{canonical_tag}', html, count=1, flags=re.IGNORECASE)
    
    # 10. Update Open Graph & Twitter Cards
    html = re.sub(r'<meta content="[^"]*" property="og:title"/>', f'<meta content="{title}" property="og:title"/>', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{title}"/>', html)
    html = re.sub(r'<meta content="[^"]*" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*"/>', f'<meta property="og:description" content="{desc}"/>', html)
    html = re.sub(r'<meta content="[^"]*" property="og:image"/>', f'<meta content="{image}" property="og:image"/>', html)
    html = re.sub(r'<meta property="og:image" content="[^"]*"/>', f'<meta property="og:image" content="{image}"/>', html)
    
    # Add og:url and og:site_name if missing
    if 'property="og:url"' not in html:
        html = re.sub(r'(property="og:type"[^>]*>)', f'\\1\n  <meta content="{canonical}" property="og:url"/>\n  <meta content="Adeeshy Mountain Manor" property="og:site_name"/>', html)
    else:
        html = re.sub(r'<meta content="[^"]*" property="og:url"/>', f'<meta content="{canonical}" property="og:url"/>', html)
    
    html = re.sub(r'<meta content="[^"]*" name="twitter:title"/>', f'<meta content="{title}" name="twitter:title"/>', html)
    html = re.sub(r'<meta name="twitter:title" content="[^"]*"/>', f'<meta name="twitter:title" content="{title}"/>', html)
    html = re.sub(r'<meta content="[^"]*" name="twitter:description"/>', f'<meta content="{desc}" name="twitter:description"/>', html)
    html = re.sub(r'<meta name="twitter:description" content="[^"]*"/>', f'<meta name="twitter:description" content="{desc}"/>', html)
    html = re.sub(r'<meta content="[^"]*" name="twitter:image"/>', f'<meta content="{image}" name="twitter:image"/>', html)
    html = re.sub(r'<meta name="twitter:image" content="[^"]*"/>', f'<meta name="twitter:image" content="{image}"/>', html)

    # 11. Structured Data Schemas
    schemas = []
    if page_type == "resort_home":
        schemas.append(RESORT_SCHEMA)
        schemas.append(FAQ_SCHEMA)
    elif page_type == "contact":
        schemas.append(FAQ_SCHEMA)
        schemas.append(get_breadcrumb_schema([
            ("Home", f"{DOMAIN}/"),
            ("Contact Us", canonical)
        ]))
    elif page_type == "about":
        schemas.append({
            "@context": "https://schema.org",
            "@type": "AboutPage",
            "name": title,
            "description": desc,
            "url": canonical,
            "mainEntity": {"@id": f"{DOMAIN}/#resort"}
        })
        schemas.append(get_breadcrumb_schema([
            ("Home", f"{DOMAIN}/"),
            ("About Adeeshy", canonical)
        ]))
    elif page_type == "accommodation_collection":
        schemas.append(get_breadcrumb_schema([
            ("Home", f"{DOMAIN}/"),
            ("Rooms & Suites", canonical)
        ]))
    elif page_type.startswith("room_"):
        room_name = title.split("|")[0].strip()
        schemas.append(get_room_schema(room_name, desc))
        schemas.append(get_breadcrumb_schema([
            ("Home", f"{DOMAIN}/"),
            ("Rooms & Suites", f"{DOMAIN}/en/accommodation/"),
            (room_name, canonical)
        ]))
    else:
        # Generic subpage breadcrumb
        segments = [s for s in norm_path.replace('index.html', '').strip('/').split('/') if s]
        crumbs = [("Home", f"{DOMAIN}/")]
        cur = f"{DOMAIN}"
        for s in segments:
            cur += f"/{s}"
            crumbs.append((s.replace('-', ' ').title(), f"{cur}/"))
        schemas.append(get_breadcrumb_schema(crumbs))

    schema_markup = build_schema_block(schemas)
    # Inject schema right before </head>
    html = html.replace('</head>', f'{schema_markup}\n</head>', 1)
    
    # 12. Speed Optimization on Images:
    # Add loading="lazy" and decoding="async" to images where not already present,
    # except hero / logo images.
    def optimize_img(match):
        img_str = match.group(0)
        # Preserve hero logo or hero video posters as high priority
        if 'logo' in img_str.lower() or 'brand' in img_str.lower() or 'hero' in img_str.lower() or 'poster' in img_str.lower():
            if 'decoding=' not in img_str.lower():
                img_str = img_str[:-1] + ' decoding="async">'
            return img_str
        
        if 'loading=' not in img_str.lower():
            img_str = img_str[:-1] + ' loading="lazy">'
        if 'decoding=' not in img_str.lower():
            img_str = img_str[:-1] + ' decoding="async">'
        return img_str

    html = re.sub(r'<img\b[^>]*>', optimize_img, html, flags=re.IGNORECASE)
    
    # 13. Clean any remaining occurrences of "Sandanska" or Bulgarian river/city names in body copy
    html = html.replace("Sandanska Hillside River", "Sirumalai Mountain Valley")
    html = html.replace("Sandanska Bistritsa River", "Sirumalai Mountain Valley")
    html = html.replace("Sandanska Bistritsa", "Sirumalai Mountain Valley")
    html = html.replace("Sandanska River", "Sirumalai Mountain Valley")
    html = html.replace("www.parkhotelpirin.com", "adeeshymanor.com")
    html = html.replace("parkhotelpirin.com", "adeeshymanor.com")
    html = html.replace("instagram.com/parkhotelpirin", "instagram.com/adeeshymanor")
    html = html.replace("facebook.com/ParkHotelPirin", "facebook.com/adeeshymanor")
    html = html.replace("facebook.com/parkhotelpirin", "facebook.com/adeeshymanor")
    html = html.replace("@parkhotelpirin", "@adeeshymanor")
    html = html.replace("Park Hotel Pirin", "Adeeshy Mountain Manor")
    html = html.replace("Park Hotel “Pirin”", "Adeeshy Mountain Manor")
    html = html.replace('Park Hotel "Pirin"', "Adeeshy Mountain Manor")
    
    if html != original:
        with open(p, 'w', encoding='utf-8') as fp:
            fp.write(html)
        return True, "Updated successfully"
    return False, "No changes needed"

def generate_robots_txt():
    content = f"""# Robots.txt for Adeeshy Mountain Manor
User-agent: *
Allow: /

# AI Crawlers & Answer Engines (GEO & AEO optimization)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot
Allow: /

# Sitemap Index
Sitemap: {DOMAIN}/sitemap.xml
"""
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created robots.txt")

def generate_sitemap(html_files):
    urls = []
    
    for f in html_files:
        norm = f.replace('\\', '/')
        if norm == "index.html":
            loc = f"{DOMAIN}/"
            prio = "1.0"
            freq = "daily"
        else:
            clean_url = norm.replace('index.html', '')
            loc = f"{DOMAIN}/{clean_url}"
            if norm in PAGE_METADATA:
                prio = PAGE_METADATA[norm]["priority"]
                freq = PAGE_METADATA[norm]["changefreq"]
            else:
                prio = "0.7"
                freq = "weekly"
        
        urls.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""")

    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
    print(f"Created sitemap.xml with {len(urls)} URLs")

if __name__ == "__main__":
    html_files = [str(p) for p in Path('en').glob('**/*.html')] + (['index.html'] if Path('index.html').exists() else [])
    html_files.sort()
    
    updated_count = 0
    for f in html_files:
        print(f"Processing {f}...", flush=True)
        changed, msg = process_file(f)
        if changed:
            updated_count += 1
            print(f"[UPDATED] {f}")
        else:
            print(f"[UNCHANGED] {f} - {msg}")
            
    print(f"\nTotal files processed: {len(html_files)}, Updated: {updated_count}")
    
    generate_robots_txt()
    generate_sitemap(html_files)

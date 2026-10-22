# Adeeshy Mountain Manor - Luxury Mountain Resort

A pixel-perfect, fully localized, high-performance website for **Adeeshy Mountain Manor**.

All 70+ pages, luxury typography, interactive animations, mobile navigation drawer, and 560+ high-resolution assets are fully self-contained for standalone execution, zero-dependency hosting, and lightning-fast loading speeds.

---

## 🌟 Key Features

- **100% Fully Self-Contained Assets**: 567 WebP/SVG images, 5 WOFF2 luxury fonts (*PP Right Gothic Wide* and *Manrope*), CSS stylesheets, and JavaScript libraries localized locally into `/assets/`.
- **Refined Luxury Design System**:
  - Consistent Dark Emerald theme (`#082A1A`) and Gold accents (`#C8A27A`).
  - Streamlined 5-item primary navigation: **Amenities**, **Activities**, **Getting Here**, **Local Attractions**, **Contacts**.
  - Fully responsive mobile drawer navigation and compact call-to-action buttons.
  - Subpage header styling with high contrast readability.
- **Dedicated Route Hierarchy**:
  - **Homepage**: `/index.html` & `/en/index.html`
  - **Amenities**: `/en/amenities/`
  - **Activities**: `/en/activities/`
  - **Getting Here**: `/en/getting-here/`
  - **Local Attractions**: `/en/local-attractions/` & `/en/sightseeing/`
  - **Contact & Inquiry**: `/en/contact/`
  - **Accommodation & Suites**: All luxury room and suite pages
  - **Dining & Terraces**: Mediterranean, Balkan, and panoramic lounge bars
- **Modern Animations & Interactions**:
  - GSAP animations and ScrollTrigger effects
  - Swiper carousels for photo galleries, rooms, and testimonials
  - Smooth Lenis inertial scrolling

---

## 📁 Directory Structure

```text
adeesymountainmanor/
├── index.html                   # Root English homepage
├── package.json                 # Node.js launch scripts
├── server.py                    # Zero-dependency Python server with clean URL support
├── README.md                    # Project documentation
│
├── assets/
│   ├── css/
│   │   ├── pirin.webflow.css    # Core responsive layout & styling
│   │   └── swiper-bundle.min.css# Swiper carousel stylesheet
│   ├── fonts/                   # High-res WOFF2 typography files
│   ├── js/                      # Interactive libraries & animations
│   │   ├── jquery.min.js
│   │   ├── gsap.min.js
│   │   ├── ScrollTrigger.min.js
│   │   ├── swiper-bundle.min.js
│   │   ├── lenis.min.js
│   │   └── webflow.js
│   └── images/                  # 567 localized WebP, SVG, and PNG images
│
├── en/                          # Complete site pages
│   ├── amenities/               # Dedicated Manor Amenities page
│   ├── activities/              # Hiking, nature trails & outdoor experiences
│   ├── getting-here/            # Travel directions, mountain transit & maps
│   ├── local-attractions/       # Regional sights, natural landmarks
│   ├── contact/                 # Contact info, inquiry forms & reservations
│   ├── accommodation/           # Suites & rooms
│   └── restaurants-and-bars/    # Dining & bars
│
└── tools/                       # Maintenance & build utilities
```

---

## 🚀 How to Run Locally

### Option 1: Python (Recommended - Zero Dependencies)
Run the included static web server:
```bash
python server.py 3000
```
Then open: **[http://localhost:3000/](http://localhost:3000/)**

### Option 2: Node.js / NPM
```bash
npm start
```
Then open: **[http://localhost:3000/](http://localhost:3000/)**

---

## 🚢 Deployment

Ready for instant deployment to any static hosting provider (GitHub Pages, Vercel, Netlify, Cloudflare Pages, or traditional cPanel / Nginx).

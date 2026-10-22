import os
import re
import shutil
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
IMG_DIR = os.path.join(WORKSPACE, 'assets', 'images')
CSS_FILE = os.path.join(WORKSPACE, 'assets', 'css', 'pirin.webflow.css')

# 1. High-contrast, radiant white & gold Adeeshy Mountain Manor Logo
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 110" width="320" height="110">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E5D1B8" />
      <stop offset="50%" stop-color="#C8A27A" />
      <stop offset="100%" stop-color="#A47E52" />
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>
  <!-- Luxury Monogram Crest -->
  <g transform="translate(160, 22)" stroke="url(#goldGrad)" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" filter="url(#shadow)">
    <path d="M 0,-16 C 14,-16 22,-7 24,0 C 22,7 14,16 0,16 C -14,16 -22,7 -24,0 C -22,-7 -14,-16 0,-16 Z" />
    <path d="M -12,4 L -4,-8 L 0,-2 L 4,-8 L 12,4" />
    <circle cx="0" cy="-10" r="1.5" fill="#C8A27A" stroke="none" />
  </g>
  <!-- Main Name: ADEESHY -->
  <text x="160" y="74" text-anchor="middle" fill="#FFFFFF" font-family="'Cinzel', 'Playfair Display', 'Georgia', serif" font-size="28" font-weight="600" letter-spacing="4" filter="url(#shadow)">ADEESHY</text>
  <!-- Subtitle: MOUNTAIN MANOR -->
  <text x="160" y="98" text-anchor="middle" fill="#C8A27A" font-family="'Manrope', sans-serif" font-size="10.5" font-weight="600" letter-spacing="5" filter="url(#shadow)">MOUNTAIN MANOR</text>
</svg>"""

with open(os.path.join(IMG_DIR, 'adeeshy-mountain-manor-logo.svg'), 'w', encoding='utf-8') as f:
    f.write(logo_svg)

orig_logo_name = '67a4016fe500e14a4d5340d2_a3b61caacd33aaa535f422454da4713e_pirin-logo-full.svg'
with open(os.path.join(IMG_DIR, orig_logo_name), 'w', encoding='utf-8') as f:
    f.write(logo_svg)

print('Updated Adeeshy Mountain Manor SVG logo!')

# 2. Append comprehensive CSS rules to pirin.webflow.css
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove any old custom CSS blocks if re-running
css = re.sub(r'/\* High Contrast Readability Fixes \*/.*', '', css, flags=re.DOTALL)

master_css_rules = """
/* High Contrast Readability Fixes */
.section_layout254,
.background-color-alternative {
  background-color: #082A1A !important;
  color: #FFFFFF !important;
}

.section_layout254 h1,
.section_layout254 h2,
.section_layout254 h3,
.section_layout254 .heading-style-h2,
.background-color-alternative h1,
.background-color-alternative h2,
.background-color-alternative h3,
.background-color-alternative h4 {
  color: #FFFFFF !important;
  text-shadow: 0 1px 3px rgba(0,0,0,0.5) !important;
}

.section_layout254 p,
.background-color-alternative p,
.background-color-alternative .text-size-medium,
.background-color-alternative .text-size-regular {
  color: rgba(255, 255, 255, 0.92) !important;
}

.section_layout254 .heading-style-h4,
.section_layout254 .heading-style-h5,
.section_layout254 .layout254_item h3 {
  color: #E2CCA8 !important;
}

.section_layout254 svg,
.section_layout254 .icon-embed-medium,
.background-color-alternative svg {
  color: #C8A27A !important;
  fill: #C8A27A !important;
}

/* FOOTER FIXES: Crisp white & gold contrast */
.footer3_component {
  background-color: #051A10 !important;
  color: #FFFFFF !important;
}

.footer3_link {
  color: rgba(255, 255, 255, 0.85) !important;
  font-family: 'Manrope', Arial, sans-serif !important;
  font-size: 0.9rem !important;
  transition: color 0.25s ease !important;
}

.footer3_link:hover {
  color: #C8A27A !important;
}

.footer3_details-wrapper .text-size-medium,
.footer3_details-wrapper .text-size-small,
.footer3_details-wrapper .is-bright {
  color: #FFFFFF !important;
}

.footer3_details-wrapper a {
  color: #C8A27A !important;
  text-decoration: none !important;
}

.footer3_details-wrapper a:hover {
  color: #FFFFFF !important;
}

.footer3_social-link svg {
  color: #C8A27A !important;
  fill: #C8A27A !important;
}

.footer3_social-link:hover svg {
  color: #FFFFFF !important;
  fill: #FFFFFF !important;
}

.footer3_legal-list,
.footer3_legal-link {
  color: rgba(255, 255, 255, 0.65) !important;
  font-family: 'Manrope', Arial, sans-serif !important;
  transition: color 0.2s ease !important;
}

.footer3_legal-link:hover {
  color: #C8A27A !important;
}

.footer3_credit-text,
.footer3_credit-text.is-bright {
  color: rgba(255, 255, 255, 0.65) !important;
  font-family: 'Manrope', Arial, sans-serif !important;
}

/* Prevent inverting white logo into black */
.logo-footer,
.logo-nav {
  filter: none !important;
}

/* Hide BG language switcher completely */
.nav-locales-wrapper,
.desktop-locales {
  display: none !important;
  visibility: hidden !important;
  width: 0 !important;
  height: 0 !important;
  overflow: hidden !important;
  pointer-events: none !important;
}

/* Hide promo banner */
.promo-banner {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
  overflow: hidden !important;
}
"""

css += '\n' + master_css_rules
with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated pirin.webflow.css with footer & contrast fixes!')

# 3. Clean & Compact Header with user-requested MANROPE font & NO BG language switcher
CLEAN_HEADER_STYLE = """<style id="desktop-navbar-style">
/* Adeeshy Mountain Manor - Clean, Transparent, Compact Header with Manrope Font */
.desktop-nav-menu {
  display: none;
}

.promo-banner,
.nav-locales-wrapper,
.desktop-locales {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
}

/* Header has NO background by default (transparent over hero) */
.navbar {
  background: transparent !important;
  background-color: transparent !important;
  box-shadow: none !important;
  transition: all 0.35s ease !important;
}

/* Scrolled header gets sleek glass blur */
.navbar.scrolled {
  background: rgba(8, 38, 24, 0.92) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  box-shadow: 0 4px 20px rgba(0,0,0,0.25) !important;
}

@media screen and (min-width: 992px) {
  .nav-menu-button {
    display: none !important;
  }
  
  .nav-wrapper {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 0.65rem 2.5rem !important; /* COMPACT & CLEAN */
    height: auto !important;
    min-height: 56px !important;
  }
  
  .nav-menu-button-wrapper {
    display: none !important;
  }
  
  /* Logo on Left - Crisp White & Gold */
  .nav-logo-link {
    order: 1 !important;
    flex: 0 0 auto !important;
    display: inline-flex !important;
    align-items: center !important;
    padding: 0 !important;
    margin: 0 !important;
    width: auto !important;
    max-width: 175px !important;
  }
  
  .logo-nav {
    max-width: 165px !important;
    max-height: 46px !important;
    width: auto !important;
    height: auto !important;
    object-fit: contain !important;
    filter: none !important; /* Never invert! */
  }
  
  /* Desktop Navigation in Center - RESTORED TO USER-REQUESTED MANROPE FONT */
  .desktop-nav-menu {
    order: 2 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 1.85rem !important;
    flex: 1 1 auto !important;
    margin: 0 2rem !important;
  }
  
  .desktop-nav-link {
    color: #FFFFFF !important;
    font-family: 'Manrope', Arial, sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    padding: 0.35rem 0.15rem !important;
    position: relative !important;
    transition: color 0.25s ease, opacity 0.25s ease !important;
    white-space: nowrap !important;
    display: inline-block !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.5) !important;
  }
  
  .desktop-nav-link:hover {
    color: #C8A27A !important;
    opacity: 1 !important;
  }
  
  .desktop-nav-link::after {
    content: '' !important;
    position: absolute !important;
    bottom: 0 !important;
    left: 0 !important;
    width: 0% !important;
    height: 2px !important;
    background-color: #C8A27A !important;
    transition: width 0.25s cubic-bezier(0.25, 1, 0.5, 1) !important;
  }
  
  .desktop-nav-link:hover::after {
    width: 100% !important;
  }
  
  /* Right Side: CTA Button (NO BG LANGUAGE SWITCHER) */
  .button-group_nav {
    order: 3 !important;
    flex: 0 0 auto !important;
    display: flex !important;
    align-items: center !important;
    gap: 1.25rem !important;
    margin-top: 0 !important;
  }
  
  .button-group_nav .button, .button-group_nav .button.w-button {
    background-color: #C8A27A !important;
    border: 1px solid #C8A27A !important;
    color: #082A1A !important;
    font-family: 'Manrope', Arial, sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    padding: 0.55rem 1.35rem !important;
    border-radius: 6px !important;
    text-transform: uppercase !important;
    box-shadow: 0 3px 10px rgba(0,0,0,0.2) !important;
    transition: all 0.25s ease !important;
  }
  
  .button-group_nav .button:hover, .button-group_nav .button.w-button:hover {
    background-color: #0F5132 !important;
    border-color: #C8A27A !important;
    color: #FFFFFF !important;
  }
}

@media screen and (max-width: 991px) {
  .desktop-nav-menu {
    display: none !important;
  }
  .nav-menu-button {
    display: flex !important;
  }
}
</style>
"""

# Text replacements for footer and branding
TEXT_UPDATES = {
    '© 1999-2026 Sharlopov Group.': '© 2026 Adeeshy Mountain Manor.',
    'Sharlopov Group': 'Adeeshy Mountain Manor',
    'Sharlopov Hotels': 'Adeeshy Mountain Manor',
    'reservations@parkhotelpirin.com': 'reservations@adeeshymountainmanor.com',
    'About Pamporovo': 'About Our Region',
    'SPA center “Pirin”': 'Adeeshy Mountain SPA Sanctuary',
    'SPA center "Pirin"': 'Adeeshy Mountain SPA Sanctuary',
    'SPA center ?Pirin?': 'Adeeshy Mountain SPA Sanctuary',
    'Shyadé Stone Cabin': 'Adeeshy Mountain Manor',
    'Shyadé': 'Adeeshy',
}

html_files = [os.path.join(WORKSPACE, 'index.html')]
for root, dirs, files in os.walk(os.path.join(WORKSPACE, 'en')):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove .desktop-locales and .nav-locales-wrapper HTML if present
    soup = BeautifulSoup(content, 'html.parser')
    for loc in soup.find_all('div', class_=re.compile(r'desktop-locales|nav-locales-wrapper')):
        loc.decompose()
        
    content = str(soup)

    # 2. Text updates
    for old_txt, new_txt in TEXT_UPDATES.items():
        content = content.replace(old_txt, new_txt)

    # 3. Replace style tag with CLEAN_HEADER_STYLE
    if 'id="desktop-navbar-style"' in content:
        content = re.sub(r'<style id="desktop-navbar-style">.*?</style>', CLEAN_HEADER_STYLE, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'{CLEAN_HEADER_STYLE}\n</head>')

    with open(fpath, 'w', encoding='utf-8') as file:
        file.write(content)
    count += 1

print(f'Processed and updated {count} HTML files!')

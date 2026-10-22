import os
import re
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
CSS_FILE = os.path.join(WORKSPACE, 'assets', 'css', 'pirin.webflow.css')

# 1. Update pirin.webflow.css for global contrast
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure .background-color-alternative has white high-contrast text
contrast_css = """
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
}

.section_layout254 p,
.background-color-alternative p,
.background-color-alternative .text-size-medium,
.background-color-alternative .text-size-regular {
  color: rgba(255, 255, 255, 0.92) !important;
}

.section_layout254 h3,
.section_layout254 .heading-style-h4,
.section_layout254 .heading-style-h5 {
  color: #E2CCA8 !important;
}

.section_layout254 svg,
.section_layout254 .icon-embed-medium,
.background-color-alternative svg {
  color: #C8A27A !important;
}
"""

if '/* High Contrast Readability Fixes */' not in css:
    css += '\n' + contrast_css
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(css)
    print('Added high contrast readability fixes to pirin.webflow.css!')

# 2. Compact & Clean Header Style with PP Right Gothic Wide
COMPACT_HEADER_STYLE = """<style id="desktop-navbar-style">
/* Adeeshy Mountain Manor - Compact & Clean Header */
.desktop-nav-menu {
  display: none;
}

.promo-banner {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
}

.navbar {
  transition: all 0.35s ease !important;
  background: linear-gradient(180deg, rgba(8, 38, 24, 0.82) 0%, rgba(8, 38, 24, 0.4) 65%, transparent 100%) !important;
}

.navbar.scrolled {
  background: rgba(8, 38, 24, 0.96) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
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
    padding: 0.55rem 2.5rem !important; /* COMPACT & CLEAN */
    height: auto !important;
    min-height: 56px !important;
  }
  
  .nav-menu-button-wrapper {
    display: none !important;
  }
  
  /* Logo on Left - Crisp White/Gold */
  .nav-logo-link {
    order: 1 !important;
    flex: 0 0 auto !important;
    display: inline-flex !important;
    align-items: center !important;
    padding: 0 !important;
    margin: 0 !important;
    width: auto !important;
    max-width: 165px !important;
  }
  
  .logo-nav {
    max-width: 155px !important;
    max-height: 44px !important;
    width: auto !important;
    height: auto !important;
    object-fit: contain !important;
    filter: none !important;
  }
  
  /* Navigation Menu in Center - Website Font: PP Right Gothic Wide */
  .desktop-nav-menu {
    order: 2 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 1.65rem !important;
    flex: 1 1 auto !important;
    margin: 0 1.5rem !important;
  }
  
  .desktop-nav-link {
    color: #FFFFFF !important;
    font-family: "PP Right Gothic Wide", "PP Right Gothic", sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 400 !important;
    text-decoration: none !important;
    text-transform: uppercase !important;
    letter-spacing: 0.14em !important;
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
    height: 1.5px !important;
    background-color: #C8A27A !important;
    transition: width 0.25s cubic-bezier(0.25, 1, 0.5, 1) !important;
  }
  
  .desktop-nav-link:hover::after {
    width: 100% !important;
  }
  
  /* Right Side: Language & Compact Button */
  .button-group_nav {
    order: 3 !important;
    flex: 0 0 auto !important;
    display: flex !important;
    align-items: center !important;
    gap: 1.15rem !important;
    margin-top: 0 !important;
  }
  
  .desktop-locales .nav-locale {
    color: #FFFFFF !important;
    font-family: 'Manrope', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.4) !important;
  }
  
  .button-group_nav .button, .button-group_nav .button.w-button {
    background-color: #C8A27A !important;
    border: 1px solid #C8A27A !important;
    color: #082A1A !important;
    font-family: "PP Right Gothic Wide", "PP Right Gothic", sans-serif !important;
    font-size: 0.74rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.14em !important;
    padding: 0.45rem 1.15rem !important;
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

# Text replacements across pages
BRAND_REPLACEMENTS = {
    'Shyadé Stone Cabin': 'Adeeshy Mountain Manor',
    'Shyadé': 'Adeeshy',
    'Shyade': 'Adeeshy',
    'Park Hotel Pirin': 'Adeeshy Mountain Manor',
    'Парк Хотел Пирин': 'Adeeshy Mountain Manor',
    'SPA center “Pirin”': 'Adeeshy Mountain SPA Sanctuary',
    'SPA center "Pirin"': 'Adeeshy Mountain SPA Sanctuary',
    'SPA center ?Pirin?': 'Adeeshy Mountain SPA Sanctuary',
    'SPA center Пирин': 'Adeeshy Mountain SPA Sanctuary',
    'Pirin SPA Center': 'Adeeshy Mountain SPA Sanctuary',
    '“Park Hotel Pirin”': 'Adeeshy Mountain Manor',
    '„Park Hotel Pirin“': 'Adeeshy Mountain Manor',
    '?Park Hotel Pirin?': 'Adeeshy Mountain Manor',
    'park hotel pirin': 'Adeeshy Mountain Manor',
}

# Update all HTML files
html_files = [os.path.join(WORKSPACE, 'index.html')]
for root, dirs, files in os.walk(os.path.join(WORKSPACE, 'en')):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

updated_count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update branding text
    for old_str, new_str in BRAND_REPLACEMENTS.items():
        content = content.replace(old_str, new_str)
    
    # 2. Update page title
    content = re.sub(
        r'<title>[^<]*</title>',
        '<title>Adeeshy Mountain Manor – Luxury Mountain Resort &amp; SPA</title>',
        content,
        count=1
    )
    
    # 3. Update desktop navbar style
    if 'id="desktop-navbar-style"' in content:
        content = re.sub(r'<style id="desktop-navbar-style">.*?</style>', COMPACT_HEADER_STYLE, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'{COMPACT_HEADER_STYLE}\n</head>')
        
    with open(fpath, 'w', encoding='utf-8') as file:
        file.write(content)
    updated_count += 1

print(f'Successfully updated {updated_count} HTML files with Adeeshy Mountain Manor branding, compact PP Right Gothic Wide header, and high-contrast readable styling!')

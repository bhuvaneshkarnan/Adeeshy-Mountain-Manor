import os
import re
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
CSS_FILE = os.path.join(WORKSPACE, 'assets', 'css', 'pirin.webflow.css')

print('Step 1: Removing Cookies Consent and Newsletter Popups from all 70 HTML files...')

removed_cookies = 0
removed_newsletter = 0
total_pages = 0

for root, dirs, files in os.walk(WORKSPACE):
    if any(p in root for p in ['.git', 'node_modules', '.gemini', 'tools']):
        continue
    for file in files:
        if file.endswith('.html'):
            total_pages += 1
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read()
            
            orig = content
            
            # Use BeautifulSoup to safely extract the popup nodes
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find and remove cookies consent
            cookie_els = soup.find_all(class_='cookies-consent') + soup.find_all(attrs={'cookies-consent': True})
            for c in cookie_els:
                c.decompose()
                removed_cookies += 1
                
            # Find and remove newsletter pop-up
            news_els = soup.find_all(class_='newsletter-pop-up') + soup.find_all(attrs={'newsletter-pop-up': True})
            for n in news_els:
                n.decompose()
                removed_newsletter += 1
                
            new_html = str(soup)
            if new_html != orig:
                with open(path, 'w', encoding='utf-8') as fp:
                    fp.write(new_html)

print(f'Processed {total_pages} pages.')
print(f'Removed {removed_cookies} cookies consent elements.')
print(f'Removed {removed_newsletter} newsletter popup elements.')

print('\nStep 2: Updating assets/css/pirin.webflow.css with pixel-perfect mobile header...')

# Read current css
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    current_css = f.read()

# Define the flawless mobile CSS block
perfect_mobile_css = """
/* ==========================================================================
   ADEESHY MOUNTAIN MANOR - FLAWLESS MOBILE HEADER & POPUP REMOVAL
   ========================================================================== */

/* 1. Complete Suppression of Cookie Screen & Marketing Popups */
.cookies-consent,
.cookies-consent_wrapper,
.cookies-consent_buttons,
.newsletter-pop-up,
.newsletter-wrapper,
.newsletter-container,
[cookies-consent],
[newsletter-pop-up] {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
  height: 0 !important;
  width: 0 !important;
  max-height: 0 !important;
  max-width: 0 !important;
  overflow: hidden !important;
  position: absolute !important;
  top: -9999px !important;
  left: -9999px !important;
}

/* 2. Global Viewport & Overflow Safety */
html,
body {
  overflow-x: hidden !important;
  max-width: 100vw !important;
  width: 100% !important;
  -webkit-text-size-adjust: 100% !important;
  touch-action: manipulation;
}

.page-wrapper,
.main-wrapper {
  overflow-x: hidden !important;
  width: 100% !important;
  max-width: 100% !important;
}

.w-layout-grid > * {
  min-width: 0 !important;
  max-width: 100% !important;
}

a, p, span, h1, h2, h3, h4, h5, h6, .text-size-regular, .text-size-medium, .text-size-small {
  overflow-wrap: break-word !important;
  word-wrap: break-word !important;
}

.contact16_item.is-padded {
  padding: 1.25rem 1rem !important;
  word-break: break-word !important;
}

.contact16_item a,
.contact16_item-text-wrapper a {
  word-break: break-all !important;
}

img, video, iframe, embed, object, .tally-form, .tally-form iframe {
  max-width: 100% !important;
  box-sizing: border-box !important;
}

/* 3. Guaranteed Visibility of Page Content */
section,
.section_header30,
.section_header64,
.section_header127,
.header127_component,
.header127_content,
.section_layout254,
.section_product11,
.product11_component,
.section_gallery14,
.section_testimonial17,
.section_faq5,
.button-group,
.button,
.button.w-button,
a.button,
[data-scroll-scrub],
[scroll-reveal],
[data-animate] {
  opacity: 1 !important;
  visibility: visible !important;
}

.section_header30 .button-group a,
.section_header30 .button-group .button {
  transform: none !important;
  opacity: 1 !important;
  visibility: visible !important;
}

/* 4. PIXEL-PERFECT MOBILE HEADER BAR (<= 991px) */
@media screen and (max-width: 991px) {
  .navbar {
    height: 64px !important;
    min-height: 64px !important;
    max-height: 64px !important;
    padding: 0 !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    z-index: 1000 !important;
    box-sizing: border-box !important;
    background: transparent !important;
    box-shadow: none !important;
    border-bottom: none !important;
  }

  body.is-subpage .navbar,
  body:not(.is-home) .navbar {
    position: relative !important;
    background: #082A1A !important;
    background-color: #082A1A !important;
    border-bottom: 1px solid rgba(200, 162, 122, 0.25) !important;
  }

  .navbar[menu-open-mobile],
  .navbar[menu-open],
  .navbar.menu-is-open {
    background: #082A1A !important;
    background-color: #082A1A !important;
  }

  .nav-container {
    width: 100% !important;
    max-width: 100% !important;
    height: 100% !important;
    min-height: 64px !important;
    padding: 0 16px !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center !important;
    box-sizing: border-box !important;
  }

  .nav-wrapper {
    width: 100% !important;
    height: 100% !important;
    min-height: 64px !important;
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 0 !important;
    margin: 0 !important;
    position: relative !important;
    box-sizing: border-box !important;
  }

  /* 1. Left: Hamburger Toggle */
  .nav-menu-button-wrapper {
    order: 1 !important;
    flex: 0 0 44px !important;
    width: 44px !important;
    height: 44px !important;
    margin: 0 !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    align-self: center !important;
    position: relative !important;
    z-index: 1005 !important;
    transform: none !important;
    opacity: 1 !important;
    visibility: visible !important;
  }

  .nav-menu-button {
    width: 40px !important;
    height: 40px !important;
    margin: 0 !important;
    padding: 8px 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    align-self: center !important;
    cursor: pointer !important;
    background: transparent !important;
    border: none !important;
  }

  .nav-menu-icon {
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    width: 24px !important;
    height: 16px !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  .nav-menu-line {
    width: 100% !important;
    height: 2px !important;
    background-color: #C8A27A !important;
    border-radius: 2px !important;
    margin: 0 !important;
  }

  .nav-menu-text {
    display: none !important;
  }

  /* 2. Center: Logo - Vertically & Horizontally Centered in 64px Bar */
  .nav-logo-link {
    order: 2 !important;
    position: absolute !important;
    left: 50% !important;
    top: 50% !important;
    transform: translate(-50%, -50%) !important;
    margin: 0 !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    max-width: 135px !important;
    height: 38px !important;
    z-index: 1005 !important;
  }

  .logo-nav {
    max-width: 125px !important;
    max-height: 36px !important;
    width: auto !important;
    height: auto !important;
    object-fit: contain !important;
    display: block !important;
    margin: 0 auto !important;
  }

  /* 3. Right: Button Group with Sleek Gold BOOK NOW Button */
  .button-group_nav {
    order: 3 !important;
    flex: 0 0 auto !important;
    width: auto !important;
    max-width: none !important;
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: flex-end !important;
    align-self: center !important;
    margin: 0 !important;
    padding: 0 !important;
    gap: 8px !important;
    position: relative !important;
    z-index: 1005 !important;
    transform: none !important;
    opacity: 1 !important;
    visibility: visible !important;
  }

  /* Remove the awkward cut-off phone circle */
  .button_icon {
    display: none !important;
  }

  /* Sleek, prominent, luxury BOOK NOW button */
  .button-group_nav .button,
  .button-group_nav .button.is-desktop,
  .button-group_nav a.button,
  .button-group_nav .button.w-button {
    display: inline-flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    align-items: center !important;
    justify-content: center !important;
    background-color: #C8A27A !important;
    border: 1px solid #C8A27A !important;
    color: #082A1A !important;
    font-family: 'Manrope', Arial, sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    padding: 0 1rem !important;
    height: 36px !important;
    min-height: 36px !important;
    max-height: 36px !important;
    width: auto !important;
    max-width: none !important;
    min-width: 0 !important;
    border-radius: 4px !important;
    white-space: nowrap !important;
    align-self: center !important;
    box-shadow: 0 3px 10px rgba(0,0,0,0.3) !important;
    margin: 0 !important;
    text-decoration: none !important;
    box-sizing: border-box !important;
  }

  .button-group_nav .button:active {
    background-color: #B58F66 !important;
    transform: scale(0.98) !important;
  }

  /* 4. Full-Screen Drawer Menu */
  .nav-menu {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100vh !important;
    height: 100dvh !important;
    background-color: #082A1A !important;
    z-index: 1000 !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }

  .nav-menu-wrapper {
    min-height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    background-color: #082A1A !important;
  }

  .nav-main {
    background-color: #082A1A !important;
    padding-top: 5.5rem !important;
    padding-bottom: 2.5rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    min-height: 100% !important;
    box-sizing: border-box !important;
  }

  .nav-links-wrapper {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.5rem !important;
    margin-top: 0.5rem !important;
    margin-bottom: 2rem !important;
  }

  .nav-link {
    font-family: 'PP Right Gothic Wide', 'Manrope', Arial, sans-serif !important;
    font-size: 1.35rem !important;
    line-height: 1.3 !important;
    font-weight: 500 !important;
    color: #FFFFFF !important;
    text-decoration: none !important;
    padding: 0.75rem 0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    display: flex !important;
    align-items: center !important;
    min-height: 48px !important;
    transition: all 0.2s ease !important;
  }

  .nav-link:hover,
  .nav-link:active,
  .nav-link.w--current {
    color: #C8A27A !important;
    padding-left: 0.5rem !important;
  }

  .nav-menu-footer {
    display: flex !important;
    flex-direction: column !important;
    gap: 1rem !important;
    margin-top: auto !important;
    padding-top: 1rem !important;
  }

  .button.is-mobile,
  .nav-menu-footer .button {
    display: flex !important;
    width: 100% !important;
    padding: 0.95rem 1.5rem !important;
    font-family: 'Manrope', Arial, sans-serif !important;
    font-size: 0.92rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    text-align: center !important;
    align-items: center !important;
    justify-content: center !important;
    border-radius: 6px !important;
    background-color: #C8A27A !important;
    border: 1px solid #C8A27A !important;
    color: #082A1A !important;
    min-height: 50px !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
  }

  .nav-secondary,
  .locales-wrapper {
    display: none !important;
  }
}

/* 5. Fluid Responsive Headings & Section Spacing (<= 767px) */
@media screen and (max-width: 767px) {
  h1, .heading-style-h1 {
    font-size: clamp(2rem, 7.5vw, 3rem) !important;
    line-height: 1.15 !important;
  }

  h2, .heading-style-h2 {
    font-size: clamp(1.6rem, 6vw, 2.4rem) !important;
    line-height: 1.2 !important;
  }

  h3, .heading-style-h3 {
    font-size: clamp(1.3rem, 5vw, 1.85rem) !important;
    line-height: 1.25 !important;
  }

  .padding-section-large {
    padding-top: 3.5rem !important;
    padding-bottom: 3.5rem !important;
  }

  .padding-section-medium {
    padding-top: 2.5rem !important;
    padding-bottom: 2.5rem !important;
  }

  .padding-global {
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
  }

  .button-group {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    gap: 0.75rem !important;
  }

  .button-group .button,
  .button-group .button.w-button {
    width: 100% !important;
    min-height: 48px !important;
    text-align: center !important;
    justify-content: center !important;
  }

  /* 6. Footer Layout on Mobile */
  .footer3_component {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    background-color: #062014 !important;
  }

  .footer3_top-wrapper {
    grid-template-columns: 1fr !important;
    gap: 2rem !important;
  }

  .footer3_menu-wrapper {
    grid-template-columns: 1fr 1fr !important;
    gap: 1.5rem !important;
  }

  .footer3_link {
    display: inline-flex !important;
    align-items: center !important;
    min-height: 38px !important;
    padding: 0.25rem 0 !important;
    font-size: 0.92rem !important;
    color: rgba(255, 255, 255, 0.85) !important;
    transition: color 0.2s ease !important;
  }

  .footer3_link:hover,
  .footer3_link:active {
    color: #C8A27A !important;
  }

  .footer3_social-list {
    display: flex !important;
    gap: 1rem !important;
  }

  .footer3_social-link {
    width: 44px !important;
    height: 44px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    background: rgba(200, 162, 122, 0.12) !important;
    border-radius: 50% !important;
    color: #C8A27A !important;
  }

  .footer3_bottom-wrapper {
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    gap: 1.25rem !important;
    padding-top: 1.5rem !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
  }

  .footer3_credit-text {
    font-size: 0.82rem !important;
    color: rgba(255, 255, 255, 0.6) !important;
  }

  .footer3_logo-link.master {
    display: none !important;
  }

  .back-to-top {
    position: fixed !important;
    bottom: 1.25rem !important;
    right: 1.25rem !important;
    width: 44px !important;
    height: 44px !important;
    z-index: 99 !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
  }
}
"""

# Replace existing custom mobile block or append
marker = '/* ==========================================================================\n   ADEESHY MOUNTAIN MANOR - COMPREHENSIVE MOBILE OPTIMIZATION'
idx = current_css.find(marker)
if idx != -1:
    new_css = current_css[:idx] + perfect_mobile_css.strip() + '\n'
else:
    new_css = current_css + '\n' + perfect_mobile_css.strip() + '\n'

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(new_css)

print('Updated pirin.webflow.css with pixel-perfect mobile header & popup removal.')

import os
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
ARTIFACT_DIR = r'C:\Users\bhuva\.gemini\antigravity\brain\15e53f08-6a83-4c12-a200-a1a3d73e0ee1'

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:3000/', wait_until='networkidle')
    time.sleep(2)

    # 1. Capture Header Closeup
    p_header = os.path.join(ARTIFACT_DIR, 'preview_clean_header_manrope.png')
    page.screenshot(path=p_header, clip={'x': 0, 'y': 0, 'width': 1440, 'height': 110})
    print('Saved preview_clean_header_manrope.png')

    # 2. Capture Footer
    page.evaluate('document.querySelector("footer").scrollIntoView()')
    time.sleep(1)
    p_footer = os.path.join(ARTIFACT_DIR, 'preview_fixed_footer.png')
    page.screenshot(path=p_footer)
    print('Saved preview_fixed_footer.png')

    # Inspect computed styles of header links and footer links
    data = page.evaluate('''() => {
        const headerLink = document.querySelector('.desktop-nav-link');
        const footerLink = document.querySelector('.footer3_link');
        const bgExists = document.querySelector('.nav-locales-wrapper, .desktop-locales');
        const footerLogo = document.querySelector('.logo-footer');
        return {
            header_font: headerLink ? window.getComputedStyle(headerLink).fontFamily : null,
            header_color: headerLink ? window.getComputedStyle(headerLink).color : null,
            footer_color: footerLink ? window.getComputedStyle(footerLink).color : null,
            footer_font: footerLink ? window.getComputedStyle(footerLink).fontFamily : null,
            bg_locale_in_dom: !!bgExists,
            footer_logo_filter: footerLogo ? window.getComputedStyle(footerLogo).filter : null
        };
    }''')
    print('Computed Verification Data:', data)

    browser.close()

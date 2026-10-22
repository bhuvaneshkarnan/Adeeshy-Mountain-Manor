import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
ARTIFACT_DIR = r'C:\Users\bhuva\.gemini\antigravity\brain\15e53f08-6a83-4c12-a200-a1a3d73e0ee1'

# Clean and minimal compact button styles
clean_button_css = """
<style id="minimal-compact-buttons">
/* Clean & Minimal Compact Buttons */
.button, 
.button.w-button {
  font-family: 'Manrope', Arial, sans-serif !important;
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  padding: 0.45rem 1.15rem !important; /* COMPACT */
  border-radius: 4px !important;       /* MINIMAL */
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  line-height: 1.25 !important;
  transition: all 0.25s cubic-bezier(0.25, 1, 0.5, 1) !important;
  box-shadow: none !important;
  text-decoration: none !important;
  cursor: pointer !important;
}

/* Primary Button (e.g. Book Now) */
.button:not(.is-secondary):not(.is-link):not(.is-tertiary),
.button.is-alternate:not(.is-secondary),
.button-group_nav .button {
  background-color: #C8A27A !important;
  border: 1px solid #C8A27A !important;
  color: #082A1A !important;
}

.button:not(.is-secondary):not(.is-link):not(.is-tertiary):hover,
.button.is-alternate:not(.is-secondary):hover,
.button-group_nav .button:hover {
  background-color: #0F5132 !important;
  border-color: #0F5132 !important;
  color: #FFFFFF !important;
}

/* Secondary / Outline Minimal Button (e.g. Check Out The Rooms) */
.button.is-secondary,
.button.is-secondary.is-alternate {
  background-color: transparent !important;
  border: 1px solid rgba(255, 255, 255, 0.75) !important;
  color: #FFFFFF !important;
  backdrop-filter: blur(4px) !important;
}

.button.is-secondary:hover,
.button.is-secondary.is-alternate:hover {
  background-color: #C8A27A !important;
  border-color: #C8A27A !important;
  color: #082A1A !important;
}

/* On light sections, secondary button has dark emerald border */
.background-color-secondary .button.is-secondary,
.section_header127 .button.is-secondary {
  border: 1px solid #0F5132 !important;
  color: #0F5132 !important;
}

.background-color-secondary .button.is-secondary:hover,
.section_header127 .button.is-secondary:hover {
  background-color: #0F5132 !important;
  color: #FFFFFF !important;
}

/* Small Buttons (newsletter, cookies, etc.) */
.button.is-small {
  padding: 0.35rem 0.95rem !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.08em !important;
}

/* Button Group spacing */
.button-group {
  gap: 0.85rem !important;
}
</style>
"""

with open(os.path.join(WORKSPACE, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

if 'id="minimal-compact-buttons"' in html:
    html = re.sub(r'<style id="minimal-compact-buttons">.*?</style>', clean_button_css, html, flags=re.DOTALL)
else:
    html = html.replace('</head>', f'{clean_button_css}\n</head>')

with open(os.path.join(WORKSPACE, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print('Applied minimal compact buttons to index.html! Capturing screenshot...')

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:3000/', wait_until='networkidle')
    time.sleep(2)
    
    # Capture the two hero buttons closeup
    btn_group = page.locator('.section_header30 .button-group').bounding_box()
    print('Hero buttons box:', btn_group)
    if btn_group:
        p_clip = os.path.join(ARTIFACT_DIR, 'preview_clean_compact_buttons.png')
        page.screenshot(path=p_clip, clip={
            'x': max(0, btn_group['x'] - 40),
            'y': max(0, btn_group['y'] - 30),
            'width': min(1440, btn_group['width'] + 80),
            'height': btn_group['height'] + 60
        })
        print('Saved preview_clean_compact_buttons.png')
    
    # Also capture full hero with new buttons
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'preview_hero_with_clean_buttons.png'))
    print('Saved preview_hero_with_clean_buttons.png')

    browser.close()

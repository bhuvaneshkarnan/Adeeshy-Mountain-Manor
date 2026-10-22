import os
import re
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
ARTIFACT_DIR = r'C:\Users\bhuva\.gemini\antigravity\brain\15e53f08-6a83-4c12-a200-a1a3d73e0ee1'
CSS_FILE = os.path.join(WORKSPACE, 'assets', 'css', 'pirin.webflow.css')

# Well-proportioned, confident, clean and minimal luxury buttons
updated_button_rules = """
/* Clean & Minimal Luxury Buttons - Perfectly Proportioned */
.button, 
.button.w-button {
  font-family: 'Manrope', Arial, sans-serif !important;
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  padding: 0.82rem 2.1rem !important;   /* CONFIDENT, WELL-PROPORTIONED */
  border-radius: 4px !important;        /* CLEAN MINIMAL CORNERS */
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  line-height: 1.3 !important;
  transition: all 0.25s cubic-bezier(0.25, 1, 0.5, 1) !important;
  box-shadow: none !important;
  text-decoration: none !important;
  cursor: pointer !important;
  min-height: 48px !important;
}

/* Primary Solid Button (e.g. Book Now) */
.button:not(.is-secondary):not(.is-link):not(.is-tertiary),
.button.is-alternate:not(.is-secondary) {
  background-color: #C8A27A !important;
  border: 1.5px solid #C8A27A !important;
  color: #082A1A !important;
}

.button:not(.is-secondary):not(.is-link):not(.is-tertiary):hover,
.button.is-alternate:not(.is-secondary):hover {
  background-color: #0F5132 !important;
  border-color: #C8A27A !important;
  color: #FFFFFF !important;
}

/* Header Book Now Button (proportional to header) */
.button-group_nav .button,
.button-group_nav .button.w-button {
  padding: 0.55rem 1.45rem !important;
  min-height: 40px !important;
  font-size: 0.82rem !important;
  background-color: #C8A27A !important;
  border: 1.5px solid #C8A27A !important;
  color: #082A1A !important;
}

.button-group_nav .button:hover,
.button-group_nav .button.w-button:hover {
  background-color: #0F5132 !important;
  border-color: #C8A27A !important;
  color: #FFFFFF !important;
}

/* Secondary / Outline Ghost Button (e.g. Check Out The Rooms) */
.button.is-secondary,
.button.is-secondary.is-alternate {
  background-color: rgba(255, 255, 255, 0.05) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
  color: #FFFFFF !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
}

.button.is-secondary:hover,
.button.is-secondary.is-alternate:hover {
  background-color: #C8A27A !important;
  border-color: #C8A27A !important;
  color: #082A1A !important;
}

/* On light sections, secondary button has dark emerald border */
.background-color-secondary .button.is-secondary,
.section_header127 .button.is-secondary,
.section_product11 .button.is-secondary {
  background-color: transparent !important;
  border: 1.5px solid #0F5132 !important;
  color: #0F5132 !important;
}

.background-color-secondary .button.is-secondary:hover,
.section_header127 .button.is-secondary:hover,
.section_product11 .button.is-secondary:hover {
  background-color: #0F5132 !important;
  border-color: #0F5132 !important;
  color: #FFFFFF !important;
}

/* Small Buttons (newsletter, cookies, etc.) */
.button.is-small {
  padding: 0.5rem 1.25rem !important;
  min-height: 38px !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.08em !important;
}

/* Button Group spacing */
.button-group {
  gap: 1.15rem !important;
}
"""

# Update pirin.webflow.css
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'/\* Clean & Minimal Compact Buttons \*/.*', '', css, flags=re.DOTALL)
css = re.sub(r'/\* Clean & Minimal Luxury Buttons - Perfectly Proportioned \*/.*', '', css, flags=re.DOTALL)
css += '\n' + updated_button_rules

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# Update all HTML files
html_files = [os.path.join(WORKSPACE, 'index.html')]
for root, dirs, files in os.walk(os.path.join(WORKSPACE, 'en')):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

STYLE_TAG = f"<style id='minimal-compact-buttons'>{updated_button_rules}</style>"

count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="minimal-compact-buttons"' in content or "id='minimal-compact-buttons'" in content:
        content = re.sub(r'<style id=[\'"]minimal-compact-buttons[\'"]>.*?</style>', STYLE_TAG, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'{STYLE_TAG}\n</head>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1

print(f'Applied updated well-proportioned buttons to {count} HTML files!')

# Capture screenshot with Playwright
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
        p_clip = os.path.join(ARTIFACT_DIR, 'preview_buttons_well_proportioned.png')
        page.screenshot(path=p_clip, clip={
            'x': max(0, btn_group['x'] - 30),
            'y': max(0, btn_group['y'] - 60),
            'width': min(1440, btn_group['width'] + 60),
            'height': btn_group['height'] + 80
        })
        print('Saved preview_buttons_well_proportioned.png')

    # Full hero screenshot
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'preview_hero_proportioned.png'))
    print('Saved preview_hero_proportioned.png')

    browser.close()

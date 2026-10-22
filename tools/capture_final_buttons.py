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

    # Capture the two hero buttons closeup
    btn_group = page.locator('.section_header30 .button-group').bounding_box()
    if btn_group:
        p_clip = os.path.join(ARTIFACT_DIR, 'preview_clean_compact_buttons.png')
        page.screenshot(path=p_clip, clip={
            'x': max(0, btn_group['x'] - 20),
            'y': max(0, btn_group['y'] - 20),
            'width': min(1440, btn_group['width'] + 40),
            'height': btn_group['height'] + 40
        })
        print('Saved preview_clean_compact_buttons.png')

    # Full hero screenshot
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'preview_clean_hero_complete.png'))
    print('Saved preview_clean_hero_complete.png')

    browser.close()

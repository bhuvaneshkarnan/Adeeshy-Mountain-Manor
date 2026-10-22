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
    
    # 1. Capture Header closeup
    header_box = page.locator('.navbar').bounding_box()
    print('Header bounding box:', header_box)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'preview_adeeshy_header.png'), clip={
        'x': 0, 'y': 0, 'width': 1440, 'height': 120
    })
    print('Saved preview_adeeshy_header.png')

    # 2. Capture Full Hero & Header
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'preview_adeeshy_hero.png'))
    print('Saved preview_adeeshy_hero.png')

    # 3. Capture SPA Section (Image 1 fix verification)
    page.evaluate('document.querySelector(".section_layout254").scrollIntoView()')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'preview_adeeshy_spa_readable.png'))
    print('Saved preview_adeeshy_spa_readable.png')

    # 4. Scrolled Header
    page.evaluate('window.scrollTo(0, 700)')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'preview_adeeshy_scrolled.png'))
    print('Saved preview_adeeshy_scrolled.png')

    browser.close()

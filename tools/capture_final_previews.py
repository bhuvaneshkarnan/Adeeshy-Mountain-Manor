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
    
    # 1. Desktop 1440px
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:3000/', wait_until='networkidle')
    time.sleep(2)
    p1 = os.path.join(ARTIFACT_DIR, 'preview_pc_menu_1440.png')
    page.screenshot(path=p1)
    print('Saved preview_pc_menu_1440.png')

    # 2. Laptop 1200px
    page.set_viewport_size({'width': 1200, 'height': 900})
    time.sleep(1)
    p2 = os.path.join(ARTIFACT_DIR, 'preview_pc_menu_1200.png')
    page.screenshot(path=p2)
    print('Saved preview_pc_menu_1200.png')

    # 3. Accommodation Page 1440px
    page.set_viewport_size({'width': 1440, 'height': 900})
    page.goto('http://localhost:3000/en/accommodation/', wait_until='networkidle')
    time.sleep(2)
    p3 = os.path.join(ARTIFACT_DIR, 'preview_pc_accommodation.png')
    page.screenshot(path=p3)
    print('Saved preview_pc_accommodation.png')

    # 4. Mobile 768px (verifying hamburger menu is still there on mobile)
    page.set_viewport_size({'width': 768, 'height': 900})
    time.sleep(1)
    p4 = os.path.join(ARTIFACT_DIR, 'preview_mobile_hamburger.png')
    page.screenshot(path=p4)
    print('Saved preview_mobile_hamburger.png')

    browser.close()

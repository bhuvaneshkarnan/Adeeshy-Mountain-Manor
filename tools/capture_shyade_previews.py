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
    p_home = os.path.join(ARTIFACT_DIR, 'preview_shyade_home.png')
    page.screenshot(path=p_home)
    print('Home screenshot saved, size:', os.path.getsize(p_home))

    # Also capture scrolled view to see emerald green & gold button and navbar
    page.evaluate('window.scrollTo(0, 800)')
    time.sleep(1)
    p_scrolled = os.path.join(ARTIFACT_DIR, 'preview_shyade_scrolled.png')
    page.screenshot(path=p_scrolled)
    print('Scrolled screenshot saved, size:', os.path.getsize(p_scrolled))

    # Capture rooms section
    page.evaluate('document.querySelector(".section_product11").scrollIntoView()')
    time.sleep(1)
    p_rooms = os.path.join(ARTIFACT_DIR, 'preview_shyade_rooms.png')
    page.screenshot(path=p_rooms)
    print('Rooms screenshot saved, size:', os.path.getsize(p_rooms))

    browser.close()

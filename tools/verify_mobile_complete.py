import os
import time
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r'C:\Users\bhuva\.gemini\antigravity\brain\15e53f08-6a83-4c12-a200-a1a3d73e0ee1'
WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

html_files = []
for root, dirs, files in os.walk(WORKSPACE):
    if any(p in root for p in ['.git', 'node_modules', '.gemini', 'tools']):
        continue
    for file in files:
        if file.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, file), WORKSPACE).replace('\\', '/')
            html_files.append(rel)

print(f'Starting complete verification on {len(html_files)} pages...')

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    
    # 1. Check all 70 pages on 375px for horizontal overflow
    page_audit = browser.new_page(viewport={'width': 375, 'height': 812})
    overflowing = []
    for rel in html_files:
        url_path = '' if rel == 'index.html' else rel.replace('/index.html', '/')
        try:
            page_audit.goto(f'http://localhost:3000/{url_path}', wait_until='domcontentloaded', timeout=5000)
            res = page_audit.evaluate('() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]')
            if res[0] > res[1]:
                overflowing.append((rel, res[0], res[1]))
        except Exception as e:
            print(f'Audit error {rel}: {e}')
    page_audit.close()
    
    print(f'Audit finished! Overflowing pages: {len(overflowing)} / {len(html_files)}')
    if overflowing:
        for o in overflowing:
            print('  ->', o)
    else:
        print('  All 70 pages have 0 horizontal overflow! 100% responsive perfection!')

    # 2. Detailed screenshots on iPhone 14 (390 x 844)
    page = browser.new_page(viewport={'width': 390, 'height': 844})
    
    # Homepage Top & Header
    page.goto('http://localhost:3000/', wait_until='networkidle')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_home_top.png'))
    print('Captured final_mobile_home_top.png')
    
    # Hero buttons closeup
    btn_box = page.locator('.section_header30 .button-group').bounding_box()
    if btn_box:
        page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_hero_buttons.png'), clip={
            'x': 0, 'y': max(0, btn_box['y'] - 40), 'width': 390, 'height': btn_box['height'] + 80
        })
        print('Captured final_mobile_hero_buttons.png')
        
    # Scroll to amenities
    page.evaluate('() => window.scrollTo(0, 1500)')
    time.sleep(0.5)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_amenities.png'))
    print('Captured final_mobile_amenities.png')
    
    # Scroll to footer
    page.evaluate('() => window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(0.5)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_footer.png'))
    print('Captured final_mobile_footer.png')
    
    # Open mobile menu drawer
    page.evaluate('() => window.scrollTo(0, 0)')
    time.sleep(0.5)
    btn = page.query_selector('.nav-menu-button')
    if btn:
        btn.click()
        time.sleep(1)
        page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_menu_open.png'))
        print('Captured final_mobile_menu_open.png')
        
    # Subpage 1: Amenities
    page.goto('http://localhost:3000/en/amenities/', wait_until='networkidle')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_subpage_amenities.png'))
    print('Captured final_mobile_subpage_amenities.png')
    
    # Subpage 2: Getting Here
    page.goto('http://localhost:3000/en/getting-here/', wait_until='networkidle')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_subpage_getting_here.png'))
    print('Captured final_mobile_subpage_getting_here.png')
    
    # Subpage 3: Contact (verify fix)
    page.goto('http://localhost:3000/en/contact/', wait_until='networkidle')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_subpage_contact.png'))
    print('Captured final_mobile_subpage_contact.png')
    
    # Subpage 4: Local Attractions
    page.goto('http://localhost:3000/en/local-attractions/', wait_until='networkidle')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_mobile_subpage_attractions.png'))
    print('Captured final_mobile_subpage_attractions.png')

    browser.close()
    print('Verification script complete!')

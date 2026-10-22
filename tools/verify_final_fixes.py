import os
import time
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r'C:\Users\bhuva\.gemini\antigravity\brain\15e53f08-6a83-4c12-a200-a1a3d73e0ee1'

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    
    # 1. Test iPhone 14 (390 x 844)
    page = browser.new_page(viewport={'width': 390, 'height': 844})
    page.goto('http://localhost:3000/', wait_until='networkidle')
    time.sleep(1)
    
    # Header close up
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_header_iphone14.png'), clip={
        'x': 0, 'y': 0, 'width': 390, 'height': 80
    })
    print('final_header_iphone14.png captured')
    
    # Full hero view
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_home_top_iphone14.png'))
    print('final_home_top_iphone14.png captured')
    
    # Measure vertical center Y alignment
    alignments = page.evaluate('''() => {
        const getB = sel => {
            const el = document.querySelector(sel);
            if (!el) return null;
            const r = el.getBoundingClientRect();
            return {
                x: Math.round(r.x),
                y: Math.round(r.y),
                w: Math.round(r.width),
                h: Math.round(r.height),
                cy: Math.round(r.y + r.height / 2)
            };
        };
        return {
            bar: getB('.nav-wrapper'),
            hamburger: getB('.nav-menu-button'),
            logo: getB('.nav-logo-link'),
            bookNow: getB('.button-group_nav .button')
        };
    }''')
    print('iPhone 14 Alignments (cy should match):', alignments)
    
    # Check if cookies consent or newsletter is in DOM or visible
    popups = page.evaluate('''() => {
        const cookies = document.querySelector('.cookies-consent, [cookies-consent]');
        const news = document.querySelector('.newsletter-pop-up, [newsletter-pop-up]');
        return {
            cookiesInDOM: !!cookies,
            newsInDOM: !!news
        };
    }''')
    print('Popups check:', popups)
    
    # Open Mobile Drawer
    page.click('.nav-menu-button')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_drawer_open_iphone14.png'))
    print('final_drawer_open_iphone14.png captured')
    
    # 2. Test Subpage Amenities (Dark Emerald Bar)
    page.goto('http://localhost:3000/en/amenities/', wait_until='networkidle')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_subpage_amenities_iphone14.png'), clip={
        'x': 0, 'y': 0, 'width': 390, 'height': 80
    })
    print('final_subpage_amenities_iphone14.png captured')
    
    # 3. Test Subpage Contact (Verify form & zero popup)
    page.goto('http://localhost:3000/en/contact/', wait_until='networkidle')
    time.sleep(1)
    page.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_subpage_contact_iphone14.png'))
    print('final_subpage_contact_iphone14.png captured')
    
    # 4. Test iPhone SE (375 x 667)
    page_se = browser.new_page(viewport={'width': 375, 'height': 667})
    page_se.goto('http://localhost:3000/', wait_until='networkidle')
    time.sleep(1)
    page_se.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_header_iphoneSE.png'), clip={
        'x': 0, 'y': 0, 'width': 375, 'height': 80
    })
    print('final_header_iphoneSE.png captured')
    
    # 5. Test Android (360 x 800)
    page_android = browser.new_page(viewport={'width': 360, 'height': 800})
    page_android.goto('http://localhost:3000/', wait_until='networkidle')
    time.sleep(1)
    page_android.screenshot(path=os.path.join(ARTIFACT_DIR, 'final_header_android360.png'), clip={
        'x': 0, 'y': 0, 'width': 360, 'height': 80
    })
    print('final_header_android360.png captured')

    browser.close()
    print('All checks successfully captured!')

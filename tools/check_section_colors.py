from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:3000/', wait_until='networkidle')
    data = page.evaluate('''() => {
        const sec = document.querySelector('.section_layout254');
        const h2 = sec ? sec.querySelector('h2') : null;
        const p = sec ? sec.querySelector('p') : null;
        return {
            sec_bg: sec ? window.getComputedStyle(sec).backgroundColor : null,
            body_bg: window.getComputedStyle(document.body).backgroundColor,
            h2_color: h2 ? window.getComputedStyle(h2).color : null,
            p_color: p ? window.getComputedStyle(p).color : null
        };
    }''')
    print('Computed styles:', data)
    browser.close()

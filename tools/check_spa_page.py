from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:3000/en/spa-center/', wait_until='networkidle')
    data = page.evaluate('''() => {
        const sections = Array.from(document.querySelectorAll('section, header, div[class*="section"]')).map(s => ({
            tag: s.tagName,
            cls: s.className,
            bg: window.getComputedStyle(s).backgroundColor,
            color: window.getComputedStyle(s).color,
            h: s.querySelector('h1, h2, h3') ? s.querySelector('h1, h2, h3').innerText : null,
            h_color: s.querySelector('h1, h2, h3') ? window.getComputedStyle(s.querySelector('h1, h2, h3')).color : null
        }));
        return sections;
    }''')
    for s in data:
        if s['h']:
            print(f"H: {s['h']} | BG: {s['bg']} | H_Color: {s['h_color']}")
    browser.close()

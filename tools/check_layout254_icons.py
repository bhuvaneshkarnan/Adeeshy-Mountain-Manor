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
        if (!sec) return 'sec not found';
        const imgs = Array.from(sec.querySelectorAll('.layout254_item img, .icon-1x1-medium')).map((img, i) => {
            const rect = img.getBoundingClientRect();
            const cs = window.getComputedStyle(img);
            return {
                index: i,
                src: img.src,
                w: rect.width,
                h: rect.height,
                x: rect.x,
                y: rect.y,
                display: cs.display,
                visibility: cs.visibility,
                opacity: cs.opacity,
                filter: cs.filter,
                naturalWidth: img.naturalWidth
            };
        });
        return imgs;
    }''')
    print('Icons data:', data)
    browser.close()

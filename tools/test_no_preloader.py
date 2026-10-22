from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:3000/')
    preloader = page.evaluate('document.querySelector(".preloader")')
    main_visible = page.evaluate('window.getComputedStyle(document.querySelector("main")).opacity')
    print('Preloader element in DOM:', preloader)
    print('Main wrapper opacity:', main_visible)
    browser.close()

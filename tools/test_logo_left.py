import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

with open(os.path.join(WORKSPACE, 'index.html'), 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

nav_wrapper = soup.find('div', class_='nav-wrapper')

# In nav-wrapper:
# Currently children:
# 1. nav-menu-button-wrapper (has hamburger + locales)
# 2. nav-logo-link
# 3. button-group_nav
# 4. nav-overlay
# 5. nav-menu

# Let's add desktop-nav-menu into nav-wrapper between logo and button-group_nav
desktop_nav_html = """
<div class="desktop-nav-menu">
  <a href="/en/accommodation/" class="desktop-nav-link">Rooms</a>
  <a href="/en/restaurants-and-bars/" class="desktop-nav-link">Dining</a>
  <a href="/en/about/" class="desktop-nav-link">Hotel</a>
  <a href="/en/spa-center/" class="desktop-nav-link">SPA Center</a>
  <a href="/en/offers/" class="desktop-nav-link">Offers</a>
  <a href="/en/contact/" class="desktop-nav-link">Contact</a>
</div>
"""
nav_logo = nav_wrapper.find('a', class_='nav-logo-link')
nav_logo.insert_after(BeautifulSoup(desktop_nav_html, 'html.parser'))

css = """
<style id="logo-left-css">
@media screen and (min-width: 992px) {
  .nav-menu-button {
    display: none !important;
  }
  .nav-wrapper {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 1.25rem 2.5rem !important;
  }
  .nav-menu-button-wrapper {
    display: none !important;
  }
  .nav-logo-link {
    order: 1 !important;
    flex: 0 0 auto !important;
    width: auto !important;
    padding: 0 !important;
  }
  .logo-nav {
    max-width: 170px !important;
    width: auto !important;
    height: auto !important;
  }
  .desktop-nav-menu {
    order: 2 !important;
    display: flex !important;
    align-items: center !important;
    gap: 2rem !important;
  }
  .desktop-nav-link {
    color: inherit;
    font-family: "Manrope", sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 0.4rem 0.1rem;
    position: relative;
    transition: opacity 0.25s ease;
    white-space: nowrap;
  }
  .desktop-nav-link:hover {
    opacity: 0.7;
  }
  .desktop-nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0%;
    height: 2px;
    background-color: currentColor;
    transition: width 0.25s cubic-bezier(0.25, 1, 0.5, 1);
  }
  .desktop-nav-link:hover::after {
    width: 100%;
  }
  .button-group_nav {
    order: 3 !important;
    flex: 0 0 auto !important;
    display: flex !important;
    align-items: center !important;
    gap: 1.25rem !important;
    margin-top: 0 !important;
  }
}

@media screen and (max-width: 991px) {
  .desktop-nav-menu {
    display: none !important;
  }
  .nav-menu-button {
    display: flex !important;
  }
}
</style>
"""
soup.head.append(BeautifulSoup(css, 'html.parser'))

test_file = os.path.join(WORKSPACE, 'test_logo_left.html')
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    for width in [1440, 1200, 1024]:
        page = browser.new_page(viewport={'width': width, 'height': 900})
        page.goto('http://localhost:3000/test_logo_left.html', wait_until='networkidle')
        time.sleep(2)
        out_png = os.path.join(WORKSPACE, f'preview_logo_left_{width}.png')
        page.screenshot(path=out_png)
        print(f'Screenshot saved for width {width}: {out_png}')
        page.close()
    browser.close()

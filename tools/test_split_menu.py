import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

with open(os.path.join(WORKSPACE, 'index.html'), 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

button_wrapper = soup.find('div', class_='nav-menu-button-wrapper')
button_group = soup.find('div', class_='button-group_nav')

# Split Menu: Left Links in nav-menu-button-wrapper
left_menu_html = """
<div class="desktop-nav-menu desktop-nav-left">
  <a href="/en/accommodation/" class="desktop-nav-link">Rooms</a>
  <a href="/en/restaurants-and-bars/" class="desktop-nav-link">Dining</a>
  <a href="/en/about/" class="desktop-nav-link">Hotel</a>
  <a href="/en/spa-center/" class="desktop-nav-link">SPA Center</a>
</div>
"""

# Right Links in button-group_nav (before Book now button)
right_menu_html = """
<div class="desktop-nav-menu desktop-nav-right">
  <a href="/en/offers/" class="desktop-nav-link">Offers</a>
  <a href="/en/contact/" class="desktop-nav-link">Contact</a>
</div>
"""

# Insert left menu in nav-menu-button-wrapper (after hamburger button, before or after locales)
btn = button_wrapper.find('div', class_='nav-menu-button')
btn.insert_after(BeautifulSoup(left_menu_html, 'html.parser'))

# Insert right menu in button-group_nav before Book now button
book_btn = button_group.find('a', class_=lambda c: c and 'button' in c)
book_btn.insert_before(BeautifulSoup(right_menu_html, 'html.parser'))

# Styles
split_css = """
<style id="split-menu-css">
.desktop-nav-menu {
  display: none;
  align-items: center;
  gap: 1.6rem;
}

.desktop-nav-link {
  color: inherit;
  font-family: "Manrope", sans-serif;
  font-size: 0.88rem;
  font-weight: 600;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.35rem 0;
  position: relative;
  transition: opacity 0.25s ease, color 0.25s ease;
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

@media screen and (min-width: 992px) {
  .nav-menu-button {
    display: none !important;
  }
  .desktop-nav-menu {
    display: flex !important;
  }
  .nav-wrapper {
    align-items: center !important;
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }
  .nav-menu-button-wrapper {
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 1.75rem !important;
  }
  .button-group_nav {
    align-items: center !important;
    justify-content: flex-end !important;
    gap: 1.75rem !important;
    margin-top: 0 !important;
  }
  .nav-logo-link {
    padding-top: 0 !important;
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
soup.head.append(BeautifulSoup(split_css, 'html.parser'))

test_file = os.path.join(WORKSPACE, 'test_split_menu.html')
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    for width in [1440, 1200, 1024]:
        page = browser.new_page(viewport={'width': width, 'height': 900})
        page.goto('http://localhost:3000/test_split_menu.html', wait_until='networkidle')
        time.sleep(2)
        out_png = os.path.join(WORKSPACE, f'preview_split_{width}.png')
        page.screenshot(path=out_png)
        print(f'Screenshot saved for width {width}: {out_png}')
        page.close()
    browser.close()

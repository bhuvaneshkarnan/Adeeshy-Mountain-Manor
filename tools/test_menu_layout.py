import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

with open(os.path.join(WORKSPACE, 'index.html'), 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

button_wrapper = soup.find('div', class_='nav-menu-button-wrapper')

# Create desktop nav menu HTML
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
desktop_nav_soup = BeautifulSoup(desktop_nav_html, 'html.parser')

# Insert before nav-locales-wrapper
locales = button_wrapper.find('div', class_='nav-locales-wrapper')
if locales:
    locales.insert_before(desktop_nav_soup)

# Add custom CSS styles for desktop nav
custom_css = """
<style id="desktop-menu-css">
.desktop-nav-menu {
  display: none;
  align-items: center;
  gap: 1.5rem;
}

.desktop-nav-link {
  color: inherit;
  font-family: "Manrope", sans-serif;
  font-size: 0.95rem;
  font-weight: 500;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.4rem 0.2rem;
  position: relative;
  transition: opacity 0.3s ease, color 0.3s ease;
  white-space: nowrap;
}

.desktop-nav-link:hover {
  opacity: 0.75;
}

.desktop-nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 1.5px;
  background-color: currentColor;
  transition: width 0.3s cubic-bezier(0.25, 1, 0.5, 1);
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
  }
  .nav-menu-button-wrapper {
    align-items: center !important;
    gap: 1.5rem !important;
  }
  .button-group_nav {
    align-items: center !important;
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
soup.head.append(BeautifulSoup(custom_css, 'html.parser'))

test_file = os.path.join(WORKSPACE, 'test_menu.html')
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Saved test_menu.html. Capturing screenshot...')

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:3000/test_menu.html', wait_until='networkidle')
    time.sleep(2)
    page.screenshot(path=os.path.join(WORKSPACE, 'preview_desktop_menu.png'))
    print('Screenshot saved: preview_desktop_menu.png')
    
    # Also test tablet/mobile viewport (800x900)
    page.set_viewport_size({'width': 800, 'height': 900})
    time.sleep(1)
    page.screenshot(path=os.path.join(WORKSPACE, 'preview_mobile_menu.png'))
    print('Mobile screenshot saved: preview_mobile_menu.png')
    
    browser.close()

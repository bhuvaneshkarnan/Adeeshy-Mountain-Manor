import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

with open(os.path.join(WORKSPACE, 'index.html'), 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

button_wrapper = soup.find('div', class_='nav-menu-button-wrapper')
button_group = soup.find('div', class_='button-group_nav')

# Desktop Navigation Links
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

# Insert desktop nav menu in nav-menu-button-wrapper right after the hamburger button
btn = button_wrapper.find('div', class_='nav-menu-button')
btn.insert_after(BeautifulSoup(desktop_nav_html, 'html.parser'))

# High-end luxury navbar styling
custom_nav_css = """
<style id="luxury-desktop-nav-css">
/* Desktop Navbar styling */
.desktop-nav-menu {
  display: none;
  align-items: center;
  gap: 1.25rem;
}

.desktop-nav-link {
  color: inherit;
  font-family: "Manrope", sans-serif;
  font-size: 0.88rem;
  font-weight: 600;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.4rem 0.1rem;
  position: relative;
  transition: opacity 0.25s ease, color 0.25s ease;
  white-space: nowrap;
  display: inline-block;
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
  /* Hide hamburger button on desktop */
  .nav-menu-button {
    display: none !important;
  }
  
  /* Show desktop menu */
  .desktop-nav-menu {
    display: flex !important;
  }
  
  /* Proper desktop navbar alignment */
  .nav-wrapper {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    padding-top: 1.25rem !important;
    padding-bottom: 1.25rem !important;
  }
  
  .nav-menu-button-wrapper {
    flex: 1 1 auto !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 1.5rem !important;
  }
  
  .nav-logo-link {
    flex: 0 0 auto !important;
    width: auto !important;
    max-width: 180px !important;
    padding: 0 !important;
    margin: 0 1.5rem !important;
  }
  
  .logo-nav {
    max-width: 175px !important;
    width: auto !important;
    height: auto !important;
  }
  
  .button-group_nav {
    flex: 0 0 auto !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-end !important;
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
soup.head.append(BeautifulSoup(custom_nav_css, 'html.parser'))

test_file = os.path.join(WORKSPACE, 'test_perfect_menu.html')
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Saved test_perfect_menu.html. Capturing screenshots across viewports...')

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    for width in [1440, 1200, 1024, 768]:
        page = browser.new_page(viewport={'width': width, 'height': 900})
        page.goto('http://localhost:3000/test_perfect_menu.html', wait_until='networkidle')
        time.sleep(2)
        out_png = os.path.join(WORKSPACE, f'preview_perfect_{width}.png')
        page.screenshot(path=out_png)
        print(f'Screenshot saved for width {width}: {out_png}')
        page.close()
    browser.close()

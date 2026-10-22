import os
import re
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

DESKTOP_NAV_HTML = """
<div class="desktop-nav-menu">
  <a href="/en/accommodation/" class="desktop-nav-link">Rooms</a>
  <a href="/en/restaurants-and-bars/" class="desktop-nav-link">Dining</a>
  <a href="/en/about/" class="desktop-nav-link">Hotel</a>
  <a href="/en/spa-center/" class="desktop-nav-link">SPA Center</a>
  <a href="/en/offers/" class="desktop-nav-link">Offers</a>
  <a href="/en/contact/" class="desktop-nav-link">Contact</a>
</div>
"""

NAV_STYLE = """
<style id="desktop-navbar-style">
/* Desktop Navbar styling */
.desktop-nav-menu {
  display: none;
}

@media screen and (min-width: 992px) {
  /* Hide hamburger button on desktop */
  .nav-menu-button {
    display: none !important;
  }
  
  .nav-wrapper {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 1rem 2.5rem !important;
  }
  
  /* Keep mobile hamburger wrapper from taking up space on desktop */
  .nav-menu-button-wrapper {
    display: none !important;
  }
  
  /* Logo on left */
  .nav-logo-link {
    order: 1 !important;
    flex: 0 0 auto !important;
    width: auto !important;
    max-width: 175px !important;
    padding: 0 !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center !important;
  }
  
  .logo-nav {
    max-width: 165px !important;
    width: auto !important;
    height: auto !important;
  }
  
  /* Navigation menu in center */
  .desktop-nav-menu {
    order: 2 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 2rem !important;
    flex: 1 1 auto !important;
    margin: 0 2rem !important;
  }
  
  .desktop-nav-link {
    color: inherit;
    font-family: "Manrope", sans-serif;
    font-size: 0.88rem;
    font-weight: 600;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    padding: 0.35rem 0.1rem;
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
  
  /* Right side: language switcher + CTA */
  .button-group_nav {
    order: 3 !important;
    flex: 0 0 auto !important;
    display: flex !important;
    align-items: center !important;
    gap: 1.5rem !important;
    margin-top: 0 !important;
  }
  
  .desktop-locales {
    display: flex !important;
    align-items: center !important;
  }
}

@media screen and (max-width: 991px) {
  .desktop-nav-menu {
    display: none !important;
  }
  .desktop-locales {
    display: none !important;
  }
  .nav-menu-button {
    display: flex !important;
  }
}
</style>
"""

def update_page_navbar(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    nav_wrapper = soup.find('div', class_='nav-wrapper')
    if not nav_wrapper:
        return html_content

    # Check if desktop-nav-menu already exists
    if not nav_wrapper.find('div', class_='desktop-nav-menu'):
        nav_logo = nav_wrapper.find('a', class_='nav-logo-link')
        if nav_logo:
            nav_logo.insert_after(BeautifulSoup(DESKTOP_NAV_HTML, 'html.parser'))

    # Add desktop language selector inside button-group_nav if not present
    button_group = nav_wrapper.find('div', class_='button-group_nav')
    if button_group and not button_group.find('div', class_='desktop-locales'):
        # Copy nav-locales-wrapper content
        locales = nav_wrapper.find('div', class_='nav-locales-wrapper')
        if locales:
            desktop_loc = BeautifulSoup(f'<div class="desktop-locales">{locales.decode_contents()}</div>', 'html.parser')
            button_group.insert(0, desktop_loc)

    # Inject or update style tag
    if not soup.head.find(id='desktop-navbar-style'):
        soup.head.append(BeautifulSoup(NAV_STYLE, 'html.parser'))
    else:
        soup.head.find(id='desktop-navbar-style').replace_with(BeautifulSoup(NAV_STYLE, 'html.parser'))

    return str(soup)

# Apply to index.html and all pages
count = 0
for root, dirs, files in os.walk(WORKSPACE):
    for f in files:
        if f == 'index.html':
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as file:
                content = file.read()
            updated = update_page_navbar(content)
            with open(fpath, 'w', encoding='utf-8') as file:
                file.write(updated)
            count += 1

print(f'Applied PC navbar menu across {count} pages!')

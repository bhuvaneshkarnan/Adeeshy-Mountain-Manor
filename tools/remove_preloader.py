import os
import re
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
CSS_FILE = os.path.join(WORKSPACE, 'assets', 'css', 'pirin.webflow.css')

# 1. Update pirin.webflow.css
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

preloader_css_killer = """
/* Preloader Completely Disabled */
.preloader,
.preloader-container,
[preloader] {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
  height: 0 !important;
  width: 0 !important;
  max-height: 0 !important;
  max-width: 0 !important;
  overflow: hidden !important;
  z-index: -9999 !important;
  transform: translateY(-200%) !important;
}

.navbar[preloader] .logo-nav {
  filter: none !important;
}
"""

if '/* Preloader Completely Disabled */' not in css:
    css += '\n' + preloader_css_killer
else:
    css = re.sub(r'/\* Preloader Completely Disabled \*/.*', preloader_css_killer, css, flags=re.DOTALL)

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated pirin.webflow.css to kill preloader completely!')

# 2. Process all HTML files
html_files = [os.path.join(WORKSPACE, 'index.html')]
for root, dirs, files in os.walk(os.path.join(WORKSPACE, 'en')):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove preloader div
    soup = BeautifulSoup(html, 'html.parser')
    for p in soup.find_all('div', class_='preloader'):
        p.decompose()

    html = str(soup)

    # Change preloaderStyle in window.site to "none"
    html = re.sub(r'preloaderStyle:\s*["\'][^"\']+["\']', 'preloaderStyle: "none"', html)

    # Ensure preloader style override is in head
    if 'preloader-killer-style' not in html:
        style_override = f"<style id='preloader-killer-style'>{preloader_css_killer}</style>"
        html = html.replace('</head>', f'{style_override}\n</head>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1

print(f'Completely removed preloader from {count} HTML files!')

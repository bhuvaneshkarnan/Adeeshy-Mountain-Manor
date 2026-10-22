import os
import re

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
CSS_FILE = os.path.join(WORKSPACE, 'assets', 'css', 'pirin.webflow.css')
RULES_FILE = os.path.join(WORKSPACE, 'tools', 'mobile_optimizations.css')

# 1. Read mobile rules and append to pirin.webflow.css
with open(RULES_FILE, 'r', encoding='utf-8') as f:
    mobile_css = f.read()

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    current_css = f.read()

# Avoid duplicate appending
if 'ADEESHY MOUNTAIN MANOR - COMPREHENSIVE MOBILE OPTIMIZATION' not in current_css:
    with open(CSS_FILE, 'a', encoding='utf-8') as f:
        f.write('\n' + mobile_css + '\n')
    print('Appended mobile optimizations CSS to pirin.webflow.css')
else:
    # Replace existing block with latest
    idx = current_css.find('/* ==========================================================================\n   ADEESHY MOUNTAIN MANOR - COMPREHENSIVE MOBILE OPTIMIZATION')
    if idx != -1:
        updated_css = current_css[:idx] + mobile_css + '\n'
        with open(CSS_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_css)
        print('Updated mobile optimizations CSS in pirin.webflow.css')

# 2. Update footers in all HTML files
updated_pages = 0
for root, dirs, files in os.walk(WORKSPACE):
    if any(p in root for p in ['.git', 'node_modules', '.gemini', 'tools']):
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as fp:
                html = fp.read()
            
            orig = html
            
            # Replace Wellness & Relax with Amenities
            html = re.sub(
                r'<a[^>]*class="footer3_link"[^>]*href="/en/spa-center/"[^>]*>[\s\n]*Wellness\s*&(?:amp;)?\s*Relax[\s\n]*</a>',
                '<a class="footer3_link" href="/en/amenities/">Amenities</a>',
                html,
                flags=re.IGNORECASE
            )
            
            # Replace Sightseeing link text with Local Attractions if pointing to sightseeing
            html = re.sub(
                r'<a([^>]*class="footer3_link"[^>]*href="/en/sightseeing/"[^>]*)>[\s\n]*Sightseeing[\s\n]*</a>',
                r'<a\1>Local Attractions</a>',
                html,
                flags=re.IGNORECASE
            )
            
            # Ensure Getting Here is present in the second column if not already there
            if '/en/getting-here/' not in html and 'footer3_link-list' in html:
                # Add Getting Here after Local Attractions
                html = html.replace(
                    '<a class="footer3_link" href="/en/sightseeing/">Local Attractions</a>',
                    '<a class="footer3_link" href="/en/local-attractions/">Local Attractions</a>\n  <a class="footer3_link" href="/en/getting-here/">Getting Here</a>'
                )
                
            if html != orig:
                with open(path, 'w', encoding='utf-8') as fp:
                    fp.write(html)
                updated_pages += 1

print(f'Updated {updated_pages} HTML pages with modernized footer links.')

import os
from bs4 import BeautifulSoup
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

sample_html_files = [
    'index.html',
    'en/index.html',
    'en/accommodation/index.html',
    'en/accommodation/presidential-suite/index.html',
    'en/restaurants-and-bars/index.html',
    'en/spa-center/index.html',
    'en/offers/index.html',
    'en/contact/index.html',
    'en/gallery/index.html'
]

total_checked = 0
missing_assets = []

for rel_path in sample_html_files:
    full_path = os.path.join(WORKSPACE, rel_path)
    if not os.path.exists(full_path):
        print(f'Missing HTML file: {rel_path}')
        continue
    with open(full_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Check images
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and src.startswith('/assets/'):
            total_checked += 1
            local_file = os.path.join(WORKSPACE, src.lstrip('/'))
            if not os.path.exists(local_file):
                missing_assets.append((rel_path, src))
        srcset = img.get('srcset')
        if srcset:
            for part in srcset.split(','):
                u = part.strip().split(' ')[0]
                if u.startswith('/assets/'):
                    total_checked += 1
                    local_file = os.path.join(WORKSPACE, u.lstrip('/'))
                    if not os.path.exists(local_file):
                        missing_assets.append((rel_path, u))

    # Check scripts
    for s in soup.find_all('script', src=True):
        src = s['src']
        if src.startswith('/assets/'):
            total_checked += 1
            local_file = os.path.join(WORKSPACE, src.lstrip('/'))
            if not os.path.exists(local_file):
                missing_assets.append((rel_path, src))

    # Check styles
    for l in soup.find_all('link', rel='stylesheet'):
        href = l.get('href')
        if href and href.startswith('/assets/'):
            total_checked += 1
            local_file = os.path.join(WORKSPACE, href.lstrip('/'))
            if not os.path.exists(local_file):
                missing_assets.append((rel_path, href))

print(f'Total local asset references checked across key pages: {total_checked}')
print(f'Total missing local assets: {len(missing_assets)}')
if missing_assets:
    for page, asset in missing_assets[:15]:
        print(f'  [MISSING in {page}]: {asset}')
else:
    print('ALL ASSETS EXIST LOCALLY ON DISK! 100% INTEGRITY!')

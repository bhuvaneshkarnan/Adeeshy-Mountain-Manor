import os
import re
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

html_files = [os.path.join(WORKSPACE, 'index.html')]
for root, dirs, files in os.walk(os.path.join(WORKSPACE, 'en')):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

visible_spa_phrases = set()
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    for s in soup.find_all(string=re.compile(r'\b(?:SPA|Spa|spa)\b')):
        txt = s.strip()
        if txt and len(txt) < 100:
            visible_spa_phrases.add(txt)

print(f'Total unique visible text nodes containing SPA/Spa/spa: {len(visible_spa_phrases)}')
for p in sorted(list(visible_spa_phrases))[:30]:
    print(' •', p)

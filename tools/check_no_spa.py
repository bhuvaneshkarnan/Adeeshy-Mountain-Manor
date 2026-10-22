import os
import re
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

with open(os.path.join(WORKSPACE, 'index.html'), 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

visible_spa = []
for s in soup.find_all(string=re.compile(r'\b(?:SPA|Spa|spa)\b')):
    if s.parent.name not in ['script', 'style']:
        t = s.strip()
        if t:
            visible_spa.append((s.parent.name, s.parent.get('class'), t))

print(f'Remaining visible SPA strings in index.html: {len(visible_spa)}')
for p, cls, t in visible_spa[:20]:
    print(f'<{p} class="{cls}">: {t}')

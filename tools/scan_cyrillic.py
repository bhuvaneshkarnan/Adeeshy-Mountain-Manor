import os
import re
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

with open(os.path.join(WORKSPACE, 'index.html'), 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cyrillic_texts = []
for el in soup.find_all(string=re.compile(r'[\u0400-\u04FF]')):
    t = el.strip()
    if t:
        cyrillic_texts.append((el.parent.name, el.parent.get('class'), t))

with open('cyrillic_report.txt', 'w', encoding='utf-8') as out:
    out.write(f'Total Cyrillic nodes: {len(cyrillic_texts)}\n')
    for parent_name, parent_cls, text in cyrillic_texts:
        out.write(f'<{parent_name} class="{parent_cls}"> : {text}\n')

    out.write('\n--- Attributes ---\n')
    for tag in soup.find_all():
        for attr, val in tag.attrs.items():
            if isinstance(val, str) and re.search(r'[\u0400-\u04FF]', val):
                out.write(f'<{tag.name} {attr}="{val}">\n')

print('Wrote cyrillic_report.txt')

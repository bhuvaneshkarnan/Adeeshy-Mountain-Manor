from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('--- Searching for close button / banner / bar elements ---')
for el in soup.find_all(attrs={'class': True}):
    cls = ' '.join(el.get('class', []))
    if any(k in cls.lower() for k in ['banner', 'cookie', 'notice', 'alert', 'announcement', 'promo', 'top-bar']):
        if el.name in ['div', 'section']:
            print(f'<{el.name} class="{cls}" id="{el.get("id")}">')

print('\n--- Elements with close/cross ---')
for btn in soup.find_all(['button', 'a', 'div'], class_=re.compile(r'close|cross', re.I)):
    print('Close button found:', btn.name, btn.get('class'), 'Parent:', btn.parent.name if btn.parent else '', btn.parent.get('class') if btn.parent else '')

print('\n--- Search for SVG with close cross (e.g. M... or cross) ---')
for svg in soup.find_all('svg'):
    parent = svg.parent
    if parent:
        text = str(svg)
        if 'M' in text and ('close' in str(parent.get('class', '')).lower() or 'cross' in str(parent.get('class', '')).lower() or len(text) < 400):
            print('SVG in parent:', parent.name, parent.get('class'))

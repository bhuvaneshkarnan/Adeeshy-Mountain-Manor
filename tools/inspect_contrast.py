from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('--- Sections and background classes in index.html ---')
for tag in soup.find_all(['section', 'header', 'footer', 'div']):
    cls = tag.get('class', [])
    cls_str = ' '.join(cls)
    if any(k in cls_str for k in ['background', 'alternate', 'section_', 'color-']):
        if tag.name in ['section', 'header', 'footer'] or 'background' in cls_str:
            print(f"<{tag.name} class='{cls_str}'>")

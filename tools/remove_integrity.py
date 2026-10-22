import os
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

count = 0
for root, dirs, files in os.walk(WORKSPACE):
    for f in files:
        if f.endswith('.html'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as file:
                content = file.read()
            if 'integrity=' in content:
                soup = BeautifulSoup(content, 'html.parser')
                for tag in soup.find_all(['link', 'script']):
                    if tag.has_attr('integrity'):
                        del tag['integrity']
                    if tag.has_attr('crossorigin'):
                        del tag['crossorigin']
                with open(fpath, 'w', encoding='utf-8') as file:
                    file.write(str(soup))
                count += 1

print(f'Cleaned integrity attributes from {count} HTML files!')

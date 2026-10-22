with open('scraped_home.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'([^}]*section_layout254[^}]*\{[^}]+\})', html)
print('In scraped_home.html:', matches)

with open('tools/full_cloner.py', 'r', encoding='utf-8') as f:
    fc = f.read()

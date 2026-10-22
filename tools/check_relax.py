with open('assets/css/pirin.webflow.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'([^}]*pirin-relax[^}]*\{[^}]+\})', css)
print(f'Matches for pirin-relax: {len(matches)}')
for m in matches[:10]:
    print(m)

matches2 = re.findall(r'([^}]*section_layout254[^}]*)', css)
print('layout254 in CSS:', matches2)

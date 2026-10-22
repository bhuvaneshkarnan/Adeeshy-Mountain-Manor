import os
import re

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

with open(os.path.join(WORKSPACE, 'assets/css/pirin.webflow.css'), 'r', encoding='utf-8') as f:
    css = f.read()

vars_found = re.findall(r'(--[a-zA-Z0-9_\-]+:\s*[^;]+;)', css)
print(f'Total CSS custom properties found: {len(vars_found)}')
color_vars = [v for v in vars_found if '#' in v or 'rgb' in v or 'hsl' in v or 'color' in v.lower()]
for v in color_vars[:30]:
    print(v)

print('\nSearching for #7f7f2e (old olive):')
olive_matches = re.findall(r'#7f7f2e', css, re.I)
print(f'Occurrences of #7f7f2e: {len(olive_matches)}')

with open(os.path.join(WORKSPACE, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

olive_in_html = re.findall(r'#7f7f2e', html, re.I)
print(f'Occurrences of #7f7f2e in index.html: {len(olive_in_html)}')

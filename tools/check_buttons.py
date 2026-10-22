with open('assets/css/pirin.webflow.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
button_rules = re.findall(r'(\.button[^{]*\{[^}]+\})', css)
print('Button rules in CSS:')
for r in button_rules[:5]:
    print(r)

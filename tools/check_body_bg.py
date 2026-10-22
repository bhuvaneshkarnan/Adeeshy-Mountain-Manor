with open('assets/js/dev-46.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'body', text)]
for p in matches:
    snippet = text[max(0, p-30):min(len(text), p+60)]
    if 'background' in snippet or 'color' in snippet or 'set' in snippet:
        print(snippet.encode('ascii', errors='replace').decode('ascii'))

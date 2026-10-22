import os
from playwright.sync_api import sync_playwright

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

html_files = []
for root, dirs, files in os.walk(WORKSPACE):
    if any(p in root for p in ['.git', 'node_modules', '.gemini', 'tools']):
        continue
    for file in files:
        if file.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, file), WORKSPACE).replace('\\', '/')
            html_files.append(rel)

print(f'Auditing all {len(html_files)} pages...')

bad_pages = []

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        headless=True
    )
    page = browser.new_page(viewport={'width': 375, 'height': 812})
    
    for rel in html_files:
        url_path = '' if rel == 'index.html' else rel.replace('/index.html', '/')
        try:
            page.goto(f'http://localhost:3000/{url_path}', wait_until='domcontentloaded', timeout=5000)
            res = page.evaluate('''() => {
                const sw = document.documentElement.scrollWidth;
                const cw = document.documentElement.clientWidth;
                return { sw, cw, overflow: sw > cw };
            }''')
            if res['overflow']:
                bad_pages.append((rel, res['sw'], res['cw']))
                print(f'[FAIL] {rel}: scrollWidth {res["sw"]} > {res["cw"]}')
        except Exception as e:
            print(f'[ERR] {rel}: {e}')
            
    browser.close()

print(f'\nTotal overflowing pages: {len(bad_pages)} / {len(html_files)}')
for bp in bad_pages:
    print(bp)

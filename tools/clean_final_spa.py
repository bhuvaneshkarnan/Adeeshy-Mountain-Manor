import os

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

replacements = {
    'SPA treatments': 'wellness treatments',
    'spa treatments': 'wellness treatments',
    'spa programs': 'wellness programs',
    'SPA programs': 'wellness programs',
    '>SPA & Relax<': '>Wellness & Relax<',
    '>SPA &amp; Relax<': '>Wellness &amp; Relax<',
    'SPA & Relax': 'Wellness & Relax',
    'SPA &amp; Relax': 'Wellness &amp; Relax',
    'SPA and Relax': 'Wellness and Relax',
}

html_files = [os.path.join(WORKSPACE, 'index.html')]
for root, dirs, files in os.walk(os.path.join(WORKSPACE, 'en')):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    changed = False
    for k, v in replacements.items():
        if k in content:
            content = content.replace(k, v)
            changed = True
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f_out:
            f_out.write(content)
        count += 1

print(f'Done! Cleaned last SPA sentences in {count} files.')

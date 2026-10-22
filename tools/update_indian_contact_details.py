import os
import re
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

# Replacements dictionary for exact strings
REPLACEMENTS = [
    # Phones
    ('tel:+35974635600', 'tel:+919876543210'),
    ('tel:+35974635656', 'tel:+919876543211'),
    ('tel:+359893300300', 'tel:+919876543212'),
    ('tel:+35974631960', 'tel:+919876543210'),
    ('+359 746 35 600', '+91 98765 43210'),
    ('+359 746 35600', '+91 98765 43210'),
    ('+359 74 635 656', '+91 98765 43211'),
    ('+359 746 35 656', '+91 98765 43211'),
    ('+359 893 300 300', '+91 98765 43212'),
    ('+359 746 31 960', '+91 98765 43210'),
    ('+359 746 31960', '+91 98765 43210'),
    ('+35974635600', '+919876543210'),
    
    # Emails
    ('marketing@parkhotelpirin.com', 'marketing@adeeshymountainmanor.com'),
    ('spareception@parkhotelpirin.com', 'events@adeeshymountainmanor.com'),
    ('fbmanager@parkhotelpirin.com', 'dining@adeeshymountainmanor.com'),
    ('reservations@parkhotelpirin.com', 'reservations@adeeshymountainmanor.com'),
    ('info@parkhotelpirin.com', 'info@adeeshymountainmanor.com'),
    ('office@parkhotelpirin.com', 'info@adeeshymountainmanor.com'),
]

updated_count = 0

for root, dirs, files in os.walk(WORKSPACE):
    if any(p in root for p in ['.git', 'node_modules', '.gemini', 'tools']):
        continue
    for file in files:
        if file.endswith(('.html', '.js', '.json', '.md')):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            orig = content
            for old, new in REPLACEMENTS:
                content = content.replace(old, new)
            
            if content != orig:
                with open(path, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                updated_count += 1

print(f'Updated contact info across {updated_count} files.')

# Step 2: Specific updates to en/contact/index.html
contact_html_path = os.path.join(WORKSPACE, 'en', 'contact', 'index.html')
with open(contact_html_path, 'r', encoding='utf-8') as f:
    contact_content = f.read()

# Replace address block
old_address_patterns = [
    r'Sandanski 2800<br\s*/?>\s*District [“"]Hydrostroy[”"] 27',
    r'Sandanski 2800[\s\S]*?District [“"]Hydrostroy[”"] 27'
]
new_address = 'Manor Estate, Hill Top Road<br/>Kodaikanal, Tamil Nadu 624101, India'

for pat in old_address_patterns:
    contact_content = re.sub(pat, new_address, contact_content)

# Replace "Fax" heading with "Inquiries & Front Desk"
contact_content = re.sub(
    r'<h3[^>]*>[\s\n]*Fax[\s\n]*</h3>',
    '<h3 class="heading-style-h6">Inquiries &amp; Front Desk</h3>',
    contact_content,
    flags=re.IGNORECASE
)

# Replace Privacy notice checkbox label text if "Park Hotel Pirin" was mentioned
contact_content = contact_content.replace(
    'Notice of "Park Hotel Pirin"',
    'Notice of "Adeeshy Mountain Manor"'
).replace(
    'Notice of “Park Hotel Pirin”',
    'Notice of “Adeeshy Mountain Manor”'
)

with open(contact_html_path, 'w', encoding='utf-8') as f:
    f.write(contact_content)

print('Updated en/contact/index.html address, headings, and privacy statement.')

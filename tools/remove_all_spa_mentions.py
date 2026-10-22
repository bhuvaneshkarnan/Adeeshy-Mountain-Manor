import os
import re

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

# Ordered replacement tuples (most specific first)
REPLACEMENTS = [
    # Navigation & Header
    ('>SPA Center<', '>Wellness<'),
    ('>SPA center<', '>Wellness<'),
    ('>SPA & Relax<', '>Wellness & Relax<'),
    ('>SPA & Wellness<', '>Wellness & Relaxation<'),
    ('>SPA and Wellness<', '>Wellness & Relaxation<'),
    ('>Medical SPA<', '>Medical Wellness<'),
    ('>SPA<', '>Wellness<'),
    
    # Headings & Specific Phrases
    ('SPA center “Pirin”', 'Adeeshy Mountain Wellness Sanctuary'),
    ('SPA center "Pirin"', 'Adeeshy Mountain Wellness Sanctuary'),
    ('SPA center ?Pirin?', 'Adeeshy Mountain Wellness Sanctuary'),
    ('Adeeshy Mountain SPA Sanctuary takes care of your health!', 'Adeeshy Mountain Wellness Sanctuary takes care of your health!'),
    ('Adeeshy Mountain SPA Sanctuary', 'Adeeshy Mountain Wellness Sanctuary'),
    ('Pirin SPA Center', 'Adeeshy Mountain Wellness Sanctuary'),
    ('European SPA Association', 'European Wellness Association'),
    ('Luxury holiday and SPA in “Adeeshy Mountain Manor”', 'Luxury Holiday and Wellness at Adeeshy Mountain Manor'),
    ('Luxury holiday and SPA in „Adeeshy Mountain Manor“', 'Luxury Holiday and Wellness at Adeeshy Mountain Manor'),
    ('Luxury holiday and SPA in ?Adeeshy Mountain Manor?', 'Luxury Holiday and Wellness at Adeeshy Mountain Manor'),
    ('Luxury holiday and SPA in Adeeshy Mountain Manor', 'Luxury Holiday and Wellness at Adeeshy Mountain Manor'),
    ('Luxury, SPA and relaxation', 'Luxury, wellness and relaxation'),
    ('Luxury SPA experience', 'Luxury wellness experience'),
    ('Accommodation and SPA relaxation', 'Accommodation and wellness relaxation'),
    ('Healing SPA Programs', 'Healing Wellness Programs'),
    ('Professional massages and SPA therapies', 'Professional massages and wellness therapies'),
    ('Premium spa and wellness services', 'Premium wellness and thermal bath services'),
    ('Mineral pools and SPA', 'Mineral pools and thermal wellness'),
    ('mineral pools and SPA', 'mineral pools and thermal wellness'),
    ('SPA and wellness pleasures', 'Wellness and thermal pleasures'),
    ('spa and wellness pleasures', 'wellness and thermal pleasures'),
    ('spa and wellness services', 'wellness and thermal services'),
    ('spa and wellness treatments', 'wellness and relaxation treatments'),
    ('spa and wellness', 'wellness and relaxation'),
    ('SPA and wellness', 'wellness and relaxation'),
    ('SPA & Wellness', 'Wellness & Relaxation'),
    ('spa therapies and wellness treatments', 'wellness therapies and holistic treatments'),
    ('spa therapies', 'wellness therapies'),
    ('SPA therapies', 'wellness therapies'),
    ('SPA procedures', 'wellness procedures'),
    ('spa procedures', 'wellness procedures'),
    ('spa rituals', 'wellness rituals'),
    ('Spa rituals', 'Wellness rituals'),
    ('Full Spa Day', 'Full Wellness Day'),
    ('Spa Day', 'Wellness Day'),
    ('spa facilities', 'wellness facilities'),
    ('Spa Hotel Devin', 'Wellness Hotel Devin'),
    ('LEARN MORE ABOUT THE SPA', 'LEARN MORE ABOUT WELLNESS'),
    ('Find out more about our SPA', 'Find out more about our Wellness Center'),
    ('Unlimited access to the spa', 'Unlimited access to the wellness center'),
    ('access to the spa', 'access to the wellness center'),
    ('to the spa area', 'to the wellness area'),
    ('the spa area', 'the wellness area'),
    ('Weekday SPA package', 'Weekday Wellness Package'),
    ('Weekday SPA Package', 'Weekday Wellness Package'),
    ('weekday SPA package', 'weekday wellness package'),
    ('weekday spa package', 'weekday wellness package'),
    ('SPA package', 'Wellness Package'),
    ('spa package', 'wellness package'),
    ('Medical SPA programs', 'Medical Wellness programs'),
    ('Medical SPA Programs', 'Medical Wellness Programs'),
    ('Medical SPA', 'Medical Wellness'),
    ('medical spa', 'medical wellness'),
    ('Med Spa', 'Medical Wellness'),
    ('med spa', 'medical wellness'),
    ('SPA Center', 'Wellness Center'),
    ('SPA center', 'Wellness Center'),
    ('spa center', 'wellness center'),
    ('SPA complex', 'wellness complex'),
    ('spa complex', 'wellness complex'),
    ('SPA Resort', 'Wellness Resort'),
    ('SPA resort', 'wellness resort'),
    ('SPA Pleasure', 'Relaxation & Pleasure'),
    ('spa pleasure', 'relaxation & pleasure'),
    ('& SPA', '& Wellness Retreat'),
    ('&amp; SPA', '&amp; Wellness Retreat'),
    ('and SPA', 'and Wellness'),
    ('and spa', 'and wellness'),
]

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
    for old, new in REPLACEMENTS:
        if old in content:
            content = content.replace(old, new)
            changed = True

    # Also regex for any remaining standalone visible "SPA" or "Spa" in HTML tags
    # e.g. >SPA< or >Spa<
    content = re.sub(r'>\s*SPA\s*<', '>Wellness<', content)
    content = re.sub(r'>\s*Spa\s*<', '>Wellness<', content)
    content = re.sub(r'\bSPA Center\b', 'Wellness Center', content)
    content = re.sub(r'\bSPA center\b', 'Wellness Center', content)
    content = re.sub(r'\bspa center\b', 'wellness center', content)
    content = re.sub(r'\bMedical SPA\b', 'Medical Wellness', content)
    content = re.sub(r'\bmedical spa\b', 'medical wellness', content)

    # In desktop menu specifically
    content = content.replace('>SPA Center</a>', '>Wellness</a>')
    content = content.replace('>SPA</a>', '>Wellness</a>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1

print(f'Processed {count} HTML files and replaced all mentions of SPA with Wellness!')

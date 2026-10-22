import os

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'

final_fixes = {
    'Луксозен хотел в подножието на Пирин, съчетаващ лечебна минерална вода, модерен СПА център и комфорт в Mountain Resort.': 'A luxury resort at the foot of scenic alpine peaks, combining healing mineral thermal waters, a modern spa sanctuary, and five-star comfort.',
    'Ресторант в Mountain Resort, предлагащ автентични ястия от българска, сръбска, гръцка, турска и македонска кухня, допълнени с подбрани напитки и жива музика.': 'An authentic alpine restaurant offering artisanal regional dishes, fine wines, and atmospheric music.',
    'Луксозен СПА център в Mountain Resort, предлагащ разнообразие от уелнес процедури, ароматерапии и терапии с минерална вода.': 'A luxurious mountain SPA sanctuary offering a rich variety of wellness treatments, aromatherapy, and therapeutic mineral water sessions.',
    'Снимка на уютна хотелска стая в Shyadé Stone Cabin, Mountain Resort, с голямо двойно легло, меки възглавници, декоративно подреждане на кърпи и поднос с приготвена закуска. Стаята е с приглушено осветление и създава усещане за комфорт и релакс.': 'Cozy luxury suite at Shyadé Stone Cabin with king bed, plush bedding, ambient lighting, and breakfast service.'
}

# Collect html files directly without crawling assets
html_files = [os.path.join(WORKSPACE, 'index.html')]
for root, dirs, files in os.walk(os.path.join(WORKSPACE, 'en')):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as file:
        content = file.read()
    changed = False
    for k, v in final_fixes.items():
        if k in content:
            content = content.replace(k, v)
            changed = True
    if changed:
        with open(fpath, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1

print(f'Done! Updated {count} HTML files.')

import os
import re
import shutil
from bs4 import BeautifulSoup

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
IMG_DIR = os.path.join(WORKSPACE, 'assets', 'images')
CSS_FILE = os.path.join(WORKSPACE, 'assets', 'css', 'pirin.webflow.css')

# 1. Update logo files
# Copy new SVG logo to the old logo filename so any direct image reference gets the new logo
orig_logo_name = '67a4016fe500e14a4d5340d2_a3b61caacd33aaa535f422454da4713e_pirin-logo-full.svg'
shutil.copyfile(
    os.path.join(IMG_DIR, 'shyade-stone-cabin-logo.svg'),
    os.path.join(IMG_DIR, orig_logo_name)
)
print('Updated main logo file with Shyadé Stone Cabin logo!')

# 2. Update CSS Colors in pirin.webflow.css
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace brand colors
# Old olive #7f7f2e -> Emerald Green #0F5132
css = css.replace('#7f7f2e', '#0F5132')
# Old sage #c2c5aa -> Emerald Green tint or Gold
css = css.replace('--base-color-brand--pirin-main:#7f7f2e', '--base-color-brand--pirin-main:#0F5132')
css = css.replace('--base-color-brand--pirin-relax:#c2c5aa', '--base-color-brand--pirin-relax:#0F5132')
css = css.replace('--base-color-brand--pirin-shine:#d8d45c', '--base-color-brand--pirin-shine:#C8A27A')
css = css.replace('--base-color-brand--pirin-relaxx:#e8f2d6', '--base-color-brand--pirin-relaxx:#f4efe6')
css = css.replace('--base-color-neutral--neutral-dark:#333d29', '--base-color-neutral--neutral-dark:#093320')
css = css.replace('--base-color-neutral--neutral-darkest:#1f2518', '--base-color-neutral--neutral-darkest:#062114')
css = css.replace('--base-color-neutral--neutral-darker:#1f2518', '--base-color-neutral--neutral-darker:#082819')

# Hide promo-banner completely in CSS
if '.promo-banner' not in css or 'display:none' not in css:
    css += '\n.promo-banner{display:none!important;visibility:hidden!important;height:0!important;opacity:0!important;overflow:hidden!important;pointer-events:none!important;}\n'

# Add custom luxury color rules to CSS
custom_theme_css = """
/* Shyadé Stone Cabin - Emerald Green & Gold Luxury Theme */
:root {
  --brand-emerald: #0F5132;
  --brand-emerald-dark: #082A1A;
  --brand-emerald-light: #166E45;
  --brand-gold: #C8A27A;
  --brand-gold-hover: #B58F66;
  --brand-gold-light: #E8D7C2;
}

/* Primary Buttons */
.button, .button.w-button {
  background-color: #C8A27A !important;
  border-color: #C8A27A !important;
  color: #082A1A !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  transition: all 0.3s ease !important;
}

.button:hover, .button.w-button:hover {
  background-color: #0F5132 !important;
  border-color: #0F5132 !important;
  color: #FFFFFF !important;
}

/* Text selections & links */
::selection {
  background-color: #C8A27A !important;
  color: #082A1A !important;
}

.button.is-link {
  color: #C8A27A !important;
}

.button.is-link:hover {
  color: #0F5132 !important;
}

/* Accent elements */
.text-color-gold, .gold-accent {
  color: #C8A27A !important;
}
"""
css += '\n' + custom_theme_css

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated pirin.webflow.css with Emerald Green (#0F5132) & Gold (#C8A27A)!')

# 3. Bulgarian to English translation mapping
CYRILLIC_REPLACEMENTS = {
    # Section headings & major labels
    'Стаи и апартаменти': 'Rooms & Suites',
    'ВАЛИДНИ ДО 14 АПРИЛ 2025': 'EXCLUSIVE OFFERS AVAILABLE',
    'ЗЗЛСПОИН': 'Legal Protection & Notice',
    'Български': 'English',
    'Формуляр абонаменти': 'Newsletter Subscription Form',
    
    # Brand Names
    'Парк Хотел Пирин': 'Shyadé Stone Cabin',
    'Парк Хотел „Пирин“': 'Shyadé Stone Cabin',
    '„Парк Хотел Пирин“': 'Shyadé Stone Cabin',
    '„Парк Хотел “Пирин“': 'Shyadé Stone Cabin',
    'Парк хотел Пирин': 'Shyadé Stone Cabin',
    'Park Hotel Pirin': 'Shyadé Stone Cabin',
    'Park Hotel "Pirin"': 'Shyadé Stone Cabin',
    '“Park Hotel Pirin”': 'Shyadé Stone Cabin',
    '„Park Hotel Pirin“': 'Shyadé Stone Cabin',
    '?Park Hotel Pirin?': 'Shyadé Stone Cabin',
    'Park hotel Pirin': 'Shyadé Stone Cabin',
    
    # Menus
    'Настаняване': 'Accommodation',
    'Заведения': 'Dining',
    'Хотел': 'Hotel',
    'Релакс': 'Relax & SPA',
    'Активности': 'Activities',
    'Забележителности': 'Sightseeing',
    'Оферти': 'Offers',
    
    # Image Alt tags
    'Интериор на луксозен СПА център с дървена облицовка, зелени растения и мека светлина.': 'Interior of luxury wellness center with ambient lighting, cedar finishes, and natural greenery.',
    'Интериор на хотелско фоайе с мека мебел в сиво, зелени растения и декоративно осветление.': 'Lobby lounge at Shyadé Stone Cabin with plush seating, rich greenery, and ambient lighting.',
    'Външен басейн с мозайка, заобиколен от шезлонги и сгради в топъл цвят.': 'Outdoor heated mineral pool surrounded by sun loungers and scenic mountain views.',
    'Снимка на хотелска стая с двойно легло, бели възглавници и декоративни елементи.': 'Cozy luxury bedroom suite with plush king-size bed and alpine decor.',
    'Човешка ръка, държаща красиво цвете с 5 листа.': 'Pristine mountain flora and botanical wellness details.',
    'Термометър на СПА център с капка': 'Mineral thermal water temperature indicator.',
    'Интериор на СПА център с дървени сауни, каменен под, стъклени прегради и джакузи от дърво.': 'Thermal spa wellness sanctuary with cedar saunas, stone walkways, and wooden hydrotherapy baths.',
    'Професионален масаж в луксозен СПА център': 'Therapeutic restorative body massage at Shyadé Stone Cabin SPA.',
    'Медикъл СПА процедури в луксозен хотел': 'Revitalizing medical wellness and hydrotherapy treatments.',
    'Снимка на уютна хотелска стая в Парк Хотел Пирин, Сандански, с голямо двойно легло, меки възглавници, декоративно подреждане на кърпи и поднос с приготвена закуска. Стаята е с приглушено осветление и създава усещане за комфорт и релакс.': 'Cozy luxury room at Shyadé Stone Cabin with plush double bed, soft pillows, and breakfast service.',
    'Зелени листа с капки роса, подчертаващи свежестта на природата.': 'Fresh morning mountain foliage highlighting pure nature.',
    'СПА и уелнес център': 'Spa and Wellness Center',
    'Минерални басейни': 'Mineral Pools',
    'Фитнес': 'Fitness',
    'Ресторанти': 'Restaurants',
    'Конферентни зали': 'Conference Halls',
    'Детски кът': 'Kids’ Corner',
    'Безплатен Wi-Fi': 'Free Wi-Fi',
    'Сандански': 'Mountain Resort',
    'Област Благоевград': 'Mountain Valley',
    'Балкански ресторант': 'Alpine Gourmet Restaurant',
    'СПА център Пирин': 'Shyadé Mountain SPA Center',
    'Вътрешни и външни басейни': 'Indoor and Outdoor Mineral Pools',
    'Масажи и терапии': 'Massages and Holistic Therapies',
    'ВИП зона за двама': 'VIP Couples Wellness Suite',
    'Медикъл СПА': 'Medical SPA',
    'Козметични процедури': 'Beauty & Facial Treatments',
    'Работно време': 'Opening Hours',
    'Българска кухня': 'Artisan Cuisine',
    'Балканска кухня': 'Mountain Cuisine',
    'Интернационална кухня': 'International Cuisine',
    'Общи работни часове': 'General Opening Hours',
    'Резервации - ': 'Reservations - '
}

def process_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove promo-banner element
    soup = BeautifulSoup(html, 'html.parser')
    for banner in soup.find_all('div', class_='promo-banner'):
        banner.decompose()

    # 2. Update brandColor in window.site
    # replace brandColor: "#7f7f2e" with "#0F5132"
    html = str(soup)
    html = re.sub(r'brandColor:\s*["\']#7f7f2e["\']', 'brandColor: "#0F5132"', html)
    html = re.sub(r'textColor:\s*["\']#ffffff["\']', 'textColor: "#C8A27A"', html)

    # 3. Replace all Bulgarian and old brand occurrences
    for k, v in CYRILLIC_REPLACEMENTS.items():
        html = html.replace(k, v)

    # 4. Clean up any remaining Park Hotel Pirin mentions
    html = re.sub(r'Park\s+Hotel\s+Pirin', 'Shyadé Stone Cabin', html, flags=re.I)
    html = re.sub(r'Park\s+Hotel\s+“Pirin”', 'Shyadé Stone Cabin', html, flags=re.I)
    html = re.sub(r'Park\s+Hotel\s+„Pirin“', 'Shyadé Stone Cabin', html, flags=re.I)
    html = re.sub(r'Park\s+Hotel\s+\?Pirin\?', 'Shyadé Stone Cabin', html, flags=re.I)

    # 5. Fix titles
    if '<title>' in html:
        html = re.sub(
            r'<title>[^<]*</title>',
            '<title>Shyadé Stone Cabin – Luxury Mountain Resort &amp; SPA</title>',
            html,
            count=1
        )

    # 6. Update desktop navbar style to reflect emerald and gold colors
    new_style = """
<style id="desktop-navbar-style">
/* Shyadé Stone Cabin - Emerald & Gold Desktop Navbar */
.desktop-nav-menu {
  display: none;
}

.promo-banner {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
}

@media screen and (min-width: 992px) {
  .nav-menu-button {
    display: none !important;
  }
  
  .nav-wrapper {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 1rem 2.5rem !important;
  }
  
  .nav-menu-button-wrapper {
    display: none !important;
  }
  
  .nav-logo-link {
    order: 1 !important;
    flex: 0 0 auto !important;
    width: auto !important;
    max-width: 175px !important;
    padding: 0 !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center !important;
  }
  
  .logo-nav {
    max-width: 170px !important;
    width: auto !important;
    height: auto !important;
  }
  
  .desktop-nav-menu {
    order: 2 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 2rem !important;
    flex: 1 1 auto !important;
    margin: 0 2rem !important;
  }
  
  .desktop-nav-link {
    color: inherit;
    font-family: "Manrope", sans-serif;
    font-size: 0.88rem;
    font-weight: 600;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 0.35rem 0.1rem;
    position: relative;
    transition: opacity 0.25s ease, color 0.25s ease;
    white-space: nowrap;
    display: inline-block;
  }
  
  .desktop-nav-link:hover {
    color: #C8A27A !important;
  }
  
  .desktop-nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0%;
    height: 2px;
    background-color: #C8A27A;
    transition: width 0.25s cubic-bezier(0.25, 1, 0.5, 1);
  }
  
  .desktop-nav-link:hover::after {
    width: 100%;
  }
  
  .button-group_nav {
    order: 3 !important;
    flex: 0 0 auto !important;
    display: flex !important;
    align-items: center !important;
    gap: 1.5rem !important;
    margin-top: 0 !important;
  }
  
  .button-group_nav .button, .button-group_nav .button.w-button {
    background-color: #C8A27A !important;
    border: 1px solid #C8A27A !important;
    color: #082A1A !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15) !important;
  }
  
  .button-group_nav .button:hover, .button-group_nav .button.w-button:hover {
    background-color: #0F5132 !important;
    border-color: #C8A27A !important;
    color: #FFFFFF !important;
  }
}

@media screen and (max-width: 991px) {
  .desktop-nav-menu {
    display: none !important;
  }
  .nav-menu-button {
    display: flex !important;
  }
}
</style>
"""
    if 'id="desktop-navbar-style"' in html:
        html = re.sub(r'<style id="desktop-navbar-style">.*?</style>', new_style, html, flags=re.DOTALL)
    else:
        html = html.replace('</head>', f'{new_style}\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

count = 0
for root, dirs, files in os.walk(WORKSPACE):
    for f in files:
        if f.endswith('.html'):
            fpath = os.path.join(root, f)
            process_html_file(fpath)
            count += 1

print(f'Processed, rebranded, and cleaned {count} HTML files!')

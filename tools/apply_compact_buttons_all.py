import os
import re

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
CSS_FILE = os.path.join(WORKSPACE, 'assets', 'css', 'pirin.webflow.css')

# 1. Update pirin.webflow.css
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old button override blocks if present
css = re.sub(r'/\* Clean & Minimal Compact Buttons \*/.*', '', css, flags=re.DOTALL)

compact_button_rules = """
/* Clean & Minimal Compact Buttons */
.button, 
.button.w-button {
  font-family: 'Manrope', Arial, sans-serif !important;
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  padding: 0.45rem 1.15rem !important; /* COMPACT & MINIMAL */
  border-radius: 4px !important;       /* SLEEK RADIUS */
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  line-height: 1.25 !important;
  transition: all 0.25s cubic-bezier(0.25, 1, 0.5, 1) !important;
  box-shadow: none !important;
  text-decoration: none !important;
  cursor: pointer !important;
}

/* Primary Solid Button (e.g. Book Now) */
.button:not(.is-secondary):not(.is-link):not(.is-tertiary),
.button.is-alternate:not(.is-secondary),
.button-group_nav .button {
  background-color: #C8A27A !important;
  border: 1px solid #C8A27A !important;
  color: #082A1A !important;
}

.button:not(.is-secondary):not(.is-link):not(.is-tertiary):hover,
.button.is-alternate:not(.is-secondary):hover,
.button-group_nav .button:hover {
  background-color: #0F5132 !important;
  border-color: #0F5132 !important;
  color: #FFFFFF !important;
}

/* Secondary / Outline Ghost Button (e.g. Check Out The Rooms) */
.button.is-secondary,
.button.is-secondary.is-alternate {
  background-color: transparent !important;
  border: 1px solid rgba(255, 255, 255, 0.75) !important;
  color: #FFFFFF !important;
  backdrop-filter: blur(4px) !important;
}

.button.is-secondary:hover,
.button.is-secondary.is-alternate:hover {
  background-color: #C8A27A !important;
  border-color: #C8A27A !important;
  color: #082A1A !important;
}

/* On light sections, secondary button has dark emerald border */
.background-color-secondary .button.is-secondary,
.section_header127 .button.is-secondary,
.section_product11 .button.is-secondary {
  border: 1px solid #0F5132 !important;
  color: #0F5132 !important;
}

.background-color-secondary .button.is-secondary:hover,
.section_header127 .button.is-secondary:hover,
.section_product11 .button.is-secondary:hover {
  background-color: #0F5132 !important;
  border-color: #0F5132 !important;
  color: #FFFFFF !important;
}

/* Small Buttons (newsletter, cookies, etc.) */
.button.is-small {
  padding: 0.35rem 0.95rem !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.08em !important;
}

/* Button Group spacing */
.button-group {
  gap: 0.85rem !important;
}
"""

css += '\n' + compact_button_rules
with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated pirin.webflow.css with compact minimal button rules!')

# 2. Update all HTML files with inline style tag for guaranteed priority
html_files = [os.path.join(WORKSPACE, 'index.html')]
for root, dirs, files in os.walk(os.path.join(WORKSPACE, 'en')):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

STYLE_TAG = f"<style id='minimal-compact-buttons'>{compact_button_rules}</style>"

count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="minimal-compact-buttons"' in content or "id='minimal-compact-buttons'" in content:
        content = re.sub(r'<style id=[\'"]minimal-compact-buttons[\'"]>.*?</style>', STYLE_TAG, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'{STYLE_TAG}\n</head>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1

print(f'Applied minimal compact buttons to {count} HTML files!')

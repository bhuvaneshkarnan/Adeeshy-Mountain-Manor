import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

WORKSPACE = r'e:\Clients\Website\From Sathesh bro\adeesymountainmanor'
IMG_DIR = os.path.join(WORKSPACE, 'assets', 'images')
ARTIFACT_DIR = r'C:\Users\bhuva\.gemini\antigravity\brain\15e53f08-6a83-4c12-a200-a1a3d73e0ee1'

# 1. Create Adeeshy Mountain Manor Logo in SVG
# Bright, crisp, high-contrast white & gold
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 110" width="320" height="110">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E5D1B8" />
      <stop offset="50%" stop-color="#C8A27A" />
      <stop offset="100%" stop-color="#A47E52" />
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>
  <!-- Luxury Monogram Crest -->
  <g transform="translate(160, 22)" stroke="url(#goldGrad)" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" filter="url(#shadow)">
    <!-- Elegant outer oval / diamond silhouette -->
    <path d="M 0,-16 C 14,-16 22,-7 24,0 C 22,7 14,16 0,16 C -14,16 -22,7 -24,0 C -22,-7 -14,-16 0,-16 Z" />
    <!-- Inner mountain / manor crest -->
    <path d="M -12,4 L -4,-8 L 0,-2 L 4,-8 L 12,4" />
    <circle cx="0" cy="-10" r="1.5" fill="#C8A27A" stroke="none" />
  </g>
  <!-- Main Name: ADEESHY -->
  <text x="160" y="74" text-anchor="middle" fill="#FFFFFF" font-family="'PP Right Gothic Wide', 'Playfair Display', 'Cinzel', serif" font-size="28" font-weight="600" letter-spacing="4" filter="url(#shadow)">ADEESHY</text>
  <!-- Subtitle: MOUNTAIN MANOR -->
  <text x="160" y="98" text-anchor="middle" fill="#C8A27A" font-family="'Manrope', sans-serif" font-size="10.5" font-weight="600" letter-spacing="5" filter="url(#shadow)">MOUNTAIN MANOR</text>
</svg>"""

with open(os.path.join(IMG_DIR, 'adeeshy-mountain-manor-logo.svg'), 'w', encoding='utf-8') as f:
    f.write(logo_svg)

# Also update the original logo file so any script/reference picks it up
orig_logo_name = '67a4016fe500e14a4d5340d2_a3b61caacd33aaa535f422454da4713e_pirin-logo-full.svg'
with open(os.path.join(IMG_DIR, orig_logo_name), 'w', encoding='utf-8') as f:
    f.write(logo_svg)

print('Saved adeeshy-mountain-manor-logo.svg!')

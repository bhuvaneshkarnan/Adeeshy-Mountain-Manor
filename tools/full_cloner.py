import os
import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import concurrent.futures
import time
import json

BASE_URL = 'https://www.parkhotelpirin.com'
WORKSPACE = os.path.dirname(os.path.abspath(__file__))
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Directories
DIRS = {
    'css': os.path.join(WORKSPACE, 'assets', 'css'),
    'js': os.path.join(WORKSPACE, 'assets', 'js'),
    'fonts': os.path.join(WORKSPACE, 'assets', 'fonts'),
    'images': os.path.join(WORKSPACE, 'assets', 'images'),
}
for d in DIRS.values():
    os.makedirs(d, exist_ok=True)

# 1. Target English pages
with open(r'C:\Users\bhuva\.gemini\antigravity\brain\15e53f08-6a83-4c12-a200-a1a3d73e0ee1\.system_generated\tasks\task-38.log', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

en_links = sorted(list(set(l.strip() for l in lines if l.strip().startswith('/en'))))
print(f'Total target English pages to clone: {len(en_links)}')

# 2. Key CSS & JS Assets to download
CSS_ASSETS = {
    'pirin.webflow.css': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/css/pirin.webflow.shared.99ba5304b.min.css',
    'swiper-bundle.min.css': 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css',
}

JS_ASSETS = {
    'jquery.min.js': 'https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=67a4016fe500e14a4d533ee6',
    'webflow.schunk.1.js': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/js/webflow.schunk.36b8fb49256177c8.js',
    'webflow.schunk.2.js': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/js/webflow.schunk.49020ff84dc17de6.js',
    'webflow.js': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/js/webflow.c29773b2.29a50882d06a41af.js',
    'gsap.min.js': 'https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js',
    'ScrollTrigger.min.js': 'https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js',
    'barba.min.js': 'https://cdn.jsdelivr.net/npm/@barba/core',
    'barba-prefetch.min.js': 'https://cdn.jsdelivr.net/npm/@barba/prefetch',
    'lenis.min.js': 'https://unpkg.com/lenis@1.2.3/dist/lenis.min.js',
    'dev-46.js': 'https://cdn.jsdelivr.net/gh/kall0m/kall0m.github.io@latest/src/dev-46.js',
    'swiper-bundle.min.js': 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js',
}

FONT_ASSETS = {
    'PPRightGothic-WideLight.woff2': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/67a40204b3f4efe8cf0effd9_PPRightGothic-WideLight.woff2',
    'Manrope-Regular.woff2': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/67a402312ece8444d0211190_Manrope-Regular.woff2',
    'Manrope-Bold.woff2': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/67a402428c364a6c442596f6_Manrope-Bold.woff2',
    'Manrope-RegularItalic.woff2': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/67b5f9be0bdb93ec0c5cec2e_Manrope-RegularItalic.woff2',
    'Manrope-BoldItalic.woff2': 'https://cdn.prod.website-files.com/67a4016fe500e14a4d533ee6/67b5f9c7a2353898cfb4cfd3_Manrope-BoldItalic.woff2',
}

def download_file(url, out_path):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
        return out_path, True
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(out_path, 'wb') as f:
                f.write(data)
            return out_path, True
    except Exception as e:
        print(f'Failed to download {url}: {e}')
        return out_path, False

print('Downloading CSS assets...')
for fname, url in CSS_ASSETS.items():
    download_file(url, os.path.join(DIRS['css'], fname))

print('Downloading JS assets...')
for fname, url in JS_ASSETS.items():
    download_file(url, os.path.join(DIRS['js'], fname))

print('Downloading Fonts...')
for fname, url in FONT_ASSETS.items():
    download_file(url, os.path.join(DIRS['fonts'], fname))

# Rewrite pirin.webflow.css font paths to local relative paths
css_path = os.path.join(DIRS['css'], 'pirin.webflow.css')
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    # Replace CDN font URLs with local relative font URLs
    for font_file, font_url in FONT_ASSETS.items():
        css_content = css_content.replace(font_url, f'../fonts/{font_file}')
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print('Updated pirin.webflow.css font paths.')

# 3. Fetch all HTML pages concurrently
print('Fetching all HTML pages...')
pages_raw = {}
def fetch_page(path):
    url = BASE_URL + path
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return path, resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f'Error fetching {url}: {e}')
        return path, None

with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
    for path, content in executor.map(fetch_page, en_links):
        if content:
            pages_raw[path] = content

print(f'Successfully fetched {len(pages_raw)} / {len(en_links)} pages!')

# 4. Collect all unique image URLs
image_urls = set()
for path, html in pages_raw.items():
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and src.startswith('http'):
            image_urls.add(src)
        srcset = img.get('srcset')
        if srcset:
            for part in srcset.split(','):
                s = part.strip().split(' ')[0]
                if s and s.startswith('http'):
                    image_urls.add(s)
    for link in soup.find_all('link', rel=lambda r: r and any(x in r for x in ['icon', 'apple-touch-icon'])):
        href = link.get('href')
        if href and href.startswith('http'):
            image_urls.add(href)
    # Background images in inline style
    for el in soup.find_all(style=re.compile(r'url\(')):
        m = re.findall(r'url\(([^)]+)\)', el.get('style', ''))
        for u in m:
            u = u.strip('"\'')
            if u.startswith('http'):
                image_urls.add(u)

print(f'Discovered {len(image_urls)} unique image URLs to download.')

# Map each URL to a safe local filename
url_to_local_file = {}
for u in image_urls:
    parsed = urllib.parse.urlparse(u)
    base = os.path.basename(parsed.path)
    if not base or '.' not in base:
        base = f'img_{abs(hash(u))}.webp'
    # Ensure safe filename
    safe_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', base)
    url_to_local_file[u] = safe_name

# Download images concurrently
print('Downloading images in parallel...')
def download_image_task(item):
    url, filename = item
    dest = os.path.join(DIRS['images'], filename)
    return download_file(url, dest)

with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
    results = list(executor.map(download_image_task, url_to_local_file.items()))

success_count = sum(1 for _, ok in results if ok)
print(f'Successfully downloaded {success_count} / {len(url_to_local_file)} images!')

# 5. Process and rewrite HTML for each page
def process_html(html_str, current_path):
    soup = BeautifulSoup(html_str, 'html.parser')

    # Remove bot detection script
    for s in soup.find_all('script', src=re.compile(r'/haqt6iy0yx2e|BoIS8CLfAeqiHvsTbPuTnr0GkHE')):
        s.decompose()

    # Rewrite CSS links
    for l in soup.find_all('link', rel='stylesheet'):
        href = l.get('href', '')
        if 'pirin.webflow.shared' in href:
            l['href'] = '/assets/css/pirin.webflow.css'
        elif 'swiper-bundle' in href:
            l['href'] = '/assets/css/swiper-bundle.min.css'

    # Rewrite Favicons
    for l in soup.find_all('link', rel=lambda r: r and any(x in r for x in ['icon', 'apple-touch-icon'])):
        href = l.get('href', '')
        if href in url_to_local_file:
            l['href'] = f'/assets/images/{url_to_local_file[href]}'

    # Rewrite JS scripts
    for s in soup.find_all('script'):
        src = s.get('src', '')
        if 'jquery-3.5.1' in src:
            s['src'] = '/assets/js/jquery.min.js'
        elif 'webflow.schunk.36b8fb49256177c8' in src:
            s['src'] = '/assets/js/webflow.schunk.1.js'
        elif 'webflow.schunk.49020ff84dc17de6' in src:
            s['src'] = '/assets/js/webflow.schunk.2.js'
        elif 'webflow.c29773b2' in src:
            s['src'] = '/assets/js/webflow.js'
        elif 'gsap.min.js' in src:
            s['src'] = '/assets/js/gsap.min.js'
        elif 'ScrollTrigger.min.js' in src:
            s['src'] = '/assets/js/ScrollTrigger.min.js'
        elif '@barba/core' in src:
            s['src'] = '/assets/js/barba.min.js'
        elif '@barba/prefetch' in src:
            s['src'] = '/assets/js/barba-prefetch.min.js'
        elif 'lenis' in src:
            s['src'] = '/assets/js/lenis.min.js'
        elif 'dev-46.js' in src:
            s['src'] = '/assets/js/dev-46.js'
        elif 'swiper-bundle' in src:
            s['src'] = '/assets/js/swiper-bundle.min.js'

    # Rewrite images (src and srcset)
    for img in soup.find_all('img'):
        src = img.get('src')
        if src in url_to_local_file:
            img['src'] = f'/assets/images/{url_to_local_file[src]}'
        srcset = img.get('srcset')
        if srcset:
            parts = []
            for part in srcset.split(','):
                part = part.strip()
                if not part:
                    continue
                tokens = part.split(' ')
                u = tokens[0]
                size = tokens[1] if len(tokens) > 1 else ''
                if u in url_to_local_file:
                    local_url = f'/assets/images/{url_to_local_file[u]}'
                    parts.append(f'{local_url} {size}'.strip())
                else:
                    parts.append(part)
            img['srcset'] = ', '.join(parts)

    # Rewrite background images in style
    for el in soup.find_all(style=re.compile(r'url\(')):
        style = el.get('style', '')
        for orig_url, safe_fname in url_to_local_file.items():
            if orig_url in style:
                style = style.replace(orig_url, f'/assets/images/{safe_fname}')
        el['style'] = style

    # Fix links
    for a in soup.find_all('a', href=True):
        href = a['href']
        # External domain to local path
        if 'parkhotelpirin.com' in href:
            parsed = urllib.parse.urlparse(href)
            href = parsed.path
        if href == '/' or href == '/en' or href == '/en/':
            a['href'] = '/en/'
        elif href.startswith('/en/'):
            # Ensure trailing slash for directory resolution in static servers
            path_part = href.split('?')[0].split('#')[0]
            query_part = ('?' + href.split('?')[1]) if '?' in href else ''
            hash_part = ('#' + href.split('#')[1]) if '#' in href else ''
            if not path_part.endswith('/') and '.' not in os.path.basename(path_part):
                path_part += '/'
            a['href'] = path_part + query_part + hash_part

    return str(soup)

print('Processing and saving HTML pages...')
saved_count = 0
for path, html in pages_raw.items():
    processed = process_html(html, path)
    clean_path = path.strip('/')
    if not clean_path or clean_path == 'en':
        target_dir = os.path.join(WORKSPACE, 'en')
    else:
        target_dir = os.path.join(WORKSPACE, clean_path)
    os.makedirs(target_dir, exist_ok=True)
    out_file = os.path.join(target_dir, 'index.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(processed)
    saved_count += 1

# Also write root index.html from /en
if '/en' in pages_raw:
    root_html = process_html(pages_raw['/en'], '/en')
    with open(os.path.join(WORKSPACE, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(root_html)
    print('Wrote root index.html!')

print(f'Successfully processed and wrote {saved_count} pages!')

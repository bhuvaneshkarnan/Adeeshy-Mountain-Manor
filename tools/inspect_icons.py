import os
import re

for f in [
    '67cd8e846041daac257841c4_icon-flower-5570433.svg',
    '67cd8e9c6027fcffa3796643_icon-thermometer-6424700.svg',
    '67cd8e7e3ef92e0b18b371cc_icon-body-6928133.svg',
    '67cd8e9e7fd3b5efa1b3f6af_icon-yoga-5570486.svg'
]:
    p = os.path.join('assets/images', f)
    content = open(p, 'r', encoding='utf-8').read()
    fills = re.findall(r'fill="([^"]+)"', content)
    strokes = re.findall(r'stroke="([^"]+)"', content)
    print(f'{f}: fills={set(fills)}, strokes={set(strokes)}')
    # If no fill or stroke specified, SVG defaults to fill="#000000" (black)!
    has_fill = 'fill=' in content
    has_stroke = 'stroke=' in content
    print(f'   has_fill={has_fill}, has_stroke={has_stroke}')

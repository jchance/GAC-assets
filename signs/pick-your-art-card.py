"""Build the pick-your-art table card as an SVG with live, editable text.

Half letter landscape (612 x 396 pt), no bleed. It lies flat on the
membership table among the Artist Trading Cards on their easels.
Run it from script/build-signs, or directly:

    python3 signs/pick-your-art-card.py OUT.svg
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGOS = HERE.parent / "images" / "logos"
out = Path(sys.argv[1])
NAVY, TEAL, CORAL, GOLD = "#162B48", "#00A89C", "#F26A51", "#F9C646"
FF = "FatFrank-Heavy, FatFrank, sans-serif"
BOOK = "RuckSack-Book, RuckSack, sans-serif"
DEMI = "RuckSack-Demi, RuckSack, sans-serif"

logo_svg = (LOGOS / "Arts Council Logo - Color Stacked.svg").read_text()
vb_w = float(re.search(r'viewBox="0 0 ([\d.]+)', logo_svg).group(1))
logo_body = re.search(r"<svg[^>]*>(.*)</svg>", logo_svg, re.S).group(1).strip()
LOGO_W = 100
LOGO_X = LOGO_Y = 28.8 + 0.28 * LOGO_W
TX = LOGO_X + LOGO_W + 0.28 * LOGO_W   # text column, one clear space from the logo

def t(x, y, s, fam, size, fill, weight, spacing=None, opacity=None, anchor=None):
    a = f'x="{x:.2f}" y="{y:.2f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" fill="{fill}"'
    if spacing: a += f' letter-spacing="{spacing}"'
    if opacity: a += f' fill-opacity="{opacity}"'
    if anchor: a += f' text-anchor="{anchor}"'
    return f'    <text {a}>{s}</text>'

BAND_Y, BAND_B = 222, 367.2
STEPS = [
    ("1", "SCAN", ["Join with the QR code", "on the sign."]),
    ("2", "PICK", ["Choose one card", "from the easels."]),
    ("3", "KEEP", ["It\u2019s yours to", "take home."]),
]
col_w = (583.2 - 28.8) / 3

L = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg xmlns="http://www.w3.org/2000/svg" width="8.5in" height="5.5in" viewBox="0 0 612 396">',
     '  <title>Griffin Arts Council pick-your-art table card</title>',
     '  <!-- Half letter landscape, no bleed. Live text: FatFrank Heavy, RuckSack Book and Demi (Adobe Fonts). -->',
     '  <rect id="paper" width="612" height="396" fill="#ffffff"/>',
     f'  <g id="logo" transform="translate({LOGO_X:.2f} {LOGO_Y:.2f}) scale({LOGO_W / vb_w:.6f})">',
     '    ' + logo_body, '  </g>',
     '  <g id="headline">',
     t(TX, 76, "JOIN TODAY", FF, 46, NAVY, 900),
     t(TX, 120, "PICK YOUR ART", FF, 46, CORAL, 900),
     '  </g>',
     f'  <text id="supporting-line" font-family="{DEMI}" font-size="16" font-weight="600" fill="{NAVY}">',
     f'    <tspan x="{TX:.2f}" y="152">Every new member takes home one original</tspan>',
     f'    <tspan x="{TX:.2f}" y="173">Artist Trading Card by a local artist.</tspan>',
     '  </text>',
     '  <g id="color-stripe">',
     f'    <rect x="28.8" y="{BAND_Y - 8}" width="184.8" height="8" fill="{TEAL}"/>',
     f'    <rect x="213.6" y="{BAND_Y - 8}" width="184.8" height="8" fill="{CORAL}"/>',
     f'    <rect x="398.4" y="{BAND_Y - 8}" width="184.8" height="8" fill="{GOLD}"/>',
     '  </g>',
     f'  <rect id="navy-band" x="28.8" y="{BAND_Y}" width="554.4" height="{BAND_B - BAND_Y:.2f}" fill="{NAVY}"/>',
     '  <g id="steps">']
for i, (n, head, sub) in enumerate(STEPS):
    x0 = 28.8 + i * col_w + 22
    L.append(t(x0 + 6, 304, n, FF, 56, GOLD, 900))
    L.append(t(x0 + 52, 282, head, FF, 21, "#ffffff", 900, spacing=0.3))
    for j, line in enumerate(sub):
        L.append(t(x0 + 52, 302 + j * 16, line, BOOK, 12.5, "#ffffff", 400))
L += ['  </g>',
      '</svg>', '']
out.write_text("\n".join(L)); print(out)

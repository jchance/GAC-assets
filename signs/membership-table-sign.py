"""Build the membership table sign as an SVG with live, editable text.

US Letter portrait (612 x 792 pt), no bleed, for a vertical acrylic
tabletop holder. Run it from script/build-signs, or directly:

    python3 signs/membership-table-sign.py OUT.svg
"""
import base64
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGOS = HERE.parent / "images" / "logos"
out = Path(sys.argv[1])

NAVY, TEAL, CORAL, GOLD = "#162B48", "#00A89C", "#F26A51", "#F9C646"

FATFRANK = "FatFrank-Heavy, FatFrank, sans-serif"
RUCK_BOOK = "RuckSack-Book, RuckSack, sans-serif"
RUCK_DEMI = "RuckSack-Demi, RuckSack, sans-serif"
RUCK_BOLD = "RuckSack-Bold, RuckSack, sans-serif"

# Logo: inline its paths, scaled into the measured box.
logo_svg = (LOGOS / "Arts Council Logo - Color Stacked.svg").read_text()
logo_vb_w = float(re.search(r'viewBox="0 0 ([\d.]+)', logo_svg).group(1))
logo_body = re.search(r"<svg[^>]*>(.*)</svg>", logo_svg, re.S).group(1).strip()
logo = dict(x=43.2, y=66.43, w=151.2)
logo_scale = logo["w"] / logo_vb_w

# Ghost G-mark: the complete G-logo, every shape in white, at 10% on the navy panel.
ghost_svg = (LOGOS / "Arts Council Logo - Color G-Logo.svg").read_text()
ghost_vb_w = float(re.search(r'viewBox="0 0 ([\d.]+)', ghost_svg).group(1))
ghost_body = re.search(r"<svg[^>]*>(.*)</svg>", ghost_svg, re.S).group(1)
ghost_shapes = [re.sub(r'style="fill:[^;"]*;?"', 'fill="#ffffff"', s)
                for s in re.findall(r"<(?:path|rect)\b[^>]*/>", ghost_body)]
assert ghost_shapes and all('fill="#ffffff"' in s for s in ghost_shapes)
GHOST = dict(x=454, y=534.8, w=109)
ghost_scale = GHOST["w"] / ghost_vb_w

# QR: inline its path. The file's path is in module units, 29 modules wide.
qr_svg = (HERE.parent / "images" / "qr-codes" / "GAC QR Code - Membership Signup.svg").read_text()
qr_d = re.search(r'<path fill-rule="evenodd" d="([^"]+)"', qr_svg).group(1)
qr_img = dict(x=67.68, y=546.49, w=185.04)
qr_scale = qr_img["w"] / 29

# Photo: embed the JPEG, cropped like CSS cover at 50% 42%.
photo_bytes = (HERE / "art-club-tiny-canvases.jpg").read_bytes()
photo_b64 = base64.b64encode(photo_bytes).decode()
img_w_px, img_h_px = 2000, 1600
PHOTO_TOP = 318
box = dict(x=28.8, y=PHOTO_TOP, w=554.4, h=504.93 - PHOTO_TOP)
scale = max(box["w"] / img_w_px, box["h"] / img_h_px)
pw, ph = img_w_px * scale, img_h_px * scale
px = box["x"] + (box["w"] - pw) * 0.5
py = box["y"] + (box["h"] - ph) * 0.42


def text(x, y, s, family, size, fill, weight=None, spacing=None, opacity=None, ident=None):
    attrs = [f'x="{x}"', f'y="{y}"', f'font-family="{family}"', f'font-size="{size}"', f'fill="{fill}"']
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if spacing:
        attrs.append(f'letter-spacing="{spacing}"')
    if opacity:
        attrs.append(f'fill-opacity="{opacity}"')
    if ident:
        attrs.insert(0, f'id="{ident}"')
    return f'    <text {" ".join(attrs)}>{s}</text>'


# Member benefits: two columns between the header and the photo.
B_HEAD_Y, B_LEAD, B_FIRST = 238, 19, 259
COLS = [
    (43.2, "WHAT YOU GET", [
        "Calls for artists and show openings",
        "First word on new shows and classes",
        "Monthly Art Club dates and places",
    ]),
    (322, "YOUR SUPPORT HELPS", [
        "Keep community classes free or low cost",
        "Create opportunities for local artists",
        "Cover the GAC\u2019s operating costs",
    ]),
]
BULLETS = [TEAL, CORAL, GOLD]


def benefits_group():
    out = ['  <g id="benefits">']
    for ci, (x, head, items) in enumerate(COLS):
        out.append(text(x, B_HEAD_Y, head, FATFRANK, 17, CORAL if ci == 0 else TEAL, weight=900, spacing=0.4))
        for i, item in enumerate(items):
            y = B_FIRST + i * B_LEAD
            out.append(f'    <rect x="{x}" y="{y - 7.5}" width="6" height="6" fill="{BULLETS[i % 3]}"/>')
            out.append(text(x + 14, y, item, RUCK_DEMI, 13, NAVY, weight=600))
    out.append("  </g>")
    return out


lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"',
    '     width="8.5in" height="11in" viewBox="0 0 612 792">',
    "  <title>Griffin Arts Council membership table sign</title>",
    "  <!-- US Letter, no bleed. Text is live: FatFrank (heavy weight) and RuckSack (Book, Demi, Bold) from Adobe Fonts. -->",
    "  <defs>",
    f'    <clipPath id="photo-crop"><rect x="{box["x"]}" y="{box["y"]}" width="{box["w"]}" height="{box["h"]}"/></clipPath>',
    '    <clipPath id="panel-crop"><rect x="28.8" y="514.81" width="554.4" height="248.39"/></clipPath>',
    "  </defs>",
    '  <rect id="paper" width="612" height="792" fill="#ffffff"/>',
    "",
    f'  <g id="logo" transform="translate({logo["x"]} {logo["y"]}) scale({logo_scale:.6f})">',
    "    " + logo_body,
    "  </g>",
    "",
    '  <g id="headline">',
    text(237.59, 88.95, "BECOME", FATFRANK, 56, NAVY, weight=900),
    text(237.59, 140.46, "A MEMBER", FATFRANK, 56, CORAL, weight=900),
    "  </g>",
    '  <text id="supporting-line" font-family="' + RUCK_DEMI + '" font-size="17" font-weight="600" fill="' + NAVY + '">',
    '    <tspan x="237.59" y="173.55">Support emerging artists and arts</tspan>',
    '    <tspan x="237.59" y="195.65">education in Griffin and Spalding County.</tspan>',
    "  </text>",
    "",
    *benefits_group(),
    "",
    '  <g id="photo" clip-path="url(#photo-crop)">',
    f'    <image x="{px:.2f}" y="{py:.2f}" width="{pw:.2f}" height="{ph:.2f}" preserveAspectRatio="none"',
    f'           xlink:href="data:image/jpeg;base64,{photo_b64}" href="data:image/jpeg;base64,{photo_b64}"/>',
    "  </g>",
    '  <g id="color-stripe">',
    f'    <rect x="28.8" y="504.93" width="184.8" height="9.88" fill="{TEAL}"/>',
    f'    <rect x="213.6" y="504.93" width="184.8" height="9.88" fill="{CORAL}"/>',
    f'    <rect x="398.4" y="504.93" width="184.8" height="9.88" fill="{GOLD}"/>',
    "  </g>",
    "",
    f'  <rect id="navy-panel" x="28.8" y="514.81" width="554.4" height="248.39" fill="{NAVY}"/>',
    '  <g id="ghost-mark" opacity="0.1" clip-path="url(#panel-crop)">',
    f'    <g transform="translate({GHOST["x"]} {GHOST["y"]}) scale({ghost_scale:.6f})">',
    *["      " + g for g in ghost_shapes],
    "    </g>",
    "  </g>",
    '  <rect id="qr-backing" x="57.6" y="536.41" width="205.2" height="205.2" fill="#ffffff"/>',
    f'  <path id="qr-code" transform="translate({qr_img["x"]} {qr_img["y"]}) scale({qr_scale:.6f})"',
    f'        fill-rule="evenodd" fill="#000000" d="{qr_d}"/>',
    "",
    '  <g id="scan-to-join">',
    text(291.59, 571.22, "SCAN", FATFRANK, 40, GOLD, weight=900),
    text(291.59, 608.02, "TO JOIN", FATFRANK, 40, GOLD, weight=900),
    "  </g>",
    '  <g id="levels">',
    text(291.59, 650.59, "$15", FATFRANK, 30, "#ffffff", weight=900),
    text(398.87, 650.96, "Student", RUCK_BOLD, 15, "#ffffff", weight=700, spacing=0.6),
    text(291.59, 681.79, "$30", FATFRANK, 30, "#ffffff", weight=900),
    text(398.87, 682.16, "Member", RUCK_BOLD, 15, "#ffffff", weight=700, spacing=0.6),
    text(291.59, 712.98, "$125", FATFRANK, 30, "#ffffff", weight=900),
    text(398.87, 713.36, "Patron", RUCK_BOLD, 15, "#ffffff", weight=700, spacing=0.6),
    "  </g>",
    text(291.59, 737.53, "Yearly memberships · griffinarts.org", RUCK_BOOK, 11, "#ffffff",
         weight=400, spacing=0.22, opacity=0.85, ident="footnote"),
    "</svg>",
    "",
]
out.write_text("\n".join(lines))
print(out, out.stat().st_size)

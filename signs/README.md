# Membership table signs

Print pieces for the membership table at GAC art shows. They aren't part of the assets site, and Jekyll skips this folder.

- **GAC Membership Table Sign**: 8.5 x 11 in, portrait, for the vertical acrylic holder. The QR code goes to the GiveButter membership campaign.
- **GAC Pick Your Art Card**: 8.5 x 5.5 in, landscape. It lies flat on the table among the Artist Trading Cards on their easels. The PDF prints two per letter sheet, so cut on the dashed line.

Both are made for a color laser printer, with no bleed. Print the PDFs at 100% (Actual Size).

## Files

| File | What it is |
| --- | --- |
| `GAC Membership Table Sign.pdf` | Ready to print |
| `GAC Membership Table Sign.svg` | Editable, with live text |
| `GAC Pick Your Art Card - 2 per page.pdf` | Ready to print, two per sheet |
| `GAC Pick Your Art Card.svg` | Editable, one card |
| `*- proof.png` | Quick previews |
| `membership-table-sign.py`, `pick-your-art-card.py` | The sources that write the SVGs |
| `membership-qr-code.svg` | The GiveButter QR code, on a white background |
| `art-club-tiny-canvases.jpg` | The Art Club photo on the sign, from the GAC site (`images/art-club/2026-10-11/finished-tiny-canvases.jpg`) |

The logos come straight from `images/logos/`, so the signs pick up any change to the official files.

## Fonts

The text uses FatFrank Heavy and RuckSack Book, Demi and Bold from the GAC's Adobe Fonts plan. Turn them on in Creative Cloud before you open an SVG in Illustrator or rebuild. Without them the text falls back to a plain sans serif.

## Changing a sign

For a quick one-off change, open the SVG in Illustrator and edit the text.

For a change you want to keep, like new prices, benefits or a new QR code, edit the matching `.py` file and rebuild:

```bash
script/build-signs
```

That rewrites the SVG, PDF and proof for both pieces. The build stops if a font didn't make it into the PDF. If you swap the QR code, scan the new proof with a phone before you print.

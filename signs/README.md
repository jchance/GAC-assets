# Sign sources

The sources for the signs on the assets site's [Signs page](https://assets.griffinarts.org/docs/documents/signs.html). Jekyll skips this folder, so none of it is published.

The finished files (PDFs, SVGs, proofs, and the page's share image) live in `images/signs/`, and the Signs page links to them.

| File | What it is |
| --- | --- |
| `membership-table-sign.py` | Writes the 8.5 × 11 in membership table sign |
| `pick-your-art-card.py` | Writes the 8.5 × 5.5 in pick-your-art card |
| `art-club-tiny-canvases.jpg` | The Art Club photo on the sign, from the GAC site (`images/art-club/2026-10-11/finished-tiny-canvases.jpg`) |

The logos come from `images/logos/` and the QR code from `images/qr-codes/GAC QR Code - Membership Signup.svg`, so the signs pick up any change to those files.

## Changing a sign

Edit the matching `.py` file, like for new prices, benefits, or wording, then rebuild:

```bash
script/build-signs
```

That rewrites the SVG, PDF, and proof for both signs, plus the share image, in `images/signs/`. The build needs Google Chrome, python3, poppler, and ImageMagick.

The text uses FatFrank Heavy and RuckSack Book, Demi, and Bold from the GAC's Adobe Fonts plan. Turn them on in Creative Cloud first. The build stops if a font didn't make it into a PDF.

If you swap the QR code, scan the new proof with a phone before you print.

#!/usr/bin/env python3
"""Build a Word letterhead template from a printed letterhead PDF.

The header and footer artwork are cropped from the PDF at 600 dpi, so the
Word file matches the PDF exactly and does not need the brand font installed.
Body text uses Georgia, which ships with Windows, macOS, and Google Docs.

Usage: letterhead_docx.py LETTERHEAD.pdf OUTPUT.docx

Requires python-docx (pip install python-docx) and pdftoppm (poppler).
"""

import subprocess
import sys
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_LINE_SPACING
from docx.shared import Inches, Pt

DPI = 600

# Crop boxes in inches: (left, top, width, height). These must match the
# positions in letterhead/letterhead.html.
HEADER_BOX = (1.0, 0.55, 6.5, 1.35)
FOOTER_BOX = (1.0, 10.15, 6.5, 0.35)

# Body text starts below the header rule and ends above the footer.
TOP_MARGIN = 2.35
BOTTOM_MARGIN = 1.25
SIDE_MARGIN = 1.0


def crop(pdf, box, out_prefix):
    left, top, width, height = (round(v * DPI) for v in box)
    subprocess.run(
        ["pdftoppm", "-r", str(DPI), "-png", "-singlefile",
         "-x", str(left), "-y", str(top), "-W", str(width), "-H", str(height),
         str(pdf), str(out_prefix)],
        check=True,
    )
    return Path(f"{out_prefix}.png")


def set_alt_text(inline_shape, text):
    doc_pr = inline_shape._inline.docPr
    doc_pr.set("descr", text)
    doc_pr.set("title", text)


def tight(paragraph):
    fmt = paragraph.paragraph_format
    fmt.space_before = Pt(0)
    fmt.space_after = Pt(0)
    fmt.line_spacing_rule = WD_LINE_SPACING.SINGLE


def build(pdf, out):
    with tempfile.TemporaryDirectory() as tmp:
        header_png = crop(pdf, HEADER_BOX, Path(tmp) / "header")
        footer_png = crop(pdf, FOOTER_BOX, Path(tmp) / "footer")

        doc = Document()

        normal = doc.styles["Normal"]
        normal.font.name = "Georgia"
        normal.font.size = Pt(11)
        normal.paragraph_format.space_after = Pt(11)
        normal.paragraph_format.line_spacing = 1.15

        section = doc.sections[0]
        section.page_width = Inches(8.5)
        section.page_height = Inches(11)
        section.left_margin = Inches(SIDE_MARGIN)
        section.right_margin = Inches(SIDE_MARGIN)
        section.top_margin = Inches(TOP_MARGIN)
        section.bottom_margin = Inches(BOTTOM_MARGIN)
        section.header_distance = Inches(HEADER_BOX[1])
        section.footer_distance = Inches(11 - FOOTER_BOX[1] - FOOTER_BOX[3])

        header_p = section.header.paragraphs[0]
        tight(header_p)
        set_alt_text(
            header_p.add_run().add_picture(str(header_png), width=Inches(HEADER_BOX[2])),
            "Griffin Arts Council logo, 109 S Hill St, Suite B, Griffin, GA 30223, hello@griffinarts.org, griffinarts.org",
        )

        footer_p = section.footer.paragraphs[0]
        tight(footer_p)
        set_alt_text(
            footer_p.add_run().add_picture(str(footer_png), width=Inches(FOOTER_BOX[2])),
            "Griffin Arts Council, Inc. is a 501(c)(3) public charity. EIN 42-5116046. "
            "Igniting creativity. Championing emerging artists.",
        )

        for text in [
            "Date",
            "Recipient Name\nOrganization\nStreet Address\nCity, State ZIP",
            "Dear Recipient Name,",
            "Letter text.",
            "Sincerely,",
        ]:
            p = doc.add_paragraph()
            lines = text.split("\n")
            run = p.add_run(lines[0])
            for line in lines[1:]:
                run.add_break()
                run = p.add_run(line)

        signature = doc.add_paragraph()
        signature.paragraph_format.space_before = Pt(36)
        signature.add_run("Name").add_break()
        signature.add_run("Title, Griffin Arts Council")

        doc.core_properties.title = "Griffin Arts Council Letterhead"
        doc.core_properties.author = "Griffin Arts Council"
        doc.save(out)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(Path(sys.argv[1]), Path(sys.argv[2]))

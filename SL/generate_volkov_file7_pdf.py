#!/usr/bin/env python3
"""
Genererar Volkovs "Fil 7" (2010) som PDF-handout.
Digitaliserat dokument från Stanford Libraries.
Output: SL/volkov_file7.pdf
"""

import os, math
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Fonts ──────────────────────────────────────────────────────────────────
FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Arial",        os.path.join(FONT_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold",   os.path.join(FONT_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic", os.path.join(FONT_DIR, "ariali.ttf")))
pdfmetrics.registerFont(TTFont("Courier-New",  os.path.join(FONT_DIR, "cour.ttf")))
pdfmetrics.registerFont(TTFont("Courier-Bold", os.path.join(FONT_DIR, "courbd.ttf")))

# ── Colours ────────────────────────────────────────────────────────────────
STANFORD_RED  = HexColor("#8C1515")
PAPER_BG      = HexColor("#f5f0e8")   # aged paper
INK_DARK      = HexColor("#1a1a1a")   # main ink
INK_FADED     = HexColor("#4a4035")   # faded typewriter
INK_LATER     = HexColor("#2c1a0e")   # darker ink, added later
GRAY_MID      = HexColor("#555555")
GRAY_LIGHT    = HexColor("#999999")
BORDER_LIGHT  = HexColor("#c8bfa8")
STAMP_RED     = HexColor("#b03020")
STAMP_BLUE    = HexColor("#1a3a6b")

PAGE_W, PAGE_H = A4
MARGIN_L = 72
MARGIN_R = 72
TEXT_W   = PAGE_W - MARGIN_L - MARGIN_R

OUTPUT = os.path.join(os.path.dirname(__file__), "volkov_file7.pdf")


# ── Helpers ────────────────────────────────────────────────────────────────

def aged_paper(c):
    """Fill page with aged paper colour."""
    c.setFillColor(PAPER_BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def stanford_lib_header(c, y):
    """Stanford Libraries digitization banner at top."""
    bar_h = 6
    c.setFillColor(STANFORD_RED)
    c.rect(0, y - bar_h, PAGE_W, bar_h, fill=1, stroke=0)

    c.setFillColor(STANFORD_RED)
    c.setFont("Arial-Bold", 11)
    c.drawString(MARGIN_L, y - bar_h - 22, "STANFORD UNIVERSITY LIBRARIES")

    c.setFont("Arial", 8)
    c.setFillColor(GRAY_MID)
    c.drawString(MARGIN_L, y - bar_h - 35,
                 "Green Library · Department of Special Collections & University Archives")

    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(0.5)
    c.line(MARGIN_L, y - bar_h - 44, PAGE_W - MARGIN_R, y - bar_h - 44)

    return y - bar_h - 56


def meta_box(c, x, y, w):
    """Digitization metadata box."""
    fields = [
        ("Samling:",        "Applied Physics — D. Volkov Research Materials (2003–2010)"),
        ("Dokument:",       "Fil 7  /  File 7  [sista i serien · final in series]"),
        ("Digitaliserat:",  "2024-03-12  ·  Stanford Libraries Digital Services"),
        ("Status:",         "Ej publicerat · Begränsat tillträde · Restricted Access"),
        ("Anmärkning:",     "Delvis svårläst original. Transkription ej utförd."),
    ]
    row_h = 16
    box_h = row_h * len(fields) + 14
    c.setFillColor(HexColor("#eee9de"))
    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(0.5)
    c.roundRect(x, y - box_h, w, box_h, 3, fill=1, stroke=1)

    cy = y - 9
    for label, value in fields:
        c.setFont("Arial-Bold", 7.5)
        c.setFillColor(GRAY_MID)
        c.drawString(x + 8, cy, label)
        c.setFont("Arial", 7.5)
        c.setFillColor(INK_DARK)
        c.drawString(x + 82, cy, value)
        cy -= row_h

    return y - box_h - 12


def wrap_text(text, font_name, font_size, max_w, c_obj):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if c_obj.stringWidth(test, font_name, font_size) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_section_label(c, text, x, y):
    """Small all-caps section label."""
    c.setFont("Arial-Bold", 7.5)
    c.setFillColor(STANFORD_RED)
    c.drawString(x, y, text.upper())
    c.setStrokeColor(STANFORD_RED)
    c.setLineWidth(0.4)
    label_w = c.stringWidth(text.upper(), "Arial-Bold", 7.5)
    c.line(x, y - 2, x + label_w, y - 2)
    return y - 12


def draw_crystal_sketch(c, cx, cy, size=55):
    """
    Simple geometric sketch of the crystal apparatus described in Fil 7.
    An irregular crystal mounted in a metal frame — impossible geometry.
    Drawn with thin dark lines on aged paper.
    """
    c.setStrokeColor(INK_FADED)
    c.setLineWidth(0.8)
    c.setFillColor(HexColor("#e8e0d0"))

    # Outer frame — rectangular with corner brackets
    fw = size * 1.6
    fh = size * 1.2
    fx = cx - fw / 2
    fy = cy - fh / 2
    c.rect(fx, fy, fw, fh, fill=0, stroke=1)

    # Corner brackets
    b = 8
    for bx, by in [(fx, fy + fh), (fx + fw, fy + fh), (fx, fy), (fx + fw, fy)]:
        c.setLineWidth(1.2)
        c.line(bx - b if bx > cx else bx, by, bx + b if bx < cx else bx, by)
        c.line(bx, by - b if by < cy else by, bx, by + b if by > cy else by)

    c.setLineWidth(0.7)

    # Crystal — irregular hexagonal form, slightly off-center
    # 6 points with uneven spacing to suggest "impossible" geometry
    import math
    points = []
    radii = [size*0.38, size*0.45, size*0.32, size*0.48, size*0.30, size*0.43]
    for i, r in enumerate(radii):
        angle = math.radians(i * 60 + 15)
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))

    # Fill crystal lightly
    c.setFillColor(HexColor("#d8d4c8"))
    path = c.beginPath()
    path.moveTo(*points[0])
    for p in points[1:]:
        path.lineTo(*p)
    path.close()
    c.drawPath(path, fill=1, stroke=1)

    # Internal lines — facets
    c.setLineWidth(0.4)
    c.setStrokeColor(INK_FADED)
    for i in range(len(points)):
        if i % 2 == 0:
            c.line(cx, cy, *points[i])

    # Mounting bolts — 4 points on frame
    bolt_r = 3
    for bx, by in [
        (fx + fw * 0.25, fy),
        (fx + fw * 0.75, fy),
        (fx + fw * 0.25, fy + fh),
        (fx + fw * 0.75, fy + fh),
    ]:
        c.setFillColor(INK_FADED)
        c.circle(bx, by, bolt_r, fill=1, stroke=0)
        c.setFillColor(HexColor("#c0b89a"))
        c.circle(bx, by, bolt_r - 1, fill=1, stroke=0)

    # Measurement arrow and label "247 Hz ?"
    arrow_x = cx + fw / 2 + 12
    c.setStrokeColor(INK_FADED)
    c.setLineWidth(0.6)
    c.line(arrow_x, cy - size * 0.4, arrow_x, cy + size * 0.4)
    c.line(arrow_x - 4, cy - size * 0.4 + 4, arrow_x, cy - size * 0.4)
    c.line(arrow_x + 4, cy - size * 0.4 + 4, arrow_x, cy - size * 0.4)
    c.line(arrow_x - 4, cy + size * 0.4 - 4, arrow_x, cy + size * 0.4)
    c.line(arrow_x + 4, cy + size * 0.4 - 4, arrow_x, cy + size * 0.4)

    c.setFont("Courier-New", 7)
    c.setFillColor(INK_FADED)
    c.drawString(arrow_x + 6, cy - 4, "247 Hz ?")

    # Small question marks near impossible geometry intersection
    c.setFont("Courier-New", 8)
    c.setFillColor(INK_DARK)
    c.drawString(cx - 5, cy - 4, "?")


# ── Main content ───────────────────────────────────────────────────────────

def generate():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Volkov – Fil 7 – Stanford Libraries")
    c.setAuthor("Stanford University Libraries")

    # ── PAGE 1 ──────────────────────────────────────────────────────────────
    aged_paper(c)

    y = PAGE_H - 48
    y = stanford_lib_header(c, y)
    y -= 8
    y = meta_box(c, MARGIN_L, y, TEXT_W)
    y -= 14

    # Ruled lines background (notebook feel)
    c.setStrokeColor(HexColor("#ddd5c0"))
    c.setLineWidth(0.3)
    rule_y = y
    while rule_y > 55:
        c.line(MARGIN_L - 10, rule_y, PAGE_W - MARGIN_R + 10, rule_y)
        rule_y -= 18

    # ── SECTION 1: Date / origin ───────────────────────────────────────────
    y = draw_section_label(c, "Datum & ursprung", MARGIN_L, y)

    c.setFont("Courier-New", 9.5)
    c.setFillColor(INK_FADED)
    for line in [
        "D. Volkov  —  Applied Physics Lab, Stanford University",
        "Notebook Series 7  ·  Final volume  ·  Jan–Apr 2010",
        "Transcribed from original handwritten notes.",
        "[Note: original increasingly difficult to read from approximately p. 34 onwards]",
    ]:
        c.drawString(MARGIN_L, y, line)
        y -= 15

    y -= 8

    # ── SECTION 2: Opening remarks ─────────────────────────────────────────
    y = draw_section_label(c, "Inledande anteckningar (sida 1–3)", MARGIN_L, y)

    notes_p1 = [
        "The mathematics is sound. I have checked it twice. The geometry does not occur",
        "in nature — but that is not evidence against it. It is evidence that it was made.",
        "",
        "The apparatus described in the 1940 documentation operated at a narrow resonance",
        "band. I have triangulated this to approximately 247 Hz based on the material",
        "properties described. The frequency was not incidental. It was the point.",
        "",
        "Biological tissue responds. This is not speculation. The data exists.",
        "Ho will not look at it. Nguyen has stopped returning my messages.",
    ]
    c.setFont("Courier-New", 9)
    c.setFillColor(INK_FADED)
    for line in notes_p1:
        if y < 120:
            break
        c.drawString(MARGIN_L, y, line)
        y -= 15

    y -= 10

    # ── SECTION 3: The apparatus sketch ────────────────────────────────────
    y = draw_section_label(c, "Skiss — Apparaten (sida 17)", MARGIN_L, y)

    sketch_h = 140
    if y - sketch_h > 55:
        sketch_cx = PAGE_W / 2
        sketch_cy = y - sketch_h / 2
        draw_crystal_sketch(c, sketch_cx, sketch_cy, size=52)

        # Caption
        c.setFont("Courier-New", 7.5)
        c.setFillColor(INK_FADED)
        c.drawCentredString(PAGE_W / 2, y - sketch_h - 4,
            "Fig. 1 — Rekonstruktion av apparaten. Geometri ej möjlig i naturlig kristall.")
        c.drawCentredString(PAGE_W / 2, y - sketch_h - 16,
            "[Volkovs anteckning: 'Någon tillverkade detta. Det finns ännu ett.]'")
        y -= sketch_h + 28

    # Footer p1
    c.setFont("Arial", 7)
    c.setFillColor(GRAY_LIGHT)
    c.drawCentredString(PAGE_W / 2, 30,
        "Stanford University Libraries · Special Collections · Restricted Access · Digitized 2024")
    c.drawRightString(PAGE_W - MARGIN_R, 30, "1 / 2")

    # ── PAGE 2 ──────────────────────────────────────────────────────────────
    c.showPage()
    aged_paper(c)

    # Minimal header
    c.setFillColor(STANFORD_RED)
    c.rect(0, PAGE_H - 10, PAGE_W, 10, fill=1, stroke=0)
    c.setFont("Arial-Italic", 7.5)
    c.setFillColor(GRAY_LIGHT)
    c.drawString(MARGIN_L, PAGE_H - 22,
                 "Stanford University Libraries · Volkov Materials · Fil 7 · fortsättning")
    c.setStrokeColor(BORDER_LIGHT)
    c.line(MARGIN_L, PAGE_H - 28, PAGE_W - MARGIN_R, PAGE_H - 28)

    y2 = PAGE_H - 50

    # Ruled lines
    c.setStrokeColor(HexColor("#ddd5c0"))
    c.setLineWidth(0.3)
    ry = y2
    while ry > 55:
        c.line(MARGIN_L - 10, ry, PAGE_W - MARGIN_R + 10, ry)
        ry -= 18

    # ── SECTION 4: Mathematical notes ─────────────────────────────────────
    y2 = draw_section_label(c, "Matematiska anteckningar (sida 22–31)", MARGIN_L, y2)

    math_notes = [
        "Coupled oscillatory state: Q(f) = f0 / Δf",
        "For synthetic lattice geometry G7:  f0 ≈ 247.3 ± 0.8 Hz",
        "Q-factor exceeds 10^4 — not possible in natural mineral structures.",
        "",
        "Neural coupling coefficient (estimated, extrapolated from tissue data):",
        "  κ = 0.0034 · A · sin(2πft)  where A = amplitude at source",
        "  Effect radius r ≈ 4.2m at A=1  [increases nonlinearly with fragment count]",
        "",
        "[marginalanteckning, svårläst:] 'vid fullständig assembly — okänd räckvidd'",
    ]

    c.setFont("Courier-New", 9)
    c.setFillColor(INK_FADED)
    for line in math_notes:
        c.drawString(MARGIN_L, y2, line)
        y2 -= 15

    y2 -= 14

    # ── SECTION 5: Historical documentation ───────────────────────────────
    y2 = draw_section_label(c, "Historisk dokumentation — Pennsylvania 1940 (sida 38)", MARGIN_L, y2)

    c.setFont("Courier-New", 9.5)
    c.setFillColor(INK_DARK)

    confirmed_lines = [
        '"Original apparatus: Pennsylvania, August 1940.',
        ' Confirmed functional. Fragments dispersed post-crash."',
    ]
    for line in confirmed_lines:
        c.drawString(MARGIN_L + 16, y2, line)
        y2 -= 16

    # Box around the key quote
    c.setStrokeColor(INK_FADED)
    c.setLineWidth(0.8)
    box_top = y2 + 16 * len(confirmed_lines) + 8
    c.rect(MARGIN_L + 8, y2 - 4, TEXT_W - 16, box_top - y2 + 4, fill=0, stroke=1)

    y2 -= 18

    c.setFont("Courier-New", 8.5)
    c.setFillColor(INK_FADED)
    follow = [
        "Cross-reference: CAB Report 40-19 (Penn Central Airlines, Lovettsville VA).",
        "Senator Lundeen. Briefcase not recovered. See also: Harriet Johnson correspondence,",
        "Stanford Hoover Archives Box 147 [RESTRICTED to 2045].",
    ]
    for line in follow:
        c.drawString(MARGIN_L, y2, line)
        y2 -= 14

    y2 -= 16

    # ── SECTION 6: Final entry — different ink ─────────────────────────────
    y2 = draw_section_label(c, "Sista anteckning — annat bläck, tillagd senare (sida 44)", MARGIN_L, y2)

    # Slightly different visual treatment — darker, more deliberate
    c.setFont("Courier-Bold", 10)
    c.setFillColor(INK_LATER)

    final_line = '"De tre männen har ett fragment. Frankfurt Clinic, 1951–.'
    final_line2 = ' De vet inte vad de bär."'

    c.drawString(MARGIN_L + 10, y2, final_line)
    y2 -= 16
    c.drawString(MARGIN_L + 10, y2, final_line2)
    y2 -= 10

    # Underline
    line_w = c.stringWidth(final_line, "Courier-Bold", 10)
    c.setStrokeColor(INK_LATER)
    c.setLineWidth(0.6)
    c.line(MARGIN_L + 10, y2, MARGIN_L + 10 + line_w, y2)

    y2 -= 20

    c.setFont("Courier-New", 8)
    c.setFillColor(GRAY_MID)
    c.drawString(MARGIN_L, y2, "[Antecknat med mörkare bläck. Datering osäker — troligen efter april 2010.]")

    y2 -= 30

    # ── Archival stamp ─────────────────────────────────────────────────────
    stamp_cx = PAGE_W / 2
    stamp_cy = y2 - 20
    if stamp_cy > 70:
        c.setStrokeColor(STAMP_BLUE)
        c.setFillColor(white)
        c.setLineWidth(1.5)
        c.ellipse(stamp_cx - 70, stamp_cy - 22, stamp_cx + 70, stamp_cy + 22, fill=1, stroke=1)
        c.setFont("Arial-Bold", 7)
        c.setFillColor(STAMP_BLUE)
        c.drawCentredString(stamp_cx, stamp_cy + 8, "STANFORD UNIVERSITY LIBRARIES")
        c.setFont("Arial", 6.5)
        c.drawCentredString(stamp_cx, stamp_cy - 1, "SPECIAL COLLECTIONS · DIGITIZED")
        c.setFont("Arial-Bold", 6)
        c.drawCentredString(stamp_cx, stamp_cy - 11, "RESTRICTED ACCESS")

    # Footer p2
    c.setFont("Arial", 7)
    c.setFillColor(GRAY_LIGHT)
    c.drawCentredString(PAGE_W / 2, 30,
        "Stanford University Libraries · Special Collections · Restricted Access · Digitized 2024")
    c.drawRightString(PAGE_W - MARGIN_R, 30, "2 / 2")

    c.save()
    print(f"PDF skapad: {OUTPUT}")


if __name__ == "__main__":
    generate()

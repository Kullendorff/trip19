#!/usr/bin/env python3
"""
Genererar Magda Orlovas svarsemail till cellen som PDF-handout.
Output: SL/magda_reply_hamburg.pdf
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Arial",        os.path.join(FONT_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold",   os.path.join(FONT_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic", os.path.join(FONT_DIR, "ariali.ttf")))

PAGE_W, PAGE_H = A4
ML = 72
MR = 72
TEXT_W = PAGE_W - ML - MR

BG_HEADER   = HexColor("#1a1a2e")
BG_META     = HexColor("#f5f5f5")
BORDER      = HexColor("#dddddd")
GRAY_LABEL  = HexColor("#666666")
GRAY_DIM    = HexColor("#aaaaaa")
GOLD        = HexColor("#b5860d")
GOLD_LIGHT  = HexColor("#fff8e1")
GOLD_BORDER = HexColor("#d4b87a")

OUTPUT = os.path.join(os.path.dirname(__file__), "magda_reply_hamburg.pdf")

META = [
    ("Från:",   "Magda Orlova  <magda.orlova@uni-hamburg.de>"),
    ("Till:",   "[Chesapeake Cell]"),
    ("Ämne:",   "Re: Jag hittade det — Välkomna till Hamburg"),
    ("Datum:",  "15 september 2025, 08:23"),
]

PARAGRAPHS = [
    ("normal", "Tack för att ni kan komma. Det betyder mer än ni vet."),
    ("space",  ""),
    ("normal", "Jag har bokat hotell åt er. Hotel Wedina, Gurlittstraße 23, St. Georg — ett litet"
               " litteraturhotell, varje rum dedicerat till en författare. Ni är inbokade 17–20 september,"
               " tre nätter. Jag betalar. Detta är viktigt."),
    ("space",  ""),
    ("normal", "Presentationen är på fredag kväll — 19 september, kl 19:00, Thalia Flagship Store,"
               " Überseeboulevard 7, HafenCity. Det är ett litet arrangemang. Kanske 30–40 personer."),
    ("space",  ""),
    ("normal", "Kan vi ses dagen efter, kl 10:00, vid min lägenhet? Jag visar er allt då — dagboken,"
               " dokumenten, allt jag hittade."),
    ("space",  ""),
]

ADDRESS_LINES = [
    "Brahmsallee 16, Harvestehude",
    "20144 Hamburg",
    "(tredje våningen — ring på Orlova)",
]

PARAGRAPHS2 = [
    ("space",  ""),
    ("normal", "Ni frågar om Filip. Filip Kramer är en av de tre männen i min forskning."
               " Han var på Camp S-17 nära Leningrad 1942, som liten pojke. Han var på Frankfurt-kliniken"
               " under DDR-tid. Han ringde mig igen förra natten. Han vet att jag hittade dagboken."),
    ("space",  ""),
    ("normal", "Ni frågar om jag kan skjuta upp presentationen. Jag kan inte. Jag är sjuk. Om inte nu, när?"),
    ("space",  ""),
    ("normal", "Kom på fredag. Håll er nära mig under kvällen."),
    ("space",  ""),
    ("italic", "Magda"),
]


def wrap(text, font, size, max_w, c):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if c.stringWidth(test, font, size) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def generate():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("E-post: Magda Orlova — Svar: Välkomna till Hamburg")

    y = PAGE_H - 50

    # ── Top bar ──────────────────────────────────────────────────────────
    c.setFillColor(BG_HEADER)
    c.rect(0, y, PAGE_W, 44, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Arial-Bold", 13)
    c.drawString(ML, y + 16, "E-POST — SVAR")
    c.setFont("Arial", 8)
    c.setFillColor(HexColor("#aaaacc"))
    c.drawRightString(PAGE_W - MR, y + 16, "uni-hamburg.de")
    y -= 2

    # ── Meta box ─────────────────────────────────────────────────────────
    row_h = 19
    box_h = row_h * len(META) + 14
    c.setFillColor(BG_META)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.rect(ML - 10, y - box_h, TEXT_W + 20, box_h, fill=1, stroke=1)

    cur_y = y - 10
    for label, value in META:
        c.setFont("Arial-Bold", 8.5)
        c.setFillColor(GRAY_LABEL)
        c.drawString(ML, cur_y, label)
        font = "Arial-Bold" if label == "Ämne:" else "Arial"
        c.setFont(font, 8.5)
        c.setFillColor(black)
        c.drawString(ML + 52, cur_y, value)
        cur_y -= row_h

    y -= box_h + 20

    # ── Body ─────────────────────────────────────────────────────────────
    LINE_H   = 16
    PARA_GAP = 8

    def draw_paragraphs(paras):
        nonlocal y
        for ptype, text in paras:
            if ptype == "space":
                y -= PARA_GAP
                continue
            if ptype == "bold":
                font, size, color = "Arial-Bold", 11, black
            elif ptype == "italic":
                font, size, color = "Arial-Italic", 10.5, black
            else:
                font, size, color = "Arial", 10.5, black
            c.setFont(font, size)
            c.setFillColor(color)
            for line in wrap(text, font, size, TEXT_W, c):
                if y < 90:
                    c.showPage()
                    y = PAGE_H - 60
                    c.setFont(font, size)
                    c.setFillColor(color)
                c.drawString(ML, y, line)
                y -= LINE_H
            y -= 2

    draw_paragraphs(PARAGRAPHS)

    # ── Address box ───────────────────────────────────────────────────────
    addr_h = 20 * len(ADDRESS_LINES) + 18
    c.setFillColor(GOLD_LIGHT)
    c.setStrokeColor(GOLD_BORDER)
    c.setLineWidth(1.5)
    c.rect(ML, y - addr_h, TEXT_W, addr_h, fill=1, stroke=1)
    # left gold bar
    c.setFillColor(GOLD)
    c.rect(ML, y - addr_h, 4, addr_h, fill=1, stroke=0)

    ay = y - 12
    c.setFont("Arial-Bold", 8.5)
    c.setFillColor(HexColor("#7a3300"))
    c.drawString(ML + 14, ay, "Möte 20 september, kl 10:00 — Adress:")
    ay -= 20
    for line in ADDRESS_LINES:
        c.setFont("Arial", 9.5)
        c.setFillColor(black)
        c.drawString(ML + 14, ay, line)
        ay -= 20

    y -= addr_h + 14

    draw_paragraphs(PARAGRAPHS2)

    # ── Footer ───────────────────────────────────────────────────────────
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.4)
    c.line(ML, 50, PAGE_W - MR, 50)
    c.setFont("Arial", 7.5)
    c.setFillColor(GRAY_DIM)
    c.drawCentredString(PAGE_W / 2, 35,
        "Konfidentiellt — Delta Green Operation Trip 19 // Black Madonna")
    c.drawCentredString(PAGE_W / 2, 24, "Hanteras i enlighet med DG-protokoll")

    c.save()
    print(f"PDF skapad: {OUTPUT}")


if __name__ == "__main__":
    generate()

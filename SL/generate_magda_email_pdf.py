#!/usr/bin/env python3
"""
Genererar Magda Orlovas email till cellen som PDF-handout.
Output: SL/magda_email_invitation.pdf
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

# Färger — neutralt email-klient-tema
BG_HEADER   = HexColor("#1a1a2e")
BG_META     = HexColor("#f5f5f5")
BG_BODY     = white
BORDER      = HexColor("#dddddd")
RED_WARN    = HexColor("#cc3333")
BLUE_LINK   = HexColor("#1a56c4")
GRAY_LABEL  = HexColor("#666666")
GRAY_DIM    = HexColor("#aaaaaa")

OUTPUT = os.path.join(os.path.dirname(__file__), "magda_email_invitation.pdf")

META = [
    ("Från:",   "Magda Orlova  <magda.orlova@uni-hamburg.de>"),
    ("Till:",   "[Chesapeake Cell]"),
    ("Ämne:",   "Jag hittade det  //  I found it"),
    ("Datum:",  "14 september 2025, 23:47"),
]

PARAGRAPHS = [
    ("normal", "Hej,"),
    ("space",  ""),
    ("normal", "Jag hoppas detta når er. Efter vårt möte i Lovettsville fortsatte jag forska hemma i Hamburg. Jag letade överallt efter mammans saker som jag aldrig hittade."),
    ("space",  ""),
    ("bold",   "Jag hittade hennes dagbok."),
    ("space",  ""),
    ("normal", "Den var gömd bakom en lös panel i hennes gamla sovrumsgarderob. Jag har aldrig känt till den. Det mesta är på ryska, men jag kan läsa tillräckligt för att förstå..."),
    ("space",  ""),
    ("normal", "Det handlar om dem. Anton. Sasha. Filip. Och Leningrad, januari 1942."),
    ("space",  ""),
    ("normal", "Jag vet vad som hände nu. Eller åtminstone början på sanningen."),
    ("space",  ""),
    ("normal", "Jag ska presentera min forskning vid en bokhandel här i Hamburg nästa vecka – \"The Forgotten of Leningrad 1942\". Det är ett litet arrangemang, kanske 30–40 personer. Akademiker, lokalhistoriker."),
    ("space",  ""),
    ("normal", "Kan ni komma? Jag behöver visa er dagboken. Och... jag är rädd. Filip ringde mig igen igår. Han vet att jag hittade något."),
    ("space",  ""),
]

EVENT = [
    ("Författarkvällen:", "19 september 2025, kl 19:00"),
    ("Plats:",            "Thalia Flagship Store"),
    ("Adress:",           "Westfield Hamburg-Überseequartier"),
    ("",                  "Überseeboulevard 7, HafenCity, Hamburg"),
]

CLOSING = [
    ("space",  ""),
    ("normal", "Hoppas vi ses där."),
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
    c.setTitle("E-post: Magda Orlova — Jag hittade det")

    y = PAGE_H - 50

    # ── Top bar ──────────────────────────────────────────────────────────
    c.setFillColor(BG_HEADER)
    c.rect(0, y, PAGE_W, 44, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Arial-Bold", 13)
    c.drawString(ML, y + 16, "E-POST")
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

    # ── Event box ────────────────────────────────────────────────────────
    ev_row  = 20
    ev_h    = ev_row * len(EVENT) + 18
    ev_x    = ML
    ev_w    = TEXT_W

    c.setFillColor(HexColor("#fff8f0"))
    c.setStrokeColor(HexColor("#e07b39"))
    c.setLineWidth(1.5)
    c.rect(ev_x, y - ev_h, ev_w, ev_h, fill=1, stroke=1)

    # Left orange accent bar
    c.setFillColor(HexColor("#e07b39"))
    c.rect(ev_x, y - ev_h, 4, ev_h, fill=1, stroke=0)

    ey = y - 12
    for label, value in EVENT:
        if label:
            c.setFont("Arial-Bold", 9)
            c.setFillColor(HexColor("#7a3300"))
            c.drawString(ev_x + 14, ey, label)
        c.setFont("Arial", 9)
        c.setFillColor(black)
        c.drawString(ev_x + 110, ey, value)
        ey -= ev_row

    y -= ev_h + 10

    draw_paragraphs(CLOSING)

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

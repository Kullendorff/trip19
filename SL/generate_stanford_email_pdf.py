#!/usr/bin/env python3
"""
Genererar Stanford-email (Prof. Raymond Ho → Dr. Engler) som PDF-handout.
Output: SL/stanford_ho_email.pdf
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Fonts ──────────────────────────────────────────────────────────────────
FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Arial",       os.path.join(FONT_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold",  os.path.join(FONT_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic",os.path.join(FONT_DIR, "ariali.ttf")))
pdfmetrics.registerFont(TTFont("Courier-New", os.path.join(FONT_DIR, "cour.ttf")))

# ── Page setup ─────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
MARGIN_L = 72
MARGIN_R = 72
MARGIN_T = 72
TEXT_W   = PAGE_W - MARGIN_L - MARGIN_R

STANFORD_RED   = HexColor("#8C1515")
STANFORD_LIGHT = HexColor("#f4ede4")
GRAY_MID       = HexColor("#555555")
GRAY_LIGHT     = HexColor("#aaaaaa")
GRAY_BG        = HexColor("#f8f8f8")
BORDER_COLOR   = HexColor("#dddddd")

OUTPUT = os.path.join(os.path.dirname(__file__), "stanford_ho_email.pdf")

# ── Text content ───────────────────────────────────────────────────────────
HEADER_FIELDS = [
    ("Från:",    "Prof. Raymond Ho <r.ho@stanford.edu>"),
    ("Till:",    "[mottagarens e-post]"),
    ("Ämne:",   "SV: Förfrågan gällande Dr. Dmitri Volkov"),
    ("Datum:",   "September 2025"),
]

BODY_PARAGRAPHS = [
    ("normal", "Dr. Engler,"),
    ("space",  ""),
    ("normal", "Er förfrågan är välkommen – om än inte helt oväntad med tanke på de senaste händelserna."),
    ("space",  ""),
    ("normal", "Ja, Dmitri var min doktorand. Jag handledde hans avhandling: \"Electromagnetic Resonance Patterns in Crystalline Lattice Structures Under Variable Frequency Stimulation.\" Han disputerade i juni 2005. Arbetet var – i sin tidiga form – genuint imponerande. Rigoröst, originellt, med potentiella tillämpningar inom materialteknologi och sensorteknik."),
    ("space",  ""),
    ("heading","Hur han definierade resonans, och vilka frekvenser:"),
    ("normal", "Hans ramverk handlade om vad han kallade \"kopplade oscillatoriska tillstånd\" i icke-standardiserade kristallgeometrier – formationer som inte uppstår naturligt, men som han argumenterade för hade syntetiserats under kontrollerade laboratorieförhållanden. Han fokuserade särskilt på ett smalt frekvensband som enligt honom producerade ovanligt stabil resonans med exceptionellt höga Q-faktorer. Han publicerade aldrig de exakta värdena; när forskningen nådde den punkten hade den tagit en riktning jag inte längre kunde följa."),
    ("space",  ""),
    ("heading","Biologiska effekter och medvetande:"),
    ("normal", "Det var här det blev svårt. Under sitt tredje år började Dmitri hävda att vissa resonansfrekvenser producerade mätbara effekter på biologisk vävnad – specifikt på neural elektrokemisk aktivitet. Han formulerade det tillräckligt försiktigt i akademiska termer för att det inte omedelbart skulle avfärdas. Men han kunde inte producera konsekvent experimentella data, och den teoretiska grunden var... inte konventionell fysik. Han blev övertygad om att effekten var verklig, och att inkonsekvensen i hans data berodde på att de naturliga kristaller han arbetade med var orena approximationer av något som hade tillverkats avsiktligt, någonstans, av någon."),
    ("space",  ""),
    ("heading","Hur hans idéer togs emot inom institutionen:"),
    ("normal", "Skeptiskt, sedan med oro. Dr. Nguyen och jag diskuterade att avbryta hans forskning 2004. Vi gjorde det inte – dels för att hans matematik var sund även när hans tolkningar inte var det, dels för att jag trodde han skulle korrigera sin kurs. Det gjorde han inte."),
    ("space",  ""),
    ("heading","När han återvände 2008:"),
    ("normal", "Han kom tillbaka som gästforskare. Vid det laget var han övertygad om att han hade identifierat ett historiskt prejudikat för en fungerande apparat – något från 1940-talet, sa han, utan att specificera källan. Han började få tillgång till databaser han inte var behörig att använda. Vi avslutade hans anknytning i april 2010. Jag upprättade anmälan om beteendeproblem personligen."),
    ("space",  ""),
    ("heading","Arkiverat material:"),
    ("normal", "Hans avhandling finns i Stanfords bibliotekssystem och är offentligt tillgänglig. Hans laboratorieanteckningar från perioden 2008–2010 behölls av institutionen efter hans avsked. Jag vet inte vad som hände med dem efter det. Jag skulle inte beskriva dem som sammanhängande vetenskapliga dokument. De senare var svårlästa."),
    ("space",  ""),
    ("normal", "Jag har talat med FBI-agenter om detta. Jag berättade för dem samma sak som jag berättar för er: vad Dmitri än trodde sig ha funnit – trodde han på det fullständigt. Det gjorde honom metodisk på ett sätt som var omöjligt att skilja från legitim vetenskaplig praktik. Ända tills det inte längre var det."),
    ("space",  ""),
    ("normal", "Jag hoppas att er förfrågan är av rent akademisk natur."),
    ("space",  ""),
    ("sig",    "Raymond Ho, Ph.D."),
    ("sig",    "Professor i tillämpad fysik"),
    ("sig",    "Stanford University"),
    ("sig",    "Avdelningen för tillämpad fysik och Geballe Laboratory for Advanced Materials"),
]

# ── Drawing helpers ────────────────────────────────────────────────────────

def draw_stanford_header(c, page_w, margin_l, margin_r, top_y):
    """Red bar + Stanford wordmark."""
    bar_h = 8
    c.setFillColor(STANFORD_RED)
    c.rect(0, top_y - bar_h, page_w, bar_h, fill=1, stroke=0)

    c.setFillColor(STANFORD_RED)
    c.setFont("Arial-Bold", 18)
    c.drawString(margin_l, top_y - bar_h - 28, "STANFORD UNIVERSITY")

    c.setFont("Arial", 10)
    c.setFillColor(GRAY_MID)
    c.drawString(margin_l, top_y - bar_h - 44, "Department of Applied Physics")
    c.drawString(margin_l, top_y - bar_h - 57, "Varian Physics Building, 382 Via Pueblo Mall, Stanford, CA 94305")

    # Divider
    c.setStrokeColor(STANFORD_RED)
    c.setLineWidth(0.5)
    c.line(margin_l, top_y - bar_h - 68, page_w - margin_r, top_y - bar_h - 68)

    return top_y - bar_h - 80  # return y after header


def draw_email_header_box(c, fields, x, y, w):
    """Email metadata box."""
    row_h = 18
    box_h = row_h * len(fields) + 16
    c.setFillColor(GRAY_BG)
    c.setStrokeColor(BORDER_COLOR)
    c.setLineWidth(0.5)
    c.roundRect(x, y - box_h, w, box_h, 3, fill=1, stroke=1)

    cur_y = y - 10
    for label, value in fields:
        c.setFont("Arial-Bold", 8.5)
        c.setFillColor(GRAY_MID)
        c.drawString(x + 10, cur_y, label)

        c.setFont("Arial", 8.5)
        c.setFillColor(black)
        c.drawString(x + 58, cur_y, value)
        cur_y -= row_h

    return y - box_h - 14


def wrap_text(text, font_name, font_size, max_width, c_canvas):
    """Wrap text into lines fitting max_width."""
    words = text.split()
    lines = []
    current = ""
    for w in words:
        test = (current + " " + w).strip()
        if c_canvas.stringWidth(test, font_name, font_size) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines


def draw_body(c, paragraphs, x, start_y, w, page_h, margin_t, margin_l, margin_r):
    """Draw body paragraphs, with auto page-break."""
    y = start_y
    BODY_SIZE   = 10.0
    HEADING_SIZE= 10.0
    LINE_H      = 15
    PARA_GAP    = 8
    BOTTOM_LIMIT= 60

    def new_page():
        nonlocal y
        c.showPage()
        # Minimal header on continuation pages
        c.setFillColor(STANFORD_RED)
        c.rect(0, page_h - 10, PAGE_W, 10, fill=1, stroke=0)
        c.setFont("Arial-Italic", 8)
        c.setFillColor(GRAY_LIGHT)
        c.drawString(margin_l, page_h - 24, "Stanford University — Prof. Raymond Ho — Fortsättning")
        c.setStrokeColor(BORDER_COLOR)
        c.line(margin_l, page_h - 30, PAGE_W - margin_r, page_h - 30)
        y = page_h - 50

    for (ptype, text) in paragraphs:
        if ptype == "space":
            y -= PARA_GAP
            continue

        if ptype == "heading":
            if y < BOTTOM_LIMIT + LINE_H:
                new_page()
            c.setFont("Arial-Bold", HEADING_SIZE)
            c.setFillColor(STANFORD_RED)
            lines = wrap_text(text, "Arial-Bold", HEADING_SIZE, w, c)
            for line in lines:
                c.drawString(x, y, line)
                y -= LINE_H
            y -= 2
            continue

        if ptype in ("normal", "sig"):
            font = "Arial-Italic" if ptype == "sig" else "Arial"
            size = BODY_SIZE
            c.setFont(font, size)
            c.setFillColor(black)
            lines = wrap_text(text, font, size, w, c)
            for line in lines:
                if y < BOTTOM_LIMIT:
                    new_page()
                    c.setFont(font, size)
                    c.setFillColor(black)
                c.drawString(x, y, line)
                y -= LINE_H
            y -= 2

    return y


# ── Main ───────────────────────────────────────────────────────────────────

def generate():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Stanford – Prof. Ho till Dr. Engler")
    c.setAuthor("Stanford University")

    # Page 1
    header_bottom = draw_stanford_header(c, PAGE_W, MARGIN_L, MARGIN_R, PAGE_H - MARGIN_T)
    header_bottom -= 10

    fields_bottom = draw_email_header_box(c, HEADER_FIELDS, MARGIN_L, header_bottom, TEXT_W)
    fields_bottom -= 10

    draw_body(c, BODY_PARAGRAPHS, MARGIN_L, fields_bottom, TEXT_W, PAGE_H, MARGIN_T, MARGIN_L, MARGIN_R)

    # Footer page 1
    c.setFont("Arial", 7.5)
    c.setFillColor(GRAY_LIGHT)
    c.drawCentredString(PAGE_W / 2, 30, "Stanford University · Department of Applied Physics · Konfidentiellt")

    c.save()
    print(f"PDF skapad: {OUTPUT}")


if __name__ == "__main__":
    generate()

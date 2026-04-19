#!/usr/bin/env python3
"""
Generate a fillable PDF character sheet for Kai "Sparky" Zhang.

Uses reportlab AcroForm to create editable fields pre-filled with canonical data.
Data sourced from character_sheet.html (website canon).

Run:    python Sparky/generate_character_sheet_pdf.py
Output: Sparky/character_sheet.pdf
"""

import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas

# ============================================================
# Constants
# ============================================================

PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pts
MARGIN = 30
MARGIN_TOP = 30
MARGIN_BOTTOM = 40
CONTENT_W = PAGE_W - 2 * MARGIN
RIGHT_EDGE = PAGE_W - MARGIN

# Colors
GREEN_DG = HexColor('#2d5016')
PAPER_BG = HexColor('#f5f2eb')
BLUE_FIELD = HexColor('#e8eef4')
RED_DG = HexColor('#8b1a1a')
RED_FAINT = HexColor('#c48888')
INK = HexColor('#1a1a1a')
INK_LIGHT = HexColor('#444444')
INK_FAINT = HexColor('#888888')
BORDER_COLOR = HexColor('#999999')
BORDER_LIGHT = HexColor('#bbbbbb')
WHITE = HexColor('#ffffff')
NEON_GREEN = HexColor('#39ff14')


# ============================================================
# Character Data  (source: character_sheet.html = website canon)
# ============================================================

PERSONAL = {
    'name': 'Zhang, Kai',
    'code_name': 'SPARKY',
    'profession': 'Technical Analyst, SIGINT Division',
    'employer': 'National Security Agency (NSA)',
    'nationality': 'American',
    'sex_age': 'F / 28',
    'education': 'B.S. Computer Science, MIT (2019). Top Secret/SCI Clearance.',
}

STATS = [
    ('STR', 9, 45),
    ('CON', 12, 60),
    ('DEX', 12, 60),
    ('INT', 18, 90),
    ('POW', 14, 70),
    ('CHA', 10, 50),
]

DERIVED = {
    'hp': (10, 10, '(STR+CON)/2'),
    'wp': (14, 14, '= POW'),
    'san': (63, 70, 'POWx5=70, lost 7'),
    'bp': (56, None, 'SAN - POW'),
}

FEATURES = (
    'INT 18 - Brilliant analytical mind. Sees patterns others miss. '
    'POW 14 - Strong-willed, stubborn, obsessive focus. '
    'CON 12 - Above average endurance, running helps. '
    'STR 9 - Below average physical strength.'
)

# Skills: (name, base, current)
SKILLS_COL1 = [
    ('Accounting', 10, 10),
    ('Alertness', 20, 40),
    ('Anthropology', 0, 0),
    ('Archeology', 0, 0),
    ('Athletics', 30, 30),
    ('Bureaucracy', 10, 50),
    ('Computer Science', 0, 90),
    ('Craft (Electronics)', 0, 60),
    ('Craft (Locksmithing)', 0, 41),
    ('Criminology', 10, 20),
    ('Demolitions', 0, 0),
    ('Disguise', 10, 30),
    ('Dodge', 30, 30),
    ('Drive', 20, 20),
    ('Firearms', 20, 40),
    ('First Aid', 10, 30),
    ('Foreign Lang. (Mandarin)', 0, 40),
    ('Foreign Lang. (Russian)', 0, 60),
    ('Foreign Lang. (Japanese)', 0, 20),
    ('Forensics', 0, 20),
    ('Heavy Machinery', 10, 0),
    ('Heavy Weapons', 0, 0),
]

SKILLS_COL2 = [
    ('History', 10, 10),
    ('HUMINT', 10, 30),
    ('Law', 0, 30),
    ('Medicine', 0, 0),
    ('Melee Weapons', 30, 20),
    ('Navigate', 10, 30),
    ('Occult', 10, 10),
    ('Persuade', 20, 30),
    ('Pharmacy', 0, 0),
    ('Pilot', 0, 0),
    ('Psychotherapy', 10, 0),
    ('Ride', 10, 10),
    ('Science (Comp. Eng.)', 0, 50),
    ('Search', 20, 40),
    ('SIGINT', 0, 80),
    ('Stealth', 10, 32),
    ('Surgery', 0, 0),
    ('Survival', 10, 20),
    ('Swim', 20, 20),
    ('Unarmed Combat', 40, 30),
    ('Unnatural', 0, 0),
]

BONDS = [
    ('Susan Zhang', 'Mother (Denver, CO)', 8, False),
    ('Mr. Walsh', 'Neighbor, 3F (father figure)', 8, False),
    ('Null Space Collective', 'Former hacktivist crew', 8, False),
    ('', '', '', False),
]

MOTIVATIONS = [
    'Find Dmitri Volkov at any cost',
    'Prove competence (impostor syndrome)',
    'Protect the team from her failures',
    'Maintain control in a chaotic world',
    'Keep the people she loves safe (from a distance)',
]

DISORDERS = 'None (yet)'

VIOLENCE_CHECKS = [True, True, False]       # 2/3
HELPLESSNESS_CHECKS = [False, False, False]  # 0/3

WOUNDS = 'No current physical wounds.'
WOUNDS_CHRONIC = (
    'Chronic sleep deprivation (4-5 hrs/night). '
    'Caffeine dependency (4-6 cups/day). '
    'Deteriorating mental health from Volkov obsession.'
)

ARMOR = 'Kevlar vest (AR 3) - operations only'
GEAR = [
    '"Spark" - Custom Flipper Zero',
    'Dell XPS 15 (Kali Linux)',
    'Raspberry Pi 4 (portable hack station)',
    'RTL-SDR dongle (radio scanning)',
    'USB Rubber Ducky',
    'Lockpicking set',
    'RF detector & camera lens detector',
    'Faraday bags, Pepper spray',
]

# Weapons: (name, skill%, range, damage, ap, lethality, ammo)
WEAPONS = [
    ('Glock 19 (primary)', '40%', '20m', '1D10', '-', '-', '15+1'),
    ('Glock 19 (backup)', '40%', '20m', '1D10', '-', '-', '15+1'),
    ('Unarmed', '30%', '-', '1D4-1', '-', '-', '-'),
]

TRAINING = [
    ('Offensive Cyber Operations', 'Computer Science (INT)'),
    ('Network Penetration Testing', 'Computer Science (INT)'),
    ('Malware Creation & Reverse Eng.', 'Science: Comp. Eng. (INT)'),
    ('RFID/NFC Cloning', 'Craft: Electronics (DEX)'),
    ('Electronic Surv. / Counter-Surv.', 'SIGINT (INT)'),
    ('Car Computer Hacking', 'Craft: Electronics (INT)'),
]

NOTES = (
    'Recruited Aug 2022 after flagging anomalous SIGINT patterns from '
    'Appalachian operation. Agent REDFIELD (controller). 7 operations '
    'completed. Currently obsessed with tracking Dmitri Volkov '
    '(encountered Dec 2024, "Mall Before Christmas"). Built custom AI '
    'model scanning global SIGINT for Volkov\'s digital footprint. '
    'Risking NSA clearance with off-books database queries.\n\n'
    'Aliases: Sarah Mitchell (safehouse), Maya Nakamura (intl. escape), '
    'Jennifer Park (emergency). 31 custom OPSEC apps.\n\n'
    'Address: Apt 3G, 24 C Street, Laurel, MD 20707.\n'
    'Safehouse: 142 Dartmouth Ave, College Park, MD 20740.\n'
    'Safety Deposit: M&T Bank, Baltimore (as Maya Nakamura).'
)

RECRUIT_WHY = (
    'SIGINT expertise. Offensive cyber capabilities. '
    'Already cleared TS/SCI. '
    '"Expendable enough to risk, skilled enough to use."'
)
RECRUIT_ACCEPTED = (
    'Curiosity (impossible signals). '
    'Desperation for meaning (NSA drone work). '
    '"Real work, not just watching spreadsheets."'
)


# ============================================================
# Drawing Helpers
# ============================================================

def draw_header(c, y):
    """Green header bar with Delta Green title."""
    h = 36
    c.setFillColor(GREEN_DG)
    c.rect(0, y - h, PAGE_W, h, fill=1, stroke=0)

    # Triangle
    c.setFillColor(NEON_GREEN)
    c.setFont('Helvetica-Bold', 20)
    c.drawString(MARGIN, y - 25, 'A')  # placeholder triangle

    # Actually draw a triangle
    c.setFillColor(NEON_GREEN)
    tri_x, tri_y = MARGIN + 4, y - 28
    p = c.beginPath()
    p.moveTo(tri_x, tri_y)
    p.lineTo(tri_x + 8, tri_y + 16)
    p.lineTo(tri_x + 16, tri_y)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    # Overwrite the 'A' with blank
    c.setFillColor(GREEN_DG)
    c.rect(MARGIN, y - h, 22, h, fill=1, stroke=0)
    # Redraw triangle
    c.setFillColor(NEON_GREEN)
    p = c.beginPath()
    p.moveTo(tri_x, tri_y)
    p.lineTo(tri_x + 8, tri_y + 16)
    p.lineTo(tri_x + 16, tri_y)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    # Title
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 15)
    c.drawString(MARGIN + 24, y - 18, 'DELTA GREEN')
    c.setFont('Helvetica', 8)
    c.drawString(MARGIN + 24, y - 30, 'Agent Documentation Sheet')

    # Right side
    c.setFont('Helvetica', 8)
    c.drawRightString(RIGHT_EDGE, y - 22, 'OPERATION: TRIP 19')

    return y - h - 4


def draw_section_title(c, y, number, title):
    """Numbered section heading with green underline."""
    y -= 4
    badge = 14
    c.setFillColor(GREEN_DG)
    c.rect(MARGIN, y - badge + 2, badge, badge, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawCentredString(MARGIN + badge / 2, y - badge + 6, str(number))

    c.setFillColor(GREEN_DG)
    c.setFont('Helvetica-Bold', 9)
    c.drawString(MARGIN + badge + 4, y - badge + 5, title.upper())

    c.setStrokeColor(GREEN_DG)
    c.setLineWidth(1.5)
    c.line(MARGIN, y - badge - 1, RIGHT_EDGE, y - badge - 1)
    return y - badge - 5


def draw_footer(c):
    """Green footer bar at page bottom."""
    h = 18
    c.setFillColor(GREEN_DG)
    c.rect(0, 0, PAGE_W, h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica', 6)
    c.drawCentredString(
        PAGE_W / 2, 6,
        'DELTA GREEN  --  Agent Documentation Sheet  --  '
        'Chesapeake Cell  --  Need to Know'
    )


def add_text_field(c, name, x, y, w, h, value='', font_size=9,
                   multiline=False):
    """Add an editable AcroForm text field."""
    flags = 'multiline' if multiline else ''
    c.acroForm.textfield(
        name=name,
        tooltip=name.replace('_', ' ').title(),
        x=x, y=y,
        width=w, height=h,
        value=str(value),
        fontSize=font_size,
        fontName='Courier',
        borderWidth=0.5,
        borderColor=BORDER_LIGHT,
        fillColor=BLUE_FIELD,
        textColor=INK,
        fieldFlags=flags,
    )


def add_checkbox(c, name, x, y, checked=False, size=14):
    """Add an AcroForm checkbox."""
    c.acroForm.checkbox(
        name=name,
        tooltip=name.replace('_', ' ').title(),
        x=x, y=y,
        size=size,
        checked=checked,
        borderWidth=1,
        borderColor=BORDER_COLOR,
        fillColor=white,
        textColor=RED_DG,
        buttonStyle='cross',
    )


# ============================================================
# Section Drawers
# ============================================================

def draw_section1(c, y):
    """Section 1: Personal Data."""
    y = draw_section_title(c, y, 1, 'Personal Data')

    field_h = 16
    label_w = 92       # HTML min-width: 90px
    col_gap = 20       # HTML gap: 4px 20px
    row_gap = 4
    col_w = (CONTENT_W - col_gap) / 2

    rows = [
        (('NAME:', 'p_name', PERSONAL['name']),
         ('CODE NAME:', 'p_code_name', PERSONAL['code_name'])),
        (('PROFESSION:', 'p_profession', PERSONAL['profession']),
         ('EMPLOYER:', 'p_employer', PERSONAL['employer'])),
        (('NATIONALITY:', 'p_nationality', PERSONAL['nationality']),
         ('SEX / AGE:', 'p_sex_age', PERSONAL['sex_age'])),
    ]

    for i, (left, right) in enumerate(rows):
        fy = y - i * (field_h + row_gap)

        for col, (label, key, value) in enumerate([left, right]):
            x = MARGIN + col * (col_w + col_gap)

            # Label (match HTML: 9px uppercase, baseline-aligned)
            c.setFillColor(INK_FAINT)
            c.setFont('Helvetica', 7)
            c.drawString(x, fy + 4, label)

            # Field value
            add_text_field(c, key,
                           x + label_w, fy, col_w - label_w, field_h,
                           value, font_size=10)

            # Dotted underline (match HTML border-bottom: 1px dotted)
            c.setStrokeColor(BORDER_LIGHT)
            c.setLineWidth(0.5)
            c.setDash(1, 2)
            c.line(x, fy - 1, x + col_w, fy - 1)
            c.setDash()

    y -= 3 * (field_h + row_gap)

    # Education full-width (spans both columns in HTML)
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 7)
    c.drawString(MARGIN, y + 4, 'EDUCATION:')
    add_text_field(c, 'p_education', MARGIN + label_w, y,
                   CONTENT_W - label_w, field_h,
                   PERSONAL['education'], font_size=9)
    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(0.5)
    c.setDash(1, 2)
    c.line(MARGIN, y - 1, RIGHT_EDGE, y - 1)
    c.setDash()
    y -= field_h + 8
    return y


def draw_section2(c, y):
    """Section 2: Statistical Data."""
    y = draw_section_title(c, y, 2, 'Statistical Data')

    # ---- Stats table (left) ----
    # HTML: grid 50px 50px 50px, gap 2px, margin-bottom 2px
    stat_name_w = 50
    stat_score_w = 50
    stat_x5_w = 50
    stats_w = stat_name_w + stat_score_w + stat_x5_w  # 150
    row_h = 20
    sx = MARGIN

    # Headers
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 7)
    c.drawString(sx, y, 'STAT')
    c.drawCentredString(sx + stat_name_w + stat_score_w / 2, y, 'SCORE')
    c.drawCentredString(sx + stat_name_w + stat_score_w + stat_x5_w / 2,
                        y, 'x5')
    c.setStrokeColor(BORDER_COLOR)
    c.setLineWidth(0.5)
    c.line(sx, y - 3, sx + stats_w, y - 3)

    stats_top = y - 8
    for i, (name, score, x5) in enumerate(STATS):
        ry = stats_top - i * row_h
        c.setFillColor(GREEN_DG)
        c.setFont('Helvetica-Bold', 11)
        c.drawString(sx, ry + 4, name)

        # Score field (blue bg, matching HTML .stat-score)
        add_text_field(c, f'stat_{name}',
                       sx + stat_name_w, ry, stat_score_w - 4, row_h - 2,
                       str(score), font_size=14)

        # x5 value (plain text, matching HTML .stat-x5)
        c.setFillColor(INK_LIGHT)
        c.setFont('Courier', 12)
        c.drawCentredString(
            sx + stat_name_w + stat_score_w + stat_x5_w / 2,
            ry + 4, str(x5))

    # ---- Derived stats (right) ----
    # HTML: flex:1, gap:6px, 2x2 grid, starts at same top as stats
    flex_gap = 15   # HTML gap between stats-table and derived-stats
    dx = sx + stats_w + flex_gap
    derived_total_w = CONTENT_W - stats_w - flex_gap
    d_gap = 6       # HTML grid gap
    dw = (derived_total_w - d_gap) / 2
    dh = 55
    drow_gap = 6

    derived_items = [
        ('HIT POINTS', 'hp', False),
        ('WILLPOWER', 'wp', False),
        ('SANITY', 'san', True),
        ('BREAKING PT', 'bp', True),
    ]

    for i, (label, key, critical) in enumerate(derived_items):
        col = i % 2
        row = i // 2
        bx = dx + col * (dw + d_gap)
        by = y - row * (dh + drow_gap)

        cur, mx, formula = DERIVED[key]
        border = RED_DG if critical else GREEN_DG

        c.setStrokeColor(border)
        c.setLineWidth(2)
        c.setFillColor(WHITE)
        c.roundRect(bx, by - dh, dw, dh, 4, fill=1, stroke=1)

        # Label at top of box
        c.setFillColor(INK_FAINT)
        c.setFont('Helvetica', 7)
        c.drawCentredString(bx + dw / 2, by - 12, label)

        # Editable value centered in box
        fw = 48
        fx = bx + (dw - fw) / 2
        add_text_field(c, f'd_{key}', fx, by - 38, fw, 18,
                       str(cur), font_size=16)

        # Max value
        if mx is not None:
            c.setFillColor(INK_FAINT)
            c.setFont('Helvetica', 7)
            c.drawCentredString(bx + dw / 2, by - dh + 14, f'max {mx}')

        # Formula
        c.setFont('Helvetica', 6)
        c.drawCentredString(bx + dw / 2, by - dh + 5, formula)

    # Advance y past whichever column is taller
    bottom_stats = stats_top - len(STATS) * row_h
    bottom_derived = y - 2 * (dh + drow_gap)
    y = min(bottom_stats, bottom_derived)

    # ---- Distinguishing Features ----
    y -= 6
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 7)
    c.drawString(MARGIN, y + 2, 'DISTINGUISHING FEATURES')
    feat_h = 38
    add_text_field(c, 'features', MARGIN, y - feat_h, CONTENT_W, feat_h,
                   FEATURES, multiline=True, font_size=8)
    y -= feat_h + 6
    return y


def draw_section3(c, y):
    """Section 3: Skills (43 skills in 2 columns)."""
    y = draw_section_title(c, y, 3, 'Skills')

    # HTML: skills-grid 2 cols, gap: 0 20px
    # skill-row grid: 1fr 40px 50px
    col_gap = 20
    col_w = (CONTENT_W - col_gap) / 2
    base_w = 40    # HTML: 40px
    val_w = 50     # HTML: 50px
    name_w = col_w - base_w - val_w
    row_h = 13

    for col_idx, skills in enumerate([SKILLS_COL1, SKILLS_COL2]):
        cx = MARGIN + col_idx * (col_w + col_gap)

        # Column header (HTML: skill-header, margin-bottom: 3px)
        c.setFillColor(INK_FAINT)
        c.setFont('Helvetica', 7)
        c.drawString(cx, y, 'SKILL')
        c.drawCentredString(cx + name_w + base_w / 2, y, 'BASE')
        c.drawCentredString(cx + name_w + base_w + val_w / 2, y, 'CURRENT')
        c.setStrokeColor(BORDER_COLOR)
        c.setLineWidth(0.5)
        c.line(cx, y - 3, cx + col_w, y - 3)

        # Start rows after header + margin-bottom: 3px
        sy = y - 8
        for i, (name, base, current) in enumerate(skills):
            ry = sy - i * row_h

            # Dotted underline per row (HTML: border-bottom: 1px dotted)
            c.setStrokeColor(HexColor('#dddddd'))
            c.setLineWidth(0.5)
            c.setDash(1, 2)
            c.line(cx, ry - 3, cx + col_w, ry - 3)
            c.setDash()

            # Skill name (HTML: 10px)
            c.setFillColor(INK)
            c.setFont('Courier', 8)
            c.drawString(cx, ry + 1, name)

            # Base % (HTML: 9px, center, faint)
            c.setFillColor(INK_FAINT)
            c.setFont('Helvetica', 7)
            c.drawCentredString(cx + name_w + base_w / 2, ry + 1,
                                f'{base}%')

            # Current value field (HTML: 12px, center, bold)
            safe = (name.lower()
                    .replace(' ', '_').replace('(', '')
                    .replace(')', '').replace('.', ''))
            add_text_field(c, f'sk_{safe}',
                           cx + name_w + base_w, ry - 3,
                           val_w, row_h,
                           str(current), font_size=9)

    max_rows = max(len(SKILLS_COL1), len(SKILLS_COL2))
    y -= 8 + max_rows * row_h + 6
    return y


def draw_section4(c, y):
    """Section 4: Bonds."""
    y = draw_section_title(c, y, 4, 'Bonds')

    # Headers
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y, 'PERSON / GROUP')
    c.drawString(MARGIN + 170, y, 'RELATION')
    c.drawString(MARGIN + 340, y, 'SCORE')
    c.drawString(MARGIN + 390, y, 'DMG')
    c.setStrokeColor(BORDER_COLOR)
    c.setLineWidth(0.5)
    c.line(MARGIN, y - 2, RIGHT_EDGE, y - 2)

    row_h = 17
    y -= 6
    for i, (name, relation, score, damaged) in enumerate(BONDS):
        ry = y - i * row_h
        add_text_field(c, f'bond_name_{i}', MARGIN, ry - 1, 164, row_h - 2,
                       name, font_size=9)
        add_text_field(c, f'bond_rel_{i}', MARGIN + 170, ry - 1, 164,
                       row_h - 2, relation, font_size=7)
        add_text_field(c, f'bond_score_{i}', MARGIN + 340, ry - 1, 40,
                       row_h - 2, str(score), font_size=10)
        add_checkbox(c, f'bond_dmg_{i}', MARGIN + 393, ry, checked=damaged)

    y -= len(BONDS) * row_h + 2
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y,
                 'Initial Bond score = CHA (10). Current total: 24 / 40 max.')
    y -= 10
    return y


def draw_section5(c, y):
    """Section 5: Motivations & Disorders."""
    y = draw_section_title(c, y, 5, 'Motivations & Mental Disorders')

    col_w = (CONTENT_W - 16) / 2
    box_h = 70

    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y, 'MOTIVATIONS')
    c.drawString(MARGIN + col_w + 16, y, 'MENTAL DISORDERS')
    y -= 4

    motiv_text = '\n'.join(f'> {m}' for m in MOTIVATIONS)
    add_text_field(c, 'motivations', MARGIN, y - box_h, col_w, box_h,
                   motiv_text, multiline=True, font_size=7)
    add_text_field(c, 'disorders', MARGIN + col_w + 16, y - box_h, col_w,
                   box_h, DISORDERS, multiline=True, font_size=8)

    y -= box_h + 6
    return y


def draw_section6(c, y):
    """Section 6: Incidents of SAN Loss."""
    y = draw_section_title(c, y, 6, 'Incidents of SAN Loss')

    col_w = (CONTENT_W - 16) / 2
    box_h = 32

    for idx, (title, checks, summary) in enumerate([
        ('VIOLENCE', VIOLENCE_CHECKS, '2/3 - not yet adapted'),
        ('HELPLESSNESS', HELPLESSNESS_CHECKS, '0/3 - not adapted'),
    ]):
        bx = MARGIN + idx * (col_w + 16)
        c.setStrokeColor(BORDER_LIGHT)
        c.setFillColor(WHITE)
        c.roundRect(bx, y - box_h, col_w, box_h, 3, fill=1, stroke=1)

        c.setFillColor(INK_LIGHT)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(bx + 6, y - 11, title)

        for ci, checked in enumerate(checks):
            add_checkbox(c, f'san_{title.lower()}_{ci}',
                         bx + 6 + ci * 20, y - box_h + 5,
                         checked=checked, size=13)

        c.setFillColor(INK_FAINT)
        c.setFont('Helvetica', 6)
        c.drawString(bx + 6 + 3 * 20 + 8, y - box_h + 8, summary)

    y -= box_h + 4
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y,
                 'Total SAN lost: 7 pts over 7 operations '
                 '(Aug 2022 - Dec 2024). Breaking Point buffer: 7 pts.')
    y -= 10
    return y


def draw_section7(c, y):
    """Section 7: Wounds & Ailments."""
    y = draw_section_title(c, y, 7, 'Wounds & Ailments')

    add_text_field(c, 'wounds', MARGIN, y - 16, CONTENT_W, 16,
                   WOUNDS, font_size=9)
    y -= 22
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y + 2, 'CHRONIC CONDITIONS')
    add_text_field(c, 'wounds_chronic', MARGIN, y - 22, CONTENT_W, 22,
                   WOUNDS_CHRONIC, multiline=True, font_size=7)
    y -= 28
    return y


def draw_section8(c, y):
    """Section 8: Armor & Gear."""
    y = draw_section_title(c, y, 8, 'Armor & Gear')

    col_w = (CONTENT_W - 16) / 2

    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y, 'ARMOR')
    c.drawString(MARGIN + col_w + 16, y, 'KEY EQUIPMENT')
    y -= 4

    gear_h = 80
    add_text_field(c, 'armor', MARGIN, y - 16, col_w, 16,
                   ARMOR, font_size=8)
    add_text_field(c, 'armor_extra', MARGIN, y - gear_h, col_w, gear_h - 20,
                   '', multiline=True, font_size=7)

    gear_text = '\n'.join(GEAR)
    add_text_field(c, 'gear', MARGIN + col_w + 16, y - gear_h, col_w, gear_h,
                   gear_text, multiline=True, font_size=7)

    y -= gear_h + 6
    return y


def draw_section9(c, y):
    """Section 9: Weapons."""
    y = draw_section_title(c, y, 9, 'Weapons')

    col_defs = [
        ('WEAPON', 0, 135),
        ('SKILL %', 140, 42),
        ('RANGE', 187, 38),
        ('DAMAGE', 230, 45),
        ('AP', 280, 28),
        ('LETHAL.', 313, 45),
        ('AMMO', 363, 40),
    ]

    # Header row
    c.setFillColor(GREEN_DG)
    c.rect(MARGIN, y - 13, CONTENT_W, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 6)
    for label, offset, _ in col_defs:
        c.drawString(MARGIN + offset + 2, y - 10, label)

    y -= 17
    row_h = 15
    for i, weapon_data in enumerate(WEAPONS):
        ry = y - i * row_h
        for j, ((_, offset, w), val) in enumerate(
                zip(col_defs, weapon_data)):
            add_text_field(c, f'wpn_{i}_{j}',
                           MARGIN + offset, ry - 1,
                           w - 3, row_h - 2,
                           val, font_size=7)

    y -= len(WEAPONS) * row_h + 2
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y,
                 'Carry: MD Wear & Carry Permit (legal, ~30 states). '
                 'Fake LEOSA credentials (backup, felony risk).')
    y -= 10
    return y


def draw_section10(c, y):
    """Section 10: Special Training."""
    y = draw_section_title(c, y, 10, 'Special Training')

    half = CONTENT_W / 2 - 5
    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y, 'SPECIALIZATION')
    c.drawString(MARGIN + half + 10, y, 'TESTED WITH')
    c.setStrokeColor(BORDER_COLOR)
    c.setLineWidth(0.5)
    c.line(MARGIN, y - 2, RIGHT_EDGE, y - 2)

    row_h = 15
    y -= 5
    for i, (spec, tested) in enumerate(TRAINING):
        ry = y - i * row_h
        add_text_field(c, f'train_s_{i}', MARGIN, ry - 1, half, row_h - 2,
                       spec, font_size=7)
        add_text_field(c, f'train_t_{i}', MARGIN + half + 10, ry - 1, half,
                       row_h - 2, tested, font_size=7)

    y -= len(TRAINING) * row_h + 6
    return y


def draw_section11(c, y):
    """Section 11: Personal Details & Notes."""
    y = draw_section_title(c, y, 11, 'Personal Details & Notes')

    notes_h = 120
    add_text_field(c, 'notes', MARGIN, y - notes_h, CONTENT_W, notes_h,
                   NOTES, multiline=True, font_size=7)
    y -= notes_h + 6
    return y


def draw_section12(c, y):
    """Section 12: Recruitment."""
    y = draw_section_title(c, y, 12, 'Recruitment')

    col_w = (CONTENT_W - 16) / 2
    box_h = 50

    c.setFillColor(INK_FAINT)
    c.setFont('Helvetica', 6)
    c.drawString(MARGIN, y, 'WHY RECRUITED')
    c.drawString(MARGIN + col_w + 16, y, 'WHY ACCEPTED')
    y -= 4

    add_text_field(c, 'recruit_why', MARGIN, y - box_h, col_w, box_h,
                   RECRUIT_WHY, multiline=True, font_size=7)
    add_text_field(c, 'recruit_accepted', MARGIN + col_w + 16, y - box_h,
                   col_w, box_h, RECRUIT_ACCEPTED, multiline=True,
                   font_size=7)
    y -= box_h + 6
    return y


# ============================================================
# Page Setup Helpers
# ============================================================

def new_page(c):
    """Start a new page with background and header."""
    c.showPage()
    c.setFillColor(PAPER_BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    y = PAGE_H - MARGIN_TOP
    y = draw_header(c, y)
    return y


# ============================================================
# Main
# ============================================================

def generate_pdf(output_path):
    """Generate the complete 3-page fillable character sheet."""
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setTitle('DELTA GREEN - Agent Sheet - SPARKY')
    c.setAuthor('Chesapeake Cell / Delta Green')
    c.setSubject('Kai "Sparky" Zhang - Character Sheet')

    # ── Page 1: Personal, Stats, Skills ──
    c.setFillColor(PAPER_BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    y = PAGE_H - MARGIN_TOP
    y = draw_header(c, y)

    # Faint CLASSIFIED stamp
    c.saveState()
    c.setFillColor(RED_FAINT)
    c.translate(PAGE_W - 110, PAGE_H - 90)
    c.rotate(-12)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(0, 0, 'CLASSIFIED')
    c.restoreState()

    y = draw_section1(c, y)
    y = draw_section2(c, y)
    y = draw_section3(c, y)
    draw_footer(c)

    # ── Page 2: Bonds, Motivations, SAN, Wounds, Gear ──
    y = new_page(c)
    y = draw_section4(c, y)
    y = draw_section5(c, y)
    y = draw_section6(c, y)
    y = draw_section7(c, y)
    y = draw_section8(c, y)
    draw_footer(c)

    # ── Page 3: Weapons, Training, Notes, Recruitment ──
    y = new_page(c)
    y = draw_section9(c, y)
    y = draw_section10(c, y)
    y = draw_section11(c, y)
    y = draw_section12(c, y)
    draw_footer(c)

    c.save()
    print(f'OK  {output_path}')
    print(f'    3 pages, 12 sections, all fields editable')
    print(f'    Open in Acrobat / Edge / Chrome to fill in.')


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, 'character_sheet.pdf')
    generate_pdf(out)

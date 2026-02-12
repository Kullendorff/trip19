---
name: character-sheet
description: Generate Delta Green character sheet HTML files from canonical data. Uses Sparky's template as base, populates from index.html (canon) and Complete.md.
---

# Character Sheet Generator for Trip 19

## Purpose
Create standardized Delta Green "Agent Documentation Sheet" HTML files for Chesapeake Cell characters. Each sheet is a self-contained HTML page with 12 sections matching the official DG character sheet format.

## Template
`Sparky/character_sheet.html` is the canonical template (1272 lines). All new sheets must use identical HTML structure and CSS.

## Data Sources (Priority Order)
1. **`{Character}/index.html`** = CANON (stats, skills, derived attributes, personal info)
2. **`{Character}/{Name}_Complete.md`** = Extended data (bonds, weapons, gear, backstory, recruitment, operations, disorders, wounds, special training)
3. **`{Character}/operativt.html`** = Operational details (equipment, handler, status)

## Process

### Step 1: Read template + character data
```
Read: Sparky/character_sheet.html (template)
Read: {Character}/index.html (canon stats/skills)
Read: {Character}/{Name}_Complete.md (extended data)
```

### Step 2: Extract and map data
The sheet has 12 sections that need data:

| Section | Data Source | Key Fields |
|---------|-----------|------------|
| 1. Personal Data | index.html | Name, codename, profession, employer, sex/age, education |
| 2. Statistical Data | index.html | STR/CON/DEX/INT/POW/CHA, HP/WP/SAN/BP, features |
| 3. Skills | index.html | All skills with base and current values |
| 4. Bonds | Complete.md | Person, relation, score, damaged status |
| 5. Motivations & Disorders | Complete.md | Motivations list, mental disorders |
| 6. SAN Incidents | Complete.md | Violence checks (0-3), Helplessness checks (0-3) |
| 7. Wounds & Ailments | Complete.md | Current wounds, chronic conditions |
| 8. Armor & Gear | Complete.md | Armor, key equipment list |
| 9. Weapons | Complete.md/index | Weapon name, skill%, range, damage, AP, lethality, ammo |
| 10. Special Training | Complete.md | Specialization, tested-with skill |
| 11. Notes | Complete.md | Recruitment context, aliases, addresses, key background |
| 12. Recruitment | Complete.md | Why recruited, why accepted |

### Step 3: Verify derived stats
```
HP = floor((STR + CON) / 2)
WP = POW (max = POW)
SAN max = POW * 5
BP = SAN - POW (initial), recalculates after breaks
Stats total = 75 (budget check)
```

### Step 4: Write file
Output to `{Character}/character_sheet.html`

### Step 5: Add nav link
Add to character's `index.html` in DOKUMENT section:
```html
<a href="character_sheet.html" class="nav-link">Rollformulär</a>
```

## Critical Rules

### Character-specific
- **Scalpel = SHE/HER** (never he/him - most critical rule in entire project)
- **Sullivan = Navy Chaplain** (not "priest")
- **Mac's codename = SERGEANT** (not "MAC" - Mac is his nickname)
- All characters have **75-point stat budget**
- Stats come from index.html ONLY (Complete.md may have older values)

### Template integrity
- CSS must be IDENTICAL to Sparky template (same variables, classes, layout)
- `--neon-green: #39ff14` stays - it's Delta Green theming, not character-specific
- All 12 sections must be present
- Skills grid: 2 columns, ~22 skills per column
- Keep the "CLASSIFIED" stamp overlay

### Skill values
- Skills at base value: plain style (`skill-value`)
- Skills above base: trained style (`skill-value trained`)
- Skills 60%+: expert style (`skill-value expert`)

### Context window management
- Use PARALLEL AGENTS (one per character) to avoid filling context
- Each agent reads template + character data independently
- Previous session failed due to context overflow - parallelism is essential

## Existing Sheets
| Character | File | Status |
|-----------|------|--------|
| Sparky | `Sparky/character_sheet.html` | Template/original |
| Mac | `Mac/character_sheet.html` | Created 2026-02-12 |
| Sullivan | `Sullivan/character_sheet.html` | Created 2026-02-12 |
| Scalpel | `Scalpel/character_sheet.html` | Created 2026-02-12 |
| Trench | `Trench/character_sheet.html` | Created 2026-02-12 |

## PDF Generation (Optional)
`Sparky/generate_character_sheet_pdf.py` generates a fillable PDF using reportlab.
- Requires: `pip install reportlab`
- Run: `python {Character}/generate_character_sheet_pdf.py`
- Currently only exists for Sparky - can be templated for others if needed

## Lessons Learned
1. **Parallel agents essential** - one character sheet = ~1300 lines HTML + reading ~1000 lines source data. Sequential processing fills context window.
2. **index.html is canon** - when Complete.md conflicts with index.html, index.html wins.
3. **Verify pronouns** - grep for `\bhe\b|\bhis\b|\bhim\b` in Scalpel's sheet after generation.
4. **Verify stat budget** - sum all 6 stats, must equal 75.
5. **Scalpel lacked DOKUMENT nav** - may need to create the section, not just add a link.

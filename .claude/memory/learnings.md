# Trip19-specifika lärdomar

Lärdomar som gäller specifikt för **Delta Green-kampanjen "Trip 19 / Svarta Madonnan"**.

För globala lärdomar som gäller alla projekt, se `~/.claude/memory/learnings.md`.

---

## Svenska + engelsk fackterminologi

**Datum:** 2026-01-06
**Regel:** ALL narrativ text på svenska, FACKTERMER på engelska
**Referens:** `TRANSLATION_RULES.md` (detaljerade regler)

**Exempel:**
- ✅ "SAN loss" (inte "förlustad förnuft")
- ✅ "Breaking Point" (inte "brytpunkt")
- ✅ "Bonds" (inte "band")
- ✅ "IT-forensik" (inte "datorforensik")
- ✅ "Federal law enforcement" (inte "federal brottsbekämpning")

**Varför:**
- Delta Green-termer är etablerade på engelska i communityn
- Facktermer (IT, legal) låter konstiga på svenska
- Spelarna känner igen engelska termer från regelböckerna

**Gäller:** Bara Trip19 (EON använder ren svenska)

---

## Inline CSS: Inga externa stylesheets

**Datum:** 2026-01-06
**Regel:** ALL CSS ska vara embedded i HTML-filer
**Referens:** `MALL_GUIDE.md` (HTML/CSS-standarder)

**Exempel:**
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    /* All CSS här */
    body { ... }
  </style>
</head>
<body>
  <!-- Content -->
</body>
</html>
```

**Varför:**
- Enklare deployment (en fil per sida)
- Inga broken links vid filflyttning
- Self-contained HTML-filer

**Gäller:** Bara Trip19 (EON använder både embedded och externa CSS)

---

## Character-specific theme colors

**Datum:** 2026-01-06
**Färgschema för karaktärer:**
- **Mac Riley** (FBI): Steel blue (`#4682b4`)
- **Father Sullivan** (Navy Chaplain): Copper (`#b87333`)
- **Kai "Sparky" Zhang** (NSA): Neon green (`#39ff14`)
- **Hanna "Scalpel" Engler** (Medical Examiner): Gold (`#ffd700`)
- **Sam "Trench" Novak** (USAR): Orange (`#ff8c00`)

**Användning:**
- Karaktärssidor: `/Mac/`, `/Sullivan/`, etc.
- Character badges i sessionsplaner
- Visual identity per karaktär

**Gäller:** Bara Trip19

---

## Complete.md: Source of truth för karaktärsinformation

**Datum:** 2026-01-06
**Fil:** `/<karaktär>/Complete.md` (per karaktär)
**Roll:** Ersätter gamla MD-filer som source of truth

**Struktur:**
```markdown
# Karaktärsnamn

## Stats
SAN: X/X
Bonds: X

## Breaking Points
- Breaking Point 1
- Breaking Point 2

## Pronomen
han/honom (eller hon/henne)
```

**Viktigt:**
- `master/character_reference.md` synkas från Complete.md-filerna
- Vid konflikt: Complete.md har rätt

**Gäller:** Bara Trip19 (EON har character_reference.md men ingen Complete.md)

---

## Responsive design: 3 breakpoints

**Datum:** 2026-01-06
**Breakpoints:**
- Desktop: >1024px
- Tablet: 768px - 1024px
- Mobile: <768px

**CSS-exempel:**
```css
/* Desktop default */
.container { width: 1200px; }

/* Tablet */
@media (max-width: 1024px) {
  .container { width: 100%; }
}

/* Mobile */
@media (max-width: 768px) {
  .container { padding: 1rem; }
}
```

**Gäller:** Trip19 och EON (generell best practice)

---

## Historiska källor: REAL + fictional gap-filling

**Datum:** 2026-01-06
**Filosofi:** Spelarna kan googla RIKTIGA källor - supernatural fyller GAP

**REAL källor (spelarna kan researcha):**
- CAB Aviation Accident Report (Flight 19, 1940) - 87 pages
- FBI files (Lundeen investigation, FOIA)
- Viereck Trial transcripts (Nazi propaganda)
- Stanford/Iowa university collections
- Rachel Maddow's "Ultra" podcast

**FICTIONAL additions (plausibla i dokumenterade luckor):**
- Väskan (hittades aldrig i verkligheten)
- Kristall-fragment (förklaring till mysteriet)
- Volkov's research (bakgrundshistoria)

**VIKTIGT:**
- Supernatural ERSÄTTER INTE historien - den FYLLER I LUCKOR
- Mysteries avslöjas gradvis genom investigation, inte exposition
- Autenticitet framför dramatik

**Gäller:** Bara Trip19 (EON är ren fantasy, ingen historisk research)

---

## Slow-Burn Horror: Session-struktur

**Datum:** 2026-01-06
**Kampanjstruktur (8-12 sessioner):**

**Session 1-4:** "Något är fel..."
- Underliga detaljer
- Saknad information
- Subtila anomalier

**Session 5-8:** "Det här kan inte vara sant..."
- Övernaturligt bekräftas gradvis
- SAN loss börjar påverka
- Bonds eroderar

**Session 9-12:** "Vi borde aldrig ha grävt här..."
- Full revelation
- Psykologisk nedbrytning
- Långsiktig trauma

**VIKTIGT:**
- Ingen "world-ending urgency" - slow-burn investigation
- Research-driven (spelarna googlar RIKTIGA dokument)
- Character trauma som motor (SAN, Bonds, PTSD)

**Gäller:** Bara Trip19 (EON har annan kampanjstruktur)

---

## master/timeline.md vs EON's kampanjkrönika.md

**Datum:** 2026-01-06
**Fil:** `master/timeline.md`
**Skillnad från EON:**
- Trip19: `timeline.md` - kronologisk händelselista
- EON: `kampanjkrönika.md` - narrativ tidslinje med mer detalj

**Struktur:**
```markdown
## Session X - Titel (YYYY-MM-DD)

### Händelser
- Händelse 1
- Händelse 2

### NPCs
- NPC möts

### Clues
- Ledtråd hittad
```

**Gäller:** Bara Trip19

---

## Pure HTML/CSS: No frameworks

**Datum:** 2026-01-06
**Regel:** Inga JavaScript frameworks (React, Vue, etc.)
**Varför:**
- Enklare deployment
- Snabbare laddning
- Lättare att underhålla
- Inga dependencies att uppdatera

**Tillåtet:**
- Vanilla JavaScript
- CSS (embedded)
- HTML5

**Gäller:** Trip19 och EON (båda använder vanilla approach)

---

## SL-sidor: MALL_GUIDE.md

**Datum:** 2026-01-06
**Fil:** `MALL_GUIDE.md`
**Innehåll:** HTML/CSS-standarder för SL-sidor

**Standarder:**
- Inline CSS (ingen externa stylesheets)
- Responsive design (breakpoints: 1024px, 768px)
- Character-specific colors
- Consistent navigation
- Embedded fonts (om nödvändigt)

**Gäller:** Bara Trip19 (EON har andra standarder)

---

## Chesapeake Cell: "Outlaws"

**Datum:** 2026-01-06
**Karaktärer:**
- Mac Riley (FBI) - Jonas
- Father Sullivan (Navy Chaplain) - Andreas
- Kai "Sparky" Zhang (NSA) - [spelare]
- Sam "Trench" Novak (USAR) - [spelare]
- Hanna "Scalpel" Engler (Medical Examiner) - Daniel

**Cellnamn:** "Outlaws" (unofficial)

**Viktigt:**
- Alla karaktärer har pronomen dokumenterade i Complete.md
- SAN och Bonds spåras per karaktär
- Breaking Points dokumenterade

**Gäller:** Bara Trip19

---

*Senast uppdaterad: 2026-01-06*

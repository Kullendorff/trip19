# SL STANDARDIZATION CHANGELOG

**Projekt:** Standardisering av alla speledarsidor i /SL/
**Start:** 2025-11-21
**Status:** ✅ Slutförd
**Slutdatum:** 2025-11-21

## Scope
- Alla speledarsidor under /SL/
- EXKLUDERAR: Handouts (spelarmaterial)
- EXKLUDERAR: Spelarsidor (/Mac/, /Sullivan/, etc)

## Ändringar per sida

### chapter5_scene0a_baltic_crossing.html
**Datum:** 2025-11-21
**Ändringar:**
- ✅ Font: Bytte från `-apple-system, BlinkMacSystemFont, 'Segoe UI'...` till `'Courier New', Courier, monospace`
- ✅ Färger: Bytte `--accent-primary` från `#ff6b35` (orange) till `#4a90a4` (steel blue)
- ✅ Färger: Bytte `--accent-secondary` från `#4a90e2` till `#e89a3c` (warm orange)
**Status:** ✅ Klar

---

### chapter5_scene0b_truck_crossing.html
**Datum:** 2025-11-21
**Ändringar:**
- ✅ Färger: Bytte `--accent-primary` från `#ff6b35` (orange) till `#4a90a4` (steel blue)
- ✅ Färger: Bytte `--accent-secondary` från `#9d4edd` (lila) till `#e89a3c` (warm orange)
- Font var redan korrekt (Courier New)
**Status:** ✅ Klar

---

### russia_infiltration_routes.html
**Datum:** 2025-11-21
**Ändringar:**
- ✅ Färger: Bytte `--accent-primary` från `#ff6b35` (orange) till `#4a90a4` (steel blue)
- Font och --accent-secondary var redan korrekta
**Status:** ✅ Klar

---

### CHAPTER2_SCENE_VOLKOV_WARNING.html
**Datum:** 2025-11-21
**Ändringar:**
- ✅ Font: Bytte från `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif` till `'Courier New', Courier, monospace`
**Status:** ✅ Klar

---

### scalpel_berlin_resources.html
**Datum:** 2025-11-21
**Ändringar:**
- ✅ Font: Bytte från `-apple-system, BlinkMacSystemFont, 'Segoe UI'...` till `'Courier New', Courier, monospace`
- ✅ Färger: Bytte `--accent-color` från `#ff6b35` (orange) till `#4a90a4` (steel blue)
- ✅ Färger: Bytte `--accent-dark` från `#cc5529` till `#3a7082` (mörkare blå)
**Status:** ✅ Klar

---

### us_politics_2025_timeline.html
**Datum:** 2025-11-21
**Ändringar:**
- ✅ Font: Bytte från `'Segoe UI', Roboto, Helvetica, Arial, sans-serif` till `'Courier New', Courier, monospace`
- Färger var redan korrekta (#4A90A4)
**Status:** ✅ Klar

---

### black_madonna_ritual_teknisk.html
**Datum:** 2025-11-21
**Ändringar:**
- ✅ Färger: Bytte `--accent-primary` från `#ff6b35` (orange) till `#4a90a4` (steel blue)
- Font var redan korrekt (Courier New)
**Status:** ✅ Klar

---


## Sammanfattning

**Totalt antal filer granskade:** 36 HTML-filer i /SL/
**Totalt antal filer modifierade:** 7 filer
**Handouts exkluderade:** ~10 filer

### Problem som åtgärdades:
1. **Font-inkonsekvens:** 4 filer använde sans-serif fonts istället för monospace
2. **Färg-inkonsekvens:** 5 filer använde orange (#ff6b35) som primary accent istället för steel blue (#4a90a4)

### Standardiserad mall:
```css
font-family: 'Courier New', Courier, monospace;
--accent-primary: #4a90a4;  /* Steel blue */
--accent-secondary: #e89a3c; /* Warm orange */
```

### Modifierade filer:
1. chapter5_scene0a_baltic_crossing.html - Font + Färg
2. chapter5_scene0b_truck_crossing.html - Färg
3. russia_infiltration_routes.html - Färg
4. CHAPTER2_SCENE_VOLKOV_WARNING.html - Font
5. scalpel_berlin_resources.html - Font + Färg
6. us_politics_2025_timeline.html - Font
7. black_madonna_ritual_teknisk.html - Färg

**Resultat:** Alla speledarsidor i /SL/ följer nu samma font och färgschema för en konsekvent användarupplevelse.

## SPRÅKSTANDARDISERING (Svenska)

**Datum:** 2025-11-21
**Scope:** Översättning av engelska UI-element och texter till svenska

### Modifierade filer:

**index.html:**
- "HANDLER DASHBOARD" → "SL-KONTROLLPANEL"
- "CLASSIFIED // DELTA GREEN EYES ONLY" → "KLASSIFICERAD // DELTA GREEN ENDAST FÖR SL"
- "Navigation" → "Navigering"
- "Who's Who" → "Vem är Vem"

**mythos.html:**
- "CLASSIFIED - HANDLER EYES ONLY" → "KLASSIFICERAD - ENDAST FÖR SPELLEDARE"
- "Show, don't tell. Mystery, not explanation." → "Visa, berätta inte. Mysterium, inte förklaring."

**sessions.html:**
- "Dashboard" → "Kontrollpanel" (i back-länk)

**npcs.html:**
- Title tag: "Handler Dashboard" → "SL-Kontrollpanel"

**black_madonna_chapter2.html:**
- Title tag: "Shadows from the Past" → "Skuggor från det förflutna"

**black_madonna_chapter3.html:**
- Title tag: "Dark Dreams" → "Mörka drömmar"

**black_madonna_index.html:**
- "Chapter" → "Kapitel" (6 HTML-kommentarer)
- "Chapter 5 Planning" → "Kapitel 5-planering"
- "Chapter 4 Berlin-scener" → "Kapitel 4 Berlin-scener"
- "Chapter 2, Scene 14" → "Kapitel 2, Scen 14" (flera instanser)

### Resultat:
Alla synliga UI-element och rubriker är nu på svenska, samtidigt som:
- Egennamn (Delta Green, Trip 19, Volkov, etc.) behålls som de är
- Tekniska termer och CSS-klasser behålls på engelska
- Historiska citat som är menade att vara engelska behålls

**Totalt:** 10 filer modifierade för svenskt språk

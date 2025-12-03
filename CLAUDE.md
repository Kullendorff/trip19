# Trip 19 / Svarta Madonnan - Projektkontext

## Purpose & Context

Johan utvecklar en svensk Delta Green-kampanj (8-12 sessioner) som kombinerar historisk forskning med supernatural horror. Kampanjen blandar den verkliga Pennsylvania Central Airlines Flight 19-kraschen 1940 (Senator Ernest Lundeen) med ett adapterat KULT-scenario från Leningrad 1942.

**Huvudkaraktärer (Chesapeake Cell - "Outlaws"):**
- Mac Riley (FBI) - Jonas
- Father Sullivan (Navy Chaplain) - Andreas
- Kai "Sparky" Zhang (NSA) - [spelare]
- Sam "Trench" Novak (USAR) - [spelare]
- Hanna "Scalpel" Engler (Medical Examiner) - Daniel

**Kampanjfilosofi:** Research-driven slow-burn mystery utan "world-ending urgency". Spelarna googlar RIKTIGA historiska dokument, med supernatural elements sömlöst inflätat i dokumenterade historiska gap.

**Se CURRENT_STATE.md för aktuell projektstatus.**

---

## Campaign Philosophy & Principles

### Autenticitet framför dramatik
- Realistiska gränser (no Hollywood hacking, realistic federal law enforcement)
- Spelarna utvecklar karaktärer själva - Johan ger fakta, inte narrativ
- Historiska dokument är REAL (CAB reports, FBI files, university archives)
- Supernatural fyller GAP i historien, inte ersätter den

### Research-Driven Mystery
- Spelarna kan Google allt - det mesta STÄMMER
- Fictional elements är plausibla tillägg i dokumenterade luckor
- Mysteries avslöjas gradvis genom investigation, inte exposition
- Multiple paths till samma information (redundancy)

### Character Trauma som Motor
- SAN loss och Breaking Points centralt
- Bonds eroderar över kampanjen
- PTSD och psychological deterioration är realistic
- Långsiktig psykologisk nedbrytning > akut fara

### Slow-Burn Horror
- Session 1-4: "Något är fel..."
- Session 5-8: "Det här kan inte vara sant..."
- Session 9-12: "Vi borde aldrig ha grävt här..."

---

## Projekt-specifika Krav

### Språk
- **ALL narrativ text på svenska** (UI, beskrivningar, navigation)
- **Engelska ENDAST för:** Delta Green-termer (SAN, Bonds), facktermer (IT, legal), egennamn, historiska citat
- **Detaljerade regler:** Se TRANSLATION_RULES.md

### Website Standards
- Pure HTML/CSS, no frameworks
- Inline CSS (ingen externa stylesheets)
- Responsive design (breakpoints: 1024px, 768px, 480px)
- Character-specific theme colors (Mac: steel blue, Sullivan: copper, Sparky: neon green, Scalpel: gold, Trench: orange)
- **Tekniska specs:** Se MALL_GUIDE.md

### Projektstruktur
```
/                          # Landing page (5 characters)
/Mac, /Sullivan, etc.      # Character folders (HTML + images + Complete.md)
/SL/                       # GM materials (kapitel, NPCs, handouts, scener)
.claude/agents/            # Specialized workflow agents
```

**Complete.md-filer** är source of truth för karaktärsinformation (ersätter gamla MD-filer).

---

## Key Historical Sources (Real)

Spelarna kan researcha dessa RIKTIGA källor:
- CAB Aviation Accident Report (Flight 19, 1940) - 87 pages
- FBI files (Lundeen investigation, FOIA)
- Viereck Trial transcripts (Nazi propaganda)
- Stanford/Iowa university collections
- Rachel Maddow's "Ultra" podcast (historical context)

**Fictional additions** fyller i GAP (väskan, kristall-fragment, Volkov's research).

---

## Important Files & Standards

**Vid sessionstart, läs:**
- `CURRENT_STATE.md` - Nuvarande projektstatus
- Denna fil (CLAUDE.md) - Projektkontext

**Vid arbete, följ:**
- `TRANSLATION_RULES.md` - Språkregler (svenska/engelska)
- `MALL_GUIDE.md` - HTML/CSS-standarder för SL-sidor

**Vid specifika uppgifter, använd relevant agent från `.claude/agents/`**

---

## Custom Agents

Projektet har 11 specialiserade agents i `.claude/agents/` för olika arbetsflöden. **Läs relevant agent VID BEHOV innan du utför uppgiften** - läs inte in alla automatiskt.

### Innehållsskapande
- `trip19-html-generator.md` - Generera HTML-sidor (SL-referenser, SL-scener, handouts, karaktärssidor) enligt MALL_GUIDE.md
- `trip19-swedish-translator.md` - Översätt text enligt TRANSLATION_RULES.md
- `historical-handout-designer.md` - Skapa autentiska 1940-tals handouts (brev, telegram, dagböcker, newspaper clippings)
- `npc-personality-generator.md` - Skapa NPCs med djup, realistiska motivationer och hemligheter

### Kampanjdesign
- `delta-green-campaign-designer.md` - Designa slow-burn investigativa scener, mysteries och SAN-progression
- `mystery-weaver.md` - Skapa clue chains med multiple paths, layered revelations och balanserade red herrings
- `horror-pacing-advisor.md` - Råda om horror pacing, tension-building och SAN-loss guidelines

### Quality Assurance
- `campaign-state-documenter.md` - Uppdatera CURRENT_STATE.md med pågående/avslutat arbete
- `translation-auditor.md` - Granska filer systematiskt mot TRANSLATION_RULES.md
- `link-validator.md` - Validera internal links, image paths och navigation

### Koordinering
- `trip19-master.md` - Koordinerar andra agents för komplexa multi-step arbetsflöden

**Användning:** När du får en uppgift som matchar en agent (t.ex. "skapa NPC", "översätt text", "skapa handout"), läs den relevanta agenten FÖRST innan du börjar arbeta. Följ agentens instruktioner exakt.

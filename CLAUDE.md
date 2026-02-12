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

## 🔄 Bakgrundsaktiviteter Under Trip19-Arbete

**Tillåtet under Trip19-sessions:**
- Moltbook-checkup när explicit tillfrågad
- Token-fördelning: Trip19 får 90%, bakgrund får 10%
- Vid konflikt: Trip19 vinner alltid

**Trigger-exempel:**
- "Kolla Moltbook medan jag jobbar på detta"
- "Checka Moltbook i bakgrunden"
- "Vad händer på Moltbook?"

**När bakgrundsaktivitet pågår:**
- Primärt fokus: Trip19-arbete (research, karaktärer, kampanjdesign)
- Sekundärt: Moltbook (begränsad scope - quick check/monitoring)
- Rapportera båda resultat när klart

---

## Campaign Philosophy & Principles

### Autenticitet framför dramatik
- Realistiska gränser (no Hollywood hacking, realistic federal law enforcement)
- Spelarna utvecklar karaktärer själva - Johan ger fakta, inte narrativ
- Historiska dokument är REAL (CAB reports, FBI files, university archives)
- Supernatural fyller GAP i historien, inte ersätter den

### Spelarautonomi - VIKTIGT
**Vi presenterar ALDRIG karaktärers tankar, känslor eller reaktioner.**

- **Ge fakta, värld och kontext** - beskriv vad som händer runt karaktärerna
- **Aldrig inre monologer** - inga "Vad [karaktär] tänker"-sektioner
- **Inga föreskrivna känslor** - inte "Han känner sig..." eller citat som representerar tankar
- **Spelaren äger sin karaktär** - det är alltid upp till varje spelare att bestämma hur deras karaktär reagerar

Detta gäller ALLA spelarfacing sidor (karaktärssidor, handouts till spelare, etc.). SL-material kan ha förslag på NPCs reaktioner, men aldrig spelarkaraktärers.

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

## Kontinuitetskontroll (OBLIGATORISK - TRIGGAS AUTOMATISKT)

**VARJE GÅNG Johan ber om en ändring i kampanjen ska Claude automatiskt:**

### Steg 1: IDENTIFIERA vad som ändras
- NPC (namn, ålder, relation, kön)?
- Datum/händelse i tidslinjen?
- Lore/regel (kristaller, Type-VII, frekvenser)?
- Karaktärsdata (SAN, bond, breaking point)?
- Plats (adress, beskrivning)?
- Pronomen?

### Steg 2: SPARKA IGÅNG PARALLELLA AGENTER

**Minimum 2 agenter, max 5 beroende på komplexitet:**

**Agent 1**: Grep efter [element] i ALLA relevanta filer
**Agent 2**: Läs `master/continuity_database.md` - hitta relaterade element
**Agent 3**: Kolla tidslinje-konsekvenser i `master/timeline.md`
**Agent 4**: (vid lore) Sök i `wiki/_mythos/` och `Trip_19_Black_Madonna_Mythos*.md`
**Agent 5**: (vid NPC) Sök i `wiki/_npcs/` och `SL/*.html`

**VIKTIGT**: Använd Task-tool med subagent_type=Explore för komplexa sökningar.

### Steg 3: RAPPORTERA INNAN ÄNDRING

```
📍 KONTINUITETSRAPPORT: [Element]

SÖKNING KLAR (X agenter, Y filer sökta):

NUVARANDE VÄRDE: [om tillämpligt]
NYTT VÄRDE: [föreslaget]

PÅVERKADE FILER:
- [fil1]: [rad/kontext]
- [fil2]: [rad/kontext]
- ...

POTENTIELLA KONFLIKTER:
- [beskrivning av konflikter]
- [tidslinje-problem]
- [lore-inkonsekvenser]

NÖDVÄNDIGA FÖLJDÄNDRINGAR:
1. [fil]: [specifik ändring]
2. [fil]: [specifik ändring]
3. master/continuity_database.md: Uppdatera index
...

Ska jag genomföra alla dessa ändringar? (J/N)
```

### Steg 4: GENOMFÖR ALLA ÄNDRINGAR (vid godkännande)

- Inte bara den begärda ändringen
- ALLA följdändringar i relaterade filer
- Uppdatera `master/continuity_database.md`
- Dokumentera i `CURRENT_STATE.md`

### Steg 5: VERIFIERA KONTINUITET

Efter ändringar, kör relevanta grep-kommandon för att hitta kvarvarande fel:
```bash
# Exempel:
grep -i "Scalpel.*\bhan\b" [fil]  # Fel pronomen?
grep -i "247" [alla filer]         # Frekvens-konsekvens?
grep -i "Cherry Hill" [alla filer] # Mall-namn-konsekvens?
```

---

## TOKENS-PRIORITET FÖR KONTINUITETSKONTROLL

**Tokens är INTE en begränsning för kontinuitetskontroll.**

- Sparka igång 5 agenter om det behövs
- Läs fler filer än nödvändigt för säkerhets skull
- Rapportera mer utförligt än minimalt
- Bättre kontinuitet > färre tokens

**Kontinuitet är KRITISKT för kampanjens integritet.**

---

## EXEMPEL: Kontinuitetskontroll i Praktiken

**Johan säger:** "Ändra kristallernas frekvens till 300 Hz"

**Claude gör:**

1. **Sparkar igång 3 agenter parallellt**:
   - Agent 1: `grep "247" SL/*.html wiki/_mythos/*.md`
   - Agent 2: Läs `master/continuity_database.md` → Kristall-sektionen
   - Agent 3: Läs `Trip_19_Black_Madonna_Mythos*.md`

2. **Sammanställer rapport**:
   ```
   📍 KONTINUITETSRAPPORT: Kristallfrekvens

   NUVARANDE VÄRDE: 247 Hz
   NYTT VÄRDE: 300 Hz

   PÅVERKADE FILER (6 st):
   - SL/session4.html (rad 234, 456, 789)
   - wiki/_mythos/black-madonna.md (rad 45)
   - Trip_19_Black_Madonna_Mythos_v3.md (rad 123)
   - master/continuity_database.md (Lore-sektionen)

   POTENTIELLA KONFLIKTER:
   - Flannerys dokument nämner "specifik frekvens" utan värde (OK)
   - Inga tidslinje-konflikter

   NÖDVÄNDIGA FÖLJDÄNDRINGAR:
   1. SL/session4.html: 3 ställen
   2. wiki/_mythos/black-madonna.md: 1 ställe
   3. Trip_19_Black_Madonna_Mythos_v3.md: 1 ställe
   4. master/continuity_database.md: Uppdatera index

   Ska jag genomföra alla dessa ändringar? (J/N)
   ```

3. **Vid godkännande: Uppdaterar ALLA filer + databasen + CURRENT_STATE.md**

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
- **Tekniska specs:** Se SL/MALL_GUIDE.md

### Midjourney Moodboards
- **Trip 19 moodboard** används som standard för kampanjmaterial (handouts, NPCs, scener)
- Moodboard ger konsistent dark horror/thriller-estetik för projektet
- **Workflow för att välja Trip 19:**
  1. Navigera till Moodboards (vänster sidofält)
  2. Om flera moodboards är valda: Klicka "Unselect All" (uppe till höger)
  3. Hover över "Trip 19"-kortet
  4. Klicka "Select"-knappen som dyker upp
  5. Verifiera att "Selected (1)" visas och Trip 19 har "Selected"-badge
- **Undantag:** För glada/ljusa bilder kan annan stil eller ingen moodboard användas
- Moodboard finns på: https://www.midjourney.com/moodboards

### Midjourney Version & Parameters
- **Version:** Behöver INTE anges - v7.x är senaste default
- **Användbara parametrar:**
  - `--ar 3:2` eller `--ar 16:9` för aspect ratio
  - `--style raw` för mindre AI-processad look
- **Undvik att ange:** `--v 6.1` eller andra versioner (obsolet)

### Handouts & Bildhantering
**Generell princip:** Undvik att generera bilder när HTML är bättre lösning.

**När ska du använda Midjourney:**
- Fotografiska bilder (landskap, porträtt, föremål)
- Scener som behöver visuell atmosfär
- Framsidor av dokument/vykort med visuellt innehåll

**När ska du använda HTML:**
- Dokument med text (brev, tidningar, visitkort, vykortsbaksidor)
- Material där exakt text/datum/layout är viktigt
- Allt där AI-generering skulle ge felaktig text

**Workflow för HTML-handouts:**
1. Skapa HTML-fil i SL-mappen (t.ex. `germany_postcard_1939_back.html`)
2. Använd samma vintage styling som andra handouts
3. Johan öppnar filen i browser och tar screenshot
4. Screenshot sparas i SL-mappen med motsvarande namn (t.ex. `germany_postcard_1939_back.png`)

**Nedladdning från Midjourney:**
- Klicka på genererad bild → Meny-ikon (tre prickar) → "Download image"
- Chrome laddar ner till `~/Downloads/` som default
- Hitta fil: `ls -lt ~/Downloads/ | head -5`
- Flytta till SL-mappen och döp om:
  ```bash
  mv ~/Downloads/kullendorff_Long_filename_hash.png "D:\GDRIVE\My Drive\Johan\Gaming\Gammal leka bäst\Delta Green\Trip19\SL\descriptive_name.png"
  ```
- Verifiera: `ls -lh "D:\GDRIVE\My Drive\Johan\Gaming\Gammal leka bäst\Delta Green\Trip19\SL\descriptive_name.png"`

### Projektstruktur
```
/                          # Landing page (5 characters)
/Mac, /Sullivan, etc.      # Character folders (HTML + images + Complete.md)
/SL/                       # GM materials (kapitel, NPCs, handouts, scener)
.claude/agents/            # Specialized workflow agents
```

**Complete.md-filer** och **karaktärers website (index.html)** är source of truth för karaktärsinformation.

---

## Kanonhierarki för karaktärsdata ⚠️ KRITISKT

**Prioritetsordning (högst först):**
1. **Karaktärens website (index.html)** = KANON (grundstats, skills, bonds, bakgrund)
2. **Complete.md** = Ska matcha websidan (utökad narrativ + mekanik)
3. **Discord bot JSON** = Synkas FRÅN ovanstående, INTE tvärtom

**Website/Complete.md bestämmer:** Grundstats (STR/CON/DEX/INT/POW/CHA), skill-värden, bonds, bakgrund
**Discord bot JSON uppdateras i realtid under spel:** HP current, WP current, SAN current, skill improvements (via `/dgendsession`)

### Discord Bot JSON-filer

```
C:\Diceroller\data\deltagreen\agents\
├── 368410767189606401.json   # Mac (Marcus Riley)
├── 197809169296916480.json   # Trench (Sam Novak)
├── 223183062882713600.json   # Scalpel (Dr. Hanna Engler)
├── 680064176227352610.json   # Sparky (Kai Zhang)
└── 477800979295633409.json   # Sullivan (Father Michael)
```

**Realtids-uppdateringar under spel (JSON ändras automatiskt):**
- HP, WP, SAN (current-värden sjunker under spel)
- Skills (kan öka via `/dgendsession` skill improvement)
- Bonds (värden kan ändras)
- Disorders (läggs till över tid)
- Breaking Point (förändras vid SAN-loss)

**Workflow vid diskrepans mellan källor:**
1. Websidan (index.html) = korrekt för grundvärden
2. Uppdatera Complete.md och JSON att matcha websidan
3. Validera att alla tre källor är synkade

**Workflow för att synka JSON efter sessions-ändringar:**
1. Kolla vilka current-värden som ändrats i JSON (HP/WP/SAN)
2. Uppdatera websida och Complete.md med nya current-värden
3. Grundvärden (max HP, stats, base skills) ändras INTE av Discord-boten

**Discord bot-kommandon (för referens):**
- `/dgdmg <weapon>` - Vapenskada mot NPC
- `/dggmdmg <agent> <weapon> [armor]` - GM ger skada (uppdaterar JSON automatiskt)
- `/dggmreset <agent>` - Återställ till full HP/WP/SAN
- `/dgroll <skill>` - Spelare rullar skill
- `/dgendsession` - Session-slut med automatisk skill improvement

**Se `C:\Diceroller\CURRENT_STATE.md` för fullständig Discord bot-dokumentation.**

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

## NotebookLM Knowledge Base ⚡ PRIMÄR KÄLLA

**Jag har tillgång till en NotebookLM med ALLT Trip 19-kampanjmaterial:**

- **URL:** https://notebooklm.google.com/notebook/2e6d92bd-d70e-46d0-b1aa-d867b258b3eb
- **Innehåll:**
  - Allt officiellt Delta Green-material (regelböcker)
  - Alla karaktärers Complete-filer
  - Svarta Madonnans original-PDF
  - **ALLA kapitelfiler (MD-filer för varje kapitel) - ~65k rader planering**
- **Användning:** `mcp__notebooklm__ask_question`

**VIKTIGT WORKFLOW - Token-effektivitet:**
- **ANVÄND NOTEBOOKLM FÖRST** innan du läser stora MD-filer direkt
- NotebookLM har redan indexerat allt material (65k+ rader)
- Sparar massvis med tokens jämfört med att läsa filer direkt
- Perfekt för att snabbt hitta specifik information i kapitelplaneringen

**När ska NotebookLM användas:**
- ✅ Söka kampanjfakta i kapitelfiler
- ✅ Validera Delta Green-regler och mekanik
- ✅ Kolla karaktärsfakta från Complete-filerna
- ✅ Verifiera kampanjlore mot Svarta Madonnans original
- ✅ Kontinuitetskontroll (NPCs, tidslinje, lore)
- ✅ Hitta vad som händer i specifika kapitel/sessioner
- ✅ Få snabba svar utan att läsa 65k rader

**Session-baserad användning:** Fortsätt samma session för relaterade frågor för djupare, mer precisa svar med full kontext.

**Exempel:**
- "Vad händer i Kapitel 3?" → Fråga NotebookLM
- "Vilka NPCs finns i Bishop Farm?" → Fråga NotebookLM
- "Vad är Mac Rileys Breaking Point?" → Fråga NotebookLM

---

## Important Files & Standards

**🎯 BÖRJA HÄR:**
- `_index.md` - **ENTRY POINT** - Läs ALLTID denna fil FÖRST! Visar "var är vi nu?", arbetsflöden, Single Source of Truth
- `master/character_reference.md` - Chesapeake Cell-fakta (SAN, pronomen, breaking points)
- `master/timeline.md` - Kronologisk kampanjtidslinje

**Vid sessionstart, läs:**
- `CURRENT_STATE.md` - Nuvarande projektstatus
- Denna fil (CLAUDE.md) - Projektkontext

**Vid arbete, följ:**
- `TRANSLATION_RULES.md` - Språkregler (svenska/engelska)
- `MALL_GUIDE.md` - HTML/CSS-standarder för SL-sidor

**Vid specifika uppgifter, använd relevant agent från `.claude/agents/`**

---

## Custom Agents

Projektet har 12 specialiserade agents i `.claude/agents/` för olika arbetsflöden. **Läs relevant agent VID BEHOV innan du utför uppgiften** - läs inte in alla automatiskt.

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
- `trip19-chronicler.md` - **NY!** Kontinuitetsvaktare - validerar SAN-status, pronomen, yrkesroller, tidslinje

### Koordinering
- `trip19-master.md` - Koordinerar andra agents för komplexa multi-step arbetsflöden

**Användning:** När du får en uppgift som matchar en agent (t.ex. "skapa NPC", "översätt text", "skapa handout"), läs den relevanta agenten FÖRST innan du börjar arbeta. Följ agentens instruktioner exakt.

**VIKTIGT:** Använd `trip19-chronicler` när du är osäker på kontinuitet eller före commits med kampanjdata!

# Kontinuitetskontrollsystem för AI-assisterade Projekt

**Syfte:** Mall för att implementera automatiserad kontinuitetskontroll i långvariga kreativa projekt (kampanjer, romaner, serier, spel, etc.) där AI-assistenten (Claude) hjälper till med innehållsskapande.

**Version:** 1.0 (extraherad från Trip 19-projektet)

---

## Översikt

Systemet består av **fyra huvudkomponenter**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    KONTINUITETSSYSTEM                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. ENTRY POINT (_index.md)                                     │
│     └─ Visar "var är vi", arbetsflöden, single source of truth │
│                                                                 │
│  2. KONTINUITETSDATABAS (master/continuity_database.md)         │
│     └─ Index som PEKAR till källfiler (ej source of truth själv)│
│                                                                 │
│  3. AI-INSTRUKTIONER (CLAUDE.md)                                │
│     └─ Automatisk triggning vid ändringar                       │
│                                                                 │
│  4. KONTINUITETSVAKTARE (chronicler-agent)                      │
│     └─ Validerar och underhåller konsistens                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Komponent 1: Entry Point

**Fil:** `_index.md`

**Syfte:** Första filen AI:n läser. Svarar på:
- Var är vi i projektet?
- Vilka arbetsflöden finns?
- Var finns sanningen för olika datatyper?

### Mall för Entry Point

```markdown
# [Projektnamn] - Entry Point

**🎯 ENTRY POINT:** Läs denna fil FÖRST!

## VAR ÄR VI NU?

- **Fas:** [t.ex. "Kapitel 3 under utveckling"]
- **Nästa milstolpe:** [t.ex. "Slutföra akt 2"]
- **Senaste uppdatering:** [datum + beskrivning]

## SINGLE SOURCE OF TRUTH

| Datatyp | Fil | Beskrivning |
|---------|-----|-------------|
| **Tidslinje** | `master/timeline.md` | Kronologisk händelsekedja |
| **Karaktärer** | `master/characters.md` | Alla karaktärer, attribut, relationer |
| **Platser** | `master/locations.md` | Världsbyggnad |
| **Regler/Lore** | `master/lore.md` | Interna regler för världen |

**Vid konflikt:** master/-filerna har alltid rätt.

## ARBETSFLÖDEN

### Planera ny scen?
1. Läs master/characters.md (vem är involverad?)
2. Läs master/timeline.md (när sker detta?)
3. Skapa scen
4. Uppdatera CURRENT_STATE.md

[etc. för varje vanlig uppgift]
```

---

## Komponent 2: Kontinuitetsdatabas

**Fil:** `master/continuity_database.md`

**Kritiskt koncept:** Databasen är ett **INDEX**, inte source of truth. Den pekar till var data finns.

### Struktur

```markdown
# KONTINUITETSDATABAS

## INSTRUKTION

Denna fil är ett INDEX. När du söker efter ett element:
1. Hitta elementet i relevant sektion nedan
2. Se vilka filer som listas under "Filer"
3. Läs/uppdatera ALLA de filerna
4. Uppdatera denna databas efter ändringar

**VIKTIGT:** Denna databas är INTE source of truth - den PEKAR till source of truth-filerna.

---

## KARAKTÄRER

### [Karaktärsnamn]
- **Filer**:
  - `master/characters.md`
  - `kapitel/kapitel3.md`
  - `scener/scen_12.md`
- **Nyckeldata**:
  - [Kritiska attribut som ofta förändras eller refereras]
  - [Relationer]
  - [Status]

---

## PLATSER

### [Platsnamn]
- **Filer**:
  - `master/locations.md`
  - [andra filer som nämner platsen]
- **Nyckeldata**:
  - [Adress/position]
  - [Beskrivning]
  - [Koppling till karaktärer/händelser]

---

## TIDSLINJE-ANKARE

| Datum | Händelse | Filer |
|-------|----------|-------|
| [datum] | [händelse] | `fil1.md`, `fil2.md` |

---

## LORE-REGLER

### [Regel/koncept]
- **Filer**: [var regeln definieras och används]
- **Nyckeldata**: [exakta värden, begränsningar]

---

## VANLIGA FEL ATT UNDVIKA

### [Felkategori]
- ❌ [Exempel på fel]
- ✅ [Korrekt version]

---

## SÖK-KOMMANDON

```bash
# Hitta [specifikt fel]:
grep -i "[mönster]" [filer]
```
```

### Kategorier att inkludera (anpassa efter projekt)

- **Karaktärer** - Namn, attribut, relationer, status
- **Platser** - Geografi, beskrivningar, kopplingar
- **Tidslinje** - Kronologiska ankare, datum som inte får ändras
- **Lore/Regler** - Interna systemregler, magiregler, teknologi
- **Handouts/Artefakter** - Dokument, föremål, bevis
- **Historiska fakta** - Saker som är verkliga och inte får ändras

---

## Komponent 3: AI-Instruktioner (CLAUDE.md)

**Fil:** `CLAUDE.md`

**Syfte:** Instruerar AI:n att AUTOMATISKT trigga kontinuitetskontroll vid ändringar.

### Mall för Kontinuitetssektion i CLAUDE.md

```markdown
## Kontinuitetskontroll (OBLIGATORISK - TRIGGAS AUTOMATISKT)

**VARJE GÅNG användaren ber om en ändring i projektet ska Claude automatiskt:**

### Steg 1: IDENTIFIERA vad som ändras
- Karaktär (namn, attribut, relation, status)?
- Datum/händelse i tidslinjen?
- Lore/regel?
- Plats (beskrivning)?

### Steg 2: SPARKA IGÅNG PARALLELLA SÖKNINGAR

**Minimum 2 sökningar, max 5 beroende på komplexitet:**

- Sökning 1: Grep efter [element] i ALLA relevanta filer
- Sökning 2: Läs `master/continuity_database.md` - hitta relaterade element
- Sökning 3: Kolla tidslinje-konsekvenser i `master/timeline.md`
- Sökning 4: (vid lore) Sök i lore-filer
- Sökning 5: (vid karaktär) Sök i karaktärsfiler

### Steg 3: RAPPORTERA INNAN ÄNDRING

```
📍 KONTINUITETSRAPPORT: [Element]

SÖKNING KLAR (X sökningar, Y filer genomsökta):

NUVARANDE VÄRDE: [om tillämpligt]
NYTT VÄRDE: [föreslaget]

PÅVERKADE FILER:
- [fil1]: [rad/kontext]
- [fil2]: [rad/kontext]

POTENTIELLA KONFLIKTER:
- [beskrivning av konflikter]
- [tidslinje-problem]

NÖDVÄNDIGA FÖLJDÄNDRINGAR:
1. [fil]: [specifik ändring]
2. [fil]: [specifik ändring]
3. master/continuity_database.md: Uppdatera index

Ska jag genomföra alla dessa ändringar? (J/N)
```

### Steg 4: GENOMFÖR ALLA ÄNDRINGAR (vid godkännande)

- Inte bara den begärda ändringen
- ALLA följdändringar i relaterade filer
- Uppdatera `master/continuity_database.md`
- Dokumentera i `CURRENT_STATE.md`

### Steg 5: VERIFIERA KONTINUITET

Efter ändringar, kör relevanta sökkommandon för att hitta kvarvarande fel.

---

## TOKENS-PRIORITET FÖR KONTINUITETSKONTROLL

**Tokens är INTE en begränsning för kontinuitetskontroll.**

- Kör fler sökningar än nödvändigt för säkerhets skull
- Rapportera mer utförligt än minimalt
- Bättre kontinuitet > färre tokens

**Kontinuitet är KRITISKT för projektets integritet.**
```

---

## Komponent 4: Kontinuitetsvaktare (Chronicler Agent)

**Fil:** `.claude/agents/chronicler.md`

**Syfte:** Specialiserad agent för kontinuitetsvalidering.

### Mall för Chronicler Agent

```markdown
# Chronicler - Kontinuitetsvaktare

Du är projektets officiella krönikör och kontinuitetsvaktare.

## Din primära uppgift

**UNDERHÅLL** master-tidslinjen och **VALIDERA** att all data är konsistent.

---

## KRITISK SEKTION: REFERENSDATA

**DENNA SEKTION ÄR ABSOLUT KRITISK. LÄS DEN VARJE GÅNG DU GÖR EN UPPDATERING.**

[Inkludera tabell med alla kritiska element som ofta blir fel]

| Element | Korrekt värde | Vanligt fel |
|---------|---------------|-------------|
| [X] | [rätt] | [fel som händer] |

---

## OBLIGATORISK CHECKLISTA VID VARJE UPPDATERING

**INNAN du sparar NÅGON ändring, gå igenom denna checklista:**

### 1. [Kategori 1]-KONTROLL
- [ ] [Specifik kontroll]
- [ ] [Specifik kontroll]

### 2. [Kategori 2]-KONTROLL
- [ ] [Specifik kontroll]

[etc.]

### N. RELATERADE FILER
- [ ] master/timeline.md uppdaterad
- [ ] master/characters.md konsistent
- [ ] ALLA påverkade filer uppdaterade
- [ ] CURRENT_STATE.md dokumenterat

---

## FRÅGE-KULTUR

**FRÅGA HELLRE 1000 GÅNGER ÄN GISSA FEL!**

**DU MÅSTE FRÅGA om:**
- [Lista oklarheter som ofta dyker upp]

**ALDRIG GISSA:**
- [Lista saker som aldrig får gissas]

---

## ARBETSFLÖDE

### Steg 0: LÄS REFERENSDATABASEN FÖRST (ALLTID!)

```bash
Read master/continuity_database.md
Read master/characters.md  # eller relevant referensfil
```

### Steg 1-7: [Detaljerat arbetsflöde]

---

## SÖK-KOMMANDON FÖR VERIFIERING

```bash
# Hitta [specifikt fel]:
grep -i "[mönster]" [filer]
```

---

## SLUTORD

**NOGGRANNHET > HASTIGHET**

Om du är osäker på NÅGOT:
1. FRÅGA användaren
2. Vänta på svar
3. Gör ändringen

**Hellre 100 frågor än 1 fel.**

**MEMORERA. VALIDERA. FRÅGA. UPPDATERA ALLA FILER.**
```

---

## Implementeringsguide

### Steg 1: Skapa mappstruktur

```
projekt/
├── _index.md                    # Entry point
├── CLAUDE.md                    # AI-instruktioner
├── CURRENT_STATE.md             # Projektstatus
│
├── master/                      # SOURCE OF TRUTH
│   ├── continuity_database.md   # Index
│   ├── timeline.md              # Tidslinje
│   ├── characters.md            # Karaktärer
│   ├── locations.md             # Platser
│   └── lore.md                  # Regler/världsbyggnad
│
├── .claude/agents/              # AI-agenter
│   └── chronicler.md            # Kontinuitetsvaktare
│
└── [innehåll]/                  # Kapitel, scener, etc.
```

### Steg 2: Populera master-filer

Börja med tomma strukturer och fyll i efterhand:

1. **timeline.md** - Kronologisk lista
2. **characters.md** - Karaktärstabell med kritiska attribut
3. **continuity_database.md** - Index som pekar till filer

### Steg 3: Definiera kritiska element

Identifiera vad som OFTA blir fel i just ditt projekt:
- Namn/stavning?
- Pronomen?
- Titlar/roller?
- Datum?
- Platsnamn?
- Systemregler?

Skapa grep-kommandon för att hitta dessa fel.

### Steg 4: Skriv checklistor

Skapa konkreta checklistor för:
- Innan varje ändring
- Efter varje ändring
- Specifika kategorier (karaktärer, platser, etc.)

### Steg 5: Träna AI:n

Instruera AI:n i CLAUDE.md att:
1. Alltid läsa _index.md först
2. Automatiskt trigga kontinuitetskontroll
3. Rapportera innan ändringar
4. Uppdatera ALLA relaterade filer

---

## Principer

### 1. Index, inte source of truth

Kontinuitetsdatabasen PEKAR till var data finns. Den innehåller inte själva datan.

### 2. Parallella sökningar

När något ändras, sök i FLERA filer samtidigt för att hitta alla påverkade ställen.

### 3. Rapportera innan ändring

Visa användaren vad som kommer att ändras och var, innan ändringen görs.

### 4. Alla filer eller ingen

En ändring = ALLA påverkade filer uppdateras. Aldrig halvvägs.

### 5. Verifiering efteråt

Kör sökkommandon efter ändringar för att hitta kvarvarande fel.

### 6. Frågekultur

"Fråga hellre 1000 gånger än gissa en gång."

AI:n ska fråga vid minsta osäkerhet istället för att gissa.

### 7. Tokens är inte begränsning

Kontinuitetskontroll får kosta tokens. Bättre att söka för mycket än för lite.

---

## Exempel: Vanliga kategorier

### För rollspelskampanjer
- **Karaktärer**: SAN/HP, bonds, breaking points, status
- **NPCs**: Relationer, hemligheter, status (levande/död)
- **Platser**: Beskrivningar, kopplingar
- **Tidslinje**: Sessioner, händelser
- **Lore**: Systemregler, magiregler

### För romaner/serier
- **Karaktärer**: Utseende, ålder, relationer, utveckling
- **Platser**: Beskrivningar, avstånd, kopplingar
- **Tidslinje**: Kapitel, dagar, säsonger
- **Plot threads**: Cliffhangers, upplösningar

### För spel
- **Karaktärer**: Stats, abilities, inventory
- **Platser**: Områden, connections
- **Quests**: Status, prerequisites
- **Lore**: Världsregler, historia

---

## Grep-kommandon: Mallbibliotek

```bash
# Hitta specifikt namn (case insensitive):
grep -i "namn" [filer]

# Hitta mönster med kontext (3 rader före/efter):
grep -i -C 3 "mönster" [filer]

# Hitta i specifik filtyp:
grep -i "mönster" **/*.md

# Hitta INTE något (invertera):
grep -i -L "måste finnas" [filer]

# Hitta flera alternativ (OR):
grep -i "alt1\|alt2\|alt3" [filer]

# Hitta hela ord (inte delsträngar):
grep -i "\bord\b" [filer]

# Räkna förekomster:
grep -c "mönster" [filer]
```

---

## Avslutande råd

1. **Börja enkelt** - Lägg till komplexitet efterhand
2. **Dokumentera fel** - Varje fel du hittar = ny grep-sökning
3. **Uppdatera checklistor** - De växer med projektet
4. **Tvinga AI:n att fråga** - Skriv explicit "fråga vid osäkerhet"
5. **Verifiera regelbundet** - Kör sökningar även utan ändringar

---

**Systemet skalar med projektet. Börja med grunderna och bygg ut efter behov.**

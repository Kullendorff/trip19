# CURRENT STATE - Trip 19 / Svarta Madonnan

## Senast uppdaterad
2026-01-10

## Projektöversikt
Delta Green-kampanj på svenska med 5 spelarkaraktärer (Chesapeake Cell):
- **Mac Riley** (FBI) - Jonas
- **Father Sullivan** (Navy Chaplain) - Andreas
- **Kai "Sparky" Zhang** (NSA) - [spelare]
- **Sam "Trench" Novak** (USAR) - [spelare]
- **Hanna "Scalpel" Engler** (Medical Examiner) - Daniel

## Senaste utveckling (från git-log)

### Pågående arbete
**Kontinuitetsfix: Volkov-massakern** - Fixad januari 2026 ✅
- **Problem upptäckt**: Diskrepans mellan FBI-PDFer och kampanjdata
  - PDF-filer (officiell, Mac-annoterad, Sparky-annoterad): "Cherry Hill Mall, New Jersey" + 12 döda
  - Kampanjfiler: Blandning av "Christmas Mall" och felaktiga dödsantal (14/23)
- **Lösning**: PDFerna var korrekta - kampanjfilerna behövde fixas
- **Ändringar**: 17 filer uppdaterade
  - Mall-namn: "Christmas Mall" → "Cherry Hill Mall, New Jersey"
  - Dödsantal: 14/23 → 12 döda (konsistent överallt)
  - Plats: "WASHINGTON DC" → "CHERRY HILL, NEW JERSEY"
- **Verifiering**: Inga kvarvarande diskrepanser
- **Commit**: `0f8c68e` - "Fixa Volkov-massakern: Cherry Hill Mall, NJ + 12 döda"

**Kampanjkalender 2025** - Massiv expansion med 30+ nya händelser + 5 SL-verktyg ✅
- **Fil**: `SL/campaign_calendar_2025.html`
- **Funktion**: Google Calendar-liknande månadsvy för verkliga händelser sep-nov 2025
- **Grundfeatures**:
  - Månadsnavigering (← September → Oktober → November →)
  - Klickbara dagar med modaler (kompakt sammanfattning, länk till fullständig tidslinje)
  - Karaktärstaggar (färgade prickar på dagar som påverkar Chesapeake Cell)
  - **30+ händelser** inkluderade (ursprungligen 20+, nu massivt utökad)
- **SL-verktyg** (10 jan 2026):
  - **Filterfunktion**: Filtrera per karaktär (Mac/Sullivan/Sparky/Scalpel/Trench) och kritikalitet
  - **Sökfunktion**: Live-sök i händelsetitlar och beskrivningar
  - **Event-kategorier**: 5 kategorier (Political/Violence/Law Enforcement/Delta Green/Personal) med ikoner
  - **GM Notes**: Privata SL-anteckningar per händelse (sparas i localStorage)
  - **Kampanjprogress-marker**: Markera "vi är här nu" med 🎯-ikon och grön highlight
- **Nya händelser tillagda** (10 jan 2026):
  - 6 sep: Polen NATO Article 4 + Bitcoin ATH $126k
  - 6 okt: Candace Owens-läcka + Bitcoin ATH
  - 10 okt: Bitcoin RED OCTOBER krasch ($9.89B likvideras)
  - 13 okt: Israel-Hamas sista gisslan
  - 4 nov: Tyfon Kalmaegi (200+ döda)
  - 10 nov: Delhi bilbomb (10+ döda)
  - 12 nov: Sista US penny
  - 13 nov: Operation Southern Spear (80+ döda)
  - 17 nov: FN ISF Gaza
  - 22 nov: Bitcoin botten $80,700 (-36%)
  - 30 nov: Bitcoin rebound $87,600
- **Design**: Delta Green-tema, responsive (mobil/tablet/desktop)
- **Integration**: Länkad från SL/index.html
- **Commits**: `36d8ef9` (skapande), `8b4dd83` (SL-verktyg), `59e5c5b` (massiv expansion)

**USA Inrikespolitik 2025 - Tidslinje** - Massiv expansion februari-november (10 jan 2026) ✅
- **Fil**: `SL/us_politics_2025_timeline.html`
- **Ny sektion tillagd**: FEBRUARI-MAJ 2025 (NSA & Intelligence Community)
  - 6 feb: NSA deferred resignation erbjudande
  - Mars: Elon Musk besöker Fort Meade
  - April: General Timothy Haugh sparkas från NSA (Laura Loomer-påtryckningar)
  - Maj: NSA 8% nedskärningar (1,500-2,000 positioner)
- **Juni-tillägg**:
  - 14 jun: Minnesota-morden (DFL State Rep. Melissa Hortman och man, Sen. John Hoffman och fru)
- **Juli-tillägg**:
  - NSA Hartmans nominering dras tillbaka (7 månaders ledarskapsvakuum)
- **September-tillägg**:
  - 6 sep: Ryska drönare in i Polen - NATO Article 4 + Bitcoin ATH $126k
  - Uppdaterad Charlie Kirk-doxxing (63,000 submissions, 41 namn publicerade, 350+ Texas-lärare)
- **Oktober-tillägg**:
  - 6 okt: Bitcoin ATH + Candace Owens läcker Kirk WhatsApp-meddelanden
  - 10 okt: Detaljerad Bitcoin RED OCTOBER krasch (exakta UTC-tider, $-belopp, whale-positioner)
  - 13 okt: Israel-Hamas fred (sista gisslan frisläppta, FN ISF Gaza)
- **Utökade detaljer**:
  - DC National Guard: M17-pistoler, M4-gevär (24 aug)
  - Charlotte's Web: NASCAR-fordon till ICE
  - Regeringsstängning: $7B ekonomiska förluster
- **Commit**: `59e5c5b` - "Massiv expansion av kalender och tidslinje med 30+ nya händelser"

**Karaktärsuppdateringar** - Januari 2026 ✅
- **Trench Pittsburgh-sida**: Ny wide hero banner-bild (trench_civil.png, 16:9 format)
- **Scalpel personligt.html**: Ny träningssektion tillagd
  - Krav Maga-bakgrund (Berlin 2010-2011, Schöneberg-gymmet)
  - Nuvarande status: Stoppade träningen, behöver återuppta efter DG-operation
  - Tre gym-alternativ i Baltimore (ej valt än): Krav Maga Maryland, Merritt Clubs, BJJMMA
- **Commits**: `9aa401c`, `266e610`

### Tidigare arbete
**EON-Inspirerad Kontinuitetsstruktur** - Implementerad december 2025 ✅
- **Setup**: Adapterat EON-projektets mogna kontinuitetssystem för Trip 19
- **Nya filer skapade**:
  - `_index.md` (Entry Point - obligatorisk läsning för agenter)
  - `master/` mapp (Single Source of Truth)
  - `master/timeline.md` (flyttad från rot)
  - `master/character_reference.md` (centraliserad karaktärsreferens)
  - `.claude/agents/trip19-chronicler.md` (kontinuitetsvaktare)
- **Uppdaterade filer**:
  - `CLAUDE.md` (entry point referens, 12 agenter)
  - `.claude/agents/trip19-html-generator.md` (kontinuitetschecklista)
  - `.claude/agents/npc-personality-generator.md` (karaktärsreferens)
  - `.claude/agents/trip19-master.md` (ny agent i listan)
- **Vinster**:
  - Systematisk kontinuitetsvalidering (Scalpel-pronomen, Sullivan-yrkesroll, etc.)
  - "Fråga hellre än gissa"-kultur etablerad
  - Obligatoriska checklistor i agenter
  - Snabb karaktärsreferens (undviker 15,000+ rader läsning)

### Nyligen avslutat
**Jekyll-baserad Kampanjwiki** - Skapad som komplement till befintliga HTML-sidor ✅
- **Setup**: Jekyll + GitHub Pages (samma som EON kampanjwiki)
- **Collections**: NPCs, Platser, Händelser, Mythos, Kapitel
- **Innehåll skapat**:
  - NPCs: Dmitri Volkov, Anton Mahler, Aleksandr Pogodin, Filip Kramer
  - Platser: Lovettsville Crash Site, Berlin Slavic Association
  - Händelser: Flight 19 Crash (1940), Leningrad nyårsnatt 1942
  - Mythos: Black Madonna, Yithian-kraft
  - Kapitel: Kapitel 1 (An Unexpected Meeting), Kapitel 6 (Leningrad - Slutet)
- **Styling**: Mörkt Delta Green-tema (grön/mörkgrå, monospace)
- **Layouts**: Custom HTML-layouts för varje collection-typ
- **Navigation**: Global navigation mellan collections
- **Redo för deployment**: GitHub Pages-kompatibel
- **Plats**: `wiki/` i projektroten
- **README**: Instruktioner för lokal utveckling och deployment

### Nyligen avslutat
- **Custom Claude Code Agents**: 11 specialiserade agents skapade i `.claude/agents/` ✅
  - Innehållsskapande (4): trip19-html-generator, trip19-swedish-translator, historical-handout-designer, npc-personality-generator
  - Kampanjdesign (3): delta-green-campaign-designer, mystery-weaver, horror-pacing-advisor
  - Quality Assurance (3): campaign-state-documenter, translation-auditor, link-validator
  - Master (1): trip19-master (koordinerar andra agents)
  - Totalt ~5,000 rader detaljerad dokumentation och arbetsflöden
- **CLAUDE.md streamlinad**: Reducerad från 140 till 124 rader ✅
  - Borttaget: Tekniska CSS-specs, specifika fillistings, redundans
  - Behållit: Projektkontext, kampanjfilosofi, pointers till viktiga filer
  - Tillagt: Custom Agents-sektion med beskrivningar
  - Fokus: Kontext och filosofi, inte tekniska detaljer
- **Cleanup**: Raderade gamla MD backup-filer ✅
  - Character_MD/ (gamla separata MD-filer)
  - MD_Backup_2025-01-14/ (arkiverad backup)
  - Trench/ gamla MD-filer
  - Complete.md-filer är nu source of truth
- **Karaktärskonsolidering**: Kompletta karaktärsdokument för alla 5 spelarkaraktärer ✅
  - Mac_Complete.md ✅ (1,551 rader, konsoliderat från 8 HTML + 10 MD)
  - Sullivan_Complete.md ✅ (1,568 rader, konsoliderat från 8 HTML + 8 MD)
  - Sparky_Complete.md ✅ (2,041 rader, konsoliderat från 8 HTML + 8 MD)
  - Scalpel_Complete.md ✅ (1,315 rader, konsoliderat från 6 HTML, inga MD)
  - Trench_Complete.md ✅ (1,706 rader, konsoliderat från 8 HTML + 5 MD)
- **Språkgranskning**: Alla 5 complete.md-filer granskade enligt TRANSLATION_RULES.md ✅
  - Färdighetsnamn översatta från engelska till svenska
  - Mac: 40+ översättningar (Support Skills, Career trajectory, Combat Stats, etc.)
  - Sullivan: 7 översättningar (Military Science, Persuade, Alertness, etc.)
  - Sparky: Redan väl översatt, inga ändringar behövdes
  - Scalpel: 19 översättningar (Medicine, Forensics, Science-färdigheter, etc.)
  - Trench: 17 översättningar (Alertness, First Aid, Firearms, etc.)
- Mediciner (Clozapine, Olanzapine) tillagda i Berlin-lägenheten
- Magda Hamburg-lägenhet uppdaterad till 2025-teknologi
- Bilder för Magdas Berlin och Hamburg platser

## Kampanjstruktur
- **Del 1**: Arkivforskning (DC-området)
- **Del 2**: Internationell utredning (Tyskland, Ryssland)
- Koppling mellan Trip 19 Nazi-kristallteknologi och Volkov

## Viktiga platser under utveckling
1. Magdas lägenhet Berlin
2. Magdas lägenhet Hamburg
3. Frankfurt Clinic (Dorfstraße 42c, Frankfurt (Oder)-Güldendorf)

## Teknisk status
- Webbplats: HTML/CSS utan externa beroenden
- Karaktärssidor: Komplett struktur med sidebar-navigation
- SL-material: Följer MALL_GUIDE.md
- **Kontinuitetssystem**: EON-inspirerad struktur med entry point, character reference, chronicler-agent

## Projektstruktur (Efter omorganisation)
```
Trip19/
├── _index.md                    # 🎯 ENTRY POINT (NY)
├── master/                      # 📚 SINGLE SOURCE OF TRUTH (NY)
│   ├── timeline.md              # Kampanjtidslinje (flyttad från rot)
│   └── character_reference.md   # Chesapeake Cell-fakta (NY)
├── .claude/agents/              # 12 agents (trip19-chronicler NY)
├── Complete.md-filer            # Source of truth för karaktärer
└── ...
```

## Nästa steg
- [Definieras av användaren]

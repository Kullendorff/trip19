# CURRENT STATE - Trip 19 / Svarta Madonnan

## Senast uppdaterad
2025-12-18

## Projektöversikt
Delta Green-kampanj på svenska med 5 spelarkaraktärer (Chesapeake Cell):
- **Mac Riley** (FBI) - Jonas
- **Father Sullivan** (Navy Chaplain) - Andreas
- **Kai "Sparky" Zhang** (NSA) - [spelare]
- **Sam "Trench" Novak** (USAR) - [spelare]
- **Hanna "Scalpel" Engler** (Medical Examiner) - Daniel

## Senaste utveckling (från git-log)

### Pågående arbete
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

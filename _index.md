# Trip 19 / Svarta Madonnan - Entry Point

**🎯 ENTRY POINT:** Läs denna fil FÖRST när du börjar arbeta med kampanjen!

**Senast uppdaterad:** 2025-12-18
**Version:** 1.0 (efter EON-inspirerad omstrukturering)

---

## VAR ÄR VI NU?

- **Kampanjfas:** Pre-campaign (karaktärer klara, kampanjmaterial under utveckling)
- **Nästa milstolpe:** Session 1 - "An Unexpected Meeting"
- **Status:** Jekyll wiki skapad, Complete.md-filer för alla 5 agenter, EON-kontinuitetssystem implementerat
- **Senaste uppdatering:** Strukturomorganisation december 2025

---

## FÖR AGENTER - LÄS DETTA FÖRST!

### 📝 Planera scen / SL-material?

```
1. Läs master/character_reference.md (vem är vem? SAN-status?)
2. Läs master/timeline.md (vad har hänt i kampanjhistorien?)
3. Läs relevanta Complete.md för involverade karaktärer
4. Använd delta-green-campaign-designer agent
```

### 👤 Skapa NPC?

```
1. Läs master/character_reference.md (stil-referens för agenter)
2. Använd npc-personality-generator agent
3. Dokumentera i wiki/_npcs/ (Jekyll)
```

### 🌍 Skapa plats?

```
1. Läs TRANSLATION_RULES.md (svenska/engelska-regler)
2. Använd trip19-html-generator agent
3. Dokumentera i wiki/_platser/ (Jekyll)
```

### 📄 Skapa handout (brev, telegram, 1940-tals dokument)?

```
1. Använd historical-handout-designer agent
2. Spara i SL/handouts/ (HTML-format)
```

### 🌐 Översätta / språkgranska?

```
1. Läs TRANSLATION_RULES.md (detaljerade regler)
2. Använd trip19-swedish-translator agent
```

### ✅ Validera kontinuitet?

```
1. Använd trip19-chronicler agent
2. Kör checklistor mot master/character_reference.md
```

### 🔗 Validera länkar / images / navigation?

```
1. Använd link-validator agent
2. Rapportera broken links
```

---

## SINGLE SOURCE OF TRUTH

| Data | Fil | Beskrivning |
|------|-----|-------------|
| **Tidslinje** | `master/timeline.md` | Kronologisk händelsekedja (historisk + kampanj) |
| **Karaktärer** | `master/character_reference.md` | Chesapeake Cell - SAN, stats, breaking points |
| **NPCs** | `wiki/_npcs/*.md` | Jekyll-wiki NPCs |
| **Platser** | `wiki/_platser/*.md` | Jekyll-wiki platser |
| **Mythos** | `wiki/_mythos/*.md` | Jekyll-wiki supernatural entiteter |
| **Händelser** | `wiki/_händelser/*.md` | Jekyll-wiki viktiga händelser |
| **Kapitel** | `wiki/_kapitel/*.md` | Jekyll-wiki kampanjstruktur |

**Vid konflikt:** master/-filerna har alltid rätt. Jekyll-wiki är strukturerad presentation.

---

## MAPPSTRUKTUR

```
Trip19/
├── _index.md                         # 🎯 DU ÄR HÄR - entry point
├── CLAUDE.md                         # AI-instruktioner
├── CURRENT_STATE.md                  # Nuvarande arbetsläge
├── TRANSLATION_RULES.md              # Svenska/engelska-regler
├── MALL_GUIDE.md                     # HTML/CSS-standarder
│
├── master/                           # 📚 SINGLE SOURCE OF TRUTH
│   ├── timeline.md                   # Kampanjtidslinje
│   └── character_reference.md        # Chesapeake Cell-fakta
│
├── .claude/                          # 🤖 AI-infrastruktur
│   └── agents/                       # 12 specialiserade agenter
│       ├── trip19-html-generator.md
│       ├── trip19-swedish-translator.md
│       ├── historical-handout-designer.md
│       ├── npc-personality-generator.md
│       ├── delta-green-campaign-designer.md
│       ├── mystery-weaver.md
│       ├── horror-pacing-advisor.md
│       ├── campaign-state-documenter.md
│       ├── translation-auditor.md
│       ├── link-validator.md
│       ├── trip19-master.md
│       └── trip19-chronicler.md      # NY - Kontinuitetsvaktare
│
├── Mac/                              # Karaktärsmapp - Mac Riley
│   ├── Mac_Complete.md               # Source of truth (1,551 rader)
│   ├── index.html                    # Landing page
│   └── *.html                        # Karaktärssidor
│
├── Sullivan/                         # Karaktärsmapp - Father Sullivan
│   ├── Sullivan_Complete.md          # Source of truth (1,568 rader)
│   └── ... (samma struktur)
│
├── Sparky/                           # Karaktärsmapp - Kai "Sparky" Zhang
│   ├── Sparky_Complete.md            # Source of truth (2,041 rader)
│   └── ...
│
├── Scalpel/                          # Karaktärsmapp - Dr. Hanna Engler
│   ├── Scalpel_Complete.md           # Source of truth (1,315 rader)
│   └── ...
│
├── Trench/                           # Karaktärsmapp - Sam Novak
│   ├── Trench_Complete.md            # Source of truth (1,706 rader)
│   └── ...
│
├── SL/                               # 🎲 SPELLEDARMATERIAL
│   ├── timeline.html                 # Tidslinje-visualisering
│   ├── kapitel/                      # Kapitel-övervåg
│   ├── scener/                       # Individuella scener
│   ├── handouts/                     # 1940-tals dokument
│   └── npcs/                         # NPC-referens (HTML)
│
└── wiki/                             # 📖 JEKYLL-WIKI
    ├── _npcs/                        # NPCs (markdown)
    ├── _platser/                     # Platser
    ├── _händelser/                   # Viktiga händelser
    ├── _mythos/                      # Supernatural entiteter
    ├── _kapitel/                     # Kampanjstruktur
    └── assets/images/                # Centraliserade bilder
```

---

## VANLIGA ARBETSFLÖDEN

### Ny scen-planering

```
1. Bestäm vilka agenter involverade
2. Läs master/character_reference.md (SAN-status, breaking points)
3. Använd delta-green-campaign-designer för structure
4. Använd mystery-weaver för clue chains
5. Använd trip19-html-generator för HTML-sida
6. Uppdatera CURRENT_STATE.md
```

### Uppdatera efter speltest / feedback

```
1. Uppdatera Complete.md för berörda karaktärer
2. Uppdatera master/character_reference.md (SAN, bonds)
3. Uppdatera master/timeline.md (nya händelser)
4. Dokumentera i CURRENT_STATE.md
```

### Skriva nytt kapitel-material

```
1. Läs master/timeline.md för historisk kontext
2. Använd trip19-html-generator
3. Använd trip19-swedish-translator för språkgranskning
4. Spara i SL/kapitel/
```

### Generera handouts (brev, telegram, newspaper)

```
1. Bestäm period (1940? 1942? 2025?)
2. Använd historical-handout-designer agent
3. Inkludera subtle supernatural hints
4. Spara i SL/handouts/
```

---

## CHECKLISTA FÖR AGENTER

**INNAN du gör NÅGOT:**

- [ ] Har du läst `_index.md`? (denna fil)
- [ ] Vet du vilken typ av uppgift det är? (scen/kapitel/NPC/handout)
- [ ] Har du läst `master/character_reference.md`?
- [ ] Vet du var du ska hitta data? (se SINGLE SOURCE OF TRUTH)
- [ ] Har du läst `TRANSLATION_RULES.md` om språk är relevant?

**EFTER du gjort något:**

- [ ] Har du uppdaterat ALLA relaterade filer?
- [ ] Har du validerat kontinuitet? (trip19-chronicler)
- [ ] Har du granskat språk? (trip19-swedish-translator)
- [ ] Har du uppdaterat `CURRENT_STATE.md`?
- [ ] Har du kört checklistor från `master/character_reference.md`?

---

## KONTINUITETSREGLER (FRÅN EON)

**FRÅGA HELLRE 1000 GÅNGER ÄN GISSA FEL!**

### Vad du MÅSTE fråga om:

- Vilket pronomen för nya NPCs?
- Är detta före eller efter Mac's administrative leave (augusti 2025)?
- Vilket callsign används i denna kontext?
- Vilken SAN-nivå har karaktären vid denna tidpunkt?
- Är denna händelse före eller efter Sea Glass (maj 2025)?

### Vad du ALDRIG får gissa:

- Pronomen för Scalpel (ALLTID hon!)
- SAN-värden (läs Complete.md)
- Breaking Point triggers
- Vilken agent som är cell leader (Sullivan efter augusti 2025)
- Historiska fakta (ALLTID verifiera mot timeline.md)

---

## SUPPORT

**Om du är osäker:**

- Läs CLAUDE.md för detaljerade instruktioner
- Läs `.claude/agents/` för agent-specifika instruktioner
- Läs `master/character_reference.md` för karaktärsfakta
- **FRÅGA ALLTID hellre än att gissa fel!**

**Quality Assurance:**

- Använd trip19-chronicler för kontinuitetsvalidering
- Använd translation-auditor för språkgranskning
- Använd link-validator för länk-/bildvalidering

---

## KAMPANJFILOSOFI (PÅMINNELSE)

**Från CLAUDE.md:**

- **Research-driven slow-burn mystery** utan "world-ending urgency"
- **Autenticitet framför dramatik** - realistiska gränser
- **Character trauma som motor** - SAN loss och Breaking Points centralt
- **Spelarna kan Google allt** - det mesta STÄMMER (historiskt)
- **Supernatural fyller gap i historien**, ersätter inte den

---

**Senast uppdaterad:** 2025-12-18 (efter EON-inspirerad omstrukturering)
**Version:** 1.0

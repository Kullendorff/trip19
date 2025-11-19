# Black Madonna Quality Assurance Agents

Detta dokument innehåller färdiga agent-prompts för kvalitetskontroll av Trip 19 / Black Madonna-kampanjen. Kopiera och klistra in önskade agent-prompts i en ny chat för att köra kontrollerna.

## Instruktioner

1. Öppna en ny chat med Claude Code
2. Kopiera hela agent-prompten nedan (från "Run Task agent..." till slutet av prompten)
3. Klistra in i chatten
4. Agenten kör och rapporterar tillbaka resultat

## Agent 1: Svengelska-rensning

**Syfte:** Identifierar och rapporterar blandat svenskt/engelskt språk i alla HTML-filer.

**Undantag:** Tekniska speltermer (stats, skills, Breaking Point, SAN check, Bond, Hit Points, Willpower Points, etc.) får vara på engelska.

**Prompt:**

```
Run Task agent with subagent_type="general-purpose" to scan all HTML files in /home/user/trip19/ and subdirectories for svengelska (mixed Swedish/English language).

IMPORTANT EXCEPTION: Technical game terms may remain in English, including:
- Stats: STR, CON, DEX, INT, POW, CHA
- Skills: Alertness, Firearms, HUMINT, etc.
- Game mechanics: Breaking Point, SAN check, Bond, Hit Points, Willpower Points, Lethality

The agent should:
1. Read all .html files in /home/user/trip19/ and subdirectories (characters, SL, etc.)
2. Identify Swedish text that contains English words/phrases (excluding technical terms above)
3. Categorize by severity:
   - CRITICAL: Player-facing narrative text mixing languages
   - HIGH: Section headers, labels, navigation mixing languages
   - MEDIUM: Technical descriptions that could be translated
   - LOW: Minor instances

Common svengelska patterns to find:
- "Sessions" in Swedish text → should be "Spelomgångar"
- "handouts" → should be "dokument" or "handlingar"
- "Investigation roll" → should be "Utredningsslag"
- "Clue" → should be "Ledtråd"
- "Scene" → should be "Scen"
- "NPC" → could be "SLP" (spelledarperson) but NPC is acceptable
- "Background" → should be "Bakgrund"
- "Timeline" → should be "Tidslinje"
- English verbs in Swedish sentences
- English adjectives in Swedish text

Provide:
1. Count by severity
2. Top 10 most frequent svengelska terms
3. Specific file locations with line context
4. Recommended Swedish replacements
```

---

## Agent 2: Mythos-consistency

**Syfte:** Jämför Black Madonna-kapitel mot Trip_19_Black_Madonna_Mythos_och_Spelarinformation.md och Black_Madonna_2025_Adaption_Guide.md för att hitta diskrepanser.

**Prompt:**

```
Run Task agent with subagent_type="general-purpose" to verify mythos consistency across Black Madonna chapters.

The agent should:
1. Read /home/user/trip19/Trip_19_Black_Madonna_Mythos_och_Spelarinformation.md (source of truth for Delta Green Mythos)
2. Read /home/user/trip19/Black_Madonna_2025_Adaption_Guide.md (adaptation principles)
3. Read all Black Madonna chapter files:
   - /home/user/trip19/SL/black_madonna_chapter1.html
   - /home/user/trip19/SL/black_madonna_chapter2.html
   - /home/user/trip19/SL/black_madonna_chapter3.html

Check for discrepancies:

**KULT terms that should NOT appear:**
- "Chagidiel" (Death Angel) → should use "Det Som Fängslades" or describe Yithian/Nyogtha forces
- "nepharite/nephariter" → should be "transformerade" or "korrupterade"
- "Archons" → should be "krafterna" or avoided entirely
- "Inferno" as realm → should be "den andra dimensionen" or "transformed space"
- "Lictors/Razides" → should be "transformerade agenter" or "enforcers"
- "Elysium" → avoid or use Delta Green equivalent

**Delta Green Mythos elements that SHOULD appear:**
- Yithian Echo (247 Hz signal, crystal resonators, mind-transfer)
- Nyogtha (Lesser Great Old One, physical transformation, bound under Leningrad)
- Dual manifestation (both forces attacking simultaneously)
- Nazi Type-VIII apparatus (German experimental technology)
- Soviet Project Echo (counter-frequency)
- December 31, 1941 collision event

**Consistency checks:**
- Timeline consistency (1941 Leningrad → 2025 present)
- NPC adaptations correct (Magda born 1939, dies 2024 at 85)
- Location adaptations (Hamburg 1991 → Lovettsville/DC 2025, Berlin 1991 → Berlin 2025)
- Mechanics (KULT rolls → Delta Green SAN checks, Breaking Points)

Provide:
1. List of KULT terms still used with locations
2. Missing Delta Green Mythos references
3. Timeline inconsistencies
4. Recommended search-replace table for bulk fixes
```

---

## Agent 3: NPC-consistency

**Syfte:** Kontrollerar att alla NPCs som nämns i kapitlen finns dokumenterade i npcs.html och att informationen är konsistent.

**Prompt:**

```
Run Task agent with subagent_type="general-purpose" to verify NPC consistency across Black Madonna campaign.

The agent should:
1. Read /home/user/trip19/SL/npcs.html (master NPC list)
2. Read all Black Madonna chapter files:
   - /home/user/trip19/SL/black_madonna_chapter1.html
   - /home/user/trip19/SL/black_madonna_chapter2.html
   - /home/user/trip19/SL/black_madonna_chapter3.html
3. Read /home/user/trip19/SL/KULT_Black_Madonna.txt for source material

Check for:

**Missing NPCs:**
- NPCs mentioned in chapters but not in npcs.html
- NPCs with significant roles that lack entries

**Inconsistencies:**
- Name spelling variations
- Age/birth year conflicts
- Relationship contradictions
- Role/occupation mismatches
- Address or location conflicts

**Key NPCs to verify:**
- Magda Golebowska (born 1939, dies 2024 at 85)
- Nikolay Kalenko (orphanage owner, died Dec 31, 1941)
- Father Ivan Chezenko (priest at Kaptyeno cathedral)
- Dimi Nesterov (icon painter, Magda's cousin)
- Filip Kramer (author, "The Power of Dreams")
- Arnold Weiss (Slavic Association)
- The three Russians (Pogodin, Volovich, Tischenko)
- Yelena, Alyona, Katya Kalenko (family members)

Provide:
1. List of missing NPCs with chapter references
2. Inconsistencies found with details
3. Recommended additions to npcs.html
4. Suggested corrections
```

---

## Agent 4: Timeline-validator

**Syfte:** Validerar att alla tidslinje-referenser är konsekventa över hela kampanjen.

**Prompt:**

```
Run Task agent with subagent_type="general-purpose" to validate timeline consistency across Black Madonna campaign.

The agent should:
1. Read timeline documents:
   - /home/user/trip19/complete_timeline.md
   - /home/user/trip19/SL/locations.html (has timeline info)
2. Read all Black Madonna chapters:
   - /home/user/trip19/SL/black_madonna_chapter1.html
   - /home/user/trip19/SL/black_madonna_chapter2.html
   - /home/user/trip19/SL/black_madonna_chapter3.html
3. Extract all dates and temporal references

**Key timeline anchors:**
- December 31, 1941: Leningrad collision event at Kalenko's house
- 1942-1945: Camp S-17 refugee camp (AFTER Leningrad event)
- 1951-1958: Frankfurt Clinic (patient treatment)
- 1972-1989: Slavic Forum gap period
- November 8-9, 2025: Magda's death and player investigation begins
- Magda: Born 1939, dies 2024 at age 85

Check for:
- Date conflicts between documents
- Impossible age calculations
- Event sequence violations
- Missing dates for major events
- Inconsistent references to same event

Provide:
1. List of all timeline conflicts found
2. Severity rating (CRITICAL/HIGH/MEDIUM/LOW)
3. Recommended corrections
4. Visual timeline summary of key events
```

---

## Agent 5: Ledtråd-tracker

**Syfte:** Spårar alla ledtrådar genom kampanjen och verifierar att de har:
1. Tydlig introduktion (var hittar spelarna den?)
2. Koppling till andra ledtrådar eller scener
3. Upplösning eller fortsättning

**Prompt:**

```
Run Task agent with subagent_type="general-purpose" to track all clues (ledtrådar) through the Black Madonna campaign.

The agent should:
1. Read all Black Madonna chapters
2. Identify every physical clue, document, NPC contact, or information source
3. Track each clue through the campaign

For each ledtråd, verify:
- **Introduktion:** Where/when players find it
- **Koppling:** What it connects to (other clues, locations, NPCs)
- **Upplösning:** Where it leads or how it resolves

**Critical ledtrådar to track:**

*Physical objects:*
- "The Power of Dreams" by Filip Kramer
- Black Madonna icon/doll (Svarta Madonnan)
- Berlin keys (Leibnizstraße 97)
- Medical records (Frankfurt Clinic)
- Slavic Association archive documents
- Ritual page (dog-eared in Magda's book)

*Information sources:*
- Answering machine messages (Filip's panicked calls)
- Slavic Forum records (1972-1989 gap)
- CAB investigation files (original Trip 19 crash)
- Soviet Project Echo documentation
- Nazi Type-VIII apparatus records

*NPCs as information sources:*
- Arnold Weiss (Slavic Association)
- The three Russians (Pogodin, Volovich, Tischenko)
- Frankfurt Clinic survivors
- Dimi Nesterov (if found alive/through records)

Check for:
- **Dead ends:** Clues that lead nowhere
- **Missing links:** References without introduction
- **Broken chains:** A→B referenced but B→C missing
- **Orphan clues:** Mentioned but never found by players

Provide:
1. Complete clue map with connections
2. List of dead ends or gaps
3. List of orphan clues
4. Recommended additions or fixes
```

---

## Usage Tips

- **Kör agenter parallellt:** Om du behöver köra flera agenter, klistra in alla prompts i samma meddelande (separerade). Claude kan köra flera Task-agenter samtidigt.
- **Spara rapporter:** Agenterna genererar detaljerade rapporter. Spara dessa för att spåra förbättringar över tid.
- **Uppdatera prompts:** Om kampanjen utvecklas, uppdatera detta dokument med nya checks eller undantag.

---

**Senast uppdaterad:** 2025-11-19
**Version:** 1.0

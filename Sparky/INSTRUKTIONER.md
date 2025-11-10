# INSTRUKTIONER FÖR CLAUDE CODE - SPARKY CHARACTER SHEET

## 🎯 UPPDRAG

Du ska bygga en komplett, navigerbar HTML character sheet för "Sparky" (Kai Zhang), en NSA-analyst och Delta Green-agent. Detta är för faktisk användning vid spelbord (rollspel).

**Input:** Befintlig tech guide HTML + flera markdown-filer med karaktärsdata  
**Output:** En självständig HTML-fil (`sparky_character_sheet.html`) med alla sektioner

---

## 📂 KÄLLFILER & VAD DE INNEHÅLLER

### Huvudkällor:

1. **`sparky_technical_guide_komplett.html`**
   - Befintlig tech guide (fungerar redan)
   - **Återanvänd:** Alla bilder, CSS-struktur, sidebar-navigation, collapse-funktioner
   - **Rensa:** Rollspelstips, vapen (ska flyttas), bonds (ska flyttas)
   - **Flytta:** Cheat sheet från botten till ÖVERSIKT

2. **`sparky_m.txt`**
   - **Innehåller:** Kompletta stats (STR, CON, DEX, INT, POW, CHA)
   - **Innehåller:** HP, WP, SAN (current/max + breaking points)
   - **Innehåller:** Alla färdigheter med exakta % (90+ skills listad)
   - **Innehåller:** Bonds med värden (Susan Zhang (8), Mr. Walsh (8), Null Space Collective (8))
   - **Innehåller:** Grundläggande utrustning

3. **`Sparky_Tidslinje.md`**
   - **Innehåller:** Komplett livshistoria från födelse till nu
   - **Innehåller:** Viktiga händelser årligen 1997-2025
   - **Innehåller:** Hacktivist-period, FBI-jakt, NSA-deal, Delta Green-rekrytering

4. **`Sparky_Delta_Green_Sektion.md`**
   - **Innehåller:** Delta Green-rekrytering (2022)
   - **Innehåller:** Cell structure och handler-kontakt
   - **Innehåller:** Operations före Sea Glass
   - **Innehåller:** SAN loss per operation

5. **`Sparky_Alias_System.md`**
   - **Innehåller:** Sarah Mitchell (safehouse College Park)
   - **Innehåller:** Maya Nakamura (safety deposit box Baltimore)
   - **Innehåller:** Jennifer Park (emergency backup NSA)
   - **Innehåller:** Nycklar, kostnader, burn protocols

6. **`Sparky_Boende_Detaljerat.md`**
   - **Innehåller:** C Street Flats, Apartment 3G
   - **Innehåller:** Layout, atmosfär, go-bag innehåll
   - **Innehåller:** Besökare (Mr. Walsh), dagliga rutiner
   - **Innehåller:** Säkerhet & escape routes

---

## 🏗️ SEKTION FÖR SEKTION - VAD SKA BYGGAS

### SEKTION 1: ÖVERSIKT

**Syfte:** Snabbåtkomst vid spelbord - allt viktigt på ett ställe

**Innehåll:**
1. **Agent Profile**
   - Namn: Kai "Sparky" Zhang
   - Ålder: 28 år (född 1997-03-15)
   - Yrke: Senior Analyst, NSA Cyber Defense
   - Delta Green: Tech Specialist
   - Clearance: Top Secret/SCI

2. **Core Stats** (från `sparky_m.txt`)
   ```
   STR 8  | CON 10 | DEX 12
   INT 18 | POW 14 | CHA 8
   ```

3. **Status Bars** (från `sparky_m.txt`)
   ```
   HP:  10/10  [██████████]
   WP:  14/14  [██████████████]
   SAN: 63/77  [████████░░] (Breaking Point: 48)
   ```

4. **CHEAT SHEET** (flytta hit från botten av tech guide!)
   - De 5 viktigaste färdigheterna
   - Vanligaste hacks (quick reference)
   - NSA access levels
   - "Detta kan hon hacka / Detta kan hon INTE hacka"

5. **Bonds Quick View**
   - Susan Zhang (mor): 8
   - Mr. Walsh (granne): 8
   - Null Space Collective: 8

**Källa:** `sparky_m.txt` + cheat sheet från `sparky_technical_guide_komplett.html`

---

### SEKTION 2: ATTRIBUT & STATS

**Syfte:** Fullständiga stats för regelreferens

**Innehåll:**

1. **Grundegenskaper** (från `sparky_m.txt`)
   - STR 8 (40%)
   - CON 10 (50%)
   - DEX 12 (60%)
   - INT 18 (90%)
   - POW 14 (70%)
   - CHA 8 (40%)

2. **Härledda värden**
   - HP: 10 (CON + STR / 2)
   - WP: 14 (POW)
   - SAN: 63/77 (POW × 5, current 63)
   - Breaking Point: 48 (SAN - POW)

3. **Damage Bonus:** +0 (STR + CON under 13)

4. **Tidigare SAN:** 77 (starting)
   - Total förlust: -14 (från operationer)
   - Återhämtat: +2 (via Bonds)
   - Netto: -12

**Källa:** `sparky_m.txt`

---

### SEKTION 3: FÄRDIGHETER

**Syfte:** Komplett lista för regelslag

**Innehåll:** ALL skills från `sparky_m.txt` organiserade i kategorier

**Kategorier:**

1. **Professionella färdigheter**
   - Datavetenskap: 90%
   - SIGINT: 80%
   - Elektronik: 60%
   - Ryska: 60%
   - Kinesiska: 40%
   - Biblioteksforskning: 60%
   - Bureaucracy: 50%
   - Search: 40%
   - Law: 30%

2. **Bonusfärdigheter**
   - Uppmärksamhet: 40%
   - Smyga: 30%
   - Skjutvapen: 40%

3. **Övriga färdigheter** (base skills från Delta Green)
   - Lista alla med base values
   - Format: Tabellformat för läsbarhet

**Presentation:**
```html
<table>
  <thead>
    <tr>
      <th>Färdighet</th>
      <th>%</th>
      <th>Typ</th>
    </tr>
  </thead>
  <tbody>
    <!-- Alla skills -->
  </tbody>
</table>
```

**Källa:** `sparky_m.txt`

---

### SEKTION 4: TEKNISKA OPERATIONER

**Syfte:** Renodlad tech guide - inga rollspelstips, bara mekanik

**Innehåll från `sparky_technical_guide_komplett.html`:**

1. **Datavetenskap (90%)**
   - Vad hon kan hacka
   - Svårighetsgrader
   - Tidsåtgång
   - Begränsningar

2. **SIGINT (80%)**
   - Signalspaning
   - Avlyssning
   - Dekryptering

3. **NSA Access**
   - XKEYSCORE
   - PRISM
   - UPSTREAM
   - TAO capabilities

4. **Elektronik (60%)**
   - Hårdvaruhacking
   - Flipper Zero användning

5. **Forensics (60%)**
   - Digital forensics
   - Spårning

**RENSA BORT:**
- ❌ Alla "Hur SL kan använda"-sektioner
- ❌ Rollspelstips och scenarioförslag
- ❌ Vapeninformation (flyttas till UTRUSTNING)
- ❌ Bonds-info (flyttas till BONDS)

**BEHÅLL:**
- ✅ Collapse-boxar för detaljer
- ✅ Tabeller för strukturerad data
- ✅ Badges (LÄTT/MEDIUM/SVÅRT)
- ✅ Alla bilder och ikoner

**Källa:** `sparky_technical_guide_komplett.html` (rensat)

---

### SEKTION 5: BONDS

**Syfte:** Relationer & emotional anchors

**Innehåll:**

**Format per bond:**
```markdown
### [Namn] - Värde: [X/8]

**Relation:** [Beskriv]
**Betydelse:** [Varför viktigt]
**Risk:** [Vad händer om skadat]
```

**Bonds:**

1. **Susan Zhang (mor) - 8**
   - Grundskolelärare, Denver, CO
   - Änka sedan 2007 (bilolycka)
   - Helt ovetande om Kais verkliga liv
   - Sparkys sista koppling till normalitet
   - Källa: `sparky_m.txt` + utökad info från diskussioner

2. **Mr. Robert Walsh (granne) - 8**
   - 78 år, pensionerad lärare
   - Bor i samma building (C Street Flats)
   - Söndagskaffe-tradition
   - Behandlar Sparky som barnbarn
   - Helt ovetande om hennes liv
   - Källa: `Sparky_Boende_Detaljerat.md`

3. **The Null Space Collective - 8**
   - Online hacker-community
   - Hennes alias: "NullByte"
   - Nära vänner: Cipher, RedShift, Proxy
   - Känner inte hennes riktiga namn
   - Representerar hennes hacktivist-förflutna
   - Källa: `sparky_m.txt` + diskussioner

**Källa:** `sparky_m.txt`, `Sparky_Boende_Detaljerat.md`

---

### SEKTION 6: BAKGRUND

**Syfte:** Karaktärens historia & motivation

**Innehåll från `Sparky_Tidslinje.md` + `Sparky_Delta_Green_Sektion.md`:**

**Organisera kronologiskt:**

1. **Tidiga år (1997-2012)**
   - Född San Francisco 1997-03-15
   - Första datorn (2004, ålder 7)
   - Pappas död (2012, bilolycka)
   - Flyttar till Denver med Susan

2. **Hacktivist-period (2013-2019)**
   - Aaron Swartz påverkar (2013)
   - MIT, Computer Science (2015-2018)
   - "Sparkplug" alias skapas
   - Marcus "Ghost" Reeves (mentor)
   - Null Space Collective (2017)
   - FBI-jakt börjar (2018)

3. **NSA-tiden (2019-2022)**
   - FBI Deal - NSA eller fängelse
   - Sparkplug "dör"
   - Hatar kontoret, bygger färdigheter
   - Hackar LEOSA för concealed carry

4. **Delta Green-rekrytering (2022)**
   - Upptäcker "The Sleeper"-meddelanden
   - NSA avfärdar som "konspirationsteori"
   - Kontaktas av Delta Green
   - Första operationen: Coldwater

5. **Operationer (2022-2024)**
   - Operation Nightjar (första dödandet)
   - The Mall Before Christmas (Volkov flyr)
   - Total SAN loss: -14, återhämtat +2

6. **Nuvarande status (2025)**
   - Missade Sea Glass (utlånad till Mossad)
   - Mac på "semester" (breakdown)
   - Sullivan de facto cell leader
   - Besatt av att hitta Volkov

**Format:** Collapsible timeline med årtal

**Källa:** `Sparky_Tidslinje.md`, `Sparky_Delta_Green_Sektion.md`

---

### SEKTION 7: DELTA GREEN

**Syfte:** Operational knowledge - vad Sparky vet om organisationen

**Innehåll från `Sparky_Delta_Green_Sektion.md`:**

1. **Organisation**
   - Vad Delta Green ÄR
   - Off-the-books, illegal sedan 1970
   - "Need to know"-struktur
   - Hennes clearance-nivå

2. **Cell Structure**
   - Hennes cell: 3 personer
   - Mac (FBI, cell leader)
   - Sullivan (MARSOC, operator)
   - Sparky (NSA, tech specialist)

3. **Handler-kontakt**
   - Codename: [klassificerat]
   - Krypterad kommunikation
   - Drop-punkter
   - Emergency protocols

4. **Operations-historik**
   - Operation Coldwater (2022) - First op, support role
   - Operation Nightjar (2023) - First kills (3 personer)
   - The Mall Before Christmas (2024) - Volkov flyr
   - [Andra operationer, mindre]
   - Sea Glass (2025, VÅR) - Hon var INTE där (Mossad-utlåning)

5. **Vad hon INTE vet**
   - Andra celler (compartmentalized)
   - Delta Green's full historia
   - Hur många agenter totalt
   - Om "friendly" organisationen fortfarande finns

6. **SAN Mechanics (spelmekanik)**
   - Starting SAN: 77 (POW × 5)
   - Current SAN: 63
   - Total förlust: -14
   - Återhämtat: +2 (via Bonds)
   - Breaking Point: 48 (SAN - POW)

7. **Cover-up protocols**
   - "Inget onaturligt finns"
   - Eldvapen löser ingenting mot det verkligt farliga
   - Vittnen måste hanteras
   - Ingen dokumentation (utom encrypted notes)

8. **Vad hon lärt sig**
   - Det onaturliga finns
   - Det kan inte förstås - bara bekämpas
   - Varje operation kostar SAN
   - Bonds är hennes sista förankring
   - Adaptation till våld är både nödvändigt och skrämmande

**Format:** Collapse-boxar för varje underkategori

**Källa:** `Sparky_Delta_Green_Sektion.md`

---

### SEKTION 8: UTRUSTNING

**Syfte:** Allt hon bär & äger

**Innehåll:**

1. **Standardutrustning (daglig)**
   - Custom laptop (Linux, encrypted)
   - Krypterad mobiltelefon
   - Flipper Zero
   - Leatherman Wave+
   - Ryggsäck (sliten, anonym)

2. **Digitala verktyg**
   - USB Rubber Ducky
   - Raspberry Pi Zero W
   - Lockpicks (hobby, inte expert)
   - Faraday bags
   - Diverse kablar & adapters

3. **Vapen** (flytta hit från tech guide!)
   - **Glock 43X** (9mm, subcompact)
   - NSA-utfärdad, bär sällan utanför ops
   - Custom mods (från tech guide)

4. **Go-bag** (från `Sparky_Boende_Detaljerat.md`)
   - $5,000 cash
   - 3 burner phones
   - Kläder (3 sets)
   - First aid kit (advanced)
   - Laptop (airgapped)
   - Hard drives (backups)
   - Glock 43X + 100 rounds
   - Fake beard & glasögon

**Källa:** `sparky_m.txt`, `sparky_technical_guide_komplett.html` (vapen), `Sparky_Boende_Detaljerat.md` (go-bag)

---

### SEKTION 9: ALIAS & SAFEHOUSES

**Syfte:** Hennes falska identiteter & escape-plan

**Innehåll från `Sparky_Alias_System.md`:**

**Format per alias:**
```markdown
### [ALIAS NAMN]

**Grundinfo:**
- Namn: [Full name]
- Född: [Date]
- SSN: [Number]
- Yrke: [Cover]

**Dokumentation:**
- Driver's License: [State]
- Kreditkort: [Which]
- Pass: [If applicable]

**Plats:**
- [Var finns IDs/nyckel]

**Användning:**
- [Vad används för]
- [Använd X gånger]
```

**Alias:**

1. **Sarah Mitchell**
   - Safehouse: College Park (7413 Baltimore Ave, Apt 2F)
   - Domestic ops, safehouse access
   - Innehåll i safehouse listat
   - Nycklar: 3 kopior på olika platser

2. **Maya Nakamura**
   - Safety deposit box: Baltimore (PNC Bank #437)
   - International ops, journalist cover
   - Instagram: @maya_shoots_film
   - Pass, press credentials

3. **Jennifer Park**
   - Emergency backup
   - Gömd på NSA Fort Meade
   - Minimalt utvecklad
   - Användning: 0 gånger

**System overview:**
- Compartmentalization
- Geographic separation
- Use case separation
- Kostnader: $18,420/år

**Källa:** `Sparky_Alias_System.md` (KOMPLETT)

---

### SEKTION 10: BOENDE

**Syfte:** Hennes hem & vardagsliv

**Innehåll från `Sparky_Boende_Detaljerat.md`:**

1. **Adress**
   - C Street Flats, Apartment 3G
   - 24 C Street, Laurel, MD 20707
   - 580 sq ft, 1 bedroom
   - Hyra: $1,580/månad

2. **Layout**
   - Entré
   - Kök/Vardagsrum (open-plan)
   - Sovrum (skrivbord med 3 monitorer)
   - Badrum
   - Balkong (emergency exit route)

3. **Atmosfär**
   - Steril, temporär, funktionell
   - Server rack snurrar 24/7
   - Ingen dekor (1 foto av Susan)
   - Som hotellrum där någon bor för länge

4. **Vad finns / Inte finns**
   - Finns: Tech gear överallt, go-bag
   - Finns INTE: Dekorationer, växter, gästmöbler

5. **Besökare**
   - Mr. Walsh (2 gånger)
   - Landlord/Maintenance (3 gånger)
   - Ingen annan

6. **Dagliga rutiner**
   - Morning: 06:00 alarm → NSA
   - Evening: 18:00 hem → 02:00 "övertid"
   - Söndagar: Kaffe med Mr. Walsh

7. **Säkerhet**
   - Digital: VPN, encryption, MAC rotation
   - Fysisk: Extra lås, escape routes
   - Bug-out plan: Under 5 minuter

**Källa:** `Sparky_Boende_Detaljerat.md` (KOMPLETT)

---

## 🎨 DESIGN & STYLING

### Återanvänd från `sparky_technical_guide_komplett.html`:

**CSS-klasser:**
```css
.sidebar              /* Navigation menu */
.main-content         /* Content area */
.collapse-box         /* Expandable sections */
.collapse-header      /* Click to expand */
.collapse-content     /* Hidden content */
.badge                /* Difficulty badges */
  .badge-easy         /* Green */
  .badge-medium       /* Yellow */
  .badge-hard         /* Red */
.alert                /* Important notices */
  .alert-success      /* Green background */
  .alert-warning      /* Yellow background */
  .alert-danger       /* Red background */
table                 /* Data tables */
```

**JavaScript-funktioner:**
```javascript
function toggleCollapse(element)  // Expand/collapse
function scrollToSection(id)      // Navigation
```

**Färger:**
```css
--primary-bg: #0a0a0a;      /* Nästan svart */
--primary-text: #00ff00;     /* Grön */
--accent: #00aa00;           /* Mörkare grön */
--border: #003300;           /* Mycket mörk grön */
```

**Typografi:**
```css
font-family: 'Courier New', Consolas, monospace;
```

### Bilder:

**VIKTIGT:** Kopiera EXAKTA `<img>`-taggar från nuvarande HTML.

**Exempel:**
```html
<img src="path/to/image.png" alt="Description" class="existing-class">
```

Ändra INTE:
- Sökvägar (paths)
- CSS-klasser
- Alt-text
- Sizing

---

## ✅ STEG-FÖR-STEG PROCESS

### Steg 1: Förberedelse
```bash
1. Läs CLAUDE.md
2. Läs denna fil (INSTRUKTIONER.md)
3. Öppna sparky_technical_guide_komplett.html
4. Studera struktur, CSS, JavaScript
5. Identifiera alla bilder (för återanvändning)
```

### Steg 2: Bygga grunden
```bash
1. Skapa ny fil: sparky_character_sheet.html
2. Kopiera HTML-struktur från tech guide
3. Kopiera ALL CSS
4. Kopiera ALL JavaScript
5. Säkerställ att navigation fungerar
```

### Steg 3: Sektion för sektion
```bash
För varje sektion (ÖVERSIKT → BOENDE):
  1. Läs källfil(er) för den sektionen
  2. Organisera innehållet logiskt
  3. Skriv HTML med rätt styling
  4. Lägg till collapse-boxar där lämpligt
  5. Testa att navigation scrollar dit
```

### Steg 4: Rensning av tech guide
```bash
1. Kopiera TEKNISKA OPERATIONER från tech guide
2. TA BORT:
   - Rollspelstips
   - "Hur SL kan använda"
   - Vapeninformation (flytta till UTRUSTNING)
   - Bonds-info (redan i BONDS)
3. BEHÅLL:
   - Teknisk mekanik
   - Svårighetsgrader
   - Tabeller & collapse-boxar
```

### Steg 5: Flytta cheat sheet
```bash
1. Hitta cheat sheet längst ner i tech guide
2. Extrahera komplett sektion
3. Placera i ÖVERSIKT
4. Se till att den är lätt att hitta
5. Behåll styling & funktionalitet
```

### Steg 6: Kvalitetskontroll
```bash
1. Öppna HTML i webbläsare
2. Klicka alla sidebar-länkar
3. Expandera alla collapse-boxar
4. Verifiera att alla bilder visas
5. Testa på mobil (resize browser)
6. Kontrollera svensk stavning
7. Säkerställ ingen engelsk text
```

### Steg 7: Final polish
```bash
1. Validera HTML (W3C validator om möjligt)
2. Kontrollera konsistens i styling
3. Se till att ingen info saknas
4. Dubbelkolla att tech guide är rensat
5. Verifiera att cheat sheet är i ÖVERSIKT
```

---

## 🚨 VANLIGA MISSTAG ATT UNDVIKA

❌ **Glömma flytta cheat sheet till ÖVERSIKT**
   → Den MÅSTE vara lätt åtkomlig!

❌ **Lämna kvar rollspelstips i tech guide**
   → Rensa ALLT som är "för SL"

❌ **Bryta bildreferenser**
   → Kopiera EXAKTA img-taggar

❌ **Blanda engelska & svenska**
   → ALLT ska vara på svenska

❌ **Glömma vapen från tech guide**
   → Flytta Glock-info till UTRUSTNING

❌ **Låta navigation sluta fungera**
   → Testa ALLA länkar

❌ **Göra den otrevlig på mobil**
   → Sidebar ska kollapsa

❌ **Missa alias-info**
   → Hela Alias_System.md ska inkluderas

---

## 📱 MOBIL-ANPASSNING

**Breakpoints:**
```css
@media (max-width: 768px) {
  .sidebar {
    /* Göm som hamburger-meny */
  }
  .main-content {
    /* Full bredd */
  }
}
```

**Testa:**
- iPhone (375px)
- iPad (768px)
- Desktop (1920px)

---

## 🎯 FÄRDIG NÄR...

✅ Alla 9 sektioner är kompletta  
✅ Cheat sheet är i ÖVERSIKT (inte längst ner)  
✅ Tech guide är renad (inga rollspelstips)  
✅ Alla bilder från original finns med  
✅ Navigation fungerar perfekt  
✅ Collapse-boxar funkar  
✅ Ser bra ut på mobil  
✅ Allt är på svenska  
✅ Ingen information saknas från källfiler  
✅ Hacker-estetiken bibehållen  

---

## 💬 OM DU BEHÖVER HJÄLP

**Oklart innehåll?**
→ Fråga: "Vad menas med [X] i [fil]?"

**Designbeslut?**
→ Föreslå: "Jag kan göra [A] eller [B], vilket föredrar du?"

**Teknisk implementering?**
→ Visa: "Här är min plan för [X], funkar det?"

**Hittade fel i källdata?**
→ Rapportera: "I [fil] står det [X], men i [fil] står det [Y]"

---

## 📸 BILDANVÄNDNINGSGUIDE

**Bilder tillgängliga i projektet:**

### Hero/Header-bilder:

1. **`sparky_hero_tactical.jpg`**
   - **Beskrivning:** Operations room, flera monitorer, tactical vest, purple hair tips
   - **Användning:** Top header för ÖVERSIKT eller DELTA GREEN
   - **Stil:** Professional, operational

2. **`sparky4.png`**
   - **Beskrivning:** Tactical vest med Delta Green patch, operations mode
   - **Användning:** DELTA GREEN-sektion header
   - **Stil:** Military/tactical

### Tech/Hacking-bilder:

3. **`sparky_working_late.jpg`**
   - **Beskrivning:** Hoodie, glasögon, vid dator, coding mode
   - **Användning:** TEKNISKA OPERATIONER eller NSA-relaterat
   - **Stil:** Casual hacker

4. **`sparky_operations_room.png`**
   - **Beskrivning:** Operations room, multiple screens med kod, hoodie, red/cyan lighting
   - **Användning:** TEKNISKA OPERATIONER eller BAKGRUND (NSA-sektion)
   - **Stil:** Professional hacker

5. **`sparky6.png`**
   - **Beskrivning:** Operations room, arms crossed, hoodie, confident pose
   - **Användning:** FÄRDIGHETER eller ATTRIBUT header
   - **Stil:** Confident professional

6. **`sparky5.png`**
   - **Beskrivning:** Med tablet/laptop, tactical gear, operational mode, cyberpunk lighting
   - **Användning:** TEKNISKA OPERATIONER highlight
   - **Stil:** Cyberpunk operational

### Casual/Portrait-bilder:

7. **`sparky_portrait_casual.png`**
   - **Beskrivning:** Porträtt, casual hoodie, glasögon, purple hair
   - **Användning:** BONDS eller personlig sektion
   - **Stil:** Personlig, approachable

8. **`sparky_convenience_store.png`**
   - **Beskrivning:** I butik, energidryck, casual jacket, surveillance mode
   - **Användning:** BOENDE (daglig rutin) eller lifestyle
   - **Stil:** Everyday life

### Operational/Tactical:

9. **`sparky_operational_ready.png`**
   - **Beskrivning:** Gata, tactical gear, operational stance
   - **Användning:** UTRUSTNING eller operational scenario
   - **Stil:** Field operations

10. **`sparky_street_surveillance.png`**
    - **Beskrivning:** Gata vid skymning, leather jacket, surveillance mode
    - **Användning:** ALIAS & SAFEHOUSES eller covert ops
    - **Stil:** Urban surveillance

11. **`sparky8.png`**
    - **Beskrivning:** Gata vid skymning, tactical jacket, observant pose
    - **Användning:** DELTA GREEN eller operational context
    - **Stil:** Urban tactical

### Equipment Close-up:

12. **`sparky_glock_spark_zero.png`**
    - **Beskrivning:** Glock 43X med "SPARK ZERO" graverat, Flipper Zero synlig, teal/weathered finish
    - **Användning:** UTRUSTNING-sektionen (vapen)
    - **Stil:** Product shot, detailed

---

**Rekommenderad placering:**

```html
<!-- ÖVERSIKT -->
<img src="sparky_hero_tactical.jpg" class="header-image" alt="Sparky - Operational Mode">

<!-- ATTRIBUT & STATS -->
<img src="sparky6.png" class="section-image" alt="Sparky - Confident Professional">

<!-- FÄRDIGHETER -->
<!-- Eventuellt sparky6.png igen eller hoppa över bild här -->

<!-- TEKNISKA OPERATIONER -->
<img src="sparky_working_late.jpg" class="section-image" alt="Sparky - Hacking Mode">
<img src="sparky5.png" class="detail-image" alt="Field Operations">

<!-- BONDS -->
<img src="sparky_portrait_casual.png" class="section-image" alt="Sparky - Personal Side">

<!-- BAKGRUND -->
<img src="sparky_operations_room.png" class="section-image" alt="NSA Operations">

<!-- DELTA GREEN -->
<img src="sparky4.png" class="section-image" alt="Delta Green Agent">

<!-- UTRUSTNING -->
<img src="sparky_operational_ready.png" class="section-image" alt="Operational Gear">
<img src="sparky_glock_spark_zero.png" class="equipment-detail" alt="Glock 43X - Spark Zero">

<!-- ALIAS & SAFEHOUSES -->
<img src="sparky_street_surveillance.png" class="section-image" alt="Surveillance Mode">

<!-- BOENDE -->
<img src="sparky_convenience_store.png" class="section-image" alt="Daily Life">
```

**CSS för bilder (lägg till i `<style>`):**

```css
.header-image {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  border: 2px solid var(--accent);
  margin-bottom: 2rem;
}

.section-image {
  width: 100%;
  max-width: 600px;
  height: auto;
  margin: 1rem 0;
  border: 1px solid var(--border);
}

.detail-image {
  width: 80%;
  max-width: 400px;
  height: auto;
  margin: 1rem auto;
  display: block;
}

.equipment-detail {
  width: 100%;
  max-width: 500px;
  height: auto;
  margin: 1.5rem auto;
  display: block;
  border: 2px solid var(--accent);
  padding: 0.5rem;
  background: rgba(0, 50, 0, 0.2);
}
```

**VIKTIGT:**
- Alla bildvägar är relativa till HTML-filen
- Behåll bildernas aspect ratio (använd `object-fit: cover/contain`)
- Bilder ska ha alt-text för accessibility
- Testa att alla bilder laddas korrekt

---

## 🎉 LYCKA TILL!

Du har alla verktyg och all information du behöver. Följ stegen, ta det lugnt, och bygg något användbart för spelbordet!

*Remember: Sparky är en paranoid hacker med tre falska identiteter, en död pappa, och en besatthet av att hitta en rysk mystiker med en kristallkub. Gör character sheeten lika badass som hon är.*

---

*Skapad: 2025-01-05*  
*För: Claude Code*  
*Projekt: Sparky Delta Green Character Sheet*

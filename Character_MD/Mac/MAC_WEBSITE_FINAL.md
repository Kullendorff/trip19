# MAC RILEY WEBSITE - INSTRUKTIONER

## FAKTAUNDERLAG

**VIKTIGT:** Använd befintliga .md-filer i Mac-mappen som faktakälla:
- **Mac_Stats_Skills.md** - Alla stats och färdigheter
- **Mac_Bakgrund_Tidslinje.md** - Bakgrund och tidslinje
- **Mac_FBI_Karriar_Ren.md** - FBI-karriär och expertis
- **Mac_Delta_Green.md** - Delta Green-information
- **Mac_Bonds.md** - Bonds med familj
- **Mac_Disorder.md** - Disorder-beskrivning
- **Mac_Boende_Clean.md** - Boendeinformation
- **Mac_Kontakter.md** - Alla kontakter
- **Mac_Volkov_Board.md** - Volkov-board innehåll

**Använd dessa filer för exakt information. Hitta på INGET nytt!**

## ARBETSORDNING

**INNAN du börjar skapa HTML:**
1. Läs ALLA .md-filer i Mac-mappen
2. Anteckna exakta stats, skills, bonds, etc.
3. Använd endast fakta från filerna
4. Om något saknas - fråga, hitta inte på!

**När du skapar HTML:**
1. Börja med karakter.html
2. Kopiera exakt stats/skills från Mac_Stats_Skills.md
3. Kopiera bakgrund/tidslinje från Mac_Bakgrund_Tidslinje.md
4. Fortsätt systematiskt genom alla filer
5. Testa navigation mellan sidorna

## DESIGN-FILOSOFI

**KOPIERA Sparky/Sullivan struktur EXAKT:**
- Sidebar-navigation (samma på alla sidor)
- Grid-layout: 280px sidebar + resten main content
- Faktabaserad presentation
- Minimal narrativ text
- Tydlig struktur

**SKILLNAD:** Byt färgschema till Investigation Noir

## FÄRGSCHEMA: INVESTIGATION NOIR

```css
:root {
    --bg-dark: #0D1117;
    --bg-darker: #0A0F0F;
    --accent: #4A90A4;
    --accent-dim: #3A7080;
    --text: #D1D5DB;
    --text-dim: #6B7280;
    --border: #1A2332;
    --highlight: #2C3E50;
    --warning: #E74C3C;
    --success: #4A90A4;
    --danger: #DC2626;
}
```

## TEKNISK STRUKTUR

**Filer:**
```
Mac/
├── karakter.html          (Stats, skills, bakgrund, tidslinje)
├── fbi_karriar.html       (Karriär, befogenheter, expertis)
├── delta_green.html       (DG-kunskap, Cardinal, cell, utrustning)
├── kontakter.html         (FBI, DG, personliga kontakter)
├── personligt.html        (Familj, boende, disorder, bonds)
└── volkov_board.html      (Bildgalleri - besatthet)
```

**INGEN index.html!** Karakter.html är första sidan.

## SIDEBAR NAVIGATION (SAMMA PÅ ALLA SIDOR)

```html
<div class="sidebar">
    <div class="logo">
        MAC RILEY<br>
        <span style="font-size: 0.8rem; color: var(--text-dim);">FBI // DELTA GREEN</span>
    </div>
    
    <nav>
        <div class="nav-section">
            <div class="page-link-container">
                <a href="karakter.html" class="page-link">KARAKTER</a>
                <a href="fbi_karriar.html" class="page-link">FBI KARRIÄR</a>
                <a href="delta_green.html" class="page-link">DELTA GREEN</a>
                <a href="kontakter.html" class="page-link">KONTAKTER</a>
                <a href="personligt.html" class="page-link">PERSONLIGT</a>
                <a href="volkov_board.html" class="page-link">VOLKOV-BOARD</a>
            </div>
        </div>
        
        <div class="nav-section">
            <div class="nav-title">SNABBNAVIGERING</div>
            <a href="#stats" class="nav-link">Stats</a>
            <a href="#skills" class="nav-link">Färdigheter</a>
            <a href="#bakgrund" class="nav-link">Bakgrund</a>
            <!-- Olika per sida -->
        </div>
    </nav>
    
    <div style="margin-top: auto; padding-top: 2rem; border-top: 1px solid var(--border); font-size: 0.75rem; color: var(--text-dim); text-align: center;">
        CLASSIFIED<br>DELTA GREEN<br>EYES ONLY
    </div>
</div>
```

## BILDFÖRDELNING

- **karakter.html hero**: mac4.png (casual)
- **fbi_karriar.html hero**: mac2.jpeg (professional)
- **delta_green.html hero**: mac1.jpeg (tactical)
- **kontakter.html hero**: mac3.png (investigation desk)
- **personligt.html hero**: mac10.png (symbolic)
- **volkov_board.html hero**: mac8.png (the board)

**Övriga bilder används i gallerier på respektive sida**

## INNEHÅLL PER SIDA

### 1. KARAKTER.HTML

**Hero Section:**
```html
<div class="hero-section">
    <div class="hero-content">
        <h1>MAC RILEY</h1>
        <div class="subtitle">Special Agent Marcus Patrick Riley</div>
        <p>FBI Supervisory Special Agent med specialisering i kriminell profilering och kalla fall. Delta Green Outlaw operative sedan 2018.</p>
    </div>
    <div class="hero-image">
        <img src="mac4.png" alt="Mac Riley">
    </div>
</div>
```

**Sektion: GRUNDINFO**
Tabell:
```
Namn: Marcus Patrick "Mac" Riley
Född: 27 mars 1987, Naval Hospital Camp Lejeune, NC
Ålder: 38 år
Nationalitet: Amerikansk
Yrke: FBI Supervisory Special Agent (tvångslovad augusti 2025)
Delta Green: Outlaw operative, "Chesapeake" cell
```

**Sektion: STATS**
Tabell (3 kolumner):
```
STR: 14 (70%)    |  HP: 14         |  SAN: 46/60
CON: 14 (70%)    |  WP: 12         |  Breaking Point: 36
DEX: 12 (60%)    |  Armor: 0       |  Disorder: PTSD med obsessiva drag
INT: 12 (60%)    |  
POW: 12 (60%)    |  Adapted to Violence: ADAPTED (3/3)
CHA: 10 (50%)    |  Adapted to Helplessness: 1/3
```

**Sektion: FÄRDIGHETER**
Fullständig tabell (3-4 kolumner) med ALLA färdigheter:
```
Alertness: 50%           | Firearms: 70%          | Search: 40%
Athletics: 40%           | First Aid: 20%         | SIGINT: 0%
Bureaucracy: 40%         | Forensics: 60%         | Stealth: 30%
Criminology: 50%         | Heavy Machinery: 0%    | Surgery: 0%
Demolitions: 0%          | Heavy Weapons: 0%      | Survival: 20%
Disguise: 20%            | History: 20%           | Swim: 30%
Dodge: 30%               | HUMINT: 50%            | Technology: 20%
Drive: 40%               | Law: 40%               | Unarmed Combat: 50%
                         | Medicine: 0%           | Unnatural: 8%
                         | Melee Weapons: 30%     |
                         | Military Science: 20%  |
                         | Navigate: 20%          |
                         | Occult: 20%            |
                         | Persuade: 40%          |
                         | Pharmacy: 0%           |
                         | Psychotherapy: 0%      |
                         | Ride: 20%              |
```

**Sektion: BAKGRUND**
Kortfattad faktabaserad text:
- Uppväxt i Marine Corps-familj
- USMC 2005-2011, två deployments
- Georgetown University 2011-2012
- FBI Academy 2012, Top 15%
- FBI 2012-2025: New York → Washington → BAU

**Sektion: TIDSLINJE**
Lista med årtal och händelser:
```
1987 - Född på Camp Lejeune, NC
2005 - USMC grundutbildning, Parris Island
2007 - Första utplacering (Irak)
2009-2010 - Andra utplacering (Afghanistan)
2011 - Lämnar marinkåren, påbörjar Georgetown
2012 - FBI-akademin, Quantico
2012-2014 - Specialagent, New York fältkontor
2014-2016 - Specialagent, Washington fältkontor
2016-2019 - Specialagent, BAU-2
2018 - Första kontakt med det onaturliga (St. Louis)
2019 - Befordrad till övervakande specialagent
2024 (december) - Operation Mall Before Christmas - 5 SAN-förlust
2025 (maj) - Operation Sea Glass - Breaking Point (6 SAN-förlust)
2025 (augusti) - Tvångslovad från FBI
```

### 2. FBI_KARRIAR.HTML

**Hero Section:**
```html
<div class="hero-section">
    <div class="hero-content">
        <h1>FBI KARRIÄR</h1>
        <div class="subtitle">Supervisory Special Agent / Behavioral Analysis Unit</div>
        <p>20+ år kombinerad tjänst i Marines och FBI. Specialisering: kriminell profilering, kalla fall, pattern recognition.</p>
    </div>
    <div class="hero-image">
        <img src="mac2.jpeg" alt="Mac Riley - FBI">
    </div>
</div>
```

**Sektion: KARRIÄRHISTORIK**
Tabell:
```
Period      | Position                    | Enhet                          | Grade
2012-2014   | Special Agent               | New York Field Office          | GS-10 → GS-12
2014-2016   | Special Agent               | Washington Field Office        | GS-12 → GS-13
2016-2019   | Special Agent               | Behavioral Analysis Unit 2     | GS-13
2019-2025   | Supervisory Special Agent   | BAU-2, Team Leader             | GS-14
```

**Sektion: EXPERTOMRÅDEN**
Lista med beskrivningar:
- **Forensics** - Crime scene analysis, bevis säkring, 20+ års erfarenhet
- **Criminology** - Brottslingsprofiler, mönsterigenkänning, seriebrott
- **HUMINT** - Förhörsteknik, vittnesmål, Marines-bakgrund ger fördel
- **Behavioral Analysis** - Gärningsmannaprofilering, hotbedömning, BAU-specialist
- **Pattern Recognition** - Ser samband över tid och geografi, ViCAP-expert
- **Case Management** - Långvariga utredningar, multi-jurisdiktion koordinering

**Sektion: BEFOGENHETER**
Tabell:
```
FEDERAL AUKTORITET
Jurisdiktion: Nationell (alla delstater)
Gripande: Federala gripandebefogenheter
Vapen: Beväpnad dygnet runt
Husrannsakan: Federal häktning och genomsökning
Koordinering: Myndighetsövergripande samarbete

DATABASER & RESURSER
- NCIC (Nationell brottsdatabas)
- ViCAP (Våldsbrott mönster)
- CODIS (DNA-profiler)
- Ansiktsigenkänningssystem
- Tillgång till ekonomiska register
- Kommunikationsövervakning
```

**Sektion: SÄKERHETSCLEARANCE**
Tabell:
```
Säkerhetsnivå   | Status  | Tillgång
SECRET          | Aktiv   | Standard FBI-operationer
TOP SECRET      | Aktiv   | Myndighetsövergripande sekretess
TS/SCI          | Begränsad | Avdelad underrättelse
Delta Green     | N/A     | Oerkänt program
```

**Sektion: NUVARANDE STATUS**
```
Status: TVÅNGSLOVAD (augusti 2025)
Anledning: PTSD-indikationer, stressreaktion
Utvärdering: Pågående psykologisk bedömning
Återgång: Obestämd

Byrån vet: PTSD, hypervakenhet, stress
Byrån vet INTE: Delta Green, Volkov-besatthet, Breaking Point
```

### 3. DELTA_GREEN.HTML

**Hero Section:**
```html
<div class="hero-section">
    <div class="hero-content">
        <h1>DELTA GREEN</h1>
        <div class="subtitle">Outlaw Operative / "Chesapeake" Cell</div>
        <p>Rekryterad 2018 efter St. Louis-incidenten. Specialisering: investigation lead och behavioral analysis för oförklarliga händelser.</p>
    </div>
    <div class="hero-image">
        <img src="mac1.jpeg" alt="Mac Riley - Tactical">
    </div>
</div>
```

**Sektion: VAD MAC VET OM DELTA GREEN**
Faktabaserad lista:
- Oofficiell, oerkänd organisation inom amerikanska regeringen
- Grundad för att hantera "det onaturliga"
- Outlaw-status = ingen officiell backup, cover-up = eget ansvar
- Handler: Kodnamn CARDINAL
- Cell: "Chesapeake"-cell, Washington DC-området
- Säkerhet: Döda brevlådor, engångstelefoner, avskärmning

**Sektion: CARDINAL**
```
Kodnamn: CARDINAL
Roll: Handler för "Chesapeake"-cell
Kontakt: Död brevlåda i Arlington, engångstelefon för nödsituationer
Kännedom: Högnivå Delta Green-koordinator
Macs relation: Professionell, ingen personlig info utbytt
```

**Sektion: CELLMEDLEMMAR**
Kort beskrivning av varje:

```
FATHER MICHAEL SULLIVAN
- Navy Chaplain (Lieutenant Commander)
- Specialisering: Pastoral care, occult knowledge, moralisk kompass
- Mac's syn: Pålitlig men naiv om verklig ondska

KAI "SPARKY" ZHANG
- NSA Senior Analyst
- Specialisering: SIGINT, cybersecurity, tech support
- Mac's syn: Bästa tech-asset, håller distans personligen

SAM "TRENCH" NOVAK  
- US Army Reserve (Staff Sergeant)
- Specialisering: Taktisk planering, heavy weapons, muscle
- Mac's syn: Solid operator, kan lita på under press
```

**Sektion: OPERATIONER**
Lista med datum och resultat:
```
2018 (mars) - St. Louis Incident - REKRYTERING
2019 (aug) - [Operation namn] - 2 SAN förlust
2020 (feb) - [Operation namn] - 3 SAN förlust
2024 (dec) - The Mall Before Christmas - 5 SAN förlust
2025 (maj) - Operation Sea Glass - BREAKING POINT (6 SAN förlust)
```

**Sektion: UTRUSTNING**
**Standard utrustning:**
- Glock 22 (.40 S&W) - FBI-tjänstevapen
- Sig Sauer P229 - reservpistol
- Taktisk väst (räder)
- FBI-legitimation + 3 falska identiteter
- Portabel kriminalteknisk sats

**Delta Green-förnödenheter:**
- Engångstelefoner (×3)
- Drop-telefon (CARDINAL-kontakt)
- Dyrk-set
- Minikamera + inspelningsenhet
- $5,000 kontanter (oförklarliga utgifter)

### 4. KONTAKTER.HTML

**Hero Section:**
```html
<div class="hero-section">
    <div class="hero-content">
        <h1>KONTAKTER</h1>
        <div class="subtitle">Nätverk & Kopplingar</div>
        <p>20 års karriär inom Marines och FBI har byggt ett omfattande kontaktnät. Delta Green har lagt till... andra typer av kontakter.</p>
    </div>
    <div class="hero-image">
        <img src="mac3.png" alt="Mac Riley - Investigation">
    </div>
</div>
```

**Sektion: FBI KONTAKTER**
Lista med namn, position, relation, användbarhet:
```
SSA Jennifer Martinez
Position: BAU-3 Profiler
Relation: Tidigare partner, vän
Användbarhet: Kan få inofficiell hjälp med profiler, diskret

SA David Chen
Position: New York Field Office, Organized Crime
Relation: Kollega sedan 2012
Användbarhet: Info om mob-aktivitet, kan fråga utan att väcka misstankar

SSA Robert "Bob" Anderson
Position: Washington Field Office, Supervisor
Relation: Skeptisk om Mac's mentala tillstånd
Användbarhet: RISK - håller koll på Mac's aktiviteter

Dr. Patricia Reynolds
Position: FBI Forensics Lab, DC
Relation: Professionell kontakt
Användbarhet: Expedited forensics, diskreta frågor

SA Michael Torres
Position: Cyber Division
Relation: Bekant via gemensamma fall
Användbarhet: Digital forensics, kan be om "inofficiella" tjänster
```

**Sektion: DELTA GREEN KONTAKTER**
```
CARDINAL (Handler)
Kontakt: Dead drop, burner phone
Användbarhet: Operations approval, resources, intel

A-CELL Members
- Father Sullivan: Moral support, occult knowledge
- Sparky Zhang: Tech support, SIGINT
- Sam Novak: Tactical backup, muscle

[Andra DG-agenter Mac träffat under operationer]
```

**Sektion: PERSONLIGA KONTAKTER**
```
Tom Riley
Relation: Far, Marines veteran (Gunnery Sergeant, ret.)
Kännedom: VET INTE om Delta Green, anar något är fel
Användbarhet: Militär insikt, emotionellt stöd

Sarah Riley
Relation: Ex-fru, Jake's mamma
Kännedom: VET INTE om Delta Green, vet Mac "arbetar för mycket"
Användbarhet: Koppling till Jake, varning om Mac går för långt

Jake Riley (12 år)
Relation: Son
Kännedom: Inget
Användbarhet: Motivation att överleva operationer
```

**Sektion: INFORMANTER (FBI)**
```
"Ghost" - Former mob accountant, witness protection
"Candyman" - Drug dealer, reliable intel on street activity
"The Librarian" - Researcher, off-the-books archive access
```

### 5. PERSONLIGT.HTML

**Hero Section:**
```html
<div class="hero-section">
    <div class="hero-content">
        <h1>PERSONLIGT</h1>
        <div class="subtitle">Familj, Boende & Konsekvenser</div>
        <p>Sex år med Delta Green. Sex poäng från total mental kollaps. Det här är priset.</p>
    </div>
    <div class="hero-image">
        <img src="mac10.png" alt="Mac Riley - Personal">
    </div>
</div>
```

**Sektion: FAMILJ**
Tabell:
```
Sarah Riley (f. Martinez)
Relation: Ex-fru (skild 2024)
Bond: 8/12 poäng
Status: Bor i Bethesda, MD med Jake
Kännedom: Vet att Mac "har problem" men inte varför

Jake Riley
Relation: Son, 12 år
Bond: 8/12 poäng  
Status: Bor hos Sarah, hos Mac varannan helg + onsdagar
Kännedom: Märker att pappa är "annorlunda", orolig

Thomas "Tom" Riley
Relation: Far, USMC Gunnery Sergeant (ret.)
Bond: 10/12 poäng
Status: Bor i Jacksonville, NC
Kännedom: Marines-veteran, anar att något är fel, respekterar hemligheter
```

**Sektion: BOENDE**
```
TYP: 1BR lägenhet
PLATS: Arlington, Virginia
OMRÅDE: Courthouse-Navy område
LÄGENHET: 3:e våningen, oinrett, minimalistiskt

EGENSKAPER:
- Ett sovrum (säng, byrå)
- Litet kök (används sällan)
- Vardagsrum (soffa, TV, whiskey-bar)
- "Arbetsrummet" - konverterat walk-in closet
  → VOLKOV-BOARDEN finns här
  → Dörr med lås, Jake får INTE gå in

SÄKERHET:
- Extra lås på dörr
- Alarm system
- Backup-vapen gömd i sovrum
- Burner phones i kök
```

**Sektion: DISORDER**
```
DIAGNOS: PTSD med obsessiva drag (Volkov-fokuserad)
URSPRUNG: Breaking Point efter Operation Sea Glass (maj 2025)

MANIFESTATIONER:
- Tvångstankar om Volkov-kopplingar
- Måste uppdatera boarden varje kväll
- Hypervigilance (ser mönster överallt)
- Sömnstörning (vaknar 03:00, kollar boarden)
- Ritualbeteende (samma rutiner varje dag)

TRIGGERS:
- Referenser till Maine, köpcentrum, kristaller
- Olösta fall
- När andra inte ser kopplingarna
- Tidspress under utredningar

COPING:
- Whiskey (3-4 glas/natt för att somna)
- Undviker sociala sammanhang
- Drar sig undan familj för att "fokusera"
```

**Sektion: BONDS (DETALJERAT)**
Tabell:
```
Bond                | Poäng  | Status
Sarah Riley         | 8/12   | Skadad (skilsmässa), fortsätter sjunka
Jake Riley          | 8/12   | Skadad (distans), oro ökar
Thomas Riley        | 10/12  | Stabil men utsatt
```

**Sektion: ADAPTATIONS**
```
ADAPTED TO VIOLENCE: ADAPTED (3/3)
- Förlorat 1D6 CHA + Bonds
- Kan hantera våld utan SAN-checks

ADAPTED TO HELPLESSNESS: 1/3
- Sea Glass trauma (kunde inte rädda offret)
- Fortfarande påverkas av att se andra lida
- Inte immuniserad mot hjälplöshet
```

**Sektion: FYSISKT TILLSTÅND**
```
Längd: 183 cm
Vikt: 82 kg (- 8 kg senaste 6 månaderna)
Kondition: God (Marines-träning, regelbunden gym)
Sömnmönster: 4-5h/natt, alpdrömmar, vaknar 03:00

TECKEN PÅ STRESS:
- Djupa ringar under ögonen
- Tremor i händer vid stress
- Viktförlust
- Hypervigilance (kollar över axeln konstant)

SUBSTANSBRUK:
- Alkohol: 3-4 glas whiskey/natt
- Kaffe: 6-8 koppar/dag
- Inga illegala substanser
- Inga prescription meds (vägrar psykmedicin)
```

### 6. VOLKOV_BOARD.HTML

**Hero Section:**
```html
<div class="hero-section">
    <div class="hero-content">
        <h1>VOLKOV-BOARDEN</h1>
        <div class="subtitle">Pattern Recognition / Besatthetens Kartografi</div>
        <p style="color: var(--danger);">⚠ OBSESSION LEVEL: CRITICAL</p>
    </div>
    <div class="hero-image">
        <img src="mac8.png" alt="Volkov Board">
    </div>
</div>
```

**Intro-text:**
```
När Mac kom hem från Operation Sea Glass började han bygga boarden. 
Först bara några foton och anteckningar. Nu täcker den ena väggen i hans 
"arbetsrum" - dörren låst, Jake får inte se.

Kopplingarna är där. Mönstret finns. Volkov, kristallerna, tidigare offer. 
Allt hänger ihop. Problemet är inte att Mac ser för mycket. Problemet är 
att ingen annan ser tillräckligt.
```

**Bildgalleri:**
Grid med bilder och kortfattade beskrivningar:

**Bild: mac8.png**
```
CENTRAL COMMAND
Hela boarden. Röda trådar mellan foton, dokument, kartor. 
Volkov i centrum. Kristallkuben. Flight 19. Black Madonna. Allt kopplat.
```

**Bild: mac7.png**
```
LATE NIGHT RESEARCH  
03:00. Whiskey. Nya foton på boarden. Mönstret blir tydligare. 
Eller är det bara desperationen som växer?
```

**Bild: mac3.png**
```
ARCHIVE DEEP DIVE
Varje dokument är en ledtråd. CAB-rapporter om Flight 19. 
FBI-arkiv om Lundeen. Podcast-anteckningar. Allt sparas. Allt analyseras.
```

**Bild: mac6.png**
```
PATTERN ANALYSIS
Vad ser jag som ingen annan ser? Eller har jag slutat se verkligheten?
Sullivan frågar om jag sover. Sparky undrar om jag är okej. 
Men de ser inte mönstret.
```

**Sektion: HUVUDSAKLIGA KOPPLINGAR**
Lista (faktabaserad):
```
THE MALL BEFORE CHRISTMAS (2023)
- Köpcentrum i Maine
- Kristallkub hittad på plats
- 14 dödsfall
- Volkov flydde med artefakten
- Mac kunde inte stoppa honom

OPERATION SEA GLASS (2025)
- Första direkt konfrontation med Volkov
- Ett offer dödades framför Macs ögon
- Kunde inte rädda henne
- Volkov flydde igen
- Mac nådde Breaking Point

VOLKOV
- Identitet okänd (rysk? kultist? något värre?)
- Kristallkuben från Mall-operationen
- Sedd vid minst 3 tillfällen
- Mönster av aktivitet längs östkusten
- Extremt farlig, använder onaturliga metoder

KRISTALLTEKNOLOGIN
- Onaturlig artefakt
- Okänt ursprung
- Verkar kommunicera eller kontrollera
- Koppling till offer/ritualer
- Volkov har kunskapen att använda den

NUVARANDE HOT
- Kristallkuben fortfarande aktiv
- Volkovs vistelseort okänd
- Risk för nya offer
- Mac måste hitta honom innan nästa operation
```

**Sektion: MACS ANTECKNINGAR**
```
Citat från hans egna anteckningar på boarden (korta, fragmenterade):

"Mall-operationen - 14 döda. Jag såg mönstret för sent."
"Kristaller = kommunikation? Kontroll? Något värre?"
"Volkov - 3 bekräftade observationer. Mönster: kustnära, vintermånader"
"Sea Glass-offret - varför just hon? Rituell betydelse?"
"Kunde inte rädda henne. Såg honom fly. Igen."
"MÖNSTRET ÄR SANT. De förstår bara inte än."
"Nästa gång. Nästa gång stoppar jag honom."
```

**Footer varning:**
```
⚠ DENNA INFORMATION FÅR EJ DELAS MED ICKE-DELTA GREEN PERSONAL
⚠ SÄRSKILT EJ FBI-KOLLEGOR ELLER FAMILJ
⚠ CARDINAL HAR EJ GODKÄNT DENNA OMFATTNING AV PRIVAT UTREDNING
```

## CSS - KOPIERA & ANPASSA

**Ta Sparky eller Sullivans CSS som bas, ändra bara färgerna till Investigation Noir-palettet.**

**Viktiga delar:**
- Grid: 280px sidebar + 1fr content
- Sticky sidebar
- Hero section på varje sida (2-kolumn: text + bild)
- Content sections med borders
- Tables för stats/info
- Responsive design (< 768px = single column)

## CHECKLISTA

- [ ] Alla 6 HTML-filer
- [ ] Samma sidebar på alla sidor
- [ ] Investigation Noir färger konsekvent
- [ ] Alla bilder korrekt placerade
- [ ] Stats: SAN 46/60, BP 36
- [ ] Disorder-sektion finns
- [ ] Bonds med poäng
- [ ] Adaptations dokumenterade
- [ ] Allt på svenska (utom tekniska termer)
- [ ] Snabbnavigering fungerar (# links)
- [ ] Footer på alla sidor

## SPRÅK & TON

**KORT OCH KONCIST:**
- Fakta först
- Beskrivningar kortfattade
- Inga långa citat eller narrativ
- Spelaren ska fylla i resten själv

**GOD TON:**
"Mac är specialist inom kriminell profilering med 20 års erfarenhet."

**DÅLIG TON:**
"Mac sitter framför sin dator, whiskeyglaset halvtomt, och stirrar på Volkov-boarden. 'Varför ser ingen andra mönstret?' tänker han för hundrade gången..."

**UNDANTAG:** Volkov-board får vara lite mer intensiv, men fortfarande kortfattat.

---

**BÖRJA MED karakter.html, TESTA SIDEBAR, FORTSÄTT SEDAN.**

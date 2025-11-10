# INSTRUKTIONER: Delta Green Medical Agents - Character Selection Page

## ÖVERSIKT
Skapa en enkel, snygg hemsida som presenterar 20 medicinska Delta Green-agenter för karaktärsval. Varje agent ska ha bild och collapse-box med info.

---

## FÄRGSCHEMA: "Medical Noir"

**Primära färger:**
- Bakgrund: `#0a0e14` (nästan svart med blå ton)
- Kort bakgrund: `#151b23` (mörkgrå-blå)
- Accent/Headers: `#3a9693` (medicinsk cyan/teal)
- Text primär: `#e4e4e7` (ljusgrå, läsbar)
- Text sekundär: `#94a3b8` (medium grå)
- Border/Divider: `#1e293b` (mörk blå-grå)
- Hover: `#2dd4bf` (ljusare cyan)

**Typsnitt:**
- Headers: 'Inter', sans-serif (eller system-font)
- Body: 'system-ui', sans-serif

---

## STRUKTUR

### HTML Layout:
```
<!DOCTYPE html>
<html>
<head>
    <title>Delta Green - Medical Agents</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    [CSS här]
</head>
<body>
    <header>
        <h1>DELTA GREEN: CHESAPEAKE CELL</h1>
        <h2>Medical Agent Selection</h2>
        <p class="subtitle">20 Available Operatives - Choose Your Character</p>
    </header>
    
    <main>
        <!-- 20 agent cards här -->
    </main>
    
    <footer>
        <p>Classified - Outlaw Cell Operations - Handler: "Cardinal"</p>
    </footer>
    
    [JavaScript här]
</body>
</html>
```

---

## AGENT CARD STRUKTUR

Varje agent ska ha denna struktur:

```html
<div class="agent-card">
    <div class="agent-header" onclick="toggleInfo(this)">
        <img src="1.png" alt="Triage" class="agent-photo">
        <div class="agent-title">
            <h3 class="codename">"TRIAGE"</h3>
            <h4 class="realname">Dr. James Park</h4>
            <p class="job">Traumakirurg, Johns Hopkins</p>
        </div>
        <span class="toggle-icon">▼</span>
    </div>
    
    <div class="agent-info" style="display: none;">
        <div class="info-section">
            <h5>Bakgrund</h5>
            <p>[Text från karaktärsbeskrivning]</p>
        </div>
        
        <div class="info-section">
            <h5>Personlighet</h5>
            <p>[Text från karaktärsbeskrivning]</p>
        </div>
        
        <div class="info-section">
            <h5>Delta Green</h5>
            <ul>
                <li>4 operationer (3 survival, 1 failure)</li>
                <li>Håller agents vid liv, ingen bullshit</li>
                <li>"Du dör inte på min vakt"</li>
            </ul>
        </div>
        
        <div class="info-section details">
            <p><strong>Ålder:</strong> 42 | <strong>Bor:</strong> Fells Point, Baltimore</p>
            <p><strong>Cover:</strong> Jobbschema på sjukhus förklarar allt</p>
        </div>
    </div>
</div>
```

---

## CSS REQUIREMENTS

**Key features:**
- Responsive design (fungerar på mobil och desktop)
- Smooth transitions för collapse
- Hover effects på cards
- Grid layout: 1 kolumn på mobil, 2 kolumner på tablet, 2-3 på desktop
- Agent photos: 120px × 120px, cirkulära
- Cards har subtle shadow och border
- Collapse icon roterar 180° när öppen

**Exempel CSS struktur:**
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: #0a0e14;
    color: #e4e4e7;
    font-family: system-ui, -apple-system, sans-serif;
    line-height: 1.6;
    padding: 20px;
}

header {
    text-align: center;
    margin-bottom: 40px;
    padding: 40px 20px;
    border-bottom: 2px solid #1e293b;
}

h1 {
    color: #3a9693;
    font-size: 2.5rem;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.agent-card {
    background: #151b23;
    border: 1px solid #1e293b;
    border-radius: 8px;
    margin-bottom: 20px;
    overflow: hidden;
    transition: all 0.3s ease;
}

.agent-card:hover {
    border-color: #3a9693;
    box-shadow: 0 4px 12px rgba(58, 150, 147, 0.2);
}

.agent-header {
    display: flex;
    align-items: center;
    padding: 20px;
    cursor: pointer;
    gap: 20px;
}

.agent-photo {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #3a9693;
}

.codename {
    color: #3a9693;
    font-size: 1.5rem;
    font-weight: 700;
}

/* ...etc för resten av styling */
```

---

## JAVASCRIPT REQUIREMENTS

**Toggle functionality:**
```javascript
function toggleInfo(header) {
    const card = header.parentElement;
    const info = card.querySelector('.agent-info');
    const icon = card.querySelector('.toggle-icon');
    
    if (info.style.display === 'none') {
        info.style.display = 'block';
        icon.textContent = '▲';
        icon.style.transform = 'rotate(180deg)';
    } else {
        info.style.display = 'none';
        icon.textContent = '▼';
        icon.style.transform = 'rotate(0deg)';
    }
}
```

---

## DATA: 20 AGENTER

### TRAUMA & AKUTMEDICIN

**1. "TRIAGE" - Dr. James Park** (1.png)
- Ålder: 42 | Jobb: Traumakirurg, Johns Hopkins Shock Trauma Center, Baltimore
- Bakgrund: Ex-Army combat medic (3 deployments), rekryterad 2019
- Personlighet: Kallblodig under press, perfektionist, bär skuld över de han inte kunde rädda
- DG: 4 operationer (3 survival, 1 failure), "Du dör inte på min vakt"
- Bor: Fells Point, Baltimore

**2. "NIGHT SHIFT" - Dr. Sarah Chen** (2.png)
- Ålder: 38 | Jobb: Akutläkare, DC General ER
- Bakgrund: Georgetown medicin, rekryterad 2020 efter "impossible injuries"
- Personlighet: Snabbpratande, svär mycket, gallows humor, lever på kaffe
- DG: 3 operationer, "Seen worse on a Friday night"
- Bor: Columbia Heights, DC

**3. "FLIGHT DOC" - Dr. Marcus Webb** (3.png)
- Ålder: 45 | Jobb: HEMS Flygambulansläkare, Maryland State Police Aviation Command
- Bakgrund: Ex-Air Force flight surgeon, rekryterad 2021
- Personlighet: Lugn, metodisk, kontrollbehov, älskar att flyga
- DG: 2 operationer (extraction/evac), "I'm your ride out"
- Bor: Annapolis, MD

**4. "COMBAT MEDIC" - Andre Johnson** (4.png)
- Ålder: 35 | Jobb: Paramedic, DC Fire and EMS
- Bakgrund: Navy Hospital Corpsman (MARSOC), 4 deployments, Silver Star
- Personlighet: Tyst, lojal till graven, PTSD men fungerande
- DG: 4 operationer (action-heavy), "Stay with me"
- Bor: Anacostia, DC

**5. "BURN UNIT" - Dr. Elizabeth Torres** (5.png)
- Ålder: 47 | Jobb: Plastikkirurg, Walter Reed National Military Medical Center
- Bakgrund: Guatemalansk immigrant, specialiserad brännskador, rekryterad 2022
- Personlighet: Empatisk men pragmatisk, perfektionist
- DG: 2 operationer (post-op support), "I can fix this"
- Bor: Bethesda, MD

---

### FORENSIK & RÄTTSMEDICIN

**6. "AUTOPSY" - Dr. Raymond Clarke** (6.png)
- Ålder: 44 | Jobb: Chief Medical Examiner, DC Office of the Chief Medical Examiner
- Bakgrund: Mortician-familj, rekryterad 2018 efter Deep One-obduktion
- Personlighet: Mörk humor, pratar med lik, känslomässigt avstängd
- DG: 4 operationer (clean-up, obduktioner), "This never happened"
- Bor: Capitol Hill, DC

**7. "BONES" - Dr. Michael Chen** (7.png)
- Ålder: 40 | Jobb: Forensisk Antropolog, FBI Consultant (Quantico)
- Bakgrund: Smithsonian → FBI, rekryterad 2019 efter "non-human remains"
- Personlighet: Nördig, entusiastisk om döda saker, socialt awkward
- DG: 3 operationer (research/analysis), "Officially, this is a bear"
- Bor: Fairfax, VA

**8. "LAB RAT" - Dr. Keisha Washington** (8.png)
- Ålder: 39 | Jobb: Forensisk Patolog, Maryland State Medical Examiner
- Bakgrund: Baltimore native, Howard → Johns Hopkins, rekryterad 2021
- Personlighet: Smart, skeptisk, vetenskaplig metod är religion
- DG: 2 operationer (lab support), "The data says..."
- Bor: Baltimore, MD

**9. "COLD CASE" - Dr. Frank Morrison** (9.png)
- Ålder: 52 | Jobb: Medical Examiner Consultant, FBI Cold Case Unit
- Bakgrund: Virginia bred, rekryterad 2017 efter "wrong grave"
- Personlighet: Grandfatherly, patient, bär tunga hemligheter
- DG: 4 operationer (veteran, post-op), "Let the dead rest"
- Bor: Arlington, VA

**10. "TRACE EVIDENCE" - Dr. Lisa Tran** (10.png)
- Ålder: 36 | Jobb: Forensisk Toxikolog, FBI Laboratory (Quantico)
- Bakgrund: MIT kemi → FBI, rekryterad 2020 efter "unknown substance"
- Personlighet: Obsessivt metodisk, ingen risk-taker, nyfiken på omöjligt
- DG: 3 operationer (analysis, lab-based), "Chemically impossible, but here it is"
- Bor: Fredericksburg, VA

---

### PSYKIATRI & NEUROLOGI

**11. "PSYCH WARD" - Dr. Robert Ashford** (11.png)
- Ålder: 48 | Jobb: Psykiater, St. Elizabeths Hospital, DC
- Bakgrund: Old money Virginia, rekryterad 2019 efter patient som "knew too much"
- Personlighet: Lugn, analytisk, själv inte helt stabil
- DG: 3 operationer (support, debriefs), "Tell me about the dreams"
- Bor: Georgetown, DC

**12. "BRAINSTORM" - Dr. Nina Patel** (12.png)
- Ålder: 41 | Jobb: Neurolog, Johns Hopkins Neurology Department
- Bakgrund: Brilliant researcher, rekryterad 2021 efter "impossible neural degradation"
- Personlighet: Driven, workaholic, emotionellt tillbakadragen
- DG: 2 operationer (medical analysis), "Your neurons are changing"
- Bor: Baltimore, MD

**13. "SLEEP DOC" - Dr. James Moreau** (13.png)
- Ålder: 39 | Jobb: Sömnmedicinläkare, Privat praktik DC
- Bakgrund: Louisiana Creole, rekryterad 2020 efter patienter med "same nightmare"
- Personlighet: Soft-spoken, empatisk, sover dåligt själv
- DG: 3 operationer (research + treatment), "Don't go back to sleep"
- Bor: Dupont Circle, DC

**14. "PTSD SPECIALIST" - Dr. Maria Santos** (14.png)
- Ålder: 45 | Jobb: Psykiater, Walter Reed Military PTSD Program
- Bakgrund: Navy brat, specialiserad combat trauma, rekryterad 2018
- Personlighet: Warm but firm, no-bullshit approach
- DG: 4 operationer (psychological support), "It's okay to not be okay"
- Bor: Silver Spring, MD

**15. "GERO-PSYCH" - Dr. Harold Winters** (15.png)
- Ålder: 56 | Jobb: Geriatrisk Psykiater, Baltimore VA Medical Center
- Bakgrund: Vietnam vet's son, rekryterad 2015 efter "old DG veteran interview"
- Personlighet: Faderlig, patient, har sett vad långtidsexponering gör
- DG: 4 operationer (veteran), "I've seen how this ends"
- Bor: Catonsville, MD

---

### SPECIALISTER

**16. "RAD" - Dr. Jennifer Kim** (16.png)
- Ålder: 43 | Jobb: Radiolog, Georgetown University Hospital
- Bakgrund: Stanford medicin, rekryterad 2020 efter "things in scans"
- Personlighet: Detail-oriented, skeptisk, ser mönster andra missar
- DG: 2 operationer (diagnostic support), "This shadow isn't normal"
- Bor: Bethesda, MD

**17. "INFECTIOUS" - Dr. David Okonkwo** (17.png)
- Ålder: 40 | Jobb: Infektionsläkare, NIH Bethesda
- Bakgrund: Johns Hopkins → CDC → NIH, rekryterad 2021
- Personlighet: Methodical, paranoid, germaphobe
- DG: 3 operationer (bio-threats), "Quarantine. Now."
- Bor: Rockville, MD

**18. "GENE" - Dr. Rebecca Stein** (18.png)
- Ålder: 37 | Jobb: Genetiker, NIH/CDC Consultant
- Bakgrund: MIT genetics, rekryterad 2022 efter DNA som "can't be human"
- Personlighet: Brilliant, obsessive, ethical conflicts
- DG: 1 operation (nyast, lab-support), "You're 99.7% human"
- Bor: Bethesda, MD

**19. "WILDERNESS" - Dr. Thomas Reeves** (19.png)
- Ålder: 44 | Jobb: Expeditionsmedicinare, Freelance (NGO consultant)
- Bakgrund: Montana bred, rekryterad 2019 efter "jungle incident"
- Personlighet: Rugged, self-reliant, uncomfortable i städer
- DG: 4 operationer (remote, field-heavy), "I've worked worse conditions"
- Bor: Shenandoah region, VA

**20. "CORONER" - Dr. William Patterson** (20.png)
- Ålder: 58 | Jobb: Landsbygdsläkare & Medical Examiner, Loudoun County VA
- Bakgrund: Fifth generation Virginian, rekryterad 2016
- Personlighet: Folksy, trusted by locals, hides sharp mind
- DG: 4 operationer (local fixer), "Let me make some calls"
- Bor: Leesburg, VA

---

## TEKNISKA KRAV

**Filstruktur:**
```
index.html          (hela sidan i en fil)
1.png - 20.png      (agent-bilder)
```

**Responsive breakpoints:**
- Mobile: < 768px (1 kolumn)
- Tablet: 768px - 1024px (2 kolumner)
- Desktop: > 1024px (2-3 kolumner)

**Features:**
- ✅ Smooth collapse animations
- ✅ Hover effects på cards
- ✅ Rotating toggle icon
- ✅ Cirkulära bilder med border
- ✅ Grid layout som anpassar sig
- ✅ Tydlig typografi-hierarki
- ✅ Subtle shadows och depth

**Footer info:**
```
Classified - Outlaw Cell Operations - Handler: "Cardinal"
Chesapeake Cell (DC/Maryland/Virginia)
```

---

## OUTPUT

Skapa EN ENDA HTML-fil (`index.html`) med all CSS och JavaScript inbäddat. Filen ska vara:
- Komplett och körbar direkt
- Responsive och snabb
- Professional medical noir aesthetic
- Alla 20 agenter med korrekt data
- Redo att öppna i webbläsare

**Bilderna (1.png - 20.png) förväntas finnas i samma mapp.**

---

END OF INSTRUCTIONS

# SULLIVAN HEMSIDA - KOMPLETT INSTRUKTION FÖR CLAUDE CODE

## 📋 ÖVERSIKT

Skapa en 4-sidig hemsida för Delta Green-karaktären Father Michael Sullivan, Navy Chaplain. Hemsidan ska följa samma struktur som Sparkys hemsida (använd de 4 HTML-filerna som referens) men med:
- Annat färgschema (Military: olivgrön/koppar)
- Annat innehåll (Sullivan-specifikt)
- Tyngre, mer melankolisk ton
- Militär-professionell men med underliggande sorg

---

## 🎨 FÄRGSCHEMA: MILITARY

```css
:root {
    --bg-dark: #0a0f0a;
    --bg-darker: #050805;
    --accent: #b87333;           /* Koppar */
    --accent-dim: #8b5a2b;       /* Mörkare koppar */
    --text: #e0e0e0;
    --text-dim: #a0a0a0;
    --border: #2d3d2d;           /* Olivgrön border */
    --highlight: #3d5a3d;        /* Olivgrön highlight */
}
```

---

## 📁 FILSTRUKTUR

Skapa 4 HTML-filer:

1. **sullivan_karakter.html** - Översikt, attribut, färdigheter
2. **sullivan_pastoral.html** - Navy Chaplain-rollen, cover, chaplain-arbete
3. **sullivan_operativt.html** - Delta Green, operationer, bonds
4. **sullivan_personligt.html** - Trauma, tidslinje, tro-kris

---

## 🎯 GENERELLA DESIGNPRINCIPER

### Typografi
- Huvudfont: `'Georgia', 'Times New Roman', serif` (tyngre, mer formell än Sparkys Segoe UI)
- Monospace för logo: `'Courier New', monospace`
- Line-height: 1.6 (läsbar, luftig)

### Layout
- Samma grid-struktur som Sparky: `280px sidebar | 1fr main content`
- Sticky sidebar (position: sticky, top: 0, height: 100vh)
- Max-width på main content: 1200px
- Padding: 3rem på main content

### Ton
- **Professionell** men med underliggande **melankoli**
- Citat-boxar för Sullivans inre tvivel
- Alert-boxar för varningar och klassificerad info
- Mindre "slick" än Sparky, mer "tung"

---

## 📄 SID 1: SULLIVAN_KARAKTER.HTML

### Sidebar Navigation

```
✝ DELTA GREEN
AGENT FILE: SULLIVAN

⚔ KARAKTÄR
  - Översikt
  - Attribut & Stats
  - Färdigheter

⛪ PASTORAL (länk till sullivan_pastoral.html)

🎯 OPERATIVT (länk till sullivan_operativt.html)

💔 PERSONLIGT (länk till sullivan_personligt.html)
```

### Hero Section
**Bild:** sullivan1.jpeg (porträtt i uniform med chaplain collar)

```
FATHER MICHAEL SULLIVAN
Navy Chaplain | Lieutenant Commander | Quantico Marine Base

"Jag följde order. Gjorde vad som måste göras. 
Men någonstans mellan bönerna och dödssiffrorna 
tappade jag bort vilken röst jag lyssnade på."
```

### Alert Box
```
⚠️ KLASSIFICERAT

Detta dokument innehåller sekretessbelagd information om 
Delta Green-operationer. Endast "Chesapeake" cell-medlemmar 
har tillgång. Vid fara: förstör dokumentation.
```

### Översikt Section

**Rubrik:** ÖVERSIKT

**Text:**
Father Michael Sullivan är Navy Chaplain stationerad vid Quantico Marine Base, Virginia. Officiellt tjänstgör han som andlig vägledare för Marines och deras familjer. Inofficiellt har han varit Delta Green field operative i 5 år.

Efter händelserna i Maine (Operation "Sea Glass", maj 2025) har Sullivan genomgått en djupgående tro-kris. Han utför fortfarande sina plikter som chaplain - varje mässa, varje bön, varje rådgivningssamtal - men orden känns allt mer tomma.

**Quote Box:**
```
"Varje gång jag håller mässan undrar jag: Läser jag Guds ord, 
eller bara gamla ord från döda män? Och varje gång en Marine 
frågar mig om Gud har en plan... ljuger jag och säger ja."
```

### Attribut & Stats Section

**Rubrik:** GRUNDEGENSKAPER

**Tabell:**
| Egenskap | Värde | % | Kommentar |
|----------|-------|---|-----------|
| STR | 11 | 55% | Genomsnittlig fysisk styrka |
| CON | 11 | 55% | Hållbar men inte exceptionell |
| DEX | 10 | 50% | Genomsnittlig smidighet |
| INT | 13 | 65% | Välutbildad, analytisk |
| POW | 16 | 80% | **Stark vilja trots tro-kris** |
| CHA | 14 | 70% | Naturlig ledarskap, empati |

**Total:** 75 poäng

**Härledda Attribut - Tabell:**
| Attribut | Maximum | Aktuell | Formel |
|----------|---------|---------|---------|
| HP | 11 | 11 | (CON + STR) / 2 |
| WP | 16 | 16 | POW |
| SAN | 70 | 58 | POW × 5 |
| Breaking Point | 56 | 47 | SAN - POW |

**Alert Box - SAN History:**
```
⚠️ SANITY STATUS

Starting SAN: 70 (POW × 5)
Current SAN: 58
Total förlust: ~12 poäng
Främst från: Sea Glass (maj 2025), Afghanistan (2020)
Breaking Point: 47 - Under denna nivå börjar adaptation och mental skada

Varje operation tar sin tribut. Varje onaturlig händelse river 
lite mer i tron. Snart finns ingenting kvar att tro på.
```

### Färdigheter Section

**Rubrik:** YRKESFÄRDIGHETER - NAVY CHAPLAIN

**Tabell:**
| Färdighet | % | Beskrivning |
|-----------|---|-------------|
| **Första Hjälpen** | 60% | Grundläggande medicinsk vård i fält |
| **Historia** | 60% | Teologi, kyrkohistoria, militärhistoria |
| **HUMINT** | 70% | Läsa människor, konfidentiella samtal, pastoralt arbete |
| **Latin** | 50% | Kyrkospråk, religiösa texter |
| **Medicin** | 40% | Fördjupad förståelse för trauma och PTSD |
| **Military Science** | 40% | Marines-taktik, organisation, protokoll |
| **Persuade** | 60% | Övertalning, konfliktlösning, rådgivning |
| **Psykoterapi** | 60% | Krisstöd, PTSD-hantering, grief counseling |
| **Religion** | 60% | Katolsk teologi, komparativ religion, ritual |

**Rubrik:** BONUSFÄRDIGHETER

**Tabell:**
| Färdighet | % | Beskrivning |
|-----------|---|-------------|
| **Byråkrati** | 60% | Navy-system, Delta Green compartmentalization |
| **Alertness** | 60% | Uppmärksamhet, känsla för fara |
| **Skjutvapen** | 60% | Jaktvapen främst, avskyr pistoler |
| **Computer Science** | 50% | Grundläggande digital kompetens |

**Quote Box:**
```
"Jag lärde mig skjuta för att jaga med pappa. Sedan blev det 
för att döda. Nu vet jag inte längre skillnaden."
```

### Operativ Roll Section

**Alert Box - Success:**
```
💡 OPERATIV ROLL I CHESAPEAKE CELL

Specialitet: The Chaplain / Mediator / Face
Styrkor: HUMINT, konfliktlösning, läsa människor, medicinskt stöd
Svagheter: Tro-kris undergräver auktoritet, emotionell börda
Preferens: Diplomatisk lösning först, våld som sista utväg

Efter Sea Glass: Fungerar professionellt men känslomässigt frakturerad.
De facto cell leader efter Mac's forced leave.
```

---

## 📄 SID 2: SULLIVAN_PASTORAL.HTML

### Hero Section
**Bild:** sullivan7.png (mess hall med kaffe och tidning - vardaglig military life)

```
NAVY CHAPLAIN CORPS
"Tillhandahålla och facilitera religiös vägledning för Navy och Marine Corps personal"

Lieutenant Commander Michael Sullivan
Quantico Marine Base, Virginia
```

### Navy Chaplain Section

**Rubrik:** DAGLIGA UPPGIFTER

**Text:**
Sullivan är Navy Chaplain som tjänstgör med Marines. Marines har inte egna chaplains - de använder Navy Chaplain Corps. Han bär Navy-uniform med Marines-insignia.

**Primära Uppgifter (Grid - 2 kolumner):**

**Kolumn 1:**
**Gudstjänster & Religiöst**
- Katolsk mässa 2x/vecka
- Ekumeniska tjänster
- Särskilda ceremonier
- Bröllop och begravningar

**Rådgivning (24/7)**
- Konfidentiella samtal
- Familjeproblem, PTSD
- Krisstöd, grief counseling
- Moraliska dilemman

**Kolumn 2:**
**Sjukhusbesök**
- Walter Reed wounded warriors
- Sista smörjelsen
- Stödja familjer vid dödsfall

**CACO Support**
- Casualty Assistance
- Informera familjer vid dödsfall
- Begravningar och memorial services

**Quote Box:**
```
"De kallar mig Father. De kommer till mig med sina synder, 
sina rädslor, sina döende kompisar. De tror jag har svar. 
Jag har inga svar. Men jag kan inte säga det."
```

### Cover för Delta Green Section

**Rubrik:** PERFEKT COVER

**Bild:** sullivan5.png (sittande ensam, tänker - tung stämning)

**Text:**
Chaplain-rollen är nästan för bra som Delta Green-cover. Den kombinerar:

**Alert Box - Success:**
```
✅ OPERATIONELL FLEXIBILITET

Leave: 20+ dagar kvar (30/år standard)
"Pastoral Care" excuse: Kan försvinna i veckor för att "hjälpa före detta serviceman"
Konfidentialitet: Ingen kan tvinga detaljer, inte ens CO
"Retreat" excuse: 1-2 veckor borta på spiritual retreat = helt normalt
Military Respect: Chaplains ifrågasätts aldrig

Perfect deniability. Perfect mobility. Perfect isolation.
```

**Men:**

**Alert Box - Warning:**
```
⚠️ DEN INRE KOSTNADEN

Varje "pastoral care"-lögn äter på hans själ.
Varje DG-operation använder hans präst-status som cover.
Varje gång han säger "jag hjälper någon" när han dödar något onaturligt.

Mest praktisk frihet av alla tre agenter.
Minst inre frid av alla tre agenter.
```

### Exempel Dialog Section

**Rubrik:** COVER I PRAKTIKEN

**Text med formatting:**

**Till Jimmy Walsh (hans CO):**
```
"Jimmy, jag har lovat en före detta serviceman pastoral support. 
Han bad specifikt om mig. Jag behöver ta 2-3 veckor."

"Självklart, Father. Ta den tid du behöver."

Ingen kan fråga:
- Vem är personen? (KONFIDENTIALITET)
- Var är han? (Pastoral care = anywhere)
- Vad gör ni? (Mellan präst och person)
```

**Vid längre operation:**
```
Sullivan ringer: "Jimmy, situationen är mer komplex än jag trodde. 
Personen jag hjälper har djupare problem. Jag behöver 2 veckor till."

"Michael... du låter utmattad. Är du säker?"

"Jag är okej. Denna person behöver mig. Jag kan inte ge upp på honom."

*Ironin: Det är sant. Men "personen" är ofta något onaturligt 
som måste stoppas, inte räddas.*
```

### Schema Section

**Rubrik:** TYPISK VECKA

**Tabell:**
| Tid | Måndag-Fredag |
|-----|---------------|
| 08:00 | Ankomst, emails, morning prayers |
| 09:00-12:00 | Rådgivningsmöten (2-3 schemalagda) |
| 12:00 | Lunch i dining facility med Marines |
| 13:00-15:00 | Administrativt, fler möten |
| 15:00-17:00 | PT (Physical Training) med unit |
| 17:00+ | "Officiellt slut" - men kan kallas 24/7 |

| Dag | Helg |
|-----|------|
| Lördag | Oftast ledig (om ingen bröllop/begravning) |
| Söndag | Mässor 08:00, 10:00, 13:00 |

**Text:**
Men flexibelt schema - om ingen bokat möte kan han göra annat. Ingen micromanagar en chaplain.

---

## 📄 SID 3: SULLIVAN_OPERATIVT.HTML

### Hero Section
**Bild:** sullivan2.jpeg (dramatic shot med stola, kaos i bakgrunden)

```
DELTA GREEN OPERATIVE
Chesapeake Cell | Field Agent | 5 Years Service

"Någon måste stå mellan dem och mörkret. 
Även om Gud inte gör det."
```

### Delta Green Rekrytering Section

**Rubrik:** REKRYTERING: AFGHANISTAN 2020

**Bild:** sullivan6.png (helping wounded - pastoral work i krigszon)

**Text:**
**Platsen:** Forward Operating Base, Helmand Province, Afghanistan  
**Datum:** September 2020  
**Ålder:** 41 år

Sullivan var Navy Chaplain tilldelad en Marines-enhet. En ung Marine - Corporal Ryan Miller - började uppvisa märkligt beteende. Pratade om "röster från väggen", skrev bakåt i sin dagbok, såg saker som inte fanns där.

Officerarna trodde det var PTSD eller heatstroke. Sullivan insåg det var något annat.

**Quote Box:**
```
"Jag försökte exorcism. Latin, heligt vatten, böner jag lärt mig 
i seminariet. Ingenting fungerade. Rösten fortsatte. Miller blev värre. 
Sedan en natt... något svarade tillbaka. På Latin. Men... baklänges."
```

**Vad hände:**
Sullivan och Doc Torres (combat medic, nu Bond #2) försökte rädda Miller. De misslyckades. Miller dog - men inte av naturliga orsaker.

Efteråt kontaktades Sullivan av en "consultant" från Defense Intelligence. Mannen visste exakt vad som hänt. Han erbjöd Sullivan en möjlighet att "göra något åt sånt här".

Sullivan sa ja. Inte för Gud. För plikt.

### Operationer Section

**Rubrik:** DELTA GREEN OPERATIONER (2020-2025)

**Text:**
Sullivan har deltagit i 8-10 Delta Green-operationer sedan 2020:

**Grid - 3 kolumner med operation-cards:**

**Operation "The Mall Before Christmas" (Dec 2024)**
- Första operation med Mac & Sparky
- Kristallkub, Dmitri Volkov
- 4 SAN-förlust
- Mac's besatthet började här

**Operation "Sea Glass" (Maj 2025)**
- Maine research facility
- Kristaller som transformerade människor
- THE BREAKING POINT
- 6 SAN-förlust
- Tro-krisen kulminerade

**5+ tidigare operationer (2020-2024)**
- Mix av false flags och genuina hot
- Gradvis erosion av tron
- Lärde sig Delta Green-metoder
- Träffade Mac oktober 2024

**Alert Box - Danger:**
```
⚠️ EFTER SEA GLASS

Current Status: Funktionell men frakturerad
Breaking Point: Nådd under Sea Glass
Tro: Borta eller vilande - han vet inte vilket
Roll i cell: De facto leader efter Mac's forced leave

Han fortsätter inte för tro. Han fortsätter för att någon måste.
Och om han slutar nu var allt meningslöst.
```

### Bonds Section

**Rubrik:** BONDS - FÖRBINDELSER SOM HÅLLER HONOM KVAR

**Tre stora Cards:**

**BOND 1: KATIE SULLIVAN**
**Värde:** 12  
**Relation:** Yngre syster, nunna/social worker, Boston

**Bakgrund:**
Katie blev nunna år efter Sullivan blev präst. De delar samma kallelse - hjälpa människor. Men Katie vet inte om Delta Green.

**Nuvarande status:**
Katie känner att något är fel. Michael ringer sällan. När de pratar låter han tom. Hon har frågat: "Michael, pratar du fortfarande med Gud?" Han ljög: "Varje dag."

**Citat:**
```
Katie: "Du låter så trött, Mike. Tar de hand om dig i Marines?"
Sullivan: "De gör sitt bästa."
Katie: "Pratar du med Gud? Ber du?"
Sullivan: [paus] "Varje dag, Katie."
*Lögnen brände i halsen.*
```

---

**BOND 2: DR. DAVID "DOC" TORRES**
**Värde:** 10  
**Relation:** Combat medic, Afghanistan-överlevare, PTSD

**Bakgrund:**
Doc Torres var combat medic som hjälpte Sullivan försöka rädda Corporal Miller i Afghanistan 2020. De såg samma onaturliga sak. Båda överlevde.

**Nuvarande status:**
Doc är hemma i San Antonio. Får terapi för PTSD men vet att det inte var normal PTSD. Sullivan ringer varannan månad - checkup, stöd. Doc är den enda utanför Delta Green som vet vad Sullivan såg.

**Hur denna bond kan skadas:**
- Doc frågar för mycket om vad Sullivan gör nu
- Doc blir själv måltavla för något onaturligt
- Sullivan måste välja mellan mission och att skydda Doc

---

**BOND 3: LT. COMMANDER JAMES "JIMMY" WALSH**
**Värde:** 14 (högsta)  
**Relation:** Senior Chaplain, mentor, Quantico

**Bakgrund:**
Jimmy Walsh (58) är Sullivans boss och mentor. Tjänstgjorde i Vietnam, blev chaplain, sett helvetet. Sullivan ser Jimmy som ersättning för Fader Brennan.

**Varför denna bond är viktig:**
Jimmy representerar "normala" livet - en chaplain med fast tro som genuint tror han gör skillnad. Varje gång Sullivan ser Jimmy påminns han om vem han var.

**Efter Sea Glass:**
Jimmy märkte något var fel. Beordrade Sullivan på retreat. Sullivan gick (måste), kom tillbaka lika tom. Jimmy oroar sig men respekterar gränser.

**Alert Box - Heart:**
```
💔 DEN VIKTIGASTE BONDEN

14 poäng - högst av Sullivans bonds.
Jimmy representerar inte bara en person, utan en hel livsstil, 
en identitet. Om Sullivan förlorar Jimmy förlorar han sin 
sista koppling till vem han var.

Men varje gång han ljuger för Jimmy om var han varit, 
varje "pastoral care" som egentligen var Delta Green...
det äter på bonden. Långsamt. Obönhörligt.
```

---

## 📄 SID 4: SULLIVAN_PERSONLIGT.HTML

### Hero Section
**Bild:** sullivan3.png (sitter vid eld, håller rosenkrans - ensam, contemplativ)

```
MINNENAS TYNGD
"Varje bön känns som en lögn. Varje predikan, ihåliga ord. 
Men jag fortsätter. För om jag slutar... vad var det hela för?"
```

### Tidslinje Section

**Rubrik:** LIVET SOM FORMADE HONOM

**Tidslinje med år och händelser:**

**1979 - FÖDD**
South Boston, Massachusetts. Irländsk-katolsk arbetarfamilj.

**1993 (14 år) - THE DROWNING**
Bror Patrick (16) drunknar framför Michaels ögon. Båtolycka, Boston Harbor.
Michael överlever 4 timmar i kallt vatten. Räddas av Fader Brennan "på en känsla".
*Första skulden: Varför överlevde jag och inte Patrick?*

**2001 (22 år) - FAR DÖR**
Thomas Sullivan dör i arbetsplatsolycka.
Michael tar examen från Boston College samma månad.

**2002 (23 år) - ORDINERAD**
Blir katolsk präst. Fader Brennan mentor.
Tjänar vid St. Augustine's, Boston.

**2006 (27 år) - THE SCANDAL**
Father Marcus O'Brien (kollega) anklagas för sexuellt missbruk av minderåriga.
Sullivan försvarade honom offentligt. "En god man. Offer ljuger."
Sedan kom bevisen. Allt var sant.
*Andra skulden: Jag försvarade en predator. Mina ord skadade offer.*

**2006 - FLYKTEN**
Ansöker till Navy Chaplain Corps. Lämnar Boston.

**2007-2020 - MILITARY SERVICE**
Multiple deployments. Afghanistan 2011-2013, 2019-2020.
Ser krig. Ser död. Tron börjar spricka.

**2020 (41 år) - AFGHANISTAN - THE EXORCISM**
Corporal Miller. Det onaturliga. Exorcism fungerar inte.
Delta Green rekryterar honom.
*Tredje skulden: Om exorcism inte fungerar, vad är jag då?*

**2024 DEC - THE MALL BEFORE CHRISTMAS**
Första operation med Mac & Sparky. Dmitri Volkov. Kristallkuben.
Började se att det onaturliga är större än han trodde.

**2025 MAJ - SEA GLASS**
Maine. Kristaller. Människor transformerade. Kunde inte rädda dem.
Måste döda dem istället.
*Fjärde skulden: Jesus gav aldrig upp på någon. Jag gav upp på alla.*

**2025 SEPT - NU**
Quantico. De facto cell leader. Fungerar professionellt.
Inuti: Tom. Tvivlande. Söker svar som inte kommer.

### Tro-kris Section

**Rubrik:** NÄR BÖNER INTE RÄCKER

**Bild:** sullivan4.png (typing på gammal skrivmaskin, whiskey - mörkt rum)

**Text:**
Efter Sea Glass kan Sullivan inte längre be utan att känna tomhet. Han utför ritualer mekaniskt:

**Quote Box:**
```
"In nomine Patris, et Filii, et Spiritus Sancti..."

Orden kommer automatiskt. Händerna gör korset. 
Men hjärtat? Hjärtat känner ingenting.

Är det här vad det betyder att förlora tron? 
Att orden fortsätter men meningen är borta?
```

**Alert Box - Danger:**
```
⚠️ DEN CENTRALA FRÅGAN

Om exorcism inte fungerar - finns då demoner?
Om demoner inte finns - vad är då det onaturliga?
Om det onaturliga existerar - var är Gud?

Om Gud finns men inte ingriper - är Han värd att tillbe?
Om Gud inte finns - vad är jag då? En präst utan tro?
En soldat för ingenting?
```

### Hemlighe Section

**Rubrik:** VAD INGEN VET

**Text:**
Sullivan tror inte längre på Gud. Inte sedan Sea Glass. Kanske inte sedan Afghanistan.

Han utför fortfarande alla sina plikter som chaplain. Varje mässa, varje rådgivningssamtal, varje bön. Men orden är ihåliga.

**Card - Dark:**
```
HAN ÄR RÄDD

Om han erkänner detta - för sig själv, för andra - 
kommer allt han gjort vara meningslöst.

Alla val han gjort.
Alla han inte kunde rädda.
Alla offer Delta Green krävt.

Så han fortsätter. Låtsas. Söker. 
Hoppas att tron kommer tillbaka.

Men varje dag blir det svårare att komma ihåg 
vad tro kändes som.
```

---

### Bibelcitat Section

**Rubrik:** ORDEN HAN LÄSER - CITAT FÖR SULLIVAN

**Text:**
Sullivan har läst Bibeln i tjugo år. Som präst kan han citera den ur minnet. Men efter Sea Glass har vissa citat börjat betyda något annat. Här är citat han återkommer till - i bön, i tvivel, i mörker.

**Kategori 1: LIDANDE & TVIVEL**

```
"Må den dag förgås då jag blev född, och den natt då det sades: 
'En gosse har blivit avlad.'"
— Job 3:3

"Hur länge, HERRE? Skall du för alltid glömma mig? 
Hur länge skall du dölja ditt ansikte för mig?"
— Psaltaren 13:2

"Min Gud, min Gud, varför har du övergivit mig?"
— Psaltaren 22:2 / Matteus 27:46

"Hur länge skall jag bära oro i min själ och sorg i mitt hjärta 
hela dagen?"
— Psaltaren 13:3

"Jag trodde och därför talade jag, fast jag var djupt förnedrad."
— Psaltaren 116:10
```

**Sullivan's anteckning:** *Det här är Job efter att han förlorat allt. Det här är Jesus på korset. Om även de tvivlade... får då jag?*

---

**Kategori 2: MÖRKRET & MYSTERIET**

```
"Jorden var öde och tom, och mörker var över djupet, 
och Guds Ande svävade över vattnet."
— 1 Mosebok 1:2

"Djupet ropar till djupet vid dånet av dina vattenfall; 
alla dina böljor och vågor har gått över mig."
— Psaltaren 42:8

"Jag går ned till dödsrikets portar. Skall jag berövas 
återstoden av mina år?"
— Jesaja 38:10

"Mörker blir ljus omkring mig, och natten blir klar som dagen. 
Ja, mörker är inte mörker för dig."
— Psaltaren 139:12

"Och ljuset lyser i mörkret, och mörkret har inte övervunnit det."
— Johannes 1:5
```

**Sullivan's anteckning:** *Mörker över djupet. Det är vad jag sett. Men var är Guds Ande nu? Svävar Han fortfarande där? Eller har Han lämnat oss?*

---

**Kategori 3: HAVET & DJUPET**

```
"Du som betvingar havets vågor och stillar dess brusande böljor."
— Psaltaren 65:8

"Han förvandlade stormen till stillhet, så att vågorna tystnade."
— Psaltaren 107:29

"HERREN härskade över vattenflodens svall, ja, HERREN härskar 
som konung för evigt."
— Psaltaren 29:10

"När du går genom vatten skall jag vara med dig, och genom 
strömmar skall de inte dränka dig."
— Jesaja 43:2

"Ur djupet ropar jag till dig, HERRE. Herre, hör min röst!"
— Psaltaren 130:1-2

"Vem sätter gräns för havet, som det inte får överskrida, 
och bestämmer att det inte får täcka jorden?"
— Job 38:8-11
```

**Sullivan's anteckning:** *Patrick drunknade. Jag klarade mig. Varför? Vad finns där nere i djupet? Guds svar - eller bara tystnad?*

---

**Kategori 4: PLIKT & OFFER**

```
"Större kärlek har ingen än den som ger sitt liv för sina vänner."
— Johannes 15:13

"Inte som jag vill, utan som du vill."
— Matteus 26:39

"Om någon vill komma efter mig, måste han förneka sig själv 
och ta sitt kors på sig och följa mig."
— Matteus 16:24

"Gå in genom den trånga porten. Ty bred är porten och vid är 
vägen som leder till fördärvet."
— Matteus 7:13

"Jag sänder er ut som får mitt ibland ulvar. Var därför kloka 
som ormar och oförvitliga som duvor."
— Matteus 10:16
```

**Sullivan's anteckning:** *Vi offrar. Vi dör. Men för vad? Om Kristus dog för syndare, vem dör då för dem som möter det onaturliga?*

---

**Kategori 5: SÖKANDE TROTS TVIVEL**

```
"Sök HERREN medan han låter sig finnas, åkalla honom medan han 
är nära."
— Jesaja 55:6

"Jag tror. Hjälp min otro!"
— Markus 9:24

"Be, så skall ni få. Sök, så skall ni finna. Bulta, 
och det skall öppnas för er."
— Matteus 7:7

"Saliga är de som inte har sett och ändå tror."
— Johannes 20:29

"Vi vandrar i tro och inte i åskådande."
— 2 Korintierbrevet 5:7

"HERRE, jag hoppas på dig. Du skall svara, Herre, min Gud."
— Psaltaren 38:16
```

**Sullivan's anteckning:** *"Jag tror. Hjälp min otro." Det är allt jag har kvar. Tre ord. Är det nog?*

---

**Kategori 6: NÄR ORDEN INTE RÄCKER**

```
"Anden hjälper oss i vår svaghet. Vi vet inte hur vi skall be. 
Men Anden själv går i förbön för oss med outsägliga suckar."
— Romarbrevet 8:26

"Var stilla och känn att jag är Gud."
— Psaltaren 46:11

"Ty mina tankar är inte era tankar, och era vägar är inte mina vägar, 
säger HERREN."
— Jesaja 55:8

"Vi ser nu en gåtfull spegelbild, men då skall vi se ansikte mot ansikte."
— 1 Korintierbrevet 13:12

"Allt har sin tid, och var sak under himmelen har sin stund."
— Predikaren 3:1
```

**Sullivan's anteckning:** *Kanske är tystnad också ett svar. Men vilket svar?*

---

**LATIN-CITAT (för mässor och ritualer)**

Sullivan citerar ofta på latin - dels för att det är kyrkospråk, dels för att det skapar distans från orden när de känns för tunga på svenska.

```
"De profundis clamavi ad te, Domine."
(Ur djupet ropar jag till dig, Herre.)
— Psaltaren 130:1

"Kyrie eleison, Christe eleison."
(Herre förbarma dig, Kristus förbarma dig.)
— Liturgisk text

"In manus tuas commendo spiritum meum."
(I dina händer överlämnar jag min ande.)
— Lukas 23:46

"Pater noster, qui es in caelis..."
(Fader vår som är i himmelen...)
— Matteus 6:9

"Agnus Dei, qui tollis peccata mundi, miserere nobis."
(Guds lamm som borttager världens synd, förbarma dig över oss.)
— Liturgisk text

"Requiem aeternam dona eis, Domine."
(Evig vila giv dem, o Herre.)
— Mässa för de döda
```

**Sullivan's anteckning:** *På latin känns orden mindre personliga. Mindre som lögner. Bara... formelord från en död kyrka.*

---

### Praktiska Tips för Andreas

**När Sullivan citerar Bibeln i spel:**

1. **Under stress:** Kortare citat, ofta latin ("De profundis...")
2. **Vid rådgivning:** Tröstande citat (Johannes 15:13, Jesaja 43:2)
3. **I tvivel (ensam):** Job, Psaltaren 13, Markus 9:24
4. **Vid begravningar:** Psaltaren 23, Johannes 11:25-26, Requiem på latin
5. **Efter operation:** Mörka citat (Job 3:3, Psaltaren 22:2)

**Citat som passar olika situationer:**

- **Någon frågade om Guds plan:** "Mina tankar är inte era tankar..." (Jesaja 55:8)
- **När teamet ifrågasätter uppdraget:** "Gå in genom den trånga porten..." (Matteus 7:13)
- **Efter förlust:** "Du går igenom vatten... de ska inte dränka dig" (Jesaja 43:2)
- **Vid havet/vatten:** "Djupet ropar till djupet..." (Psaltaren 42:8)
- **När han inte kan be:** "Anden går i förbön med outsägliga suckar" (Romarbrevet 8:26)

---

### Karaktärscitat Section

**Rubrik:** I HANS EGNA ORD

**Quote Boxes - flera:**

```
"Jag sa till henne att Gud sänt mig. Jag ljög. 
Eller... Gud SKICKADE mig, och jag misslyckades. 
Jag vet inte vilket som är värre."
```

```
"Jag följde order. Gjorde vad som måste göras. 
Goda män dog. Oskyldiga dog. 
Och jag är fortfarande här. Ljuger fortfarande."
```

```
"Jimmy frågar om jag ber. Jag säger ja. 
Katie frågar om jag fortfarande tror. Jag säger ja.
Mac frågar om jag mår bra. Jag säger ja.

Tre människor jag älskar. Tre lögner."
```

```
"Kanske är det här helvetet. 
Inte eld och demoner. 
Bara... att gå genom rörelserna för evigt, 
och veta att det inte betyder något."
```

### Fotogalleri Section

**Rubrik:** BETWEEN DUTY AND DESPAIR

**Image Gallery Grid (3 kolumner):**

**Bild:** sullivan1.jpeg  
**Caption:** Official Portrait - Quantico, 2025

**Bild:** sullivan2.jpeg  
**Caption:** After the Operation - Identity Unknown

**Bild:** sullivan5.png  
**Caption:** Alone with His Thoughts

**Bild:** sullivan8.png  
**Caption:** Mess Hall - Morning Routine

**Bild:** sullivan9.png  
**Caption:** The Mask He Wears - Kitchen Duty

**Bild:** sullivan6.png  
**Caption:** Pastoral Care in Action

---

## 🔧 TEKNISKA DETALJER

### Responsive Design
- Samma breakpoints som Sparky
- Mobile: Stack sidebar ovanpå main content
- Tablet: Behåll grid men mindre padding

### JavaScript
- Smooth scroll för nav-länkar
- Active section highlighting i sidebar
- Collapse-funktionalitet för bondsbeskrivningar om du vill

### Image Optimization
- Alla bilder ska vara <500KB om möjligt
- Use modern formats (webp fallback till jpg/png)
- Lazy loading för bilder under fold

### SEO & Accessibility
- Semantic HTML (nav, main, section, article)
- Alt-text på alla bilder
- ARIA labels där det behövs
- Proper heading hierarchy (h1 -> h2 -> h3)

---

## 📝 CONTENT SOURCING

Allt innehåll finns i projektet:
- `Sullivan_Bakgrund_Tidslinje.md`
- `Sullivan_Navy_Chaplain_Guide.md`
- `Sullivan_Bonds.md`
- `Sullivan_Stats_Skills.md`
- `Sullivan_Delta_Green_Sektion.md`

Använd dessa dokument för att fylla i detaljer jag inte specificerat exakt.

---

## ✅ CHECKLISTA FÖR CLAUDE CODE

När du är klar, kontrollera:

- [ ] 4 HTML-filer skapade
- [ ] Alla 9 bilder inkluderade
- [ ] Färgschema konsekvent (olivgrön/koppar)
- [ ] Navigation fungerar mellan sidor
- [ ] Responsive design funkar
- [ ] Citat-boxar har rätt styling (italic, border-left)
- [ ] Alert-boxar har rätt ikoner (⚠️, ✅, 💔, etc)
- [ ] Tabeller är läsbara och stilade
- [ ] Tonen är tyngre/mer melankolisk än Sparky
- [ ] Hero-bilder är rätt placerade
- [ ] Gallery grid fungerar

---

## 🎯 SLUTORD

Detta är en karaktär som bär tung börda. Webbplatsen ska reflektera det:
- Mörka färger men inte deprimerande
- Professionell men inte kall
- Militär men med mänsklighet
- Religiös men bruten

Han är inte "cool" som Sparky. Han är tyngd. Utmattad. Men fortfarande där.
Fortfarande tjänstgörande. Fortfarande sökande.

**"Någon måste stå mellan dem och mörkret. Även om Gud inte gör det."**

Lycka till, Claude Code. Skapa något värdigt Father Sullivan.

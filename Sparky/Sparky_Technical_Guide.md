# KAI "SPARKY" ZHANG - TEKNISK OPERATIONS MANUAL

## ðŸŽ¯ Ã–VERSIKT

**Ã…lder:** 30  
**Bakgrund:** Tidigare Anonymous-hacktivist, NSA Technical Analyst (2019-), Delta Green (2020-)  
**Clearance:** Top Secret / SCI (Sensitive Compartmented Information)  
**Specialisering:** SIGINT, Offensive Cyber Operations, Electronic Warfare

**Detta dokument beskriver dina tekniska kapaciteter och begrÃ¤nsningar.**

---

## ðŸ”§ TEKNISKA KAPACITETER

### **DATAVETENSKAP: 80%**

#### **NÃ¤tverksintrÃ¥ng (Network Penetration)**

**FÃ¶retagsnÃ¤tverk / Hotell / Skolor:**
- **Metod 1 - WiFi IntrÃ¥ng:**
  - Koppla till WiFi (Ã¤ven krypterad med WPA2)
  - KÃ¶r WiFi-handshake capture (2-5 minuter)
  - Dictionary attack eller brute-force (10 min - 2 timmar beroende pÃ¥ lÃ¶senordsstyrka)
  - Alternativt: Evil Twin attack (fake access point som loopar anvÃ¤ndare, fÃ¥r lÃ¶senord direkt)
  
- **Metod 2 - Phishing:**
  - Skicka fake email som ser ut att komma frÃ¥n IT
  - "Klicka hÃ¤r fÃ¶r att uppdatera ditt lÃ¶senord"
  - NÃ¤r offret klickar: steal credentials eller installera malware
  - Tidsfaktor: 30 min att sÃ¤tta upp, sedan vÃ¤nta pÃ¥ att nÃ¥gon klickar (1-24 timmar)

- **Metod 3 - Physical Access:**
  - FÃ¥ tag pÃ¥ dator som Ã¤r inloggad
  - USB med BadUSB-attack (ser ut som USB-minne, agerar som tangentbord)
  - Injicerar kod pÃ¥ 10 sekunder som ger dig remote access
  - Datorn behÃ¶ver inte ens vara upplÃ¥st om du anvÃ¤nder vissa exploits

**Resultat:** Full tillgÃ¥ng till intranÃ¤t, filer, kameror, emails

**Tidsfaktor:** 
- WiFi-hack: 15 minuter - 2 timmar
- Phishing campaign: Setup 30 min, vÃ¤nta pÃ¥ klick
- Physical USB: 10 sekunder - 5 minuter

#### **Kryptering - Vad gÃ¥r att knÃ¤cka?**

**LÃ„TT (minuter-timmar):**
- Basic encryption (ZIP-lÃ¶senord, gamla PDF-locks)
- WEP WiFi-kryptering (fÃ¶rÃ¥ldrad)
- Svaga RSA-nycklar (under 1024-bit)
- Standard database encryption utan salt

**MEDIUM (timmar-dagar):**
- WPA2 WiFi med svagt lÃ¶senord (dictionary attack)
- SSL/TLS med kÃ¤nda sÃ¥rbarheter (Heartbleed, POODLE)
- PGP med korta nycklar
- BitLocker med kort PIN

**SVÃ…RT (dagar-veckor):**
- WPA3 WiFi med starkt lÃ¶senord
- Modern AES-256 utan kÃ¤nda sÃ¥rbarheter
- MilitÃ¤r-grade kryptering
- Custom-byggd kryptering (vet inte protokollet)

**PRAKTISKT OMÃ–JLIGT:**
- Moderna post-quantum krypteringsalgoritmer
- Perfect forward secrecy med lÃ¥nga nycklar
- One-time pads korrekt implementerade
- Kryptering dÃ¤r nyckeln Ã¤r pÃ¥ air-gapped system

**NSA-fÃ¶rdel:** Du har access till zero-day exploits som kan kringgÃ¥ viss kryptering genom implementation-fel snarare Ã¤n att knÃ¤cka sjÃ¤lva matematiken.

#### **Malware & Remote Access**

**Du kan skapa:**

**Keyloggers:**
- Registrerar allt offret skriver
- Skickar data till dig var 10:e minut
- Byggs pÃ¥: 20-40 minuter
- SvÃ¥righet att upptÃ¤cka: Medium (standard antivirus hittar det inte)

**RAT (Remote Access Trojan):**
- Full kontroll Ã¶ver datorns kamera, mikrofon, skÃ¤rm, filer
- Kan kÃ¶ra kommandon, installera mer malware
- Byggs pÃ¥: 1-2 timmar fÃ¶r custom version
- Kan anvÃ¤nda NSA:s fÃ¤rdiga verktyg: 10 minuter att modifiera fÃ¶r mÃ¥let

**Backdoors:**
- Dold ingÃ¥ng till system som Ã¶verlever ominstallationer
- Planteras i: BIOS/UEFI, nÃ¤tverkskort firmware, eller systemfiler
- Installation: KrÃ¤ver admin-access, tar 30-60 minuter
- Varaktighet: Kan finnas kvar i Ã¥ratal

**Ransomware (ej rekommenderat fÃ¶r DG-operationer):**
- Krypterar alla filer pÃ¥ dator
- KrÃ¤ver betalning fÃ¶r dekrypteringsnyckel
- AnvÃ¤nds frÃ¤mst fÃ¶r att sabotera, inte fÃ¶r faktisk utpressning

#### **Reverse Engineering**

**NÃ¤r du hittar okÃ¤nd kod/program:**

**Statisk analys:**
- LÃ¤ser koden utan att kÃ¶ra den
- AnvÃ¤nder tools: IDA Pro, Ghidra, Binary Ninja
- Kan se vad koden GÃ–R, vilka funktioner den anropar
- Tidsfaktor: 1-4 timmar fÃ¶r medium-komplext program

**Dynamisk analys:**
- KÃ¶r programmet i isolerad miljÃ¶ (sandbox)
- Ser vad det faktiskt fÃ¶rsÃ¶ker gÃ¶ra (kontakta servrar, modifiera filer, etc.)
- Tidsfaktor: 30 minuter - 2 timmar

**Full reverse engineering:**
- Ã…terskapa source code frÃ¥n kompilerat program
- FÃ¶rstÃ¥ EXAKT vad varje del gÃ¶r
- Tidsfaktor: Dagar till veckor fÃ¶r komplex software

**Praktiskt exempel:**
"Du hittar en USB-sticka i mÃ¥lets hotellrum. Du vill veta vad som finns pÃ¥ den."
- Steg 1: Koppla INTE in den i din laptop direkt (kan innehÃ¥lla malware)
- Steg 2: AnvÃ¤nd isolerad air-gapped maskin eller virtual machine
- Steg 3: Forensic imaging fÃ¶rst (skapa exakt kopia)
- Steg 4: Skanna fÃ¶r malware (20 minuter)
- Steg 5: Analysera filer (30 min - 3 timmar beroende pÃ¥ innehÃ¥ll)

#### **Databaser & SQL Injection**

**De flesta webbplatser anvÃ¤nder databaser. Du kan:**

**SQL Injection:**
- Exploitera dÃ¥ligt byggda web forms
- Input: `' OR '1'='1` i login-ruta
- Resultat: Kan logga in utan lÃ¶senord, eller dumpa hela databasen
- Tidsfaktor: 5-30 minuter att hitta sÃ¥rbarhet, 10 minuter att extrahera data

**Database Dumps:**
- NÃ¤r du vÃ¤l Ã¤r inne i systemet, ladda ner hela databasen
- InnehÃ¥ller: AnvÃ¤ndarnamn, lÃ¶senord (ofta hashade), emails, personuppgifter
- Tidsfaktor: 5-20 minuter beroende pÃ¥ storlek

**Exempel:**
"Hotellkedja anvÃ¤nder gamla booking-system"
- Hittar SQL-injection i deras 'search guest' funktion
- Dumpar hela gÃ¤stdatabasen (200,000 gÃ¤ster)
- Kan nu sÃ¶ka pÃ¥ namn, datum, rumsnummer
- Total tid: 45 minuter

### **SIGINT (Signals Intelligence): 70%**

#### **NSA-verktyg du har access till:**

**XKEYSCORE - "Google fÃ¶r NSA"**
- SÃ¶kmotor som indexerar ALLT internet-trafik NSA samlar
- Kan sÃ¶ka pÃ¥: Email-adresser, telefonnummer, IP-adresser, sprÃ¥k, landkoder, nyckelord
- TÃ¤ckning: USA, Europa, Australien (mycket bra), MellanÃ¶stern/Asien (bra), Ryssland/Kina (begrÃ¤nsat)
- Exempel-sÃ¶kning: "Alla emails frÃ¥n target.email@[domain] senaste 30 dagarna"
- Svarstid: 2-10 minuter beroende pÃ¥ omfattning

**Vad du fÃ¥r:**
- FullstÃ¤ndiga emails (subject, body, attachments)
- Metadata (nÃ¤r skickat, frÃ¥n vilken IP, till vem)
- Tidigare sÃ¶kning

ar samma person gjort online
- Webbsidor de besÃ¶kt
- Chat-konversationer (Facebook Messenger, WhatsApp metadata)

**PRISM - Direktaccess till tech-fÃ¶retag**
- Samarbete med: Google, Facebook, Apple, Microsoft, Yahoo, Skype, YouTube
- Ger tillgÃ¥ng till: Gmail, Google Drive, Facebook messages, iCloud backups
- Juridisk tÃ¤ckning: FISA Court warrant (NSA har standing warrants)
- Svarstid: NÃ¤stan realtid fÃ¶r aktiv Ã¶vervakning, 1-2 timmar fÃ¶r historisk data-dump

**Exempel:**
"Jag behÃ¶ver allt personen har i sin Gmail"
- Steg 1: BegÃ¤r PRISM-access fÃ¶r target email
- Steg 2: FÃ¥r alla emails, Ã¤ven raderade frÃ¥n senaste 2 Ã¥ren
- Steg 3: FÃ¥r Ã¤ven Drive-filer, Calendar-events, YouTube-historik
- Total tid: 30 minuter att fÃ¥ godkÃ¤nnande, 10 minuter att dumpa data

**UPSTREAM Collection - Fiberoptisk avlyssning**
- NSA har direktaccess till internet backbone-kablar
- Samarbetar med: AT&T, Verizon, Level 3, andra ISPs
- Ser: ALL trafik som passerar dessa kablar
- Omfattning: ~75% av amerikansk internet-trafik
- BegrÃ¤nsning: Kan inte se krypterad innehÃ¥ll (HTTPS), bara metadata

**Metadata Ã¤r mer vÃ¤rdefullt Ã¤n folk tror:**
- Vem pratade med vem, nÃ¤r, hur lÃ¤nge
- FrÃ¥n vilken plats (IP-adress geolokalisering)
- Vilken enhet (telefon vs laptop, OS-version)
- MÃ¶nster: "Varje tisdag kl 14:00 ringer han samma nummer"

#### **TelefonspÃ¥rning & Ã–vervakning**

**Cell Tower Triangulation:**
- Alla telefoner pingar nÃ¤rmaste sÃ¤ndarmast
- Med 3 master kan du triangulera position till ~50-200 meter
- Fungerar Ã¤ven nÃ¤r telefonen Ã¤r i standby (mÃ¥ste vara pÃ¥slagen)
- NSA har access till alla stora operatÃ¶rers data (AT&T, Verizon, T-Mobile)

**GPS Tracking:**
- Smartphones har GPS som kan aktiveras remotely
- Precision: 5-10 meter under Ã¶ppen himmel
- KrÃ¤ver: Telefonens GPS Ã¤r pÃ¥, eller du installerar malware som tvingar igÃ¥ng den
- Batterikonsumption: Synligt fÃ¶r anvÃ¤ndaren om aktivt lÃ¤nge

**Praktiskt exempel:**
"Var Ã¤r mÃ¥let just nu?"
- Steg 1: BegÃ¤r cell tower data fÃ¶r hans telefonnummer
- Steg 2: FÃ¥r senaste pingen (uppdateras var 5-15:e minut)
- Steg 3: Om han rÃ¶r sig: Ser rutt han fÃ¤rdas
- Steg 4: Om statisk: Vet att han Ã¤r pÃ¥ specifik adress
- Total tid: 5-10 minuter att fÃ¥ realtidsdata

**Lyssna pÃ¥ samtal:**
- NSA kan aktivera microfonen i telefoner remotely
- Fungerar Ã¤ven nÃ¤r telefonen "verkar" vara av (vissa modeller)
- KrÃ¤ver: Tidigare installerad backdoor eller zero-day exploit
- Kvalitet: Bra vid direkt samtal, muffigt om telefonen Ã¤r i ficka/vÃ¤ska

**BegrÃ¤nsningar:**
- Om telefonen Ã¤r HELT avstÃ¤ngd (batteri ur): Ingen spÃ¥rning
- Faraday bag: Blockerar alla signaler
- Vissa utlÃ¤ndska telefoner (ryska, kinesiska): SvÃ¥rare att kompromitera
- Burner phones: Om de aldrig kopplas till identitet Ã¤r de anonyma tills anvÃ¤nda

#### **Email & Cloud Storage**

**Gmail / Outlook / Yahoo:**
- Via PRISM: FullstÃ¤ndig access till inbox, sent, trash, drafts
- Inkluderar raderade emails (finns kvar i 30 dagar pÃ¥ servrar)
- Kan sÃ¤tta upp real-time alerts: "Notifiera mig om han mailar nÃ¥gon"
- Tidsfaktor: 1-2 timmar att fÃ¥ historisk dump, realtid fÃ¶r framÃ¥t

**ProtonMail / Tutanota (Krypterade tjÃ¤nster):**
- End-to-end encrypted: NSA kan inte lÃ¤sa innehÃ¥llet
- Men kan se: Metadata (vem mailar vem, nÃ¤r, hur stora emails)
- Om du fÃ¥r fysisk access till hans dator medan inloggad: Kan lÃ¤sa dÃ¥
- Alternativt: Keylogger som fÃ¥ngar lÃ¶senordet

**Cloud Storage (Google Drive, Dropbox, OneDrive):**
- PRISM ger fullstÃ¤ndig access
- Kan ladda ner alla filer, se versionshistorik
- Ser Ã¤ven: Vem har delat access till vilka filer
- Tidsfaktor: 2-3 timmar fÃ¶r komplett dump av ett konto

**Encrypted Cloud (Tresorit, SpiderOak):**
- Zero-knowledge encryption: FÃ¶retaget har inte dekrypteringsnyckeln
- NSA kan inte lÃ¤sa innehÃ¥llet utan anvÃ¤ndarens lÃ¶senord/nyckel
- Men: Kan fortfarande hacka anvÃ¤ndarens device och fÃ¥ nyckeln dÃ¤rifrÃ¥n

#### **Social Media Intelligence (SOCMINT)**

**Facebook / Instagram / Twitter:**
- Via PRISM eller web scraping
- Kan se: Public posts, private messages (via PRISM), friend lists, check-ins
- Geotagging: MÃ¥nga bilder har GPS-koordinater i metadata
- Timeline-analys: Var har personen varit baserat pÃ¥ posts

**LinkedIn:**
- Professional network analysis
- Ser: Vem han arbetat med, kontakter, endorsements
- AnvÃ¤ndbart fÃ¶r att identifiera medarbetare eller kontakter

**Reddit / Forum accounts:**
- SpÃ¥ra genom username reuse
- Om samma anvÃ¤ndarnamn anvÃ¤nds pÃ¥ flera platser: Kan koppla identiteter
- Post history analysis: Vad personen pratar om, intressen, Ã¥sikter

**Dating apps (Tinder, Bumble):**
- MÃ¥nga har dÃ¥lig sÃ¤kerhet
- Via API-exploits kan se: Exakt GPS-position, alla matchningar
- AnvÃ¤ndbart om mÃ¥let anvÃ¤nder det (lÃ¥ngsÃ¶kt men mÃ¶jligt)

#### **Dark Web & Tor**

**Tor-nÃ¤tverk:**
- "Anonymt" nÃ¤tverk fÃ¶r dark web
- NSA kÃ¶r mÃ¥nga exit nodes och relay nodes
- Kan ofta de-anonymisera anvÃ¤ndare genom:
  - Traffic correlation (jÃ¤mfÃ¶r inkommande och utgÃ¥ende trafik)
  - Time-based attacks (nÃ¤r bÃ¶rjar/slutar nÃ¥gon anvÃ¤nda Tor)
  - Browser fingerprinting (Ã¤ven i Tor Browser)

**Realistisk fÃ¶rmÃ¥ga:**
- Kan inte se allt pÃ¥ Tor, men inte helt anonymt heller
- Om personen gÃ¶r misstag (loggar in pÃ¥ vanligt konto via Tor): Identitet avslÃ¶jad
- Om NSA dedikerar resurser (dagar-veckor): Kan ofta hitta anvÃ¤ndare

**Dark Web Markets:**
- Kan Ã¶vervaka vissa marknader
- Ser transaktioner (via blockchain-analys fÃ¶r Bitcoin)
- Kan infiltrera som fake sellers/buyers

#### **Cryptocurrency Tracking**

**Bitcoin / Ethereum:**
- All transaktioner Ã¤r publika pÃ¥ blockchain
- Kan spÃ¥ra pengar frÃ¥n wallet till wallet
- Om nÃ¥gon vÃ¤xlar till fiat (riktiga pengar): MÃ¥ste gÃ¥ via exchange som krÃ¤ver ID
- NSA har tools fÃ¶r blockchain analysis

**Monero / Zcash (Privacy coins):**
- Designade fÃ¶r anonymitet
- Mycket svÃ¥rare att spÃ¥ra
- Men: Om du vet wallet-adressen kan se inkommande/utgÃ¥ende (mÃ¤ngd och tid, inte destination)

**Praktiskt exempel:**
"Personen fick en Bitcoin-betalning"
- Steg 1: Identifiera wallet-adressen
- Steg 2: Trace transaktionen bakÃ¥t (vem skickade)
- Steg 3: Kolla om avsÃ¤ndaren nÃ¥gonsin anvÃ¤nt exchange (KYC-data finns)
- Steg 4: Identifiera avsÃ¤ndaren
- Total tid: 1-4 timmar beroende pÃ¥ hur mÃ¥nga steg i transaktionskedjan

### **ELEKTRONIK: 60%**

#### **RFID & NFC (Radio-Frequency Identification)**

**Hur det fungerar:**
- Kort/badges sÃ¤nder ut unik ID nÃ¤r de kommer nÃ¤ra lÃ¤sare
- Frekvenser: 125 kHz (gammal), 13.56 MHz (vanlig), 900 MHz (lÃ¥ngdistans)
- RÃ¤ckvidd: 5-10 cm fÃ¶r vanliga kort, upp till 100m fÃ¶r aktiva RFID

**Vad du kan gÃ¶ra med Spark:**

**Kloning - Basic badges (Hotell, Gym, Basic Access):**
- HÃ¥ll Spark nÃ¤ra kort/lÃ¤sare
- LÃ¤s UID (Unique Identifier)
- Kopiera till tomt kort
- Tidsfaktor: 3-10 sekunder
- SvÃ¥righet: LÃ¤tt
- Fungerar pÃ¥: Hotellkort, gymkort, basic fÃ¶retags-badges

**Kloning - SÃ¤krare badges (HID ProxCard II, MIFARE):**
- KrÃ¤ver lÃ¤sning av bÃ¥de UID och encrypted sectors
- Vissa kort har "write protection" som mÃ¥ste kringgÃ¥s
- Tidsfaktor: 30 sekunder - 3 minuter
- SvÃ¥righet: Medium
- Fungerar pÃ¥: De flesta fÃ¶retagsbadges

**Cloning - High-security badges (iClass, DESFire):**
- KrÃ¤ver bruteforce av dekrypteringsnycklar
- Vissa Ã¤r "impossible to clone" utan insider key
- Tidsfaktor: 10 minuter - 2 timmar (eller omÃ¶jligt)
- SvÃ¥righet: SvÃ¥rt
- Fungerar pÃ¥: Federal buildings (ibland), hÃ¶gra sÃ¤kerhet

**Relay Attack - Moderna badges:**
- IstÃ¤llet fÃ¶r att klona: Relay signal frÃ¥n Ã¤kta badge till lÃ¤sare
- KrÃ¤ver 2 enheter: En nÃ¤ra personen, en nÃ¤ra dÃ¶rren
- RÃ¤ckvidd: Upp till 100 meter mellan enheterna
- Tidsfaktor: Real-time (mÃ¥ste gÃ¶ras medan personen Ã¤r nÃ¤ra)
- Fungerar pÃ¥: NÃ¤stan alla badges inklusive high-security

**Brute-force - NÃ¤r du inte har badge:**
- MÃ¥nga system anvÃ¤nder fÃ¶rutsÃ¤gbara UID:n
- Ex: Hotell utfÃ¤rdar kort sekventiellt (12345, 12346, 12347...)
- Spark kan testa alla kombinationer
- Tidsfaktor: 10 sekunder - 10 minuter beroende pÃ¥ range
- FramgÃ¥ng: Medium till hÃ¶g fÃ¶r hotell/gym, lÃ¥g fÃ¶r fÃ¶retag

#### **Bilar - Keyless Entry & Ignition**

**Gamla bilar (fÃ¶re 2010):**

**Rolling Code (KeeLoq):**
- Nyckeln skickar ny kod varje gÃ¥ng (inte samma)
- Men: Algoritmen Ã¤r knÃ¤ckt, NSA har exploits
- Spark kan:
  - Sniffa signal nÃ¤r Ã¤garen lÃ¥ser
  - Replay attack (spela upp samma signal igen)
  - Brute-force alla mÃ¶jliga codes (tar 1-5 minuter)

**Fixed Code:**
- Ã„nnu Ã¤ldre system, samma kod varje gÃ¥ng
- Trivial att klona
- Tidsfaktor: 10 sekunder

**Moderna bilar (2010-2020):**

**Relay Attack - Vanligaste metoden:**
- Bilen frÃ¥gar: "Ã„r nyckeln nÃ¤ra?"
- Nyckeln svarar: "Ja, hÃ¤r Ã¤r jag"
- Spark lÃ¥tsas vara bÃ¥da

**Setup:**
- Spark Unit 1: Placeras nÃ¤ra mÃ¥lets nyckel (i deras ficka, vÃ¤ska, hem)
- Spark Unit 2: Placeras nÃ¤ra bilen
- Distance: Upp till 100 meter kan Ã¶verbryggas
- Tidsfaktor: 10-30 sekunder nÃ¤r setup Ã¤r klar

**BegrÃ¤nsningar:**
- KrÃ¤ver att nyckeln fortfarande Ã¤r inom rÃ¤ckvidd
- Om Ã¤garen lÃ¤gger nyckel i Faraday bag: Blockerat
- Vissa nya bilar har "motion detection" i nyckel (ingen relay om nyckel Ã¤r stilla)

**CAN Bus Hacking - Physical Access Required:**
- CAN = Controller Area Network (bilens interna nÃ¤tverk)
- Access via: OBD-II port (under ratten) eller cut wires i dÃ¶rr

**Metod:**
- Koppla Spark till OBD-II port
- Injicera "unlock doors" kommando
- Injicera "start engine" kommando
- Tidsfaktor: 2-5 minuter efter du kommit Ã¥t porten
- SvÃ¥righet: Medium

**Larm:**
- MÃ¥nga bilar larmar om CAN bus manipulation
- MÃ¥ste ocksÃ¥ injicera "disable alarm" kommando
- Kan vara svÃ¥rt att hitta rÃ¤tt kommando (trial and error)

**Nya bilar (2020+):**

**Ultra-Wideband (UWB) Technology:**
- Kan mÃ¤ta exakt avstÃ¥nd till nyckel (inte bara "nÃ¤ra" eller "inte nÃ¤ra")
- Relay attack fortfarande mÃ¶jligt men svÃ¥rare
- KrÃ¤ver mer sofistikerad utrustning

**Realistisk bedÃ¶mning fÃ¶r Spark:**
- Tesla, BMW, Mercedes 2022+: 15-30 minuter med fysisk access, eller omÃ¶jligt pÃ¥ distans
- Alla andra: Fortfarande mÃ¶jligt men mer komplext

#### **LÃ¥s & Access Control Systems**

**Magnetiska lÃ¥s:**
- DÃ¶rr hÃ¥lls stÃ¤ngd av elektromagnet
- NÃ¤r rÃ¤tt badge visas: Magnet slÃ¤pper
- Spark kan: Skicka rÃ¤tt signal (om klonat badge) eller avbryta strÃ¶mmen

**Power Interruption Attack:**
- Magnetiska lÃ¥s krÃ¤ver konstant strÃ¶m fÃ¶r att hÃ¥lla stÃ¤ngt
- Avbryt strÃ¶mmen = dÃ¶rren Ã¶ppnas
- Spark kan: Skapa electromagnetic pulse (EMP) som kortsluter systemet
- Tidsfaktor: 5-15 sekunder
- Synlighet: MYCKET synligt (gnistor, ljud, potentiellt eldlarm)

**Electronic Strikes:**
- Reverse av magnetiska lÃ¥s: Elektriskt pulsat fÃ¶r att Ã¶ppna
- Spark kan: Triggera pulse genom att skicka rÃ¤tt signal

**Mantraps:**
- TvÃ¥ dÃ¶rrar dÃ¤r endast en kan vara Ã¶ppen Ã¥t gÃ¥ngen
- Mycket svÃ¥rare att hacka
- KrÃ¤ver: Antingen klonad badge med rÃ¤tt clearance, eller social engineering (piggyback)

**Keypads:**

**PIN-code crackers:**
- Gamla keypads: Kan brute-force alla kombinationer
- Tidsfaktor: 4-siffrig kod = upp till 10000 kombinationer = 2-4 timmar
- Modern keypad med lockout: OmÃ¶jligt (lÃ¥ser efter X fel fÃ¶rsÃ¶k)

**Thermal Imaging Attack:**
- Efter nÃ¥gon slagit in kod: Deras fingeravtryck Ã¤r varmare Ã¤n Ã¶vriga knappar
- Spark har inte thermal camera, men en handhÃ¥llen thermal-enhet kan anvÃ¤ndas
- Ser vilka 4 siffror som anvÃ¤nts (men inte ordning)
- Tidsfaktor: MÃ¥ste gÃ¶ras inom 30-60 sekunder efter personen
- Reducerar 10000 kombinationer till ~24 mÃ¶jliga kombinationer

**Electromagnetic Emanation Reading:**
- Varje knapp ger av lite olika EM-signaler nÃ¤r tryckt
- Med kÃ¤nslig utrustning kan lÃ¤sa vilka knappar som tryckts
- Spark har denna kapacitet (modifierad fÃ¶r Ã¤ndamÃ¥let)
- Tidsfaktor: MÃ¥ste vara nÃ¤ra nÃ¤r personen slÃ¥r in kod
- SvÃ¥righet: HÃ¶g (krÃ¤ver kalibrering och tÃ¥lamod)

#### **Ã–vervakningssystem**

**CCTV / IP-kameror:**

**Ã„ldre system (DVR-baserade):**
- Ofta standardlÃ¶senord (admin/admin, admin/12345)
- Spark kan: Brute-force login, eller exploit known vulnerabilities
- Tidsfaktor: 5-20 minuter
- NÃ¤r inne: Radera footage, loop gamla filmklipp, stÃ¤ng av kameror

**Moderna IP-kameror:**
- Anslutna till nÃ¤tverk via WiFi eller ethernet
- Om du har nÃ¤tverksaccess: Kan hacka som vilken dator som helst
- Tidsfaktor: 10-30 minuter
- MÃ¥nga mÃ¤rken (Hikvision, Dahua) har kÃ¤nda backdoors

**Physical tampering:**
- Kapa kabel: Synligt att kamera Ã¤r ur funktion
- Electromagnetic jamming: StÃ¶r signalen (Ã¤ven detta detekteras av moderna system)
- Spray/laser: Blind kamera tillfÃ¤lligt (mycket synligt)

**BÃ¤sta metoden:**
- Hacka systemet digitalt
- Loopa 10 minuters "normal" footage
- FortsÃ¤tt loopa medan ni genomfÃ¶r operation
- EfterÃ¥t: Radera all footage frÃ¥n den perioden
- Verkar som tekniskt fel om nÃ¥gon kollar

#### **Alarm Systems**

**Typer:**

**Motion detectors:**
- PIR (Passive Infrared): KÃ¤nner av kroppsvÃ¤rme
- Microwave: KÃ¤nner av rÃ¶relse via microvÃ¥gsor
- Dual-tech: BÃ¥de PIR och microwave (mÃ¥ste bÃ¥da triggas)

**Hur Spark kan hantera:**
- Hack central panel (via nÃ¤tverksanslutning)
- Skicka "disable alarm" kommando
- Eller: "Fake normal" status medan ni rÃ¶r er
- Tidsfaktor: 10-20 minuter om fjÃ¤rraccess, 2-5 minuter om fysisk access

**Glass break sensors:**
- Lyssnar efter specifik frekvens av krossande glas
- Spark kan: Jamma signalen eller trigga falska alarm fÃ¶r att desensitize systemet

**Door/Window contacts:**
- Enkel magnet som kÃ¤nner av om dÃ¶rr/fÃ¶nster Ã¶ppnas
- Spark kan: Placera extern magnet som lurar sensorn att dÃ¶rren Ã¤r stÃ¤ngd

**Central Panel:**
- HjÃ¤rnan i alarmsystemet
- Om du fÃ¥r fysisk access: Kan disable helt
- Tidsfaktor: 30 sekunder - 2 minuter

**BegrÃ¤nsningar:**
- Moderna system har "tamper alarms" (larmar om nÃ¥gon fÃ¶rsÃ¶ker Ã¶ppna panelen)
- MÃ¥nga Ã¤r uppkopplade till sÃ¤kerhetsfÃ¶retag (fÃ¥r alert omedelbart)
- Spark kan hacka uppkopplingen men tar tid

#### **WiFi & Bluetooth**

**WiFi Hacking:**

**WEP (FÃ¶rÃ¥ldrad):**
- Kan knÃ¤ckas pÃ¥ 5-10 minuter
- NÃ¤stan ingen anvÃ¤nder lÃ¤ngre

**WPA2:**
- Handshake Capture: VÃ¤nta pÃ¥ att nÃ¥gon device ansluter, fÃ¥nga krypterad handshake
- Dictionary Attack: Testa miljontals vanliga lÃ¶senord mot handshaken
- Tidsfaktor: 10 minuter (capture) + 30 min - 48 timmar (cracking beroende pÃ¥ lÃ¶senordsstyrka)

**WPA3:**
- Modernaste, mycket sÃ¤krare
- Fortfarande mÃ¶jligt med downgrade attack (tvinga till WPA2)
- Tidsfaktor: 30 minuter - flera dagar

**Evil Twin Attack:**
- Spark skapar fake WiFi med samma namn som riktigt nÃ¤tverk
- Devices ansluter automatiskt (tror det Ã¤r rÃ¤tt nÃ¤tverk)
- Du ser allt de gÃ¶r (om inte HTTPS)
- Tidsfaktor: 5 minuter att sÃ¤tta upp

**Bluetooth:**

**Bluejacking:**
- Skicka meddelanden till nÃ¤rliggande Bluetooth-devices
- Mest irriterande, inte praktiskt anvÃ¤ndbart

**Bluesnarfing:**
- Exploit sÃ¥rbarheter fÃ¶r att stjÃ¤la data (kontakter, filer)
- MÃ¥nga Ã¤ldre telefoner (fÃ¶re 2015) Ã¤r sÃ¥rbara
- Tidsfaktor: 2-10 minuter
- RÃ¤ckvidd: 10-30 meter

**Bluetooth Tracking:**
- Alla Bluetooth-devices har unik MAC-adress
- Spark kan logga alla devices i nÃ¤rheten
- AnvÃ¤ndbart fÃ¶r att spÃ¥ra vem som var vid plats vid viss tid
- Tidsfaktor: Kontinuerlig logging

#### **Miscellaneous Electronics**

**ATM Skimming:**
- Spark kan inte "hacka" ATM direkt
- Men kan placeras som skimmer (lÃ¤ser av kortnummer + PIN)
- Tidsfaktor: 2-5 minuter att installera, sedan samla data
- Risk: Illegal, lÃ¤mnar fysisk enhet som kan spÃ¥ras

**Traffic Lights:**
- MÃ¥nga gamla system har wireless control (fÃ¶r ambulanser)
- Spark kan: Sniffa signalen och replay fÃ¶r att Ã¤ndra ljus
- Tidsfaktor: 10-20 minuter fÃ¶rsta gÃ¥ngen, sedan 30 sekunder per tillfÃ¤lle
- AnvÃ¤ndbart fÃ¶r: Skapa fÃ¶rvirring, ge er fri vÃ¤g

**Hotel Room Safes:**
- NÃ¤stan alla har master-code (standard 0000, 9999, eller 1234)
- Spark kan: Brute-force alla 4-siffriga kombinationer
- Tidsfaktor: 5-15 minuter
- Alternativ: MÃ¥nga sÃ¤kerhetsboxar kan Ã¶ppnas med stark magnet (bygg egen magnet-tool)

**Smart Home Devices (Alexa, Google Home, etc.):**
- Om pÃ¥ samma WiFi: Kan skicka kommandor
- AnvÃ¤ndbart fÃ¶r: Distraction (spela hÃ¶gljudd musik), surveillance (lyssna via mikrofonen)
- Tidsfaktor: 5-10 minuter att fÃ¥ access

#### **EMP (Electromagnetic Pulse) Device**

**Vad Spark KAN gÃ¶ra:**
- Bygga liten handhÃ¥llen EMP
- RÃ¤ckvidd: 1-3 meter
- Effekt: StÃ¤ng av / fÃ¶rstÃ¶r elektronik i nÃ¤rheten (telefoner, datorer, kameror)
- Tidsfaktor att bygga: 3-5 timmar med rÃ¤tt komponenter
- Varaktighet: EngÃ¥ngsbruk (vissa komponenter fÃ¶rstÃ¶rs)

**Vad Spark INTE KAN gÃ¶ra:**
- Stora EMP som i filmer (krÃ¤ver militÃ¤r utrustning)
- "Osynligt" EMP (det Ã¤r synligt, ljudligt, och lÃ¤mnar spÃ¥r)

**NÃ¤r anvÃ¤ndbart:**
- Sabotage Ã¶vervakningsutrustning
- FÃ¶rstÃ¶ra bevis pÃ¥ digital enhet
- Disable alarm systems
- Emergency: Stoppa fjÃ¤rrstyrd bomb (om elektronisk trigger)

### **SPRÃ…K & FORSKNING**

#### **Ryska: 50%**
- Kan lÃ¤sa och fÃ¶rstÃ¥ tekniska dokument
- Kan fÃ¶lja konversationer (men inte alltid idiom)
- Kan skriva emails (men kanske inte helt naturliga)
- AnvÃ¤ndbart fÃ¶r: Ryska darknet-forum, rysk dokumentation, avlyssnad kommunikation

#### **Kinesiska: 40%**
- GrundlÃ¤ggande fÃ¶rstÃ¥else
- Kan identifiera tecken och fÃ¥ Ã¶versikt
- Inte tillrÃ¤ckligt fÃ¶r komplexa texter eller snabb konversation
- AnvÃ¤ndbart fÃ¶r: Identifiera kinesiska tech-dokument, basic Ã¶versÃ¤ttning

#### **Biblioteksforskning: 60%**
- Hitta obscur information online
- Vet var man letar (dark web, akademiska arkiv, specialforum)
- Verifiera kÃ¤llor och skilja sanning frÃ¥n desinformation
- AnvÃ¤ndbart fÃ¶r: Research om okkulta Ã¤mnen, hitta akademiska papers, identifiera symboler

---

## ðŸ› ï¸ "SPARK" - CUSTOM FLIPPER ZERO

### **Teknisk spec:**

**Hardware:**
- Custom PCB baserad pÃ¥ Flipper Zero
- FÃ¶rstÃ¤rkt antenn (+20dB gain)
- Expanded memory (512GB)
- Upgraded processor (4x snabbare)
- Extra battery (12h continuous use)
- Direct laptop tethering (USB-C + WiFi)

**Frekvenser:**
- Sub-GHz: 300-928 MHz (bil-nycklar, garage-dÃ¶rrar, etc.)
- RFID: 125 kHz (LF) och 13.56 MHz (HF)
- NFC: 13.56 MHz
- Bluetooth: 2.4 GHz
- WiFi: 2.4 GHz och 5 GHz
- IR: 800-1000 nm (fjÃ¤rrkontroller)

**Software:**
- Custom firmware med NSA exploits
- AI-powered protocol detection
- Automated attack sequences
- Remote control via laptop

### **Praktiska anvÃ¤ndningsomrÃ¥den:**

| MÃ¥l | Metod | Tidsfaktor | SvÃ¥righet |
|-----|-------|------------|-----------|
| Hotellkort | RFID clone | 10 sek | LÃ¤tt |
| Bil (2000-2010) | Replay attack | 30 sek | LÃ¤tt |
| Bil (2010-2020) | Relay attack | 2 min | Medium |
| Bil (2020+) | CAN bus hack | 15 min | SvÃ¥rt |
| WiFi (WPA2) | Handshake + crack | 1-48h | Medium |
| FÃ¶retags-badge | RFID clone | 30 sek | Medium |
| Federal-badge | Clone/Impossible | 1h / âˆž | SvÃ¥rt/OmÃ¶jligt |
| Alarm system | Disable via hack | 10 min | Medium |
| CCTV system | Loop footage | 15 min | Medium |
| GaragedÃ¶rr | Sub-GHz replay | 10 sek | LÃ¤tt |

### **BegrÃ¤nsningar:**

**Kan INTE:**
- Hacka air-gapped system (mÃ¥ste ha fysisk access)
- Fejka biometrics (fingeravtryck, iris-scan, facial recognition)
- Fungera genom Faraday cage
- KnÃ¤cka moderna kryptering pÃ¥ egen hand (behÃ¶ver stÃ¶rre system)
- Ã–ppna mekaniska lÃ¥s (behÃ¶vs lockpicks)

**Risk:**
- LÃ¤mnar electromagnetic signatur (detekterbar av RF-sweeps)
- Synlig nÃ¤r du anvÃ¤nder den (folk ser dig hÃ¥lla device mot dÃ¶rr)
- Loggas av vissa system (anomaly detection)
- Illegal att anvÃ¤nda i mÃ¥nga sammanhang

---

## ðŸ’° EKONOMISKA RESURSER

**NSA-lÃ¶n:** ~$95,000/Ã¥r  
**Bitcoin-wallet:** â‚¿3.5 (~$378,000 september 2025)

**Vad du kan gÃ¶ra:**
- Betala anonyma kontakter pÃ¥ dark web (utan paper trail)
- KÃ¶pa utrustning NSA inte kan spÃ¥ra
- Muta folk diskreet
- NÃ¶dfond om Delta Green-operationen gÃ¥r Ã¥t helvete

**Levnadsstandard:**
- Studio apartment full av tech
- Delivery food (glÃ¶mmer laga mat)
- Minimal social liv
- All Ã¶verskott gÃ¥r till hardware och software

**Praktiskt fÃ¶r operationer:**
- Kan lÃ¶sa problem under $10k omedelbart
- StÃ¶rre summor ($50k+) krÃ¤ver eftertanke (mÃ¥ste sÃ¤lja bitcoin = lÃ¤mnar spÃ¥r)

---

## âš ï¸ KRITISKA BEGRÃ„NSNINGAR

### **Tekniska:**

**Air-gapped systems:**
- System helt isolerade frÃ¥n internet
- Kan INTE hackas pÃ¥ distans
- KrÃ¤ver fysisk access eller USB/media insertion

**Faraday cages:**
- Blockerar alla elektromagnetiska signaler
- Spark fungerar inte alls
- Vissa sÃ¤kra anlÃ¤ggningar har detta

**Quantum-resistant encryption:**
- Vissa nya krypteringsmetoder Ã¤r praktiskt omÃ¶jliga att knÃ¤cka
- Tar decennier med dagens datorkraft

**Old analog tech:**
- Mekaniska lÃ¥s, analog telefoner, paper records
- Inget att hacka = mÃ¥ste anvÃ¤nda andra metoder

### **Operationella:**

**Time pressure:**
- MÃ¥nga hacks tar TID
- Under aktiv operation kanske du har minuter, inte timmar

**Physical security:**
- Guards kan se dig anvÃ¤nda Spark
- Kameras kan filma dig
- MÃ¥ste kombinera tech med stealth

**Legal exposure:**
- Varje gÃ¥ng du anvÃ¤nder NSA-verktyg off-books riskerar du karriÃ¤r
- Delta Green kan inte skydda dig om du grips av lokal polis
- Spark Ã¤r illegal att anvÃ¤nda i civila sammanhang

### **Psykologiska:**

**SAN: 63/77**
- Har fÃ¶rlorat 14 poÃ¤ng i Delta Green-operationer
- Ã…terhÃ¤mtat 2 via "kod och logik" (nedskrivet som teknisk rapport)
- Paranoid: Tror alltid att nÃ¥got spÃ¥rar dig
- Isolated: Litar mer pÃ¥ kod Ã¤n mÃ¤nniskor
- Obsessive: SvÃ¥rt att slÃ¤ppa taget om mÃ¥l

**Stress-reaktioner:**
- Blir snÃ¤sig och frÃ¥nvarande nÃ¤r Ã¶verbelastad
- Drar sig undan och jobbar solo (inte alltid bra fÃ¶r teamet)
- Tar risker fÃ¶r att bevisa kompetens

---

## ðŸŽ¯ QUICK REFERENCE CHEAT SHEET

### **"Kan du hacka X?"**

**Saker du nÃ¤stan alltid kan gÃ¶ra (givet tid):**
âœ… LÃ¤sa nÃ¥gons emails (via PRISM eller hack)  
âœ… SpÃ¥ra telefon (via cell towers eller GPS)  
âœ… Klona hotellkort / basic RFID badges  
âœ… Ã–ppna gamla bilar  
âœ… Hacka WiFi (WPA2)  
âœ… Ã–vervaka sociala medier  
âœ… Manipulera Ã¶vervakningskameror

**Saker du KAN gÃ¶ra men tar lÃ¤ngre tid:**
âš ï¸ Bryta modern kryptering (dagar-veckor)  
âš ï¸ Hacka federal system (krÃ¤ver planering)  
âš ï¸ Ã–ppna nya bilar (15-30 min med fysisk access)  
âš ï¸ De-anonymisera Tor-anvÃ¤ndare (krÃ¤ver NSA-resurser)  
âš ï¸ Trace cryptocurrency (tar tid och analys)

**Saker du INTE kan gÃ¶ra:**
âŒ Hacka air-gapped system utan fysisk access  
âŒ Fejka biometrics (fingeravtryck, iris-scan)  
âŒ Fungera genom Faraday cage  
âŒ Hacka mekaniska lÃ¥s  
âŒ Instant-hacks pÃ¥ militÃ¤r-grade system

### **Typiska tidsramar:**

| Uppgift | Tid |
|---------|-----|
| LÃ¤sa emails via PRISM | 30 min - 2h |
| SpÃ¥ra telefon realtid | 5-10 min |
| Klona hotellkort | 10 sek |
| Hacka WiFi | 30 min - 48h |
| Ã–ppna bil (gammal) | 30 sek |
| Ã–ppna bil (ny) | 15-30 min |
| Loop CCTV footage | 15-30 min |
| Brute-force kryptering | Dagar-veckor |
| Bygga custom malware | 1-2h |

### **Viktiga frÃ¥gor att stÃ¤lla SL:**

1. "Hur mycket tid har vi?" (AvgÃ¶r om snabbhack eller ordentligt)
2. "Finns WiFi/4G hÃ¤r?" (PÃ¥verkar vad som Ã¤r mÃ¶jligt)
3. "Vilket sÃ¤kerhetssystem anvÃ¤nder de?" (Ã„ldre = lÃ¤ttare)
4. "Kan jag fÃ¥ fysisk access?" (Ã–ppnar fler mÃ¶jligheter)
5. "Hur mycket kan vi riskera att lÃ¤mna spÃ¥r?" (Snabbt och smutsigt vs rent och fÃ¶rsiktigt)

---

## ðŸ“¡ NSA ACCESS - VAD DU HAR TILLGÃ…NG TILL

**XKEYSCORE:**
- SÃ¶k genom all internet-trafik NSA samlar
- Emails, chattar, websÃ¶kning, browsing history
- TÃ¤ckning: VÃ¤st (utmÃ¤rkt), MellanÃ¶stern (bra), Ryssland/Kina (begrÃ¤nsat)
- Svarstid: 2-10 minuter

**PRISM:**
- Direktaccess till: Gmail, Drive, Facebook, iCloud, Microsoft
- Historik: 2 Ã¥r bakÃ¥t
- Svarstid: 30 min - 2h

**UPSTREAM:**
- Fiberoptisk avlyssning
- Ser metadata fÃ¶r ~75% av amerikansk trafik
- Kan inte se krypterat innehÃ¥ll

**TAO (Tailored Access Operations):**
- Custom zero-day exploits
- BegÃ¤r specific malware fÃ¶r specific mÃ¥l
- Svarstid: Dagar (fÃ¶r non-urgent)

**BEGRÃ„NSNINGAR:**
- Allt loggas (kan spÃ¥ras tillbaka till dig)
- MÃ¥ste kunna fÃ¶rklara varfÃ¶r du sÃ¶kte
- Delta Green Ã¤r off-books (riskerar karriÃ¤r varje gÃ¥ng)
- Vissa lÃ¤nder har isolerade nÃ¤tverk (Ryssland, Kina)

---

*Detta dokument Ã¤r sekretessbelagt. Vid fara: Destroy device, encrypt comms, deny everything.*

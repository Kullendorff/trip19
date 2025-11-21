# SPARKY'S PERSONAL OPSEC TOOLKIT

> *"Det är inte paranoia när de faktiskt är ute efter dig. Eller kommer kunna vara det. Eller bara råkar övervaka dig för att algoritmen flaggade nåt."*
> 
> — Kai "Sparky" Zhang

---

## 📋 ÖVERSIKT

En samling av 29 custom-byggda appar som Sparky har utvecklat över åren för att minimera sitt digitala fotavtryck. Varje app löser ett specifikt OPSEC-problem som någon med hennes bakgrund och kunskap inte kan ignorera.

**Filosofi:** Varje app, varje kort-swipe, varje GPS-ping är en datapunkt. Tillräckligt många datapunkter och AI:n vet mer om dig än du själv vet. Dessa appar gör hennes liv mer komplicerat - men de gör henne osynlig.

---

## 📱 KOMMUNIKATION & IDENTITET

### 1. BurnerRotate
**Funktion:** Auto-rotation av burner phone numbers  
**Hur:** Genererar nya nummer var 48:e timme, forwarding till hennes riktiga telefon (krypterat)  
**Varför:** Ingen kan spåra henne via ett persistent nummer  
**Användning:** Ger ut olika nummer till olika folk, alla går till henne  
**Status:** Always running

### 2. FaceSwap Lite
**Funktion:** Slight alteration av profilbilder för fake-konton  
**Hur:** Ändrar belysning, vinkel, hårsätt digitalt  
**Varför:** Konton ser legitima ut men AI kan inte matcha bilder  
**Användning:** Alla hennes fake Instagram/Facebook/LinkedIn  
**Teknisk not:** Fortfarande "henne" men inte igenkännbar av facial recognition

### 3. VoiceMod
**Funktion:** Realtids röstmodulering för telefonsamtal  
**Hur:** Inte "robot voice" - subtila förändringar i tonhöjd/accent  
**Varför:** Voice recognition blir värdelös  
**Användning:** När hon ringer från burner numbers  
**Teknisk not:** Låter naturligt, bara "lite annorlunda"

### 4. NameGen Pro
**Funktion:** Genererar trovärdiga fake identiteter med backstory  
**Hur:** Kopplat till US Census data för realistiska namn  
**Output:** Ålder, yrke, stad - allt statistiskt trovärdigt  
**Varför:** Snabbt skapa övertygande fake personas  
**Användning:** När hon behöver fake email/konto på sekunder  
**Exempel:** "Jennifer Martinez, 34, graphic designer, Portland OR"

---

## 💳 BETALNINGAR

### 5. CryptoDropbox
**Funktion:** Anonyma cryptocurrency-wallets med auto-tumbling  
**Hur:** Separerar hennes riktiga pengar från "operation money"  
**Varför:** Ospårbara betalningar  
**Användning:** Köpa saker utan att koppla till hennes identitet  
**Teknisk not:** Använder Monero för maximal anonymitet

### 6. GiftCardChain
**Funktion:** Köper gift cards med crypto, använder för shopping  
**Hur:** Auto-rotation så inget mönster uppstår  
**Varför:** Inga kort = inga spår  
**Användning:** Amazon, UberEats, etc. utan att koppla till riktigt namn  
**Exempel:** Crypto → Visa gift card → Amazon-köp → Ingen koppling till Kai Zhang

---

## 📍 LOKALISERING

### 8. GPSFuzz
**Funktion:** Spoofar hennes telefons GPS position med +/- 500m random drift  
**Hur:** Ser ut som normal GPS "inaccuracy"  
**Varför:** Google/Apple kan inte veta EXAKT var hon är  
**Användning:** Always on  
**Teknisk not:** Tillräckligt litet för att appar fungerar, tillräckligt stort för att förstöra precision

### 9. WifiShuffle
**Funktion:** Randomiserar MAC address varje gång hon ansluter till wifi  
**Varför:** Förhindrar wifi-tracking i butiker/hotspots  
**Användning:** Always on  
**Exempel:** Starbucks ser "ny enhet" varje gång hon kommer

### 10. RouteRandom
**Funktion:** När hon planerar rutt hem, väljer slumpmässigt olika vägar  
**Hur:** Algoritm som varierar mellan 5-7 olika routes  
**Varför:** Pattern-of-life analysis blir värdelöst  
**Användning:** Daglig pendling  
**Not:** Lägger till max 5 min extra restid

---

## 🏠 HEMMA & LIVSSTIL

### 11. SmartHomeJammer
**Funktion:** Disablar temporärt smart devices när hon pratar känsligt  
**Hur:** "Glitch" i Alexa/Google Home  
**Varför:** Inte konstant paranoia, men kan stänga av vid behov  
**Användning:** Delta Green phone calls hemma  
**Teknisk not:** Återaktiveras automatiskt efter 30 min

### 12. ScheduleChaos
**Funktion:** Randomiserar hennes dagliga rutiner  
**Exempel:** Köper kaffe olika tider, olika ställen; handlar mat oregelbundet  
**Varför:** Ingen kan prediktera hennes rörelser  
**Användning:** Daily life micro-adjustments  
**Implementation:** Push notifications: "Köp kaffe vid Starbucks 7th St idag, inte din vanliga"

### 13. PackageReroute
**Funktion:** Amazon-paket skickas till pickup-points, aldrig hem  
**Hur:** Roterar mellan 5-6 olika platser  
**Varför:** Ingen ser vad hon beställer, inga paket till lägenheten  
**Användning:** All online shopping  
**Locations:** CVS, 7-Eleven, Amazon Locker - alla minst 1km från hennes boende

---

## 🎥 ÖVERVAKNING & SÄKERHET

### 14. CamSpotter
**Funktion:** Identifierar övervakningskameror via crowdsourced data + hennes egna observationer  
**Output:** Visar coverage map över DC  
**Varför:** Planera rutter som undviker kameror  
**Användning:** Pre-operation route planning  
**Database:** 2,847 kameror mappade i DC-området (per Nov 2025)

### 15. FaceBlur IRL
**Funktion:** Beräknar optimala glasögon-vinkel/hatt-stil för att förstöra facial recognition  
**Hur:** Inte maskerad - bara "ofördelaktig vinkel" för AI  
**Varför:** Se normal ut men vara oigenkännbar för AI  
**Användning:** När hon går igenom high-surveillance areas  
**Exempel:** "Bär keps med 23° vinkel, IR-reflective glasögon"

### 16. LicensePlateLogger
**Funktion:** Fotograferar bilar som parkerar vid hennes kvarter för ofta  
**How:** Alert om samma bil dyker upp 3+ gånger på 2 veckor  
**Varför:** Upptäcka surveillance  
**Användning:** Paranoia management  
**False positive rate:** ~15% (grannar med oregelbundna scheman)

---

## 📧 KOMMUNIKATION & MEDIA

### 17. EmailExpire
**Funktion:** Temporära email-adresser som self-destructs efter 48h  
**Varför:** Registrera konton utan långsiktig koppling  
**Användning:** Registreringar, newsletters  
**Teknisk not:** Använder guerrillamail API + egen implementation

### 18. MetaStrip
**Funktion:** Tar bort ALL metadata från foton innan sharing  
**Data removed:** GPS, kamera-modell, tidsstämpel, edit-history  
**Varför:** Dela bilder utan att avslöja var/när/hur  
**Användning:** Varje foto hon delar online  
**Exempel:** Instagram-bild ser ut att vara från "någonstans" men ingen vet var

### 19. SocialMirror
**Funktion:** Fake social media accounts med scheduled posts  
**Hur:** Ser ut som hon är aktiv, men allt är pre-scheduled  
**Varför:** "Kai Zhang" verkar normal online medan hon gör annat  
**Användning:** Maintain cover under operationer  
**Schedule:** 2-3 posts per vecka, randomiserad timing

---

## 🔧 TEKNISKT & OPERATIONELLT

### 20. DeadManSwitch
**Funktion:** Om hon inte checkar in var 72:e timme, auto-encrypt och delete känslig data  
**Varför:** Om något händer henne, inga spår finns kvar  
**Användning:** Always running  
**Backup:** Krypterade backups på air-gapped USB i bankfack  
**Trigger:** 3 missed check-ins = full data wipe

### 21. TorrentClean
**Funktion:** Laddar ner via randomiserade VPN/Tor exit nodes  
**Hur:** Auto-cleaner av download history  
**Varför:** ISP ser inte vad hon laddar ner  
**Användning:** Movies, software, research papers  
**Teknisk not:** Seedbox i Netherlands för extra separation

### 22. NetworkSniffer
**Funktion:** Passivt lyssnar på wifi-trafik runtomkring henne  
**Alert:** Om någon försöker MITM-attack mot henne  
**Varför:** Upptäcka om någon försöker hacka henne  
**Användning:** Always on när connected till wifi  
**False positives:** Sällsynta men händer på coffee shops

### 23. USBCondom
**Funktion:** Software version - scannar USB-portar innan allow data transfer  
**Varför:** Förhindra BadUSB-attacker mot henne  
**Användning:** Varje gång hon pluggar in något  
**Whitelist:** Hennes egna trusted devices  
**Warning:** Ljud + popup om unknown device

---

## 🍔 VARDAGSLIV

### 24. FoodRoulette
**Funktion:** Randomiserar var hon beställer mat ifrån  
**Varför:** Inga mönster i food delivery  
**Användning:** När hon är lat och vill ha UberEats  
**Database:** 47 restauranger inom delivery-area  
**Not:** Kan filtrera på "inga hamburgare 3 dagar i rad"

### 25. CoffeeTimer
**Funktion:** Tracks när hon köpte kaffe senast, föreslår olika tid/plats  
**Varför:** Variation i rutiner  
**Användning:** Morning coffee runs  
**Suggestion algorithm:** Aldrig samma plats 2 dagar i rad, aldrig samma tid +/- 30 min  
**Locations:** 12 olika coffee shops i rotation

### 26. LaundryScramble
**Funktion:** Påminner henne att tvätta kläder olika veckodagar  
**Varför:** Förhindra "varje söndag kl 14" mönster  
**Användning:** Apartment building laundry room  
**Algorithm:** Random day between Tuesday-Sunday, random 4-hour window  
**Not:** Kollar laundry room availability via building's online booking

---

## 🎮 FUN & PERSONAL

### 28. MusicMixer
**Funktion:** Lyssnar på musik via multiple streaming accounts  
**Hur:** 3 olika Spotify-konton, 2 Apple Music, 1 YouTube Music  
**Varför:** Ingen kan profila henne via musiksmak  
**Användning:** Spotify, Apple Music, YouTube  
**Rotation:** Byter account varje vecka  
**Payment:** Alla betalas via olika gift cards

---

## 🚨 EMERGENCY

### 29. PanicWipe
**Funktion:** Single button: encrypt all sensitive data, factory reset telefon  
**Varför:** Om hon grips/kapas  
**Användning:** Hopefully never  
**Activation:** Triple-click volume down + power button  
**Time to complete:** 12 seconds  
**Backup:** Allt viktigt finns redan i cloud (krypterat)

### 30. BeaconBurst
**Funktion:** Skickar emergency location till trusted contacts (krypterat)  
**Recipients:** Mac, Priya, Sullivan (Delta Green team)  
**Varför:** Om operation går åt helvete  
**Användning:** Dead hand switch  
**Message:** GPS coordinates + timestamp + "EMERGENCY"  
**Activation:** Hold volume up + power for 5 seconds

---

## 🎯 CROWN JEWEL: GHOSTSCOOTER

### 31. GhostScooter
**Funktion:** Universal unlock för elsparkcyklar (Lime, Hopp, Spin, Veo)  
**Features:**
- Unlock utan konto/betalning
- GPS spoofing (företaget ser sparkcykel som stillastående)
- Maintenance mode trigger (företaget ignorerar den helt)

**Varför:** Ospårbar transport för Delta Green operations  
**Development:** 2022-2024, kontinuerliga uppdateringar  
**Usage:** Pre-operation standard operating procedure  

**How it works:**
1. Scan nearby scooters (visar alla inom 500m)
2. Select target (filter på företag, batteri-status)
3. Unlock (2-3 sekunder, direkt kommunikation med sparkcykel)
4. GPS Spoof (optional - loopar senaste position)
5. Maintenance Mode (optional - flaggar som "under service")

**Operational value:**
- Ingen betalning = inga spår
- Inget konto = ingen identitet
- Ingen databas-post = resan existerar inte
- Urban camouflage = ser helt normalt ut
- Snabb escape = finns överallt i DC

**Limitations:**
- Batteriet på sparkcykel måste vara >20%
- Fungerar ej på offline-mode scooters
- GPS spoof håller bara 2-3 timmar (batteridrain)
- Måste uppdatera när företag ändrar säkerhet

**Status:** Operational, används regelbundet



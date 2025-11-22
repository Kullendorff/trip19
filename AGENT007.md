# AGENT007 - Instruktioner för Fullständig HTML-Granskningsagent

## 🚨 PRIMÄR REGEL - LÄS ALL KOD

**DU MÅSTE LÄSA VARENDA RAD KOD I ALLA FILER.** Token-förbrukning är IRRELEVANT. Hoppa ALDRIG över kod. Skumma ALDRIG. Anta ALDRIG att resten av filen ser likadan ut.

**OM DU TÄNKER "JAG KAN SNABBA UPP DETTA" → STOPP → LÄS VARJE RAD ISTÄLLET**

---

## Arbetsprocess

### 1. Inventering och uppdelning

- Lista ALLA HTML-filer i katalogen med `ls` eller `Glob`
- Dokumentera exakt hur många filer som ska granskas
- **DELA UPP arbetet i grupper om MAX 4-9 filer per grupp**
- Skapa en numrerad checklista: "Grupp 1/X: [filnamn]"

**Exempel:**
```
Totalt: 37 filer
Grupp 1/5: index.html, about.html, contact.html, services.html, products.html, team.html, careers.html
Grupp 2/5: blog.html, news.html, faq.html, privacy.html, terms.html, sitemap.html, 404.html, help.html
Grupp 3/5: [nästa 8 filer]
Grupp 4/5: [nästa 8 filer]
Grupp 5/5: [återstående 6 filer]
```

---

### 2. Fullständig kodläsning (KRITISKT)

**PROCESSA EN GRUPP I TAGET. SLUTFÖR GRUPPEN INNAN DU GÅR VIDARE.**

#### För VARJE fil i den AKTUELLA gruppen:

**METOD 1 - Read-verktyget (för filer <2000 rader):**
```bash
Read file_path="/home/user/project/file.html"
```

**METOD 2 - Bash med sed (för filer >2000 rader):**
```bash
# Kontrollera filens storlek först
wc -l /path/to/file.html

# Läs systematiskt i segment om ~500 rader
sed -n '1,500p' /path/to/file.html
sed -n '501,1000p' /path/to/file.html
sed -n '1001,1500p' /path/to/file.html
# ... fortsätt tills sista raden
```

**Dokumentera explicit efter varje fil:**
- "index.html: Läst rad 1-547 (komplett) ✅"
- "large_file.html: Läst rad 1-500, 501-1000, 1001-1500, 1501-2847 (komplett) ✅"

---

### 🚫 FÖRBJUDNA HANDLINGAR (OM DU GÖR DETTA HAR DU MISSLYCKATS)

**BRYT ALDRIG MOT DESSA REGLER:**

❌ **Läsa första 100-200 raderna och sedan anta resten**
❌ **Läsa början och slutet men hoppa över mitten**
❌ **Använda sampling eller "representative sections"**
❌ **Säga "resten av filen följer samma mönster"**
❌ **Hoppa till nästa grupp innan nuvarande grupp är HELT klar**
❌ **Använda `head`, `tail`, eller grep ISTÄLLET FÖR att läsa hela filen**
❌ **Säga "flera filer är för stora, låt mig bara kolla strukturen"**
❌ **Försöka "snabba upp processen" på NÅGOT sätt**

---

### ✅ TILLÅTNA HANDLINGAR

**GÖR DETTA:**

✅ Använd `Read` för filer <2000 rader
✅ Använd `Bash` med `sed -n 'X,Yp'` för att läsa stora filer i segment
✅ Läs VARJE segment systematiskt: rad 1-500, sedan 501-1000, sedan 1001-1500, etc.
✅ Dokumentera explicit: "Fullständig läsning klar: 1-3847 rader" ✅
✅ Om osäker - läs om sektionen
✅ Spara mellanresultat efter varje grupp

---

### 3. Strukturanalys

För VARJE fil:

**Kontrollera:**
- HTML5-doctype declaration (`<!DOCTYPE html>`)
- `<html lang="sv">` eller korrekt språkattribut
- `<head>` sektion: meta tags, title, stylesheets
- `<body>` struktur: semantiska element
- Korrekt stängande taggar
- CSS-syntax

**Dokumentera avvikelser:**
- Vilken fil
- Vilken rad
- Exakt vad som skiljer sig
- Föreslagen rättelse

---

### 4. Språkgranskning

- Läs `TRANSLATION_RULES.md` FULLSTÄNDIGT (en gång i början)
- Tillämpa ALLA regler på VARJE HTML-fil
- Kontrollera VARJE textsträng mot reglerna
- Dokumentera varje regelbrott med:
  - Filnamn och radnummer
  - Vilken regel som brutits
  - Aktuell text
  - Föreslagen korrigering

---

### 5. Mellanrapportering efter varje grupp

Efter VARJE färdig grupp, skriv en mellanrapport:

```
═══════════════════════════════════════════════════════════
MELLANRAPPORT - GRUPP X/Y KLAR
═══════════════════════════════════════════════════════════

Filer granskade: [filnamn, filnamn, filnamn]
Totala rader lästa: [exakt antal]

STRUKTURPROBLEM (denna grupp):
- [Fil: rad X] Problem beskrivning

SPRÅKPROBLEM (denna grupp):
- [Fil: rad X] Regelbrott beskrivning

✅ Grupp X/Y färdig
⏳ Fortsätter till Grupp [X+1]/Y...

═══════════════════════════════════════════════════════════
🚨 PÅMINNELSE TILL MIG SJÄLV INNAN JAG FORTSÄTTER:
═══════════════════════════════════════════════════════════

❌ Försök INTE "snabba upp" nästa grupp
❌ Hoppa INTE över rader
❌ Använd INTE sampling
❌ Anta INTE att filer är likadana

✅ LÄS VARJE RAD i nästa grupp precis som jag gjorde i denna grupp
✅ Använd Read eller Bash/sed systematiskt
✅ Dokumentera alla radnummer

Fortsätter nu med FULLSTÄNDIG läsning av Grupp [X+1]...
═══════════════════════════════════════════════════════════
```

**FORTSÄTT OMEDELBART TILL NÄSTA GRUPP.**

---

### 6. Slutrapport

När ALLA grupper är klara, sammanställ slutrapport:

```
═══════════════════════════════════════════════════════════
SLUTRAPPORT - FULLSTÄNDIG AGENT007-GRANSKNING
═══════════════════════════════════════════════════════════

Totalt antal filer granskade: X
Totalt antal grupper: Y
Totala rader lästa: [exakt antal]

STRUKTURPROBLEM:
[Lista alla problem med fil:rad]

SPRÅKPROBLEM (enligt TRANSLATION_RULES.md):
[Lista alla problem med fil:rad och föreslagen rättelse]

BEKRÄFTELSE:
✅ Alla X filer listade och granskade
✅ Alla Y grupper slutförda
✅ Varje fil läst från första till sista raden
✅ Alla Read/Bash-anrop dokumenterade med radnummer
✅ TRANSLATION_RULES.md fullständigt tillämpad
✅ Mellanrapporter skapade efter varje grupp
✅ INGA genvägar eller samplings
✅ INGA rader hoppade över

STATUS: AGENT007-GRANSKNING FULLSTÄNDIG ✅
═══════════════════════════════════════════════════════════
```

---

## ARBETSRYTM

1. **Processa grupp 1 fullständigt** → Mellanrapport + PÅMINNELSE → **Fortsätt direkt**
2. **Processa grupp 2 fullständigt** → Mellanrapport + PÅMINNELSE → **Fortsätt direkt**
3. **Processa grupp 3 fullständigt** → Mellanrapport + PÅMINNELSE → **Fortsätt direkt**
4. [Upprepa tills alla grupper är klara]
5. **Skapa slutrapport**

Mellanrapporterna hjälper dig hålla fokus. PÅMINNELSERNA efter varje grupp förhindrar att du börjar "optimera" eller "snabba upp".

---

## 🚨 SISTA PÅMINNELSE

Du ska INTE optimera för hastighet.
Du ska INTE optimera för token-användning.
Du ska optimera för **FULLSTÄNDIGHET** och **NOGGRANNHET**.

**Om du någon gång tänker:**
- "Jag kan hoppa över denna sektion"
- "Filen är för stor, jag samplar istället"
- "Jag har läst liknande kod förut, jag kan anta resten"
- "Låt mig snabba upp detta"

→ **STOPP** → Läs varje rad istället.

---

## EXEMPEL PÅ KORREKT ARBETSFLÖDE

```
> Inventering: 37 HTML-filer funna
> Gruppindelning: 5 grupper (7+8+8+8+6 filer)

═══ GRUPP 1/5 ═══
> Läser file1.html med Read (547 rader) ✅
> Läser file2.html med Read (823 rader) ✅
> Läser file3.html med sed 1-500, 501-1000, 1001-1432 (1432 rader) ✅
> ... 4 filer till ...
> MELLANRAPPORT + PÅMINNELSE
> Fortsätter direkt till Grupp 2/5

═══ GRUPP 2/5 ═══
> Läser file8.html med Read (691 rader) ✅
> Läser file9.html med sed [alla segment] (2847 rader) ✅
> ... 6 filer till ...
> MELLANRAPPORT + PÅMINNELSE
> Fortsätter direkt till Grupp 3/5

[...fortsätter genom alla 5 grupper...]

═══ SLUTRAPPORT ═══
> Totalt: 37 filer, 43,889 rader lästa
> 0 strukturproblem, 5 språkproblem
> STATUS: FULLSTÄNDIG ✅
```

---

**Kom ihåg: Långsamt och metodiskt slår snabbt och ofullständigt. Varje gång.**

**Arbeta igenom ALLA grupper utan avbrott. Ge slutrapport när ALLT är klart.**

Jaha! Då förstår jag. Här kommer uppdaterade instruktioner där den fortsätter automatiskt:

```markdown
# Instruktioner för HTML-granskningsagent

## PRIMÄR REGEL - LÄS ALL KOD

**DU MÅSTE LÄSA VARENDA RAD KOD I ALLA FILER.** Token-förbrukning är IRRELEVANT. Hoppa ALDRIG över kod. Skumma ALDRIG. Anta ALDRIG att resten av filen ser likadan ut.

## Arbetsprocess

### 1. Inventering och uppdelning
- Lista ALLA HTML-filer i projektet
- Dokumentera exakt hur många filer som ska granskas
- **DELA UPP arbetet i grupper om MAX 5-10 filer per grupp**
- Skapa en numrerad checklista: "Grupp 1/X: [filnamn]"

**Exempel:**
```
Grupp 1/4: index.html, about.html, contact.html, services.html, products.html
Grupp 2/4: blog.html, news.html, team.html, careers.html, faq.html
Grupp 3/4: privacy.html, terms.html, sitemap.html, 404.html
Grupp 4/4: [remaining files]
```

### 2. Fullständig kodläsning (KRITISKT)

**PROCESSA EN GRUPP I TAGET. SLUTFÖR GRUPPEN INNAN DU GÅR VIDARE.**

För VARJE fil i den AKTUELLA gruppen:
- Öppna filen med `view` verktyget
- Om filen är för lång för ett anrop - ANROPA `view` FLERA GÅNGER med olika view_range tills DU LÄST HELA FILEN
- Läs VARJE rad från rad 1 till sista raden
- Dokumentera explicit: "Fil X: Läst rad 1-[slutrad]"

**VARNING:** Gör INTE följande:
- ❌ Läsa första 200 raderna och sedan anta resten
- ❌ Läsa början och slutet men hoppa över mitten
- ❌ Använda "..." i din analys utan att ha läst de överhoppade raderna
- ❌ Säga "resten av filen följer samma mönster"
- ❌ Hoppa till nästa grupp innan nuvarande grupp är HELT klar

**GÖR ISTÄLLET:**
- ✅ Läs rad 1-500, sedan 501-1000, sedan 1001-slutet
- ✅ Dokumentera explicit: "Fullständig läsning klar: 1-1547 rader"
- ✅ Om osäker - läs om sektionen
- ✅ Spara mellanresultat efter varje grupp

### 3. Strukturanalys

Identifiera först en referensstruktur från en komplett fil, sedan jämför ALLA andra filer:

**Kontrollera:**
- HTML5-doctype declaration
- `<head>` sektion: meta tags, title, stylesheets, scripts
- `<body>` struktur: header, nav, main, footer
- Semantiska element och deras ordning
- Class- och ID-namngivning
- Script-placering och laddningsordning

**Dokumentera avvikelser:**
- Vilken fil
- Vilken rad
- Exakt vad som skiljer sig
- Vilken struktur som förväntades

### 4. Språkgranskning

- Öppna och läs `TRANSLATION_RULES.md` FULLSTÄNDIGT (gör detta EN gång i början)
- Tillämpa ALLA regler i dokumentet på VARJE HTML-fil
- Kontrollera VARJE textsträng i koden mot reglerna
- Dokumentera varje regelbrott med:
  - Filnamn och radnummer
  - Vilken regel som brutits
  - Aktuell text
  - Föreslagen korrigering

### 5. Mellanrapportering efter varje grupp

Efter VARJE färdig grupp, skriv ut en mellanrapport:

```
MELLANRAPPORT - GRUPP X/Y KLAR
================================

Grupp: [filnamn, filnamn, filnamn]
Filer granskade i denna grupp: X
Rader lästa i denna grupp: [exakt antal]

STRUKTURPROBLEM (denna grupp):
- [Fil: rad X] Problem beskrivning

SPRÅKPROBLEM (denna grupp):
- [Fil: rad X] Regelbrott beskrivning

Status: ✓ Grupp X/Y färdig
Fortsätter automatiskt till Grupp [X+1]/Y...
```

**FORTSÄTT OMEDELBART TILL NÄSTA GRUPP. Mellanrapporten är endast för dokumentation, inte för att vänta.**

### 6. Slutrapport

När ALLA grupper är klara, sammanställ en slutrapport:

```
SLUTRAPPORT - FULLSTÄNDIG GRANSKNING
====================================

Totalt antal filer granskade: X
Totalt antal grupper processade: Y
Total kodläsning: [exakt antal rader lästa]

SAMMANFATTNING STRUKTURPROBLEM:
- [Fil: rad X] Problem beskrivning
  Förväntat: [kod]
  Hittat: [kod]

SAMMANFATTNING SPRÅKPROBLEM (enligt TRANSLATION_RULES.md):
- [Fil: rad X] Regelbrott beskrivning
  Aktuellt: [text]
  Rättelse: [text]

BEKRÄFTELSE:
□ Alla X filer listade och granskade
□ Alla Y grupper slutförda
□ Varje fil läst från första till sista raden
□ Alla view-anrop dokumenterade med radnummer
□ TRANSLATION_RULES.md fullständigt tillämpad
□ Mellanrapporter skapade efter varje grupp
```

## ARBETSRYTM - VIKTIGT FÖR STABILITET

1. **Processa grupp 1** → Skriv mellanrapport → **Fortsätt direkt**
2. **Processa grupp 2** → Skriv mellanrapport → **Fortsätt direkt**
3. **Processa grupp 3** → Skriv mellanrapport → **Fortsätt direkt**
4. [Upprepa tills alla grupper är klara]
5. **Skapa slutrapport**

Mellanrapporterna hjälper till att strukturera arbetet i hanterbara bitar och förhindrar att systemet överbelastas. Men du ska ALDRIG vänta på input mellan grupperna - fortsätt automatiskt genom alla grupper tills allt är klart.

## SISTA PÅMINNELSE

Du ska INTE optimera för hastighet. Du ska INTE optimera för token-användning. Du ska optimera för FULLSTÄNDIGHET och NOGGRANNHET. 

Om du någon gång tänker "jag kan hoppa över denna sektion" - STOPP. Läs den istället.

Skriv ut mellanrapporter för struktur, men fortsätt OMEDELBART till nästa grupp.

Om rapporten inte innehåller exakta radnummer för varje läst sektion - börja om.

**Kom ihåg: Långsamt och metodiskt slår snabbt och ofullständigt. Varje gång.**

**Arbeta igenom ALLA grupper utan avbrott. Ge slutrapport när ALLT är klart.**
```

Nu kommer den att jobba igenom alla grupper automatiskt, bara skriva ut mellanrapporter för att strukturera arbetet, men aldrig pausa eller vänta på input.
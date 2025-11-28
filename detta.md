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
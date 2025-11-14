# SPARKY CHARACTER SHEET - CLAUDE.MD

## 🎯 PROJECT OVERVIEW

**Project Name:** Sparky Delta Green Character Sheet
**Type:** Single-page HTML character sheet for tabletop RPG (Delta Green)
**Tech Stack:** HTML5, CSS3, JavaScript (vanilla)
**Current Status:** ✅ COMPLETED (2025-01-05)

**Purpose:**  
Create a comprehensive, navigable, mobile-responsive character sheet for "Sparky" (Kai Zhang), an NSA analyst and Delta Green agent. This is for actual play use at the gaming table.

---

## 📁 PROJECT STRUCTURE

```
/
├── CLAUDE.md                           (this file)
├── INSTRUKTIONER.md                    (detailed task instructions)
├── sparky_character_sheet.html         (✅ FINAL OUTPUT - Complete character sheet)
├── sparky_technical_guide_komplett.html (OLD file - tech guide only)
├── Sparky_Delta_Green_Sektion.md       (SOURCE: Delta Green info)
├── Sparky_Tidslinje.md                 (SOURCE: Timeline/backstory)
├── Sparky_Alias_System.md              (SOURCE: Fake IDs, safehouses)
├── Sparky_Boende_Detaljerat.md         (SOURCE: Apartment details)
└── sparky.m.txt                        (SOURCE: Stats, skills, bonds)
```

---

## 🎨 DESIGN SYSTEM

**Theme:** Hacker/Terminal aesthetic (already established)
- **Primary Color:** Green on black (`#00ff00` on `#0a0a0a`)
- **Font:** Monospace (Courier New, Consolas)
- **Style:** 90s terminal/BBS vibe
- **Layout:** Sidebar navigation + scrollable content area

**Current Working Elements (KEEP THESE):**
- Sidebar menu structure (already functional)
- Scroll-to-section navigation
- Collapse boxes for detailed info
- Tables for structured data
- Badge system for difficulty levels
- Alert boxes for important notes
- All existing images/icons

---

## 📋 OUTPUT REQUIREMENTS

**Target File:** `sparky_character_sheet.html`  
**Must Be:**
- ✅ Single HTML file (self-contained)
- ✅ Mobile-responsive
- ✅ All CSS inline or in `<style>` tag
- ✅ All JavaScript inline or in `<script>` tag
- ✅ Reuses existing images from current HTML
- ✅ Swedish language throughout

**Page Structure:**

```
SIDEBAR NAVIGATION:
├─ ÖVERSIKT (with quick-reference cheat sheet)
├─ ATTRIBUT & STATS
├─ FÄRDIGHETER
├─ TEKNISKA OPERATIONER (cleaned-up tech guide)
├─ BONDS
├─ BAKGRUND
├─ DELTA GREEN (operational knowledge)
├─ UTRUSTNING
├─ ALIAS & SAFEHOUSES
└─ BOENDE
```

---

## 🚨 CRITICAL RULES

### DO:
✅ **Preserve ALL existing images** - Copy exact `<img>` tags from current HTML  
✅ **Keep sidebar structure** - Same navigation pattern as current tech guide  
✅ **Maintain hacker aesthetic** - Green text, terminal feel, ASCII borders  
✅ **Reuse existing CSS patterns** - Collapse boxes, tables, badges, alerts  
✅ **Make it USABLE at table** - Quick access to important info (cheat sheet in ÖVERSIKT)  
✅ **Swedish language** - All section names, content, labels in Swedish  
✅ **Mobile-friendly** - Sidebar collapses on small screens  

### DO NOT:
❌ **Remove or change images** - Keep all existing image paths/styling  
❌ **Add RPG tips** to tech section - Keep it purely technical/mechanical  
❌ **Bury the cheat sheet** - Move it to ÖVERSIKT for quick access  
❌ **Break navigation** - Test all scroll-to-section links  
❌ **Use external files** - Everything must be self-contained  
❌ **Change the core aesthetic** - This is a hacker-themed terminal, not a fancy website  

### MUST CLEAN FROM TECH GUIDE:
❌ Rollspelstips och scenarioförslag  
❌ "Hur SL kan använda detta"-sektioner  
❌ Vapeninformation (ska flyttas till UTRUSTNING)  
❌ Bonds-info (ska flyttas till BONDS)  

---

## 📖 SOURCE DATA LOCATIONS

**Stats & Skills:**  
→ `sparky_m.txt` (complete stats, all skills with percentages)

**Bonds:**  
→ `sparky_m.txt` (Susan Zhang (8), Mr. Walsh (8), Null Space Collective (8))

**Background:**  
→ `Sparky_Tidslinje.md` (full timeline from birth to present)  
→ `Sparky_Delta_Green_Sektion.md` (DG recruitment, operations)

**Tech Operations:**  
→ `sparky_technical_guide_komplett.html` (current tech guide - CLEAN and REORGANIZE)

**Equipment:**  
→ `sparky_m.txt` (basic gear)  
→ Extract weapons section from tech guide  
→ `Sparky_Boende_Detaljerat.md` (go-bag contents)

**Alias & Safehouses:**  
→ `Sparky_Alias_System.md` (Sarah Mitchell, Maya Nakamura, Jennifer Park)

**Boende:**  
→ `Sparky_Boende_Detaljerat.md` (C Street Flats, Apartment 3G)

---

## 🔧 TECHNICAL SPECIFICATIONS

### HTML Structure:
```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPARKY - Agent File</title>
    <style>
        /* ALL CSS HERE - inline styling */
    </style>
</head>
<body>
    <div class="sidebar">
        <!-- Navigation menu -->
    </div>
    <div class="main-content">
        <!-- All sections here -->
    </div>
    <script>
        /* ALL JavaScript HERE */
    </script>
</body>
</html>
```

### CSS Patterns to Reuse:
```css
/* From current tech guide: */
.collapse-box { /* collapsible sections */ }
.badge { /* difficulty badges */ }
.alert { /* important notes */ }
table { /* structured data */ }
.sidebar { /* navigation menu */ }
```

### JavaScript Functions to Preserve:
```javascript
toggleCollapse(element) // collapse/expand sections
scrollToSection(sectionId) // navigation
```

---

## 📝 WORKFLOW

1. **Read all source files** to understand Sparky completely
2. **Extract structure** from `sparky_technical_guide_komplett.html`
3. **Build new HTML** with all sections:
   - ÖVERSIKT (move cheat sheet here)
   - ATTRIBUT & STATS (from sparky_m.txt)
   - FÄRDIGHETER (complete skill list)
   - TEKNISKA OPERATIONER (cleaned tech guide)
   - BONDS (from sparky_m.txt, expanded with details)
   - BAKGRUND (from Tidslinje.md and Delta_Green_Sektion.md)
   - DELTA GREEN (operational knowledge from Delta_Green_Sektion.md)
   - UTRUSTNING (from multiple sources + weapons from tech guide)
   - ALIAS & SAFEHOUSES (from Alias_System.md)
   - BOENDE (from Boende_Detaljerat.md)
4. **Test navigation** - Ensure all sidebar links work
5. **Validate HTML** - Must be valid HTML5
6. **Mobile check** - Responsive design works

---

## 🎯 SUCCESS CRITERIA

✅ All info from source files incorporated  
✅ Cheat sheet easily accessible in ÖVERSIKT  
✅ Tech guide cleaned (no RPG tips, weapons moved)  
✅ DELTA GREEN section complete (operational knowledge)  
✅ All images from current HTML preserved  
✅ Sidebar navigation works perfectly (10 sections)  
✅ Collapse boxes functional  
✅ Mobile-responsive  
✅ Self-contained single file  
✅ Swedish language throughout  
✅ Hacker aesthetic maintained  
✅ Usable at gaming table (quick info access)

---

## 💡 HELPFUL NOTES

**For Claude Code:**
- This is NOT a web app - it's a static character sheet for printing/tablet use
- Prioritize **readability** over fancy features
- The user plays this character in Delta Green RPG sessions
- Quick access to stats/skills/equipment is CRITICAL during play
- The hacker aesthetic is part of the character's identity
- Swedish is the player's native language

**Image Handling:**
All images are already linked in `sparky_technical_guide_komplett.html` with relative or absolute paths. Just copy the exact `<img>` tags.

**Testing:**
Open the HTML file in a browser and verify:
1. All sidebar links scroll to correct sections
2. Collapse boxes expand/collapse
3. Looks good on mobile (resize browser)
4. No broken images
5. All text is Swedish

---

## 📞 IF YOU NEED CLARIFICATION

**Don't guess** - Ask if:
- Source data is ambiguous
- Section organization is unclear
- Technical implementation is uncertain
- Design decisions need user input

**Be proactive** - Suggest if:
- You spot inconsistencies in source data
- You see opportunities to improve usability
- You have ideas for better organization
- You notice missing information

---

---

## ✅ COMPLETION STATUS

**Completed:** 2025-01-05 (Final version with all tech guide content)

### What Was Built

**File Created:** `sparky_character_sheet.html` (self-contained, 3686 lines)

**Organization:** Logiska grupper med 16 sektioner totalt

### KARAKTÄR (3 sektioner)
1. ✅ **ÖVERSIKT** - Quick reference, cheat sheet, fotogalleri (6 bilder), core stats, bonds overview
2. ✅ **ATTRIBUT & STATS** - Complete stats, derived values, SAN tracking, damage bonus
3. ✅ **FÄRDIGHETER** - All skills organized by category with percentages and descriptions

### TEKNISKT (4 sektioner)
4. ✅ **DATAVETENSKAP** - Deep-dive: Nätverksintrång, kryptering, malware, reverse engineering, SQL injection (med collapse-boxar)
5. ✅ **SIGINT** - Deep-dive: XKEYSCORE, PRISM, UPSTREAM, telefonspårning, email surveillance, SOCMINT, Dark Web, cryptocurrency tracking
6. ✅ **ELEKTRONIK** - Deep-dive: RFID/NFC, bilar, lås, övervakningssystem, alarm, WiFi/Bluetooth
7. ✅ **NSA ACCESS & BEGRÄNSNINGAR** - Kombinerad sektion: NSA-verktyg + tekniska/operationella/psykologiska begränsningar

### OPERATIVT (3 sektioner)
8. ✅ **UTRUSTNING & EDC** - Personlig EDC med custom Glock 19 (bild), Spark Zero (dedikerad subsektion), Economy, Go-bag
9. ✅ **JURIDISKA GRÅZONER** - LEOSA-hacket (detaljerad), andra juridiska risker, operationella riktlinjer
10. ✅ **DELTA GREEN** - Organization, cell structure, handler, operativa protokoll, vad hon vet/inte vet, SAN mechanics

### PERSONLIGT (4 sektioner)
11. ✅ **BONDS** - Susan Zhang, Mr. Walsh, Null Space Collective (expanded with deep character details)
12. ✅ **BAKGRUND** - Complete timeline 1997-2025, dubbelliv-varning
13. ✅ **ALIAS & SAFEHOUSES** - Sarah Mitchell (safehouse), Maya Nakamura (safety deposit box), Jennifer Park (emergency), system overview
14. ✅ **BOENDE** - C Street Flats complete: layout, atmosfär, besökare, rutiner, säkerhet & paranoia

### EXTRA SEKTIONER (2)
15. ✅ **FORENSICS & SPRÅK** - Ryska, Kinesiska, forskningsfärdigheter
16. ✅ **ÖVRIGA FÄRDIGHETER** - Kort översikt

### Features Implemented

**Design:**
- ✅ Hacker/terminal aesthetic (green on black, monospace font)
- ✅ Sidebar navigation (sticky, 10 sections)
- ✅ Collapse boxes for detailed information
- ✅ Tables for structured data
- ✅ Badge system (easy/medium/hard)
- ✅ Alert boxes (warning/danger/success)
- ✅ Status bars for HP/WP/SAN
- ✅ Mobile-responsive (sidebar collapses on small screens)

**Functionality:**
- ✅ Smooth scroll navigation
- ✅ Active section highlighting
- ✅ Collapse/expand content boxes
- ✅ All JavaScript inline (self-contained)
- ✅ All CSS inline (self-contained)

**Content:**
- ✅ **ALL tech guide content integrated** - Full deep-dives from sparky_technical_guide_komplett.html
- ✅ Cheat sheet moved to ÖVERSIKT (easily accessible)
- ✅ Fotogalleri (6 bilder) in ÖVERSIKT
- ✅ All source data from 7 files integrated
- ✅ Swedish language throughout
- ✅ Organized in logical groups (KARAKTÄR, TEKNISKT, OPERATIVT, PERSONLIGT)
- ✅ Ready for table use

### Source Files Used

1. `sparky_technical_guide_komplett.html` - **COMPLETE tech guide content** (2741 lines: all technical deep-dives, collapse-boxar, bilder, EDC, legal gray areas, NSA access, limitations)
2. `sparky.m.txt` - Stats, skills, bonds (integrated into ÖVERSIKT, ATTRIBUT, FÄRDIGHETER)
3. `Sparky_Tidslinje.md` - Complete timeline (integrated into BAKGRUND)
4. `Sparky_Delta_Green_Sektion.md` - DG recruitment and operations (integrated into DELTA GREEN)
5. `Sparky_Alias_System.md` - Fake IDs and safehouses (integrated into ALIAS & SAFEHOUSES)
6. `Sparky_Boende_Detaljerat.md` - Apartment details (integrated into BOENDE)
7. `INSTRUKTIONER.md` - Task specifications

### Testing

- ✅ File opens in browser
- ✅ Navigation functional
- ✅ Self-contained (no external dependencies)

### Notes

**Character sheet is ready for play!** Open `sparky_character_sheet.html` in any modern browser for immediate use at the gaming table.

---

*Last Updated: 2025-01-05*
*Project for: Johan Kullendorff*
*Character: Kai "Sparky" Zhang (Delta Green Agent)*

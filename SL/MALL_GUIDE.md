# SL-SIDORNAS STANDARDMALL

**Skapad:** 2025-11-21
**Version:** 1.0
**Syfte:** Standardiserad mall för alla nya speledarsidor i /SL/

---

## 1. CSS-STANDARD

### Typografi
```css
body {
    font-family: 'Courier New', Courier, monospace;
    line-height: 1.6;
}
```
**Motivering:** "Terminal/klassificerad dokument"-estetik som passar Delta Green-temat.

### Färgpalett
```css
:root {
    /* Bakgrunder */
    --bg-dark: #0a0f0f;
    --bg-darker: #050808;
    --bg-panel: #0d1414;

    /* Text */
    --text: #d1d5db;
    --text-dim: #6b7280;

    /* Kanter */
    --border: #1a2332;

    /* Accent-färger */
    --accent-primary: #4a90a4;      /* Steel blue - huvudfärg */
    --accent-secondary: #e89a3c;    /* Warm orange - highlights */

    /* Status-färger */
    --classified: #ff4444;          /* Röd - fara/klassificerat */
    --success: #4ade80;             /* Grön - framgång */
    --warning: #d4a520;             /* Gul - varning */

    /* Mythos-specifika (om behövs) */
    --yithian: #4a90a4;
    --nyogtha: #8b4789;
}
```

---

## 2. LAYOUT-STRUKTURER

### Layout A: Sidebar Navigation (för referenssidor)
Använd för: npcs.html, locations.html, mythos.html, etc.

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sidtitel - TRIP 19 SL-Kontrollpanel</title>
    <style>
        /* ... CSS här ... */
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <div class="header-content">
            <div class="logo">▲ TRIP 19 // BLACK MADONNA</div>
            <div class="status">
                <span>SL-KONTROLLPANEL</span>
            </div>
        </div>
    </div>

    <!-- Classified Banner (om relevant) -->
    <div class="classified-banner">
        KLASSIFICERAD // DELTA GREEN ENDAST FÖR SL // OPERATION TRIP 19
    </div>

    <!-- Main Container -->
    <div class="container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <nav class="nav-section">
                <div class="nav-title">Navigering</div>
                <a href="index.html" class="nav-link">Översikt</a>
                <a href="timeline.html" class="nav-link">Tidslinje</a>
                <!-- ... fler länkar ... -->
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <section class="section">
                <h2>Rubrik</h2>
                <p>Innehåll...</p>
            </section>
        </main>
    </div>

    <!-- Footer -->
    <div class="footer">
        DELTA GREEN // TRIP 19: BLACK MADONNA // SL-MATERIAL
    </div>
</body>
</html>
```

**CSS för Layout A:**
```css
.container {
    max-width: 1400px;
    margin: 2rem auto;
    padding: 0 2rem;
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 2rem;
}

.sidebar {
    position: sticky;
    top: 100px;
    height: fit-content;
}

@media (max-width: 1024px) {
    .container {
        grid-template-columns: 1fr;
    }
    .sidebar {
        position: relative;
        top: 0;
    }
}
```

### Layout B: Full Width (för scener/scenarios)
Använd för: chapter-sidor, scener, infiltration routes, etc.

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scen/Kapitel Titel</title>
    <style>
        /* ... CSS här ... */
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <div class="header-content">
            <div class="logo">SCEN TITEL</div>
            <a href="index.html" class="back-link">← Tillbaka till Kontrollpanel</a>
        </div>
    </div>

    <!-- Container -->
    <div class="container">
        <section class="section">
            <h2>Huvudrubrik</h2>
            <!-- Innehåll -->
        </section>
    </div>
</body>
</html>
```

**CSS för Layout B:**
```css
.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2rem 4rem 2rem;
}
```

---

## 3. STANDARDKOMPONENTER

### Header
```css
.header {
    background: var(--bg-darker);
    border-bottom: 2px solid var(--accent-primary);
    padding: 1.5rem 2rem;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--accent-primary);
    letter-spacing: 2px;
    text-shadow: 0 0 10px rgba(74, 144, 164, 0.3);
}
```

### Section/Panel
```css
.section {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 2rem;
    margin-bottom: 2rem;
}

.section h2 {
    color: var(--accent-primary);
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border);
    letter-spacing: 1px;
    text-transform: uppercase;
}

.section h3 {
    color: var(--accent-secondary);
    font-size: 1.3rem;
    margin: 1.5rem 0 1rem 0;
}
```

### Varningsboxar
```css
/* Röd varning */
.warning-box {
    background: linear-gradient(135deg, #2a0a0a 0%, #1a0505 100%);
    border: 2px solid var(--classified);
    border-radius: 6px;
    padding: 1rem;
    margin: 1rem 0;
}

.warning-box strong {
    color: var(--classified);
}

/* Grön framgång */
.success-box {
    background: linear-gradient(135deg, #0a2a0a 0%, #051a05 100%);
    border: 2px solid var(--success);
    border-radius: 6px;
    padding: 1rem;
    margin: 1rem 0;
}

/* Blå info */
.info-box {
    background: rgba(74, 144, 164, 0.1);
    border: 2px solid var(--accent-primary);
    border-radius: 6px;
    padding: 1rem;
    margin: 1rem 0;
}

/* GM-notis */
.gm-note {
    background: var(--bg-darker);
    border-left: 4px solid var(--accent-secondary);
    padding: 1rem;
    margin: 1rem 0;
    font-style: italic;
}

.gm-note::before {
    content: "GM: ";
    color: var(--accent-secondary);
    font-weight: bold;
    font-style: normal;
}
```

### Scen-box (narrativ text)
```css
.scene-box {
    background: var(--bg-darker);
    border-left: 4px solid var(--accent-primary);
    padding: 1.5rem;
    margin: 1rem 0;
    font-style: italic;
    color: #c9d1d9;
}

.scene-box strong {
    color: var(--accent-primary);
    font-style: normal;
}
```

### Stat Block (NPC/mekanik)
```css
.stat-block {
    background: var(--bg-darker);
    border: 2px solid var(--border);
    border-radius: 6px;
    padding: 1.5rem;
    margin: 1rem 0;
}

.stat-block h4 {
    color: var(--accent-primary);
    font-size: 1.2rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.5rem;
}

.stat-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 0.5rem;
    margin: 0.5rem 0;
}

.stat-item {
    background: var(--bg-panel);
    padding: 0.5rem;
    text-align: center;
    border: 1px solid var(--border);
}

.stat-item strong {
    color: var(--accent-secondary);
    display: block;
    font-size: 0.8rem;
}
```

### Tabeller
```css
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
}

th {
    background: var(--bg-darker);
    color: var(--accent-primary);
    padding: 0.75rem;
    text-align: left;
    border: 1px solid var(--border);
    font-weight: bold;
}

td {
    padding: 0.75rem;
    border: 1px solid var(--border);
}

tr:nth-child(even) {
    background: rgba(255, 255, 255, 0.02);
}
```

### Badges/Tags
```css
.badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 4px;
    font-size: 0.85rem;
    font-weight: bold;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}

.badge.sl-only {
    background: var(--classified);
    color: white;
}

.badge.player-can-learn {
    background: var(--accent-primary);
    color: white;
}

.badge.never-reveal {
    background: #333;
    color: #888;
}
```

### Navigation Links
```css
.nav-section {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent-primary);
    border-radius: 4px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.nav-title {
    color: var(--accent-primary);
    font-size: 0.75rem;
    font-weight: bold;
    letter-spacing: 1.5px;
    margin-bottom: 1rem;
    text-transform: uppercase;
}

.nav-link {
    display: block;
    padding: 0.6rem 1rem;
    color: var(--text);
    text-decoration: none;
    border-left: 2px solid transparent;
    transition: all 0.2s;
    font-size: 0.9rem;
}

.nav-link:hover {
    background: rgba(74, 144, 164, 0.1);
    border-left-color: var(--accent-primary);
    color: var(--accent-primary);
    padding-left: 1.2rem;
}

.nav-link.active {
    background: rgba(74, 144, 164, 0.15);
    border-left-color: var(--accent-primary);
    color: var(--accent-primary);
}
```

### Back Link
```css
.back-link {
    color: var(--accent-primary);
    text-decoration: none;
    padding: 0.5rem 1.5rem;
    border: 1px solid var(--accent-primary);
    border-radius: 4px;
    transition: all 0.2s;
    font-size: 0.9rem;
}

.back-link:hover {
    background: var(--accent-primary);
    color: var(--bg-dark);
    box-shadow: 0 0 10px rgba(74, 144, 164, 0.5);
}
```

---

## 4. GRID-SYSTEM

### 2-kolumner
```css
.grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    margin: 1.5rem 0;
}

@media (max-width: 768px) {
    .grid-2 {
        grid-template-columns: 1fr;
    }
}
```

### Auto-fit (kort/cards)
```css
.grid-auto {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

@media (max-width: 768px) {
    .grid-auto {
        grid-template-columns: 1fr;
    }
}
```

### Stat Grid (6 kolumner för stats)
```css
.stat-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 0.5rem;
}

@media (max-width: 768px) {
    .stat-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

---

## 5. SPRÅKREGLER

### Svenska UI-element
✅ **Använd svenska för:**
- Navigation: "Navigering", "Översikt", "Tillbaka"
- Status: "SL-Kontrollpanel", "Klassificerad"
- Rubriker: "Kapitel", "Scen"
- Knappar: "Visa mer", "Stäng"
- Beskrivningar och hjälptext

### Engelska undantag
✅ **Behåll engelska för:**
- Egennamn: "Delta Green", "Trip 19", "Volkov"
- Platsnamn: "Leningrad", "Berlin", "Frankfurt"
- Rollspelstermer som är standard: "Session", "Bond"
- CSS-klasser och tekniska termer
- Historiska citat i original

### Exempel:
```html
<!-- RÄTT -->
<h2>Kapitel 2: Skuggor från det förflutna</h2>
<a href="index.html">← Tillbaka till Kontrollpanel</a>
<span class="badge">SL-Kunskap</span>

<!-- FEL -->
<h2>Chapter 2: Shadows from the Past</h2>
<a href="index.html">← Back to Dashboard</a>
<span class="badge">GM-Only</span>
```

---

## 6. FIL- OCH NAMNKONVENTIONER

### Filnamn
- **Gemener (lowercase):** `npcs.html`, `timeline.html`
- **Understreck för mellanslag:** `black_madonna_chapter1.html`
- **Beskrivande:** `russia_infiltration_routes.html`
- **Undvik:** Specialtecken, åäö, mellanslag

### Katalogstruktur
```
/SL/
├── index.html                  (Dashboard/huvudsida)
├── timeline.html               (Tidslinje)
├── npcs.html                   (Karaktärer)
├── mythos.html                 (Mythos-guide)
├── black_madonna_chapter1.html (Kampanjkapitel)
├── CHAPTER2_SCENE_VOLKOV.html  (Specifika scener)
└── CHANGELOG_SL_STANDARDIZATION.md
```

### HTML-struktur
```html
<!DOCTYPE html>
<html lang="sv">  <!-- VIKTIGT: lang="sv" -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beskrivande Titel - TRIP 19 SL-Kontrollpanel</title>
    <style>
        /* Inline CSS här (inga externa stylesheets) */
    </style>
</head>
<body>
    <!-- Innehåll -->
</body>
</html>
```

---

## 7. RESPONSIV DESIGN

### Standard breakpoints
```css
/* Desktop först, sedan tablet och mobil */

/* Tablet */
@media (max-width: 1024px) {
    .container {
        grid-template-columns: 1fr;
    }

    .sidebar {
        position: relative;
        top: 0;
    }
}

/* Mobil */
@media (max-width: 768px) {
    .container {
        padding: 0 1rem 2rem 1rem;
    }

    .grid-2, .grid-auto {
        grid-template-columns: 1fr;
    }

    .stat-grid {
        grid-template-columns: repeat(3, 1fr);
    }

    .logo {
        font-size: 1.2rem;
    }
}

/* Mycket liten mobil */
@media (max-width: 480px) {
    .header {
        padding: 1rem;
    }

    .section {
        padding: 1rem;
    }
}
```

---

## 8. TILLGÄNGLIGHET

### Färgkontrast
- Text på mörk bakgrund: Använd `var(--text)` (#d1d5db)
- Viktig text: Använd `var(--accent-primary)` (#4a90a4)
- Varningar: Använd `var(--classified)` (#ff4444)

### Semantisk HTML
```html
<!-- Använd rätt element -->
<header>...</header>
<nav>...</nav>
<main>...</main>
<section>...</section>
<aside>...</aside>
<footer>...</footer>

<!-- Inte bara div:ar -->
```

### ARIA-labels (vid behov)
```html
<button aria-label="Stäng modal">×</button>
<nav aria-label="Huvudnavigation">...</nav>
```

---

## 9. JAVASCRIPT (minimalt)

### Endast vid behov
```javascript
// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Active nav tracking
window.addEventListener('scroll', () => {
    // ... implementation
});
```

---

## 10. SNABBMALL - KOMPLETT EXEMPEL

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Din Titel - TRIP 19 SL-Kontrollpanel</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg-dark: #0a0f0f;
            --bg-darker: #050808;
            --bg-panel: #0d1414;
            --accent-primary: #4a90a4;
            --accent-secondary: #e89a3c;
            --text: #d1d5db;
            --text-dim: #6b7280;
            --border: #1a2332;
            --classified: #ff4444;
            --success: #4ade80;
            --warning: #d4a520;
        }

        body {
            background: linear-gradient(135deg, var(--bg-darker) 0%, var(--bg-dark) 100%);
            color: var(--text);
            font-family: 'Courier New', Courier, monospace;
            line-height: 1.6;
            min-height: 100vh;
            background-attachment: fixed;
        }

        .header {
            background: var(--bg-darker);
            border-bottom: 2px solid var(--accent-primary);
            padding: 1.5rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }

        .header-content {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--accent-primary);
            letter-spacing: 2px;
        }

        .back-link {
            color: var(--accent-primary);
            text-decoration: none;
            padding: 0.5rem 1.5rem;
            border: 1px solid var(--accent-primary);
            border-radius: 4px;
            transition: all 0.2s;
        }

        .back-link:hover {
            background: var(--accent-primary);
            color: var(--bg-dark);
        }

        .container {
            max-width: 1400px;
            margin: 2rem auto;
            padding: 0 2rem 4rem 2rem;
        }

        .section {
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .section h2 {
            color: var(--accent-primary);
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--border);
            text-transform: uppercase;
        }

        @media (max-width: 768px) {
            .container {
                padding: 0 1rem 2rem 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <div class="logo">DIN SIDTITEL</div>
            <a href="index.html" class="back-link">← Tillbaka till Kontrollpanel</a>
        </div>
    </div>

    <div class="container">
        <section class="section">
            <h2>Huvudrubrik</h2>
            <p>Ditt innehåll här...</p>
        </section>
    </div>
</body>
</html>
```

---

## SAMMANFATTNING

✅ **Font:** `'Courier New', Courier, monospace`
✅ **Primary färg:** `#4a90a4` (steel blue)
✅ **Secondary färg:** `#e89a3c` (warm orange)
✅ **Språk:** Svenska UI, engelska egennamn
✅ **Layout:** Sidebar (referenser) eller Full width (scener)
✅ **Responsive:** 1024px, 768px, 480px breakpoints

**Vid tveksamhet:** Titta på `index.html`, `mythos.html` eller `chapter5_scene0a_baltic_crossing.html` för referens!

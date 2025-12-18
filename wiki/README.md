# Trip 19: Svarta Madonnan - Kampanjwiki

Jekyll-baserad kampanjwiki för Delta Green-kampanjen **Trip 19: The Black Madonna**.

## Översikt

Denna wiki är ett komplement till de befintliga HTML-sidorna och fungerar som ett uppslagsverk/referens för spelledaren.

### Collections

- **NPCs** (`_npcs/`) - Volkov, Magda, de transformerade, historiska personer
- **Platser** (`_platser/`) - Lovettsville, Leningrad, Berlin, Hamburg
- **Händelser** (`_handelser/`) - Flight 19, Leningrad 1942, nyckeltidpunkter
- **Mythos** (`_mythos/`) - Black Madonna, Yithian-kraft, Type-VII/VIII
- **Kapitel** (`_kapitel/`) - Black Madonna kapitel 1-6 synopsis

## Lokal utveckling

### Förutsättningar

- Ruby (2.7+)
- Bundler

### Installation

```bash
cd wiki
bundle install
```

### Kör lokalt

```bash
bundle exec jekyll serve
```

Besök: `http://localhost:4000/trip19/`

## GitHub Pages Deployment

### Setup

1. Skapa nytt repository eller branch för wikin
2. Pusha `wiki/` innehållet till repo
3. Aktivera GitHub Pages i repository settings
4. Välj source: main branch, root folder
5. Site kommer att vara tillgänglig på: `https://kullendorff.github.io/trip19-wiki/`

### Uppdatera innehåll

```bash
cd wiki
# Redigera markdown-filer i _npcs/, _platser/, etc.
git add .
git commit -m "Uppdatera wiki-innehåll"
git push
```

GitHub Pages bygger automatiskt om siten vid varje push.

## Struktur

```
wiki/
├── _config.yml          # Jekyll-konfiguration
├── Gemfile              # Ruby-dependencies
├── index.md             # Startsida
├── _npcs/               # NPC-entries
├── _platser/            # Plats-entries
├── _handelser/          # Händelse-entries
├── _mythos/             # Mythos-entries
├── _kapitel/            # Kapitelsynopser
├── _layouts/            # HTML-layouts
│   ├── default.html
│   ├── npc.html
│   ├── plats.html
│   ├── handelse.html
│   ├── mythos.html
│   └── kapitel.html
└── assets/
    └── css/
        └── style.css    # Delta Green-tema
```

## Lägga till nytt innehåll

### Skapa ny NPC

```bash
cd _npcs
# Skapa ny fil: namn-efternamn.md
```

**Exempel:**

```yaml
---
layout: npc
namn: "Ernst Lundeen"
alias: ["Senator Lundeen"]
status: "död"
roll: "Senator Minnesota, isolationist"
kopplingar: ["Flight 19", "Nazi-propaganda", "Type-VII fragment"]
platser: ["Washington DC", "Lovettsville"]
hemligheter: true
---

# ERNST LUNDEEN

**Senator från Minnesota**

## GRUNDINFO
...
```

### Skapa ny plats

Samma process som NPC, använd layout: `plats`

### Teman och styling

Mörkt Delta Green-tema i `assets/css/style.css`:
- Grön/mörkgrå färgpalett
- Monospace font (Courier New)
- Taktisk/operativ känsla

## Länkar till huvudprojektet

Från befintliga HTML-sidor, länka till wikin:

```html
<a href="https://kullendorff.github.io/trip19-wiki/">📖 Kampanjwiki</a>
```

## Underhåll

- **NPCs:** Lägg till nya när de introduceras i kampanjen
- **Platser:** Dokumentera nya locations
- **Händelser:** Uppdatera tidslinje vid behov
- **Mythos:** SL-kunskap, lägg endast till när relevant
- **Kapitel:** Synopser efter sessioner

## OBS

- Denna wiki är **SL-material** - innehåller spoilers
- Publikt tillgänglig (GitHub Pages) men spelarna ska hålla sig borta
- Komplement till huvudprojektet, inte ersättning

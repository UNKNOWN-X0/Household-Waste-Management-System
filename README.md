# Household Waste Management System — Thailand

[![Live site](https://img.shields.io/badge/live%20site-GitHub%20Pages-2ea44f?logo=github)](https://unknown-x0.github.io/Household-Waste-Management-System/)
[![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

A proposal website adapting **Germany's 4-stream waste model** (Bioabfall · Papier · Wertstoff · Restmüll) to Thai households: their infrastructure, the saleng economy, and the tropical climate. It covers sorting guides, Bokashi composting, local recycling routes, a four-week rollout plan, and printable Thai labels.

**[Open the live site →](https://unknown-x0.github.io/Household-Waste-Management-System/)**

## What's inside

| Tab | Content |
| --- | --- |
| **Overview** | Hero summary, Germany → Thailand stream mapping table |
| **5 Streams** | Bin specs, Yes/No sorting lists, bag colours, bin sizes |
| **Organic / Bokashi** | 4-step Bokashi guide, comparison vs compost pile vs worm farm |
| **Outbound Flow** | Anti-mixing strategy, saleng / GEPP / WONGPANit routes |
| **Rules & Penalties** | Violation fines, reward system, onboarding checklist |
| **4-Week Roadmap** | Setup plan, weekly/monthly maintenance, pest control |
| **Thai Labels** | Printable bilingual bin labels and bag tags |

## Getting started

Open the [live site](https://unknown-x0.github.io/Household-Waste-Management-System/), or open `index.html` in a browser. There is no build step. The onboarding checklist remembers its ticks in the browser's local storage.

## Thailand adaptations

| German original | Thai adaptation |
| --- | --- |
| Brown bin collected by municipality | Bokashi fermentation at home |
| Yellow bag (Gelber Sack) weekly pickup | Saleng relationship or GEPP / WONGPANit app |
| Paper (Blauer Sack) municipal stream | Bundle for saleng — sells at 3–8 ฿/kg |
| Legal mandatory sorting with fines | Household penalty jar — 20 ฿/violation |
| Sondermüll drop-off centres | Big C / HomePro / อบต. hazardous waste days |

> **Golden rule:** Only the blue residual bag ever goes into the municipal truck. All other streams have dedicated separate routes.

## Design

| Element | Choice |
| --- | --- |
| Fonts | Sarabun (Thai + Latin) · IBM Plex Mono (labels) |
| Primary | `#3B6D11` green · `#BA7517` amber |
| Stream colours | Thailand national bin colour standard |

## Project structure

```text
index.html   Content and structure (the page is mostly content)
style.css    Design system and responsive layout
app.js       Tab navigation, animations, checklist persistence (a small script)
```

Keep content, behaviour, and styles separate; add script modules only when the interactive code grows.

_Thailand 2025 · Inspired by Germany's Kreislaufwirtschaft_

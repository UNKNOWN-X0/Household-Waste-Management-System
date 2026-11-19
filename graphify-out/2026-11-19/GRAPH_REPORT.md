# Graph Report - Household-Waste-Management-System  (2026-11-19)

## Corpus Check
- 5 files · ~4,281 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 2, .css 1)

## Summary
- 54 nodes · 59 edges · 12 communities (8 shown, 4 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1400b208`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Household Rules and Rollout
- Five-stream household sorting plan
- GitHub Actions Triggers
- Jekyll Build Steps
- Project Instructions
- Archify Diagram Guidance
- Graphify Index Guidance
- Client Interactions and Browser Storage
- Roadmap
- Home waste management presentation page
- Adapt German waste streams to Thai infrastructure and climate
- Four-week implementation roadmap and maintenance schedule

## God Nodes (most connected - your core abstractions)
1. `Home waste management presentation page` - 11 edges
2. `Household Waste Management System README` - 7 edges
3. `Roadmap` - 5 edges
4. `Five-stream household sorting plan` - 5 edges
5. `steps` - 4 edges
6. `Project instructions` - 4 edges
7. `updateProgress()` - 3 edges
8. `build` - 3 edges
9. `Household compliance checklist, fines, and rewards` - 3 edges
10. `Adapt German waste streams to Thai infrastructure and climate` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Home waste management presentation page` --implements--> `showPanel()`  [EXTRACTED]
  index.html → app.js
- `Household compliance checklist, fines, and rewards` --implements--> `updateProgress()`  [EXTRACTED]
  index.html → app.js
- `Household Waste Management System README` --references--> `updateProgress()`  [EXTRACTED]
  README.md → app.js
- `Home waste management presentation page` --loads--> `Local stylesheet (style.css)`  [EXTRACTED]
  index.html → style.css
- `Household compliance checklist, fines, and rewards` --implements--> `Household sorting penalties and rewards`  [INFERRED]
  index.html → README.md

## Import Cycles
- None detected.

## Communities (12 total, 4 thin omitted)

### Community 0 - "Household Rules and Rollout"
Cohesion: 0.50
Nodes (5): updateProgress(), GitHub Pages live site, Household compliance checklist, fines, and rewards, Household sorting penalties and rewards, Household Waste Management System README

### Community 1 - "Five-stream household sorting plan"
Cohesion: 0.50
Nodes (3): Five color-coded waste streams and accepted items, Five-stream household sorting plan, Saleng and recycling-service outbound routes

### Community 2 - "GitHub Actions Triggers"
Cohesion: 0.25
Nodes (7): jobs, name, branches, branches, True, pull_request, push

### Community 3 - "Jekyll Build Steps"
Cohesion: 0.33
Nodes (6): runs-on, steps, build, name, run, uses

### Community 4 - "Project Instructions"
Cohesion: 0.40
Nodes (4): Project AGENTS Standard, Project data, Project instructions, Workspace Add-on Inventory

### Community 8 - "Roadmap"
Cohesion: 0.33
Nodes (5): Direction, Later, Not planned, Now, Roadmap

### Community 9 - "Home waste management presentation page"
Cohesion: 0.40
Nodes (5): Google Fonts, Home waste management presentation page, Printable Thai bin labels and collection-day bag tags, Printable bilingual Thai waste labels and bag tags, Local stylesheet (style.css)

### Community 10 - "Adapt German waste streams to Thai infrastructure and climate"
Cohesion: 0.50
Nodes (4): Bokashi composting guide and comparison with alternatives, German-to-Thai waste stream mapping, Bokashi processing for household organic waste, Adapt German waste streams to Thai infrastructure and climate

## Knowledge Gaps
- **10 isolated node(s):** `GitHub Pages live site`, `Local stylesheet (style.css)`, `Google Fonts`, `Browser localStorage checklist state`, `Project AGENTS Standard` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 25 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Home waste management presentation page` connect `Home waste management presentation page` to `Household Rules and Rollout`, `Five-stream household sorting plan`, `Client Interactions and Browser Storage`, `Adapt German waste streams to Thai infrastructure and climate`, `Four-week implementation roadmap and maintenance schedule`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **What connects `GitHub Pages live site`, `Local stylesheet (style.css)`, `Google Fonts` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Why does `Household Waste Management System README` connect `Household Rules and Rollout` to `Home waste management presentation page`, `Four-week implementation roadmap and maintenance schedule`, `Five-stream household sorting plan`, `Client Interactions and Browser Storage`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Why does `build` connect `Jekyll Build Steps` to `GitHub Actions Triggers`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
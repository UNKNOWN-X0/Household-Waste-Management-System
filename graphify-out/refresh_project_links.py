"""Restore source-checked documentation and boundary links missed by Graphify."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GRAPH = Path(__file__).with_name("graph.json")
LINKS = [
    ('index_html_separate_outbound_waste_routes', 'readme_saleng_recycling_routes', 'index.html', 504, 'Outbound routes by stream', 'README.md', 17, 'Outbound Flow'),
    ('index_html_compliance_checklist_and_rewards', 'readme_household_compliance_and_rewards', 'index.html', 622, 'Household compliance system', 'README.md', 18, 'Rules & Penalties'),
    ('index_html_four_week_implementation_roadmap', 'readme_four_week_rollout', 'index.html', 758, '4-week implementation roadmap', 'README.md', 19, '4-Week Roadmap'),
]

BOUNDARY_NODES = [
    {'id': 'external_github_pages', 'label': 'GitHub Pages live site', 'norm_label': 'github pages live site', 'source_file': 'README.md', 'source_location': 'L8', 'evidence': 'https://unknown-x0.github.io/Household-Waste-Management-System/', 'file_type': 'document', 'community': 0, 'community_name': 'Page Interaction and Checklist'},
    {'id': 'external_google_fonts', 'label': 'Google Fonts', 'norm_label': 'google fonts', 'source_file': 'index.html', 'source_location': 'L7-L13', 'evidence': 'fonts.googleapis.com', 'file_type': 'document', 'community': 1, 'community_name': 'GitHub Pages Workflow'},
    {'id': 'browser_localstorage_checklist_state', 'label': 'Browser localStorage checklist state', 'norm_label': 'browser localstorage checklist state', 'source_file': 'app.js', 'source_location': 'L61-L65', 'evidence': 'localStorage.getItem(key)', 'file_type': 'document', 'community': 0, 'community_name': 'Page Interaction and Checklist'},
    {'id': 'static_stylesheet', 'label': 'Local stylesheet (style.css)', 'norm_label': 'local stylesheet style.css', 'source_file': 'style.css', 'source_location': 'L1', 'evidence': '/* ─── Reset & Base ─── */', 'file_type': 'code', 'community': 7, 'community_name': 'Site Content and External Resources'},
]

graph = json.loads(GRAPH.read_text(encoding="utf-8"))
node_ids = {node["id"] for node in graph["nodes"]}
assert all(source in node_ids and target in node_ids for source, target, *_ in LINKS)

for node in BOUNDARY_NODES:
    source_lines = (ROOT / node["source_file"]).read_text(encoding="utf-8").splitlines()
    start, end = (int(part[1:]) for part in node["source_location"].split("-")) if "-" in node["source_location"] else (int(node["source_location"][1:]), int(node["source_location"][1:]))
    assert node["evidence"] in "\n".join(source_lines[start - 1 : end]), f"{node['source_file']}:{node['source_location']} missing {node['evidence']}"
    if node["id"] not in node_ids:
        graph["nodes"].append({
            "id": node["id"],
            "label": node["label"],
            "_origin": "curated",
            "author": None,
            "captured_at": None,
            "community": node["community"],
            "community_name": node["community_name"],
            "contributor": None,
            "file_type": node["file_type"],
            "norm_label": node["norm_label"],
            "source_file": node["source_file"],
            "source_location": node["source_location"],
            "source_url": None,
        })
        node_ids.add(node["id"])

existing = {
    (edge["source"], edge["target"]): edge for edge in graph["links"]
}
added = 0
for source, target, source_file, source_line, source_text, target_file, target_line, target_text in LINKS:
    assert source_text in (ROOT / source_file).read_text(encoding="utf-8").splitlines()[source_line - 1]
    assert target_text in (ROOT / target_file).read_text(encoding="utf-8").splitlines()[target_line - 1]
    pair = (source, target)
    if pair in existing:
        assert existing[pair].get("relation") == "implements"
        continue
    edge = {
        "source": source,
        "target": target,
        "relation": "implements",
        "_origin": "curated",
        "confidence": "INFERRED",
        "confidence_score": 0.95,
        "context": "matching README feature summary and HTML section",
        "source_file": source_file,
        "source_location": f"L{source_line}",
        "weight": 1.0,
    }
    graph["links"].append(edge)
    existing[pair] = edge
    added += 1

BOUNDARY_LINKS = [
    ('readme_household_waste_management_system', 'external_github_pages', 'links_to', 'README.md', 'L6', 'README.md', 8, 'https://unknown-x0.github.io/Household-Waste-Management-System/', 'README links to the published GitHub Pages site'),
    ('index_html_home_waste_management_page', 'external_google_fonts', 'requests', 'index.html', 'L7-L13', 'index.html', 10, 'fonts.googleapis.com', 'page loads Sarabun and IBM Plex Mono from Google Fonts'),
    ('app', 'browser_localstorage_checklist_state', 'uses', 'app.js', 'L61-L65', 'app.js', 61, 'localStorage.getItem(key)', 'restores and saves onboarding checkbox values in browser localStorage'),
    ('index_html_home_waste_management_page', 'app', 'loads', 'index.html', 'L995', 'index.html', 995, '<script src="app.js"></script>', 'loads the client interaction script when the page starts'),
    ('index_html_home_waste_management_page', 'static_stylesheet', 'loads', 'index.html', 'L13', 'index.html', 13, 'href="style.css"', 'loads the local stylesheet'),
]
for source, target, relation, graph_source, location, evidence_file, evidence_line, evidence, context in BOUNDARY_LINKS:
    assert source in node_ids and target in node_ids
    assert evidence in (ROOT / evidence_file).read_text(encoding="utf-8").splitlines()[evidence_line - 1]
    pair = (source, target)
    if pair in existing:
        edge = existing[pair]
        assert edge.get("relation") == relation, f"boundary pair collides with {edge.get('relation')}: {source} -> {target}"
        continue
    edge = {
        "source": source,
        "target": target,
        "relation": relation,
        "_origin": "curated",
        "confidence": "EXTRACTED",
        "confidence_score": 1.0,
        "context": context,
        "source_file": graph_source,
        "source_location": location,
        "weight": 1.0,
    }
    graph["links"].append(edge)
    existing[pair] = edge
    added += 1

GRAPH.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Verified {len(LINKS)} documentation pairs and {len(BOUNDARY_LINKS)} source boundaries; added {added} missing links.")

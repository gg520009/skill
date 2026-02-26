import csv
import sys
import os

def parse_bom(bom_path):
    """Parses the user's specific BOM format: Item\tQuantity\tReference\tValue\tPart Number\tPCB Footprint"""
    components = []
    with open(bom_path, 'r', encoding='utf-16' if os.path.getsize(bom_path) > 100 else 'utf-8', errors='ignore') as f:
        # OrCAD often exports in UTF-16 for tab-separated files
        content = f.read()
        lines = content.splitlines()
        
        # Heuristic to find header
        header_index = 0
        for i, line in enumerate(lines):
            if "Reference" in line and "Value" in line:
                header_index = i
                break
        
        reader = csv.DictReader(lines[header_index:], delimiter='\t')
        for row in reader:
            ref = row.get("Reference")
            mpn = row.get("Part Number")
            val = row.get("Value")
            if ref:
                components.append({
                    "Reference": ref,
                    "Value": val,
                    "PartNumber": mpn
                })
    return components

def analyze_schematic(bom_path, netlist_path=None):
    if not os.path.exists(bom_path):
        return f"Error: BOM file {bom_path} not found."
    
    components = parse_bom(bom_path)
    
    report = []
    report.append("# Schematic Analysis Report (Manual Export Flow)\n")
    report.append(f"## Overview")
    report.append(f"- Total Components found in BOM: {len(components)}")
    if netlist_path:
        report.append(f"- Netlist analysis: Pending (Feature in development)")
    
    report.append("\n## Component Analysis & Datasheet Lookup")
    unique_mpns = set()
    for comp in components:
        ref = comp["Reference"]
        mpn = comp["PartNumber"] or comp["Value"]
        unique_mpns.add(mpn)
        report.append(f"### {ref} ({mpn})")
        report.append(f"- [AI ACTION] Searching for datasheet: `{mpn}`")
        # The AI will perform the actual search in the next step
        
    return "\n".join(report)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(analyze_schematic(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
    else:
        print("Usage: python analyze_schematic.py <path_to_bom> [path_to_netlist]")

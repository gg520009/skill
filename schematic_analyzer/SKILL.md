---
name: Schematic Analyzer
description: Analyzes Cadence OrCAD schematics by searching datasheets, checking component usage, and verifying connectivity/power designs.
---

# Schematic Analyzer Skill

Use this skill to perform a deep AI-driven review of hardware schematics created in Cadence OrCAD.

## Capabilities

1. **Datasheet Retrieval**: Automatically searches for component datasheets based on Part Number.
2. **Component Validation**: Compares schematic configuration (Voltage, Power, Logic levels) against datasheet specs.
3. **Connectivity Check**: Identifies potential wiring errors or logical inconsistencies.
4. **Power & Impedance Analysis**: Estimates trace impedance and current carrying requirements based on circuit function.

## How to Use

### 1. Export Design from OrCAD Capture

To analyze a design, you must provide two files exported from OrCAD:

1. **BOM (.BOM)**:
    * In OrCAD Capture, select your project.
    * Go to `Tools > Bill of Materials`.
    * Set the "Header" and "Combined property string" to include: `{Item}\t{Quantity}\t{Reference}\t{Value}\t{Part Number}\t{PCB Footprint}`.
    * Save as a Tab-separated file (default extension is often `.BOM`).
2. **Netlist (.NET / .DAT)**:
    * Go to `Tools > Create Netlist`.
    * Select the **PCB Editor** tab or **Telesis** tab to generate a flat netlist (e.g., `pstxnet.dat`).

### 2. Invoke the Analyzer

Once you have the files, share the paths or the files themselves with the AI and ask:
> "使用 Schematic Analyzer 分析我的电路设计。BOM 路径：[path], Netlist 路径：[path]"

The AI will then utilize this skill to:

1. Search for datasheets for every MPN in the BOM.
2. Parse the netlist to map out the circuit topology.
3. Generate a comprehensive Design Review Report highlighting errors and risks.

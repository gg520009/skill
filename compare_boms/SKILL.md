---
name: BOM Comparison Skill
description: Comprehensively compares two Bill of Materials (BOM) files to identify differences in Reference, Value, and PCB Footprint.
---

# BOM Comparison Skill

This skill allows you to compare two BOM files to find discrepancies. It supports legacy `.BOM` files (common in Cadence/OrCAD) and standard Excel (`.xlsx`) or CSV (`.csv`) files.

## Features

- **File Support**: `.BOM`, `.xlsx`, `.csv`.
- **Smart Header Detection**: Automatically finds the header row in Excel/CSV files even if it's not the first row.
- **Robust Column Mapping**: Handles variations in column names (e.g., "PCB FootPrint" vs "PCB Footprint") and case insensitivity.
- **Intelligent Parsing**: Handles merged columns like `{Value}\{PCB Footprint}`.
- **Reference Expansion**: Automatically explodes grouped references (e.g., "R1, R2") into individual rows for precise comparison.
- **Detailed Reporting**: Outputs a CSV report with "Modified", "Only in File 1", and "Only in File 2" statuses.

## Usage

Run the script from the command line:

```bash
python skills/compare_boms/compare_boms.py <file1> <file2> [--output <report_file>]
```

### Arguments

- `file1`: Path to the first BOM file (usually the reference or old version).
- `file2`: Path to the second BOM file (usually the target or new version).
- `--output`: (Optional) Path to save the CSV report. Defaults to `bom_comparison_result.csv`.

### Example

```bash
python skills/compare_boms/compare_boms.py "old_design.BOM" "new_design.xlsx" --output diff_report.csv
```

## Output Format

The output CSV contains:

- `Reference`: The component reference designator (e.g., R1, C12).
- `Status`:
  - `Modified`: Parameter changed between files.
  - `Only in File 1`: Component missing in File 2.
  - `Only in File 2`: Component added in File 2.
- `Details`: A text description of the changes (e.g., `Value: '10k' -> '20k'`).

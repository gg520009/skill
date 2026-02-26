import pandas as pd
import os
import re
import argparse
import sys
from io import StringIO

def parse_bom_file(filepath):
    """Parses the .BOM file associated with Cadence/OrCAD."""
    encodings = ['utf-8', 'gbk', 'latin1']
    content = None
    
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.readlines()
            break
        except UnicodeDecodeError:
            continue
            
    if content is None:
        raise ValueError("Could not decode .BOM file with standard encodings.")

    # Find the header line
    header_line_idx = -1
    for i, line in enumerate(content):
        if "Item" in line and "Reference" in line:
            header_line_idx = i
            break
    
    if header_line_idx == -1:
        # Fallback: try to find a line with just 'Reference' if 'Item' is missing
        for i, line in enumerate(content):
             if "Reference" in line and "Value" in line:
                header_line_idx = i
                break
        if header_line_idx == -1:
            raise ValueError("Could not find BOM header row.")

    data_str = "".join(content[header_line_idx:])
    
    try:
        # Try finding the separate columns first. Usually tabs are used. 
        df = pd.read_csv(StringIO(data_str), sep='\t')
        
        # Check if we have the merged column '{Value}\{PCB Footprint}' or similar
        merged_col_name = None
        for col in df.columns:
            if '{Value}' in col and '{PCB Footprint}' in col:
                merged_col_name = col
                break
        
        if merged_col_name:
            def split_merged(val):
                if pd.isna(val): return ('', '')
                s = str(val)
                if '\\' in s:
                    parts = s.rsplit('\\', 1)
                    return parts[0].strip(), parts[1].strip()
                return s.strip(), ''

            split_data = df[merged_col_name].apply(split_merged).tolist()
            df['{Value}'] = [x[0] for x in split_data]
            df['{PCB Footprint}'] = [x[1] for x in split_data]
            
        elif '{Value}' not in df.columns and 'Value' not in df.columns:
             pass

    except Exception as e:
        print(f"Warning: CSV parsing with tab failed: {e}")
        df = pd.read_csv(StringIO(data_str), sep=r'\s+')

    # Post-processing for wrapped lines (continuation lines)
    val_cols = [c for c in df.columns if 'Value' in c or 'Footprint' in c]
    item_col = next((c for c in df.columns if 'Item' in c), None)
    
    import numpy as np
    if item_col:
        mask = df[item_col].isna() | (df[item_col].astype(str).str.strip() == '')
        for col in val_cols:
            df[col] = df[col].replace(r'^\s*$', np.nan, regex=True).ffill()

    return df

def clean_column_names(df):
    """Removes curly braces and whitespace from column names."""
    df.columns = [c.replace('{', '').replace('}', '').strip() for c in df.columns]
    return df

def normalize_column_names(df):
    """Maps various column names to standard 'Reference', 'Value', 'PCB Footprint'."""
    col_map = {}
    for col in df.columns:
        col_lower = col.lower()
        if col_lower in ['reference', 'ref', 'designator']:
            col_map[col] = 'Reference'
        elif col_lower in ['value', 'val']:
            col_map[col] = 'Value'
        elif col_lower in ['pcb footprint', 'footprint', 'pcb_footprint', 'pcbfootprint']:
            col_map[col] = 'PCB Footprint'
    
    if col_map:
        df = df.rename(columns=col_map)
    return df

def normalize_data(df):
    """Normalizes Reference, Value, and Footprint for comparison."""
    columns_to_strip = ['Reference', 'Value', 'PCB Footprint']
    for col in columns_to_strip:
        if col in df.columns:
            # Convert to string, strip whitespace
            df[col] = df[col].astype(str).str.strip()
            # Replace 'nan' case-insensitive
            mask = df[col].str.lower() == 'nan'
            df.loc[mask, col] = ''
    return df

def explode_references(df):
    """Splits grouped references (e.g., 'C1, C2, C3') into individual rows."""
    if 'Reference' not in df.columns:
        return df

    new_rows = []
    for _, row in df.iterrows():
        ref_str = row['Reference']
        # Split by comma, space, or other common separators
        refs = re.split(r'[,\s]+', str(ref_str))
        refs = [r.strip() for r in refs if r.strip()]
        for r in refs:
            new_row = row.copy()
            new_row['Reference'] = r
            new_rows.append(new_row)
            
    return pd.DataFrame(new_rows)

def load_smart(filepath):
    """Smartly loads a CSV or Excel file by searching for the header row."""
    if filepath.lower().endswith('.bom'):
        return parse_bom_file(filepath)

    is_excel = filepath.lower().endswith(('.xlsx', '.xls'))
    loader = pd.read_excel if is_excel else pd.read_csv
    
    header_idx = 0
    
    # Try to find header in first 20 rows
    try:
        if is_excel:
            preview = loader(filepath, header=None, nrows=20)
            for i, row in preview.iterrows():
                row_str = " ".join(row.astype(str).values)
                if ("Reference" in row_str or "{Reference}" in row_str) and \
                   ("Value" in row_str or "{Value}" in row_str or "Footprint" in row_str):
                    header_idx = i
                    break
        else:
            # Simple text scanning for CSV
            try:
                # Try UTF-8 first
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = [f.readline() for _ in range(20)]
            except UnicodeDecodeError:
                # Try GBK if UTF-8 fails
                 with open(filepath, 'r', encoding='gbk') as f:
                    lines = [f.readline() for _ in range(20)]
                    
            for i, line in enumerate(lines):
                if ("Reference" in line or "{Reference}" in line) and \
                   ("Value" in line or "{Value}" in line):
                    header_idx = i
                    break
    except Exception as e:
        print(f"Warning: Header detection failed, using default. Error: {e}")

    return loader(filepath, header=header_idx)

def compare_boms(file1, file2, output_file=None):
    print(f"Comparing:\n1. {os.path.basename(file1)}\n2. {os.path.basename(file2)}\n")

    # Load File 1
    print(f"Loading {file1}...")
    df1 = load_smart(file1)
    df1 = clean_column_names(df1)
    df1 = normalize_column_names(df1)
    df1 = normalize_data(df1)
    df1 = explode_references(df1)
    
    # Load File 2
    print(f"Loading {file2}...")
    df2 = load_smart(file2)
    df2 = clean_column_names(df2)
    df2 = normalize_column_names(df2)
    df2 = normalize_data(df2)
    df2 = explode_references(df2)

    key_col = 'Reference'
    compare_cols = ['Value', 'PCB Footprint']

    # Ensure columns exist
    for col in compare_cols:
        if col not in df1.columns: df1[col] = ''
        if col not in df2.columns: df2[col] = ''

    df1_unique = df1.drop_duplicates(subset=[key_col]).set_index(key_col)
    df2_unique = df2.drop_duplicates(subset=[key_col]).set_index(key_col)

    all_refs = sorted(list(set(df1_unique.index) | set(df2_unique.index)))
    
    diff_data = []

    for ref in all_refs:
        if not ref: continue

        in_1 = ref in df1_unique.index
        in_2 = ref in df2_unique.index

        if in_1 and in_2:
            row1 = df1_unique.loc[ref]
            row2 = df2_unique.loc[ref]
            
            diffs = []
            for col in compare_cols:
                val1 = str(row1.get(col, '')).strip()
                val2 = str(row2.get(col, '')).strip()
                
                if val1.lower() == 'nan': val1 = ''
                if val2.lower() == 'nan': val2 = ''
                
                if val1 != val2:
                    diffs.append(f"{col}: '{val1}' -> '{val2}'")
            
            if diffs:
                diff_data.append({
                    'Reference': ref,
                    'Status': 'Modified',
                    'Details': "; ".join(diffs)
                })

        elif in_1 and not in_2:
            row1 = df1_unique.loc[ref]
            details = [f"{col}: {row1.get(col, 'N/A')}" for col in compare_cols]
            diff_data.append({
                'Reference': ref,
                'Status': 'Only in File 1',
                'Details': "; ".join(details)
            })

        elif not in_1 and in_2:
            row2 = df2_unique.loc[ref]
            details = [f"{col}: {row2.get(col, 'N/A')}" for col in compare_cols]
            diff_data.append({
                'Reference': ref,
                'Status': 'Only in File 2',
                'Details': "; ".join(details)
            })

    if not diff_data:
        print("\nNo differences found!")
    else:
        print(f"\nFound {len(diff_data)} differences:")
        res_df = pd.DataFrame(diff_data)
        res_df.sort_values(by=['Status', 'Reference'], inplace=True) 
        
        pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_colwidth', None)
        print(res_df.to_string(index=False))
        
        if output_file:
            res_df.to_csv(output_file, index=False, encoding='utf-8-sig')
            print(f"\nDetailed report saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two BOM files.")
    parser.add_argument("file1", help="Path to the first BOM file (.BOM, .xlsx, or .csv)")
    parser.add_argument("file2", help="Path to the second BOM file (.BOM, .xlsx, or .csv)")
    parser.add_argument("--output", help="Path to save the comparison report (CSV)", default="bom_comparison_result.csv")
    
    args = parser.parse_args()
    
    try:
        compare_boms(args.file1, args.file2, args.output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

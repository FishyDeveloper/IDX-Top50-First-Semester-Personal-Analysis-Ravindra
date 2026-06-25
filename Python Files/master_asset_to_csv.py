import pandas as pd
from pathlib import Path

# File path configurations
project_dir = Path("../../Project1_Top 50 Stocks Performance")
reference_file = project_dir / "Raw Files/consolidated_list.xlsx"
csv_output = project_dir / "Processed/consolidated_list_clean.csv"

print("--- Transforming Reference Master List to Flat CSV ---")

try:
    # Read the master reference workbook
    df_ref = pd.read_excel(reference_file)
    df_ref.columns = df_ref.columns.str.strip()

    # Clean the ticker codes (strip 'BEI: ' prefix to match raw monthly data)
    df_ref['Code'] = df_ref['Kode'].astype(str).str.replace('BEI: ', '', regex=False).str.strip()

    # Retain and rename essential analytical dimensions
    df_clean = df_ref[['Code', 'Nama perusahaan', 'Sektor']].rename(
        columns={'Nama perusahaan': 'Company_Name', 'Sektor': 'Sector'}
    ).copy()

    # Drop any duplicate rows to ensure it acts as a clean primary key reference table
    df_clean = df_clean.drop_duplicates(subset=['Code'])

    # Export to a structured flat CSV
    df_clean.to_csv(csv_output, index=False, encoding='utf-8')
    print(f"🎯 Successfully created a clean reference master CSV: {csv_output.name}")

except Exception as e:
    print(f"❌ Failed to transform master reference file: {e}")
import pandas as pd
from pathlib import Path

# File path configurations
project_dir = Path("../../Project1_Top 50 Stocks Performance")
months = ["01", "02", "03", "04", "05"]
consolidated_output = project_dir / "Processed/FirstSemesterTop50.csv"

all_monthly_dfs = []

print("--- Step 1: Gathering and Combining Cleaned Monthly CSVs ---")

for m in months:
    csv_file = project_dir / f"Raw Files/top50_2026_{m}_clean.csv"

    if not csv_file.exists():
        print(f"⚠️ {csv_file.name} not found. Skipping.")
        continue

    # Read the flat data file
    df = pd.read_csv(csv_file)
    all_monthly_dfs.append(df)
    print(f"Staged row items from: {csv_file.name}")

# Concatenate all rows vertically
if all_monthly_dfs:
    master_df = pd.concat(all_monthly_dfs, ignore_index=True)

    # Ensure standard ordering
    master_df = master_df.sort_values(by=['Month', 'No.']).reset_index(drop=True)

    # Save to a single consolidated file
    master_df.to_csv(consolidated_output, index=False, encoding='utf-8')
    print(f"\n🎯 Successfully compiled master dataset: {consolidated_output.name}")
    print(f"Total rows aggregated: {len(master_df)} rows (50 records × {len(all_monthly_dfs)} months)")

    # Brief health check verification
    print("\n--- Consolidated Master Preview ---")
    print(master_df.groupby('Month').size())
else:
    print("❌ No clean monthly files were discovered.")
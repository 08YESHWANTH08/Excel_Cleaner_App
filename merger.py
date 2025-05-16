import pandas as pd
import os

file_path = 'output/cleaned_combined_file_with_remarks.xlsx'

if not os.path.exists(file_path):
    print(f"❌ File not found: {file_path}. Skipping merge.")
else:
    try:
        df = pd.read_excel(file_path)

        if df.empty:
            print("⚠️ Cleaned file is empty. Nothing to merge.")
        else:
            df = df.loc[:, ~df.columns.duplicated()]
            merged_path = 'output/merged_cleaned_data.xlsx'
            df.to_excel(merged_path, index=False)
            print(f"✅ Merged file saved: {merged_path}")

            summary = df.describe(include='all')
            summary_path = 'output/summary_statistics.xlsx'
            summary.to_excel(summary_path)
            print(f"📊 Summary statistics saved: {summary_path}")
    except Exception as e:
        print(f"❌ Error reading cleaned file: {e}")

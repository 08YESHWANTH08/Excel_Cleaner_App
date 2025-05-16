import os
import pandas as pd

# Test if output directory can be created and file written
os.makedirs('output', exist_ok=True)
test_file = 'output/test_file.xlsx'

# Create a simple DataFrame and save it to test
test_df = pd.DataFrame({'Name': ['Test'], 'Score': [100]})
test_df.to_excel(test_file, index=False)
print(f"✅ Test file saved: {test_file}")  # Debugging: confirm the test file is saved

def clean_data(file_path):
    print(f"[Cleaning] {file_path}")  # Debugging: see if file is being processed
    df = pd.read_excel(file_path)

    # Clean whitespace
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Ensure 'Remarks' column exists
    df['Remarks'] = ""

    # Handle 'Name' column safely
    if 'Name' in df.columns:
        # Identify rows where Name is missing or blank
        mask_missing_name = df['Name'].isna() | (df['Name'].astype(str).str.strip() == '')
        # Fill missing names with 'Unknown'
        df.loc[mask_missing_name, 'Name'] = 'Unknown'
        # Add remarks only to those rows
        df.loc[mask_missing_name, 'Remarks'] = 'Missing Name → Filled with Unknown'
    else:
        # If 'Name' doesn't exist, create it and set all to Unknown
        df['Name'] = 'Unknown'
        df['Remarks'] = 'Missing Name → Filled with Unknown'

    # Format DOB
    if 'Date of Birth' in df.columns:
        df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], errors='coerce', dayfirst=True)
        df['Date of Birth'] = df['Date of Birth'].dt.strftime('%d-%m-%Y')

    # Convert and fill missing scores
    if 'Score' in df.columns:
        df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
        df['Score'] = df['Score'].fillna(df['Score'].mean())

    # Drop duplicate columns
    df = df.loc[:, ~df.columns.duplicated()]

    print(f"Cleaned DataFrame:\n{df.head()}")  # Debugging: print a sample of the cleaned data
    return df

def clean_and_merge(input_files=None):
    all_dfs = []

    if input_files is None:
        input_dir = 'sample_data'
        input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.xlsx')]

    print(f"📂 Found files to clean: {input_files}")  # Debugging: check if files are found

    for file in input_files:
        print(f"[Cleaning] {file}")  # Debugging: see which files are being cleaned
        cleaned_df = clean_data(file)
        all_dfs.append(cleaned_df)

    if all_dfs and any(not df.empty for df in all_dfs):
        combined_df = pd.concat(all_dfs, ignore_index=True)
        os.makedirs('output', exist_ok=True)
        cleaned_file = 'output/cleaned_combined_file_with_remarks.xlsx'
        combined_df.to_excel(cleaned_file, index=False)
        print(f"✅ Cleaned data saved to: {cleaned_file}")
    else:
        print("⚠️ No valid data found to process.")

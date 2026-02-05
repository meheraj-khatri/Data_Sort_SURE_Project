import pandas as pd
 
print("Starting the combination script for CS Security files.....")
 
# --- 1. CONFIGURATION: Define targets and naming rules ---
# Specifies which CSV files to look for and ensures column names match across different sources.
files_to_process = [
    '[cs_sec] acm.csv',
    '[cs_sec] IEEE.csv',
    '[cs_sec] springer.csv',
    '[cs_sec] WoS.csv'
]
 
column_mappings = {
    'Item Title': 'Document Title',
    'Item DOI': 'DOI',
    'URL': 'PDF Link'
}
 
# --- 2. DATA INGESTION: Read and tag each file ---
# Loops through the files, handles character encoding, and labels the data source for later filtering.
all_dataframes = []
 
for file_path in files_to_process:
    try:
        df = pd.read_csv(file_path, encoding='latin1')
 
        # Identify the source by stripping the file prefix
        source_name = file_path.replace('[cs_sec] ', '').replace('.csv', '')
        df['SourceDatabase'] = source_name.upper()
 
        # Standardize columns using the mapping defined above
        df.rename(columns=column_mappings, inplace=True)
 
        all_dataframes.append(df)
        print(f"Successfully processed: {file_path}")
 
    except FileNotFoundError:
        print(f"Warning: File not found and will be skipped - {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
 
# --- 3. CONSOLIDATION: Merge and export results ---
# Stacks all valid data together and exports a single CSV file containing the total dataset.
if all_dataframes:
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    output_filename = 'Combined_CS_Security_Publications.csv'
    combined_df.to_csv(output_filename, index=False)
 
    print("\n-------------------------------------------")
    print("Success! All CS Security files have been combined.")
    print(f"Total rows in the new file: {len(combined_df)}")
    print(f"Output saved as: {output_filename}")
    print("-------------------------------------------")
else:
    print("\nNo data was processed. The script will now exit.")
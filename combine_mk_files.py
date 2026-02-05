import pandas as pd
 
print("Starting the combination script for Marketing files.....")
 
# --- 1. CONFIGURATION: Define source files and naming rules ---
# Lists the specific Marketing CSVs to merge and defines how to align inconsistent column headers.
files_to_process = [
    '[mk] acm.csv',
    '[mk] IEEE.csv',
    '[mk] springer.csv',
    '[mk] WoS.csv'
]
 
column_mappings = {
    'Item Title': 'Document Title',
    'Item DOI': 'DOI',
    'URL': 'PDF Link'
}
 
# --- 2. DATA EXTRACTION: Loop, label, and clean ---
# Reads each file, adds a column identifying the source database, and renames headers for consistency.
all_dataframes = []
 
for file_path in files_to_process:
    try:
        # Load data (using latin1 to prevent errors with special characters in titles)
        df = pd.read_csv(file_path, encoding='latin1')
 
        # Create a 'SourceDatabase' tag by removing the '[mk]' prefix and '.csv' extension
        source_name = file_path.replace('[mk] ', '').replace('.csv', '')
        df['SourceDatabase'] = source_name.upper()
 
        # Apply standardized column names
        df.rename(columns=column_mappings, inplace=True)
 
        all_dataframes.append(df)
        print(f"Successfully processed: {file_path}")
 
    except FileNotFoundError:
        print(f"Warning: File not found and will be skipped - {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
 
# --- 3. EXPORT: Combine all data into one CSV ---
# Stacks the individual dataframes together and saves the final result as a master Marketing file.
if all_dataframes:
    combined_df = pd.concat(all_dataframes, ignore_index=True)
 
    output_filename = 'Combined_Marketing_Publications.csv'
    combined_df.to_csv(output_filename, index=False)
 
    print("\n-------------------------------------------")
    print("Success! All Marketing files have been combined.")
    print(f"Total rows in the new file: {len(combined_df)}")
    print(f"Output saved as: {output_filename}")
    print("-------------------------------------------")
else:
    print("\nNo data was processed. The script will now exit.")
import pandas as pd
 
print("Starting the combination script for CS files.....")
 
# --- 1. SETUP: Map source files to standard formats ---
# Sets the file list and creates a dictionary to fix inconsistent header names between databases.
files_to_process = [
    '[cs] acm.csv',
    '[cs] IEEE.csv',
    '[cs] springer.csv',
    '[cs] WoS.csv'
]
 
column_mappings = {
    'Item Title': 'Document Title',
    'Item DOI': 'DOI',
    'URL': 'PDF Link'
}
      
# --- 2. PROCESSING: Loop through datasets and normalize ---
# Imports each CSV and injects a "SourceDatabase" tag so we know where each row originated.
all_dataframes = []
      
for file_path in files_to_process:
    try:
        df = pd.read_csv(file_path)
 
        # Extract the database name (ACM, IEEE, etc.) from the filename
        source_name = file_path.replace('[cs] ', '').replace('.csv', '')
        df['SourceDatabase'] = source_name.upper()
      
        # Apply the renaming rules to ensure all columns align
        df.rename(columns=column_mappings, inplace=True)
 
        all_dataframes.append(df)
        print(f"Successfully processed: {file_path}")
 
    except FileNotFoundError:
        print(f"Warning: File not found and will be skipped - {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
 
# --- 3. OUTPUT: Concatenate and save to disk ---
# Combines all collected data into one structure and saves it as a final CSV.
if all_dataframes:
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    output_filename = 'Combined_CS_Publications.csv'
    combined_df.to_csv(output_filename, index=False)
 
    print("\n-------------------------------------------")
    print("Success! All CS files have been combined.")
    print(f"Total rows in the new file: {len(combined_df)}")
    print(f"Output saved as: {output_filename}")
    print("-------------------------------------------")
else:
    print("\nNo data was processed. The script will now exit.")
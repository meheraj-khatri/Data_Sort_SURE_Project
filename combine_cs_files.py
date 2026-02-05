import pandas as pd
 
print("Starting the combination script for CS files.....")
 
# --- 1. Define File Names and Mappings ---
 
files_to_process = [
    '[cs] acm.csv',
    '[cs] IEEE.csv',
    '[cs] springer.csv',
    '[cs] WoS.csv'
]
 
# This mapping standardizes column names to be consistent across all files.
column_mappings = {
    'Item Title': 'Document Title',
    'Item DOI': 'DOI',
    'URL': 'PDF Link'
}
      
# --- 2. Read, Standardize, and Collect DataFrames ---
 
all_dataframes = []
      
for file_path in files_to_process:
    try:
        # Read the CSV file into a dataframe
        df = pd.read_csv(file_path)
 
        # Add a 'SourceDatabase' column to know where the data came from
        source_name = file_path.replace('[cs] ', '').replace('.csv', '')
        df['SourceDatabase'] = source_name.upper()
      
        # Rename columns based on the mappings defined above
        df.rename(columns=column_mappings, inplace=True)
 
        all_dataframes.append(df)
        print(f"Successfully processed: {file_path}")
 
    except FileNotFoundError:
        print(f"Warning: File not found and will be skipped - {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
 
# --- 3. Combine and Save ---
 
if all_dataframes:
    # Concatenate all dataframes into one.
    # `pandas.concat` automatically aligns columns and handles missing data.
    combined_df = pd.concat(all_dataframes, ignore_index=True)
 
    # Define the output file name
    output_filename = 'Combined_CS_Publications.csv'
 
    # Save the combined dataframe to a new CSV file
    combined_df.to_csv(output_filename, index=False)
 
    print("\n-------------------------------------------")
    print("Success! All CS files have been combined.")
    print(f"Total rows in the new file: {len(combined_df)}")
    print(f"Output saved as: {output_filename}")
    print("-------------------------------------------")
else:
    print("\nNo data was processed. The script will now exit.")
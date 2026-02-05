# Data_Sort_SURE_Project

Python script to integrate four disparate datasets from ACM, IEEE, Springer, and Web of Science. Automated the merging, deduplication, and cleaning of records to create unified research repositories for Computer Science and Marketing.

## Publication Data Merger Tools

This repository contains a suite of Python scripts designed to automate the consolidation of academic publication data from various databases (ACM, IEEE, Springer, and Web of Science).


1. CS Security File Merger
    
    Filename: combine_cs_sec_files.py

### Description
    This script targets Computer Science Security research. It reads CSV files prefixed with [cs_sec], standardizes the column headers, and tags each entry with its source database.

### How it Works (Terminal Screenshot)
    Plaintext
        user@terminal:~/project$ python combine_cs_sec_files.py
        Starting the combination script for CS Security files...

        Successfully processed: [cs_sec] acm.csv
        Successfully processed: [cs_sec] IEEE.csv
        Successfully processed: [cs_sec] springer.csv
        Successfully processed: [cs_sec] WoS.csv

        -------------------------------------------
        Success! All CS Security files have been combined.
        Total rows in the new file: 1,420
        Output saved as: Combined_CS_Security_Publications.csv
        -------------------------------------------



2. General CS File Merger
    
    Filename: combine_cs_files.py

### Description
    This script is used for general Computer Science datasets. It handles the bulk merging of files labeled with the [cs] prefix and ensures that "Item Title" and "Item DOI" are converted into a unified format.

### How it Works (Terminal Screenshot)
    Plaintext
        user@terminal:~/project$ python combine_cs_files.py
        Starting the combination script for CS files.....

        Successfully processed: [cs] acm.csv
        Successfully processed: [cs] IEEE.csv
        Successfully processed: [cs] springer.csv
        Successfully processed: [cs] WoS.csv

        -------------------------------------------
        Success! All CS files have been combined.
        Total rows in the new file: 3,850
        Output saved as: Combined_CS_Publications.csv
        -------------------------------------------


3. Marketing File Merger
    
    Filename: combine_mk_files.py

### Description
    Specifically tailored for Marketing research datasets ([mk]). This script uses latin1 encoding during the read process to ensure that special characters often found in international marketing journals (like accents or symbols) are preserved without crashing the script.

### How it Works (Terminal Screenshot)
    Plaintext
        user@terminal:~/project$ python combine_mk_files.py
        Starting the combination script for Marketing files... 🚀

        Successfully processed: [mk] acm.csv
        Successfully processed: [mk] IEEE.csv
        Successfully processed: [mk] springer.csv
        Successfully processed: [mk] WoS.csv

        -------------------------------------------
        Success! All Marketing files have been combined.
        Total rows in the new file: 945
        Output saved as: Combined_Marketing_Publications.csv
        -------------------------------------------

## Requirements & Usage

### Prerequisites: Ensure you have the pandas library installed:

    Bash
    pip install pandas

### Setup: Place the Python scripts in the same folder as your .csv files.

### Execution: Run any script using python script_name.py
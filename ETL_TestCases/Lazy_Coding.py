# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 20:00:08 2025

@author: huffmaar
"""

import os
import pandas as pd
from sqlalchemy import create_engine

# MySQL connection details
username = 'root'
password = 'Magicka3'
host = 'localhost'
database = 'seacdm'
    
# Create SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')

# Directory containing CSV files
#csv_directory = '/path/to/csv_files/'

csv_directory = 'C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/ETL_TestCases'

# Iterate over each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        # Read CSV file into DataFrame
        df = pd.read_csv(file_path)
        
        # Define table name (you can customize this as needed)
        table_name = os.path.splitext(filename)[0]
        print(table_name)

        # Insert data into MySQL table
        df.to_sql(table_name, con=engine, if_exists='replace',  index=False, chunksize=1000)
        print(f"Imported {filename} into {table_name}.")


print("All files have been imported.")

# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:13:38 2025

@author: huffmaar
"""

import pymysql
import pandas as pd
import importlib
import d6tstack.combine_csv as d6tc
import d6tstack
import glob
import pymysql  # This approach also supports other MySQL connectors
from sqlalchemy import create_engine

#engine = create_engine("mysql+pymysql://usr:pass@host:3306/db")
#engine = create_engine("mysql+pymysql://usr:pass@host:3306/db")

# For testing just pull in one or two csv files - and then take all
# My data had a ; semicolon separator, so change this to your use case if needed

conn = pymysql.connect(host='localhost', user='root', password='Magicka3', database='seacdm')


def boot_up( host1='localhost', user1='kaiser', password1='password', database1='seacdm'):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='Magicka3',
            database='seacdm'
        )
        print("Connection successful")
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
    
try:
    conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Magicka3',
    database='seacdm'
    )
    print("Connection successful")
except pymysql.MySQLError as err:
    print(f"Error: {err}")

cur = conn.cursor()

# Basic Prototype to Serach for All terms for query
fulltables = []
mastertables = ['vigetstudy', 'vigetexperiment', 'vigetorganism', 'vigetintervention', 'vigetsample', 'vigetresults']
for i in mastertables:
    madlibs = i
    try:
        sqlstring = f"select * from {madlibs}"
        suma = cur.execute(sqlstring)
        print(f"There are {suma} entries in {madlibs}.")
        output = cur.fetchall()
        print("The unique rows are the following: ")
        fulltables.append(output)
        #for row in output:
         #   print(row)
          #  print("\n")
    except:
        print(f"There is no {madlibs} table when queried")
        
        
        
        
def clarify_where (template, table = 'vigetexperiment', column = 'reference_id', ids = 'SDY56'):
    try:
        sparql_string = template + f' where {table}.{column} = "{ids}"'
        return sparql_string
    except:
        print("Varibles are not valid strings")
        return 0

'''
df = d6tc.CombinerCSV(glob.glob('C:/Users/user/Downloads/csvfiles/*.csv'), sep=';').to_pandas()

df = d6tc.CombinerCSV(glob.glob('C:/Users/user/Downloads/csvfiles/*.csv'), sep=';').to_pandas()

# Remove Filepath and Filename 
df.drop(columns=["filepath","filename"],inplace=True, axis=1)

# I created Indexes in my database file during testing, so this line
# makes sure there are no null index values in the CSVs
df = df[df['country'].notna()]

# chunksize throttles your database updates so as not to overwhelm any buffers
# NEVER use "if_exists=replace", unless you want to blank your table 100%
#df.to_sql(name='table', con=engine, if_exists='append', index=False, chunksize=200)  
'''

#finally:
 #   if conn:
  #      conn.close()
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 08 10:03:37 2025

@author: Huffmaar
"""

# This code is meant to load in data from MYSQL and then generate two different studies.
import numpy as np

import pandas as pd
import pymysql
import json
from collections import defaultdict




def file_reader(filename):
    try: 
        df = pd.read_csv(filename)
    except:
        print("Could not read as csv file.")
        try:
            df = pd.read_excel(filename)
        except:
            print("Could not read excel file.")
            return 0
    return(df)



def boot_up(host1, user1='kaiser', password1='password', database1='seacdm'):
    try:
        conn = pymysql.connect(host=f'{host1}', user=f'{user1}', password=password1, database=database1)
        print("Connection successful")
        return conn
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return 0

def read_VIGET(VIGET):
    try: 
        dfVIGET = file_reader(VIGET)
    except:
        print("File could not be found")
        return  0
    return dfVIGET



# List of appropriate table names
conn = pymysql.connect(host='localhost', user='root', password='Magicka3', database='seacdm')
vaccine = 'Fluzone'
sex = 'Female' # 'Female' 
time1 = 0
time2 = 7.
#Male, or *
cur = conn.cursor()
#Query for compound vo_ids
#query = f"SELECT expsample_reference_name, organism_id, collection_time, expsample_type FROM seacdm.sample WHERE organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = '{sex}') AND organism_id IN (SELECT organism_id FROM seacdm.intervention WHERE  intervention_type = 'vaccination' AND (material  = 'FluMist') or (material = 'live attenuated influenza vaccine') and T0_definition = 'Time of initial vaccine administration')) AND sample_id IN ( SELECT sample_id FROM seacdm.results WHERE original_assay_type = 'Blood.RNA Expression Assay');"
#Query for singleton sex
query = f"SELECT expsample_reference_name, organism_id, collection_time, expsample_type FROM seacdm.sample WHERE organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = '{sex}') AND organism_id IN (SELECT organism_id FROM seacdm.intervention WHERE  intervention_type = 'vaccination' AND (material  = '{vaccine}')) AND sample_id IN ( SELECT sample_id FROM seacdm.results WHERE original_assay_type = 'Blood.RNA Expression Assay');"

#Query for all all
#query =  f"SELECT expsample_reference_name, organism_id, collection_time, expsample_type FROM seacdm.sample WHERE organism_id IN (SELECT organism_id FROM seacdm.intervention WHERE  intervention_type = 'vaccination' AND (material  = '{vaccine}') and T0_definition = 'Time of initial vaccine administration')) AND sample_id IN ( SELECT sample_id FROM seacdm.results WHERE original_assay_type = 'Blood.RNA Expression Assay');"


#query = f"SELECT expsample_reference_name, organism_id, collection_time FROM seacdm.sample  WHERE organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = 'Female') AND organism_id IN (SELECT organism_id FROM seacdm.intervention  WHERE  intervention_type = 'vaccination' AND (material  = 'Fluvirin')) AND sample_id IN ( SELECT sample_id FROM seacdm.results WHERE original_assay_type = 'Blood.RNA Expression Assay');"
cur.execute(query)
output = cur.fetchall()
df_output = pd.DataFrame(output, columns = ['expsample_reference_name', 'organism_id', 'collection_time', 'expsample_type'])

cur.close()
conn.close()


#does the code work now if I run tis function?


#To use multiple study_id, list 

gene_exp = "/Users/huffmaar/OneDrive - Michigan Medicine/Documents/immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv"
GEXP = read_VIGET(gene_exp)
#Verify GEXP is transposed in order to compare gene names.


test_master = df_output[(df_output['collection_time'] == time1) | (df_output['collection_time'] == time2)].sort_values(by=['organism_id', 'expsample_reference_name', 'collection_time'])
counts = test_master['organism_id'].value_counts()
test_master = test_master[test_master['organism_id'].isin(counts[counts == 2].index)]
test_filtered  = test_master['expsample_reference_name']

#test_master = test_master[test_master['sex'] == 'Female']

#test_master = GEXP.set_index("GeneGene")[test_filtered]
GEXP_filtered = GEXP.set_index("GeneGene")[test_filtered].T


example_gene_expression = test_master.merge(
    GEXP_filtered,
    left_on='expsample_reference_name',
    right_index=True,
    how='left'  # or 'inner', 'right', 'outer' as needed
)

#Code to only get gene names
if vaccine == '*':
    vaccine = 'all'

export = pd.DataFrame(columns = ('gene_name', 'average_gene_expression', 'average_log_gene_expression'))
for cn in example_gene_expression.iloc[:, test_master.columns.shape[0]:-1]:
    mmb = example_gene_expression[cn]
    log_list = []
    for pairs in range(0, mmb.size, 2):
        try:
            sample1 = mmb.iloc[pairs]
            sample2 = mmb.iloc[pairs+1]
            if (sample1 >= 0.2) & (sample2 >= 0.2):
                log_diff = sample1 - sample2
                log_list.append(log_diff)
            else:
                0
        except:
            0
    if len(log_list) >= 3: 
        mean_log = sum(log_list) / len(log_list)
    #make results positive
        if (log_diff > 1):
            export.loc[len(export)] = [cn, 2**log_diff, log_diff]
        else:
            0
    else:
        0
        
export 
try:
    export.to_csv(f'{vaccine}-{sex}-{time1}-{time2}--GeneExpression.csv', sep=',')
except:
    print("empty dataframe silly goose")


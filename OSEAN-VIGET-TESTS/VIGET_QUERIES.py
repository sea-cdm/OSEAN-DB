# -*- coding: utf-8 -*-
"""
Created on Tue Jun 3 10:04:31 2025

@author: huffmaar
"""

# This code is meant to load in data from MYSQL and then generate two different studies.

import pandas as pd
import pymysql
import json
from collections import defaultdict


def SEA_INIT():
    SEA_Study  = pd.DataFrame(columns=['study_id','study_type', 'study_type_id', 'study_name', 'study_description',
                                       'reference_id','reference_source','comments'])
    SEA_Docu =  pd.DataFrame(columns=['documentation_id','study_id','document_name','document_type','document_type_id','documentation_source', 'source_id', 'reference_source', 'citation', 'citation_style','person_id', 'person_id_type','honorific','first_name','middle_name','last_name','person_role', 'comments'])
    SEA_Exper = pd.DataFrame(columns=['experiment_id', 'study_id',
                                      'experiment_type','experiment_type_id','experiment_control','source_id','reference_source','comments'])
    SEA_Inter = pd.DataFrame(columns=['intervention_id','experiment_id','organism_id','material', 'material_id', 'dosage', 'dosage_unit', 'dosage_unit_id', 'intervention_type', 'intervention_type_id',
                                      'intervention_route','intervention_route_id', 'T0_defintion', 'intervention_time', 'intervention_unit', 'intervention_time_unit_id', 'source_id', 'reference_source', 'comments'])
    SEA_Assay = pd.DataFrame(columns=['assay_id','assay_name','documentation_id','assay_type', 'assay_type_id', 'organism', 'reagents', 'platform'])
    SEA_Rslt  = pd.DataFrame(columns=['results_id','experiment_id','group_id','sample_id','analysis_name','analysis_id', 
                                  'original_assay_type', 'assay_id', 'analysis_type',
                                  'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',  'comments' ])
    SEA_Onto  = pd.DataFrame(columns=['ontology_id','documentation_id','ontology_name','ontology_string'])
    SEA_Orgo =  pd.DataFrame(columns=['organism_id','group_id','experiment_id','species','species_id','type', 'type_id',
                                      'age', 'age_unit','age_unit_id','sex','sex_id', 'reference_id' , 'reference_source' , 'comments'  ])
    SEA_Occr  = pd.DataFrame(columns=['occurence_id','organism_id','occurence_name','occurence_id','occurence_severity','occurence_start_time','occurence_start_unit', 'occurence_start_id', 
                                      'occurence_end_time','occurence_end_unit', 'occurence_end_id', 'source_id', 'reference_source', 'comments' ])
    SEA_Samp  = pd.DataFrame(columns=['sample_id','group_id','organism_id', 'collection', 'collection_id', 'collection_time', 'collection_time_unit', 'collection_time_unit_id', 'T0_definition',
                                      'expsample_type','expsample_type_id', 'expsample_reference_id', 'expsample_reference_name',
                                      'biosample_type', 'biosample_type_id', 'biosample_reference_id', 'biosample_reference_name',
                                      'replicates' ])
    SEA_Grop  = pd.DataFrame(columns=['group_id','experiment_id','group_type','group_size','reference_id','reference_source', 'max_age', 'min_age','comments'])
    SEA_Anal  = pd.DataFrame(columns=['analysis_id', 'documentation_id', 'group_id', 'analysis_name', 'analysis_name_id', 'input_data', 'input_data_id' 'reference_id', 'reference_source', 'comments'])
    SEA_Mats  = pd.DataFrame(columns=['material_id','material_name','material_name_id','organization','reference_id','reference_source','comments'])
    export = [SEA_Study, SEA_Docu, SEA_Exper, SEA_Inter, SEA_Assay, SEA_Rslt, SEA_Onto, SEA_Orgo, SEA_Occr, SEA_Samp, SEA_Grop, SEA_Mats, SEA_Anal]
    print("All tables initialized.")
    return export



def consolidate_osean(studyid):
    #Create json file format so that it is nice and pretty
    #Studyid must a valid index id.
    try:
        test_s = STUDY[STUDY['study_id']==studyid]
        try:
            test_e = EXPER[EXPER['study_id'].isin(test_s['study_id'])]
            try:
                test_o = ORGO[ORGO['experiment_id'].isin(test_e['experiment_id'])]
                try:
                    test_i = INTER[INTER['experiment_id'].isin(test_e['experiment_id'])]
                    try:
                        test_p = SAMP[SAMP['organism_id'].isin(test_o['organism_id'])]
                        try:
                            test_r = RESULT[RESULT['sample_id'].isin(test_p['sample_id'])]
                            
                            test_se = test_s.merge(test_e, on='study_id')
                            test_se = test_se.drop(columns=['comments_x', 'comments_y'])
                            test_se = test_se.rename(columns={'reference_source_x':'study_reference_source', 'reference_source_y':'experiment_reference_source'})
                            test_pr = test_p.merge(test_r, on='sample_id').drop(columns=['group_id_x']).rename(columns={'group_id_y':'group_id'})
                            test_oi = test_i.merge(test_o, on='organism_id').drop(columns=['experiment_id_x'])
                            test_oi = test_oi.rename(columns={'experiment_id_y':'experiment_id', 'reference_id_y':'intervention_reference_id', 'reference_id_x':'organism_reference_id', 'reference_source_y':'intervention_reference_source','reference_source_x':'organism_reference_source' })
                            test_oi = test_oi.rename(columns={'comments_x':'intevention_comments', 'comments_y':'organism_comments'})
                            test_proi = test_pr.merge(test_oi, on='organism_id')
                            test_proi = test_proi.drop(columns={'experiment_id_y','T0_defintion', 'group_id_y'})
                            test_proi = test_proi.rename(columns={'T0_defintion_x':'T0_definition', 'experiment_id_x':'experiment_id', 'group_id_x':'group_id'})
                            # fix typos
                            test_seproi = test_proi.merge(test_se, on='experiment_id')
                            test_seproi = test_seproi.rename(columns={'source_id_x':'intervention_source_id', 'source_id_y':'experiment_source_id', 'reference_id_y':'study_reference_id', 'reference_id_x':'intervention_reference_id'})
                            return test_seproi
                        except:
                            print("Could not find valid results")
                            return 0
                    except:
                        print("Could not find valid sanples")
                        return 0
                except: 
                    print("Could not find valid interventions")
                    return 0
            except:
                print("Could not find valid organisms")
                return 0
        except:
            print("Could not find valid experiments")
            return 0 
    except:
        print(f"Could not run using index f{studyid}, make sure it is an index.")
        return 0

def export_osean_json (osean_data, filename):
    #filename string, osean_data is created from consolidate_osean
    try:
        json_seproi = test_seproi.to_json( f'{filename}_osean_output.json', orient='table', indent=4)
    except:
        print(f"Try again.")
    return 0
    
def compare_osean_json ( studyid1, studyid2, filename1, filename2):
    # You need the study ids you ask for.
    try:
        first_data = consolidate_osean(studyid1)
        export_osean_json(first_data, filename1)
        second_data = consolidate_osean(studyid2)
        export_osean_json(second_data, filename2)
    except:
        print("Error, please try proper inputs.")
    return 0

def boot_up(host1, user1='kaiser', password1='password', database1='seacdm'):
    try:
        conn = pymysql.connect(host=f'{host1}', user=f'{user1}', password=password1, database=database1)
        print("Connection successful")
        return conn
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return 0


templates = SEA_INIT()
tables = templates
mastertables = ['study', 'document', 'experiment','intervention', 'assay', 'results', 'ontology', 'organism', 'occurence',
               'sample', 'group', 'analysis', 'material']

# List of appropriate table names
host_2='localhost',
user='user',
password='password',
database='seacdm'

conn = pymysql.connect(host='localhost', user='root', password='Magicka3', database='seacdm')
#conn = boot_up(user, password, database)    Broke but idk why.
cur = conn.cursor()


def search_GEXP(sample_ids, gene_exp):
    #sample_ids is a list of sample_id according to SEACDM
    #gene_exp is path to read VIGET file.
    GEXP = read_VIGET(gene_exp)
    GEXP = GEXP.T
    QUERIED = SAMP[SAMP['sample_id'].isin(query_ids)]['expsample_reference_name'].tolist()
    QUERIED.append('GeneGene')
    GEXP_sub = GEXP.loc[QUERIED]
    #Save data so it is good.
    GEXP_sub.to_csv('GEXP.csv', sep = '\c')

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

def read_VIGET(VIGET):
    try: 
        dfVIGET = file_reader(VIGET)
    except:
        print("File could not be found")
        return  0
    return dfVIGET


def load_VIGET(VIGET):
    try:
        VIGET = read_VIGET(VIGET)
    except:
        print("File could not be loaded.")
    template = SEA_INIT()
    STUDY = template[0]
    
    "All files are loaded."
    return 0


def load_osean(mastertables, tables):
    #mastertables is list name of tables in sea cdm
    # table is tables of interest for user
    table_columns = []
    for i in range(len(mastertables)):
        madlibs = mastertables[i]
        try:
            sqlstring = f"select * from {madlibs}"
            suma = cur.execute(sqlstring)
            print(f"There are {suma} entries in {madlibs}.")
            output = cur.fetchall()
            #colnam = f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{madlibs}' and TABLE_SCHEMA = 'seacdm'"
            #cur.execute(colnam)
            tables[i] = output
            #colnames = cur.fetchall()
            #proper order
            #sorted_list = sorted(colnames, key=lambda x: x[4])
            #col_names = [x[3] for x in sorted_list]
            #print(table_names)
            #print("The unique rows are the following: ")
            #output.columns = col_names
            print(output)
            # adding this to work
            #table_columns.append(table_names)
            try:
                #templates[i] = templates[i].concat(tables[i])
                tables[i] = pd.DataFrame(tables[i])
                #templates[i] = pd.DataFrame(tables[i], columns = templates[i].columns)
                print('Template aquired.')
            except:
               0
                # print(f"There is no {madlibs} table created")
            #for row in output:
             #   print(row)
              #  print("\n")
        except:
            print(f"There is no {madlibs} table when queried")
    return tables

masters = load_osean(mastertables, tables)


def load_columns(mastertables, tables):
    #mastertables is list name of tables in sea cdm
    # table is tables of interest for user
    column_names = []
    for i in range(len(mastertables)):
        madlibs = mastertables[i]
        try:
            colnam = f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{madlibs}' and TABLE_SCHEMA = 'seacdm'"
            cur.execute(colnam)
            colnames = cur.fetchall()
            #proper order
            sorted_list = sorted(colnames, key=lambda x: x[4])
            col_names = [x[3] for x in sorted_list]
            column_names.append(col_names)
            #print(col_names)

            try:
                #templates[i] = templates[i].concat(tables[i])
                #tables[i] = pd.DataFrame(tables[i])
                #templates[i] = pd.DataFrame(tables[i], columns = templates[i].columns)
                print('Template aquired.')
            except:
               0
                # print(f"There is no {madlibs} table created")
            #for row in output:
             #   print(row)
              #  print("\n")
        except:
            print(f"There is no {madlibs} table when queried")
    return column_names


def filtered_osean(mastertables, tables):
    tables = load_osean(mastertables, tables)
    column_names = load_columns(mastertables, tables)
    for ij in range(len(column_names)):
        if column_names[ij] != []:
            tables[ij].columns = column_names[ij]
    return tables

#filtered is table used for names to make sure code works...
filtered = filtered_osean(mastertables, tables)


STUDY = filtered[0] 
DOCU = filtered[1]
EXPER = filtered[2] 
INTER = filtered[3] 
ASSAY = filtered[4]
RESULT = filtered[5] 
ONTO = filtered[6]
ORGO = filtered[7] 
OCCR = filtered[8] 
SAMP = filtered[9]
GROUP = filtered[10]
ALYS = filtered[11]
MAT = filtered[12]

#does the code work now if I run tis function?


def osean_json(study_id, filename):
    jason = consolidate_osean(study_id)
    jason_json = jason.to_json(orient='index', indent=4)
    jason_dict = json.loads(jason_json)

    # Step 3: Convert to list of records
    records = list(jason_dict.values())

    # Step 4: Sort records by 'study_id'
    records.sort(key=lambda x: x['study_id'])

    # Step 5: Merge records by 'group_id', appending values
    merged = defaultdict(lambda: defaultdict(list))

    for record in records:
        group_id = record['group_id']
        for key, value in record.items():
            if key == 'group_id':
                merged[group_id][key] = value  # scalar
            else:
                if value not in merged[group_id][key]:
                    merged[group_id][key].append(value)

    # Step 6: Flatten single-item lists
    final = []
    for grouped_record in merged.values():
        flat_record = {}
        for k, v in grouped_record.items():
            flat_record[k] = v[0] if isinstance(v, list) and len(v) == 1 else v
        final.append(flat_record)

    # Step 7: Convert to DataFrame (optional)
    merged_df = pd.DataFrame(final)

    # Step 8: Save or inspect
    with open(f'study {study_id}.json', 'w') as f:
        json.dump(final, f, indent=2)
    return merged_df

def compare_osean_json(study_id1, study_id2, filename):
    filename1 = filename+str(study_id1)
    filename2 = filename+str(study_id2)
    osean_json(study_id1, filename1)
    osean_json(study_id2, filename2)
    return 0


# Step 1: Original DataFrame to JSON
jason = consolidate_osean(1)
jason_json = jason.to_json(orient='index', indent=4)

# Step 2: Parse JSON string to dict
jason_dict = json.loads(jason_json)

# Step 3: Convert to list of records
records = list(jason_dict.values())

# Step 4: Sort records by 'study_id'
records.sort(key=lambda x: x['study_id'])

# Step 5: Merge records by 'group_id', appending values
merged = defaultdict(lambda: defaultdict(list))

for record in records:
    group_id = record['group_id']
    for key, value in record.items():
        if key == 'group_id':
            merged[group_id][key] = value  # scalar
        else:
            if value not in merged[group_id][key]:
                merged[group_id][key].append(value)

# Step 6: Flatten single-item lists
final = []
for grouped_record in merged.values():
    flat_record = {}
    for k, v in grouped_record.items():
        flat_record[k] = v[0] if isinstance(v, list) and len(v) == 1 else v
    final.append(flat_record)

# Step 7: Convert to DataFrame (optional)
merged_df = pd.DataFrame(final)

# Step 8: Save or inspect
with open('merged_by_group_id.json', 'w') as f:
    json.dump(final, f, indent=2)
    

GEXP = read_VIGET(gene_exp)
GEXP = GEXP.T


def gene_expression(sample1, sample2, datafile):
    kholi 








test_s = STUDY[STUDY['study_id']==1]
test_e = EXPER[EXPER['study_id'].isin(test_s['study_id'])]
test_o = ORGO[ORGO['experiment_id'].isin(test_e['experiment_id'])]
test_i = INTER[INTER['experiment_id'].isin(test_e['experiment_id'])]
test_p = SAMP[SAMP['organism_id'].isin(test_o['organism_id'])]
test_r = RESULT[RESULT['sample_id'].isin(test_p['sample_id'])]
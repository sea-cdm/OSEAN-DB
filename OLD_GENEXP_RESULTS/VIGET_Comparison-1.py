# -*- coding: utf-8 -*-
"""
Created on Tue Jun 3 10:04:31 2025

@author: huffmaar
"""

# This code is meant to load in data from MYSQL and then generate two different studies.
import numpy as np
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

def big_osean():
    #Create json file format so that it is nice and pretty
    #Studyid must a valid index id.
    try:
        #test_s = STUDY[STUDY['study_id']==studyid]
        test_s = STUDY[STUDY['study_id']]
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
        print(f"Could not run using index, make sure it is an index.")

def consolidate_osean(studyid):
    #Create json file format so that it is nice and pretty
    #Studyid must a valid index id.
    try:
        #test_s = STUDY[STUDY['study_id']==studyid]
        test_s = STUDY[STUDY['study_id'].isin(studyid)]
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
        print(f"Could not run using index {studyid}, make sure it is an index.")
        return 0

def export_osean_json (osean_data, filename):
    #filename string, osean_data is created from consolidate_osean
    try:
        json_seproi = osean_data.to_json( f'{filename}_osean_output.json', orient='table', indent=4)
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


#To use multiple study_id, list 

study_id = EXPER[EXPER['experiment_id'].isin(
    INTER[(INTER['material'] == 'Yellow fever 17D vaccine vector') | 
          (INTER['material'] == 'YF-Vax')]['experiment_id']
)]['study_id']
#study_id = 4514
#study_id = np.int64(study_id)


# Step 1: Original DataFrame to JSON
debug_id = STUDY.loc[24]['study_id']
jason = consolidate_osean(debug_id)



vaccine_names = [
    'Fluzone',
    'Influenza virus vaccine',
    'Trivalent inactivated influenza',
    '2008-2009 trivalent influenza vaccine',
    'Fluarix',
    'FluMist',
    'Fluvirin',
    '2011?2012 trivalent inactivated vaccine (A/California/7/09 (H1N1,), A/Perth /16/2009 (H3N2), and B/Brisbane/60/2008)',
    'live attenuated influenza vaccine'
]

#DEBUG NAMES
vaccine_names = [
    'Fluzone',
    '2008-2009 trivalent influenza vaccine',
    'Fluarix',
    'Fluvirin',
    '2011?2012 trivalent inactivated vaccine (A/California/7/09 (H1N1,), A/Perth /16/2009 (H3N2), and B/Brisbane/60/2008)',
    'live attenuated influenza vaccine'
]

gene_exp = "/Users/huffmaar/OneDrive - Michigan Medicine/Documents/immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv"
GEXP = read_VIGET(gene_exp)
#Verify GEXP is transposed in order to compare gene names.

# Load up all pairs at date
# Append averages of each row to date
# Average of averages to return
# Rerutn filtered name list for code

def gene_expression(sample1, sample2, GEXP):
    try:
        gexp_1 = GEXP[sample1]
        gexp_2 = GEXP[sample2]
        try:
            gexp_ratio = 2**(gexp_2 - gexp_1)
            return gexp_ratio
        except:
            print('Could not divide two different rows')
            return 0
    except:
        print(f'Could not load table with samples {sample1} or {sample2}')
        return 0

'''def gene_names_interest(criteria, criteria_column, criterea_list, day1, day2, datafile):
    #critiera is table that is used to look at for restriction for massive json
    #criteria_list is values you want to look at it.
    try:
        export = pd.DataFrame(columns = jason.columns)
        export = pd.concat([export, gexp_ratio.to_frame().T])
        filtered_criteria = criteria[criteria[criteria_column].isin(criteria_list)]
        #Load in table of results for findings. 
        for i in criteria_list:
            for j in criteria_list:
                if i != j:
                    0
            gexp_1 = criteria
            gexp_2 = GEXP.T.iloc[j]
            gene_expression(gexp1, gexp2)
    except:
        print('could not intersect')
        return 0'''

genes_of_interest = 0

jjaass = big_osean()

logic_gate = 'Menactra'




# Now get study_ids from EXPER matching those experiment_ids
study_id = EXPER[EXPER['experiment_id'].isin(relevant_exp_ids)]['study_id']


study_id = EXPER[EXPER['experiment_id'].isin(INTER[INTER['material'] == 'Fluzone'])]['experiment_id']



# influenza vaccination, female, rna assay
export_criteria = ['sample_id', 'organism_id', 'sex', 'intervention_type', 'material', 'organism_id', 'expsample_reference_id', 'collection_time', 'analysis_type']
#jason.loc[export_criteria]

# Test loops to get differential expression across every filter.

#df_with_mean = pd.concat([df, mean_row.to_frame().T])

#export = pd.DataFrame(columns = jason.columns)
#export = pd.concat([export, gexp_ratio.to_frame().T])

#Code that sorts between different locations for dataset.
time1 = 0
time2 = 14

study_id = [299]

study_ids = ['SDY1119','SDY1276', 'SDY144', 'SDY180', 'SDY269', 'SDY270', 'SDY311', 'SDY61', 'SDY80']
study_id = STUDY[STUDY['reference_id'].isin(study_ids)]['study_id']
try:
    jason = consolidate_osean(study_id)
except:
    jason = consolidate_osean([study_ids])
test = jason[(jason['collection_time'] == time1) | (jason['collection_time'] == time2)].sort_values(by=['organism_id','collection_time'])
counts = test['organism_id'].value_counts()
test_master = test[test['organism_id'].isin(counts[counts >= 2].index)]  
jason_1 = test_master[test_master['sex'] == 'Male']
jason_2 = test_master[test_master['sex'] == 'Female']
test_filtered  = test_master['expsample_reference_name']

test_master = GEXP.set_index("GeneGene")[test_filtered]
GEXP_filtered = GEXP.set_index("GeneGene")[test_filtered].loc["E2F2"].T
GEXP_filtered.name = 'gene_expression'
example_gene_expression = test_master.merge(
    GEXP_filtered,
    left_on='expsample_reference_name',
    right_index=True,
    how='left'  # or 'inner', 'right', 'outer' as needed
)
example_gene_expression['gene_name'] = 'E2F2'




export = example_gene_expression[['gene_name', 'gene_expression', 'sample_id', 'organism_id', 'collection', 'collection_id',
       'collection_time', 'collection_time_unit', 'collection_time_unit_id',
       'T0_definition_x', 'expsample_type', 'expsample_type_id',
       'expsample_reference_id', 'expsample_reference_name', 'biosample_type',
       'biosample_type_id', 'biosample_reference_id',
       'biosample_reference_name', 'replicates', 'expsample_source',
       'results_id', 'experiment_id', 'group_id', 'analysis_name',
       'analysis_id', 'original_assay_type', 'assay_id', 'analysis_type',
       'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',
       'comments', 'document_id', 'original_assay_type_id', 'intervention_id',
       'material', 'material_id', 'dosage', 'dosage_unit', 'dosage_unit_id',
       'intervention_type', 'intervention_type_id', 'intervention_route',
       'intervention_route_id', 'intervention_time', 'intervention_unit',
       'intervention_time_unit_id', 'intervention_source_id',
       'organism_reference_source', 'intevention_comments', 'T0_definition_y',
       'species', 'species_id', 'type', 'type_id', 'age', 'age_unit',
       'age_unit_id', 'sex', 'sex_id', 'intervention_reference_id',
       'intervention_reference_source', 'organism_comments', 'study_id',
       'study_type', 'study_type_id', 'study_name', 'study_description',
       'study_reference_id', 'study_reference_source', 'experiment_type',
       'experiment_type_id', 'experiment_control', 'experiment_source_id',
       'experiment_reference_source', 'experiment_name'
       ]]



#Species missing... wierd.
exported = export[['gene_name', 'gene_expression', 
                 'species', 'type', 'sex', 'material', 'collection', 'age', 'age_unit',
       'collection_time', 'collection_time_unit',
       'expsample_type', 
       'expsample_reference_id', 'expsample_reference_name', 'biosample_type',
       'biosample_type_id', 'biosample_reference_id',
       'biosample_reference_name', 'replicates', 'expsample_source',
        'analysis_name',
       'analysis_id', 'original_assay_type', 'assay_id', 'analysis_type',
       'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',
       'comments', 'original_assay_type_id',
       'intervention_type', 'intervention_time', 'intervention_unit',
       'intervention_source_id',
       'organism_reference_source', 'T0_definition_y',
       'intervention_reference_id',
       'study_type', 'study_type_id', 'study_name', 'study_description',
       'study_reference_id', 'study_reference_source', 'experiment_type',
       'experiment_control', 'experiment_source_id',
       'experiment_name', 'sample_id', 'organism_id', 'study_id', 'results_id', 'experiment_id', 'group_id', ]]
exported['species'] = 'human'
exported.set_index('expsample_reference_name')
exported['gene_ratio'] = 'Null'

for pairs in range(0, exported.shape[0], 2):
    try:
        sample1 = exported.iloc[pairs]['gene_expression']
        sample2 = exported.iloc[pairs+1]['gene_expression']
        print(2**(sample1 - sample2 ))
        exported['gene_ratio'][pairs] = 2**(sample1 - sample2 )
        exported['gene_ratio'][pairs+1] = 2**(sample1 - sample2 )

    except:
        0


exported.to_csv("Intermediate_E2F2.csv", sep = ',')


exported["gene_ratio"]


 







jason.append(GEXP)

test_filtered.to_csv("Intermediate.csv", sep = ',')

test_filtered['expsample_reference_name']
GeneGene = pd.DataFrame(GEXP['GeneGene'])

final_list = GEXP.loc[test_filtered['expsample_reference_name']]
GEXP_filtered.to_csv('seacdm_raw_Gene_List_E2F2.csv')

FullGenes =  test_filtered['expsample_reference_name']



ALLMEANS = pd.DataFrame()


for pairs in range(0, test_filtered.shape[0], 2):
    try:
        sample1 = test_filtered.iloc[pairs]['expsample_reference_name']
        sample2 = test_filtered.iloc[pairs+1]['expsample_reference_name']
    
        determinant = gene_expression(sample1, sample2, GEXP)
        determinant = np.ravel(determinant)  # ensure it's a 1D vector
        
        col_name = f'{sample1}_vs_{sample2}'
        index_clean = pd.Index(GEXP['GeneGene'].astype(str).values)
    
        # Check length match
        if len(determinant) != len(index_clean):
            raise ValueError("Shape mismatch: determinant and GeneGene index are different lengths")
    
        determinant_df = pd.DataFrame({col_name: determinant}, index=index_clean)
        ALLMEANS = pd.concat([ALLMEANS, determinant_df], axis=1)
        print(ALLMEANS)
    except:
        0
gene_list = ALLMEANS.T.mean()
valid_gene_list = gene_list[gene_list.abs() > (2**.2)]
ALLMEANS = pd.concat([ALLMEANS, gene_list], axis=1)
ALLMEANS = pd.concat([ALLMEANS, valid_gene_list], axis=1)
ALLMEANS.to_csv("Gene_List.csv", sep = ',')

gsm1 = 'GSM1422029'
gsm2 = 'GSM1422026'

        


"""for pairs in range(0, test_filtered.shape[0], 2):
    sample1 = test_filtered.iloc[pairs]['expsample_reference_name']
    sample2 = test_filtered.iloc[pairs+1]['expsample_reference_name']
    determinant = gene_expression(sample1, sample2, GEXP)
    Gene"Gene[determinant "> 1.0]"""



"""
for pairs in range(0, test_filtered.shape[0], 2):
    sample1 = test_filtered.iloc[pairs]['expsample_reference_name']
    sample2 = test_filtered.iloc[pairs+1]['expsample_reference_name']

    determinant = gene_expression(sample1, sample2, GEXP)

    # Create a DataFrame with GeneGene as index and a unique column name
    col_name = f'{sample1}_vs_{sample2}'
    determinant_df = pd.DataFrame({col_name: determinant}, index=GEXP['GeneGene'])

    # Concatenate as new column
    ALLMEANS = pd.concat([ALLMEANS, determinant_df], axis=1)

ALLMEANS.mean()"""



ALLMEANS = pd.DataFrame(index = GEXP['GeneGene'])


# Get experiment_ids from INTER
relevant_exp_ids = INTER[INTER['material'].isin(vaccine_names)]['experiment_id']
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
    


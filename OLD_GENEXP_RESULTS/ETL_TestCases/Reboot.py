# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:13:38 2025

@author: huffmaar
"""
import pandas as pd
import pymysql

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


templates = SEA_INIT()
tables = templates
mastertables = ['study', 'document', 'experiment','intervention', 'assay', 'results', 'ontology', 'organism', 'occurence',
               'sample', 'group', 'analysis', 'material']

# List of appropriate table names
host_2='localhost',
user='root',
password='Magicka3',
database='seacdm'
def boot_up(host1, user1='kaiser', password1='password', database1='seacdm'):
    try:
        conn = pymysql.connect(host=f'{host1}', user=f'{user1}', password=password1, database=database1)
        print("Connection successful")
        return conn
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return 0

conn = pymysql.connect(host='localhost', user='root', password='Magicka3', database='seacdm')
#conn = boot_up(user, password, database)    Broke but idk why.
cur = conn.cursor()




for i in range(len(mastertables)):
    madlibs = mastertables[i]
    try:
        sqlstring = f"select * from {madlibs}"
        suma = cur.execute(sqlstring)
        print(f"There are {suma} entries in {madlibs}.")
        output = cur.fetchall()
        #print("The unique rows are the following: ")
        tables[i] = output
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
for ziz in range(len(tables)):
    try:
        print(ziz)
        sized = tables[ziz].shape[1]
        tables[ziz].columns = templates[ziz].columns[0:sized]
    except:
        print(f'No table found at position {ziz}.')


for j in range(len(templates[0].columns)-1):
    print(templates[0][j])
    

appended_df = pd.concat([templates[0], tables[0]], ignore_index=True)


STUDY = tables[0]
EXPER = tables[2]
INTER = tables[0]
ORGO = tables[0]
SAMP = tables[0]
RESULT = tables[12]
MATERIAL = tables[12]

        
        
        
        
def clarify_where (template, table = 'vigetexperiment', column = 'reference_id', ids = 'SDY56'):
    try:
        sparql_string = template + f' where {table}.{column} = "{ids}"'
        return sparql_string
    except:
        print("Varibles are not valid strings")
        return 0

    



# Basic Prototype to Serach for All terms for query
mastertables = ['vigetstudy', 'vigetexperiment', 'vigetorganism', 'vigetintervention', 'vigetsample', 'vigetresults']
for i in mastertables:
    madlibs = i
    try:
        sqlstring = f"select * from {madlibs}"
        suma = cur.execute(sqlstring)
        print(f"There are {suma} entries in {madlibs}.")
        output = cur.fetchall()
        print("The unique rows are the following: ")
        
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


        

#finally:
 #   if conn:
  #      conn.close()
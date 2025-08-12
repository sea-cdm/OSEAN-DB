# -*- coding: utf-8 -*-
"""
Created on Tue Jun 3 10:04:31 2025

@author: huffmaar
"""

# This code is meant to aid in be called by different scripts. 
# PURE SPARQL variation includes code set up to run.


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

def python_queries(tablename, columnname, columnvalues, tables):
    #All two must be lists of equal length and it must be good.
    pyqflag = False
    try:
        if (type(tablename) == list) & (type(columnname)) == list & (type(columnvalues) == list):
            if len(tablename) == len(columnname) == len(columnvalues):
                pyqflag = True 
            else:
                print("You do not have a matching pair of tables to columns")
    except:
        0
    else:
        0
    if pyqflag == True:
        return tables[tablename[columnname]]
    else:
        return pyqflag

def consolidate_osean(studyid, STUDY, EXPER, ORGO, INTER, SAMP, RESULT):
    #Create json file format so that it is nice and pretty
    #Studyid must a valid index id.
    try:
        test_s = STUDY[STUDY['study_id']==studyid]
        test_e = EXPER[EXPER['study_id'].isin(test_s['study_id'])]
        test_o = ORGO[ORGO['experiment_id'].isin(test_e['experiment_id'])]
        test_i = INTER[INTER['experiment_id'].isin(test_e['experiment_id'])]
        test_p = SAMP[SAMP['organism_id'].isin(test_o['organism_id'])]
        test_r = RESULT[RESULT['sample_id'].isin(test_p['sample_id'])]
        test_se = test_s.merge(test_e, on='study_id')
        test_se = test_se.drop(columns=['comments_x', 'comments_y'])
        test_se = test_se.rename(columns={'reference_source_x':'study_reference_source', 'reference_source_y':'experiment_reference_source'})
        test_pr = test_p.merge(test_r, on='sample_id').drop(columns=['group_id_x']).rename(columns={'group_id_y':'group_id'})
        test_oi = test_i.merge(test_o, on='organism_id').drop(columns=['experiment_id_x'])
        test_oi = test_oi.rename(columns={'experiment_id_y':'experiment_id', 'reference_id_y':'intervention_reference_id', 'reference_id_x':'organism_reference_id', 'reference_source_y':'intervention_reference_source','reference_source_x':'organism_reference_source' })
        test_oi = test_oi.rename(columns={'comments_x':'intevention_comments', 'comments_y':'organsim_comments'})
        test_proi = test_pr.merge(test_oi, on='organism_id')
        test_proi = test_proi.drop(columns={'experiment_id_y','T0_defintion', 'group_id_y'})
        test_proi = test_proi.rename(columns={'T0_defintion_x':'T0_definition', 'experiment_id_x':'experiment_id', 'group_id_x':'group_id'})
        # fix typos
        test_seproi = test_proi.merge(test_se, on='experiment_id')
        test_seproi = test_seproi.rename(columns={'source_id_x':'intervention_source_id', 'source_id_y':'experiment_source_id', 'reference_id_y':'study_reference_id', 'reference_id_x':'intervention_reference_id'})
        return test_seproi
    except:
        print(f"Could not run using index f{studyid}, make sure it is an index.")
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
    templates = SEA_INIT()
    for ziz in range(len(tables)):
        try:
            print(ziz)
            sized = tables[ziz].shape[1]
            tables[ziz].columns = templates[ziz].columns[0:sized]
        except:
            print(f'No table found at position {ziz}.')
    return tables







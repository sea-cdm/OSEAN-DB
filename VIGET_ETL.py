# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 10:41:46 2025

@author: huffmaar
"""

import pandas as pd
import numpy as np
import sys
    
if len(sys.argv) > 1:
   filename = sys.argv[1]
else:
   print("Please provide the absolute path of the VIGET metadata file as a command-line argument.")


VIGET = filename

#How to convert files without any rows missing....
#Only utilzie influenza files.

Study_Index = 0

def dummy_loop(term, length):
    #Must be string
    try:
        blanck = []
        print(length)
        for i in range(length):
            blanck.append(length)
            return blanck
    except:
        print("Invalid Inputs")
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

def SEA_INIT():
    SEA_Study  = pd.DataFrame(columns=['study_id','study_type', 'study_type_id', 'study_name', 
                                       'reference_id','reference_source','comments'])
    SEA_Docu =  pd.DataFrame(columns=['documentation_id','study_id','document_name','document_type','document_type_id','documentaiton_source', 'source_id', 'reference_source', 'citation', 'citation_style','person_id', 'person_id_type','honorific','first_name','middle_name','last_name','person_role', 'comments'])
    SEA_Exper = pd.DataFrame(columns=['experiment_id', 'study_id',
                                      'experiment_type','experiment_type_id','experiment_control','source_id','reference_source','comments'])
    SEA_Inter = pd.DataFrame(columns=['intervention_id','experiment_id','organism_id','material', 'material_id', 'dosage', 'dosage_unit', 'dosage_unit_id', 
                                      'intervention_route','intervention_route_id', 'T0 Defintion', 'intervention_time', 'intervention_unit', 'intervention_time_unit_id', 'source_id', 'reference_source', 'comments'])
    SEA_Assay  = pd.DataFrame(columns=['assay_id','assay_name','documentation_id','sea_assay','sea_assay_id','assay_type_id','organism', 'reagents', 'platform', 'parameters', 'parameter_values', 'input_data' ])
    SEA_Rslt  = pd.DataFrame(columns=['results_id','experiment_id','Group_id','sample_id','assay_name','assay_id', 
                                  'original_assay_type', 'original_assay_type_id', 'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',  'comments' ])
    SEA_Onto  = pd.DataFrame(columns=['ontology_id','documentation_id','ontology_name','ontology_string'])
    SEA_Orgo =  pd.DataFrame(columns=['organism_id','Group_id','experiment_id','species','species_id','type', 'type_id'
                                      'age', 'age_unit','age_unit_id','sex','sex_id', 'source_id' , 'reference_source' , 'comments'  ])
    SEA_Occr  = pd.DataFrame(columns=['occurence_id','organism_id','occurence_Name','occurence_id','occurence_severity','occurence_start_time','occurence_start_unit', 'occurence_start_id', 
                                      'occurence_end_time','occurence_end_unit', 'occurence_end_id', 'source_id', 'reference_source', 'comments' ])
    SEA_Samp  = pd.DataFrame(columns=['sample_id','group_id','organism_id', 'collection',
                                      'expsample_type','expsample_type_id', 'expsample_reference_id', 'expsample_reference_name',
                                      'biosampl_type', 'biosample_type_id', 'biosample_reference_id', 'biosample_reference_name',
                                      'expsample_source','expsamplesource_id', 'replicates' ])
    SEA_Grop  = pd.DataFrame(columns=['group_id','experiment_id','Consistency','group_size','reference_id','reference_source','comments'])
    SEA_Mats  = pd.DataFrame(columns=['material_id','material_name','ontology_id','Organization','reference_id','reference_source','comments'])
    export = [SEA_Study, SEA_Docu, SEA_Exper, SEA_Inter, SEA_Assay, SEA_Rslt, SEA_Onto, SEA_Orgo, SEA_Occr, SEA_Samp, SEA_Grop, SEA_Mats]
    print("All tables initialized.")
    return export


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

def save_list(df_list):
    try:
        for i in df_list:
            zeq = i.columns[0][0:-2]+".csv"
            i.to_csv(zeq)
    except:
        print("Could not save list.")
    return 0

def _source_keys(df1, df2, col1, col2):
    #df1 should have column joined be lost.
    outer_join_df = pd.merge(df1, df2, left_on=col1, right_on=col2, how='outer')

    return outer_join_df

# Intialize SEATEmplates
SEATemplates = SEA_INIT()
# Strings for filenames, to be changed lagter.

#GEXP = read_VIGET(gene_exp)
#GEXP = GEXP.T


#Drop duplicate _ids in tables after making sure mapping does not go.

#for i in SEATemplates:
#    print(i)
#    zeq = i.columns[0][0:-2]+".csv"
#    i.to_csv(zeq)

SEATemplates = SEA_INIT()
viget = read_VIGET(VIGET)

STUDY = SEATemplates[0]
STUDY['source_id'] = viget['immport_study_accession']
STUDY['study_name'] = viget['study_title']
STUDY = STUDY.drop_duplicates()
STUDY['study_type'] = 'Experimental Study'
STUDY['reference_source'] = 'ImmPort'
#STUDY['study_id'] = STUDY.index

viget = pd.merge(viget, STUDY.iloc[:,[0,7]], 
                         left_on="immport_study_accession", right_on="source_id", how='outer')
#viget['study_id'] = viget['source_id']

#STUDY.iloc[:,[0, 4]]
SEATemplates[0] = STUDY


ONTO = SEATemplates[6]
ontology = pd.Series({'ontology_id': 1,
                           'documentation_id': 'obofoundry.org/ontology/vo',
                           'ontology_name': "Vaccine_Ontology",
                           'ontology_string': "VO"})
ONTO = pd.concat([ONTO, ontology.to_frame().T])


ORGO = SEATemplates[7]
ORGO['reference_source'] = 'ImmPort'
#ORGO['Group_id'] = viget['']
#ORGO['organism'] = 
ORGO['species'] = 'human'
ORGO['species_id'] = 9606
ORGO['sex'] = viget['gender']
ORGO['type'] = viget['race']
#ORGO['experiment_id'] = viget['']
ORGO['source_id'] = viget['immport_subject_accession']
ORGO = ORGO.drop_duplicates()
#ORGO['organism_id'] = ORGO.index
SEATemplates[7] = ORGO.drop_duplicates()
siget = viget
siget = pd.merge(viget, ORGO.iloc[:,[0,-2]], 
                         left_on="immport_subject_accession", right_on="reference_source", how='outer')
#viget['study_id'] = viget['source_id']

# intervention Table is complete but does not generate linking _id

INTER= SEATemplates[3]
INTER['material_id'] = viget['immport_immune_exposure_material_id']
INTER['material'] = viget['vaccine']
INTER['intervention_time'] = viget['immport_vaccination_time']
INTER['intervention_unit'] = viget['immport_vaccination_time_unit']
INTER['source_id'] = viget['gpl']
INTER['t0_definition'] = viget['day_0_def']
INTER['reference_source'] = 'ImmPort'
INTER['material_name'] = viget['platform_desc']
ZINTER = INTER.drop_duplicates()
INTER['organism_id'] = viget['immport_subject_accession']

SEATemplates[3] = INTER.drop_duplicates()








# siget = pd.merge(siget, STUDY, left_on="immport_study_accession", right_on="source_id", how='outer')

EXPER =  SEATemplates[2]
#Placeholder for Experiments.
ZEXPER = EXPER
ZEXPER['experiment_type'] = viget['vaccine']+viget['immport_vaccination_time'].astype(str)
ZEXPER = ZEXPER.drop_duplicates()
ZEXPER['experiment_id'] = ZEXPER.index
SEATemplates[2] = ZEXPER




#df_binary = np.where(df > 0, 1, 0)
#df = pd.DataFrame(df_binary, index=df.index, columns=df.columns)


SEATemplates[2] = STUDY.drop_duplicates()






SAMP=SEATemplates[9]
#SAMP['source_id'] = viget['gsm']

#SAMP['organism_id'] = viget['organism_id']
SAMP['organism_id'] = viget['immport_subject_accession']
SAMP['biosample_type'] = viget['biosample_type']
SAMP['expsample_type'] =  viget['type_subtype']
SAMP['expsample_source'] = viget['expsample_repository_name']
SAMP['biosample_reference_id'] = viget['immport_biosample_accession']
SAMP['expsample_reference_id'] = viget['gse']
SAMP['expsample_reference_name'] = viget['gsm']
#SAMP['source_id']
SEATemplates[9] = SAMP.drop_duplicates()
SEATemplates[9]['biosample_reference_name'] = 'ImmPort'


# Strings for filenames, to be changed lagter.
VIGET = "/Users/huffmaar/Documents/SEA-CDM-SQL-Imports/ImmuneExposureGeneExpression_020922_Raw.csv"
VIGETGENE = "a"
gene_exp = "/Users/huffmaar/OneDrive - Michigan Medicine/Documents/immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv"


GEXP = read_VIGET(gene_exp)
GEXP = GEXP.T


# Generate REsults, does not includ mapping of appropriate _ids
RESULT = SEATemplates[5]

RESULT["sample_id"] = viget["expsample_repository_name"]
#RESULT["data_dimensions"] = 22343
RESULT["datatype"] = "VIGET"
RESULT["file_access"] = "Zenodo"
RESULT["file_type"] = "csv"
RESULT["document_id"] = "immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv"
RESULT["assay_name"] = "Gene Expression Assay"
RESULT["original_assay_type_name"] = "Gene Expression Assay"
RESULT["data_transformation"] = "Threshold"
RESULT["replications"] = 1
SEATemplates[5] = RESULT

MATS = SEATemplates[11]
MATS['material_id'] = viget['immport_immune_exposure_material_id']
MATS['material_name'] = viget['vaccine']


SEATemplates[11] = MATS

save_list(SEATemplates)
print("All tables saved.")
#test = pd.DataFrame(list(range(10)))

#STUDY['study_id'] = pd.DataFrame([list(range(test['study_name'].size))])
#.drop_duplicates() 


#dummy_id = = []
#for i in range(viget.shape[0]):
#        append.


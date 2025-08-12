# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 07:50:45 2025

@author: huffmaar

if len(sys.argv) > 1:
   filename = sys.argv[1]
else:
   print("Please provide the absolute path of the ann_data file as a command-line argument.")


"""
# Implementation is only based on cellxgene

import pandas as pd
import numpy as np
import sys
import anndata as ad


#C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/ETL_TestCases/CellGene UseCase/8c64b76f-6798-43b4-9e22-a4c69be77325.h5ad
#python VIGET_ETL.py /Users/huffmaar/Documents/SEA-CDM-SQL-Imports/ImmuneExposureGeneExpression_020922_Raw.csv

cellxgene = "C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/ETL_TestCases/CellGene UseCase/8c64b76f-6798-43b4-9e22-a4c69be77325.h5ad"
# "Users\huffmaar\Documents\SEA-CDM-SQL-Imports\CellGene UseCase\8c64b76f-6798-43b4-9e22-a4c69be77325.h5ad"

if len(sys.argv) > 1:
   filename = sys.argv[1]
else:
   print("Please provide the absolute path of the cellxgene a5hd file as a command-line argument.")




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

def SEA_INIT():
    SEA_Study  = pd.DataFrame(columns=['study_id','study_type', 'study_type_id', 'study_name', 'study_description',
                                       'reference_id','reference_source','comments'])
    SEA_Docu =  pd.DataFrame(columns=['documentation_id','study_id','document_name','document_type','document_type_id','documentation_source', 'reference_id','reference_source', 'citation', 'citation_style','person_id', 'person_id_type','honorific','first_name','middle_name','last_name','person_role', 'comments'])
    SEA_Exper = pd.DataFrame(columns=['experiment_id', 'study_id',
                                      'experiment_type','experiment_type_id','experiment_control','reference_id','reference_source','comments'])
    SEA_Inter = pd.DataFrame(columns=['intervention_id','experiment_id','organism_id','material', 'material_id', 'dosage', 'dosage_unit', 'dosage_unit_id', 'intervention_type', 'intervention_type_id',
                                      'intervention_route','intervention_route_id', 'T0_defintion', 'intervention_time', 'intervention_unit', 'intervention_time_unit_id', 'reference_id', 'reference_source', 'comments'])
    SEA_Assay = pd.DataFrame(columns=['assay_id','assay_name','documentation_id','assay_type', 'assay_type_id', 'organism', 'reagents', 'platform'])
    SEA_Rslt  = pd.DataFrame(columns=['results_id','experiment_id','group_id','sample_id','analysis_name','analysis_id', 
                                      'original_assay_type', 'assay_id', 'analysis_type',
                                      'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',  'comments' ])
    SEA_Onto  = pd.DataFrame(columns=['ontology_id','documentation_id','ontology_name','ontology_string'])
    SEA_Orgo =  pd.DataFrame(columns=['organism_id','group_id','experiment_id','species','species_id','type', 'type_id',
                                      'age', 'age_unit','age_unit_id','sex','sex_id', 'reference_id' , 'reference_source' , 'comments'  ])
    SEA_Occr  = pd.DataFrame(columns=['occurence_id','organism_id','occurence_name','occurence_id','occurence_severity','occurence_start_time','occurence_start_unit', 'occurence_start_id', 
                                      'occurence_end_time','occurence_end_unit', 'occurence_end_id', 'reference_id', 'reference_source', 'comments' ])
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


def read_cxg(filename):
    try: 
        adata = ad.read_h5ad(filename)
        "A data loaded successfuly."
        vdata = adata.var
        odata = adata.obs
    except:
        print("File could not be found. Please include absolute path of a5ad file")
        return  0
    return (vdata, odata)

h5ad = read_cxg(cellxgene)

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

cellxgene = "C:/Users/huffmaar/Documents/SEA-CDM-SQL-Imports/CellGene UseCase/8c64b76f-6798-43b4-9e22-a4c69be77325.h5ad"
# "Users\huffmaar\Documents\SEA-CDM-SQL-Imports\CellGene UseCase\8c64b76f-6798-43b4-9e22-a4c69be77325.h5ad"

vadata = h5ad[0]
oadata = h5ad[1]


SEATemplates = SEA_INIT()

STUDY = SEATemplates[0]

study_cxg = pd.Series({'study_id': 77,
                           'ontology_name': "Vaccine_Ontology",
                           'study_type': 'Clinical Investigation', # May not be correct
                           'study_type_id': 'OBI_0003697',
                           'study_name': "Longitudinal single-cell profiles of lung regeneration after viral infection reveal persistent injury-associated cell states",
                           'study_description': "Single-cell sequencing atlas of the mouse's lung’s response to influenza infection",
                           'reference_id': "39818203",
                           'reference_source':"PUBMED"
                           })
STUDY = pd.concat([study_cxg, study_cxg.to_frame().T])
SEATemplates[0] = STUDY.set_index('study_id')

EXPER =  SEATemplates[2]
#Placeholder for Experiments.
EXPER['experiment_id'] = oadata['experimental_group']
EXPER['reference_id'] = oadata['experimental_group']
EXPER['reference_source'] = oadata['experimental_group']

EXPER['experiment_control'] = 1
EXPER[EXPER['experiment_group'].contains('homeostasis')]['experimental_id'] = 0
EXPER = EXPER.drop_duplicates(subset='experiment_id')

SEATemplates[2] = ZEXPER
 
#viget['study_id'] = viget['reference_id']

#STUDY.iloc[:,[0, 4]]

ONTO = SEATemplates[6]
ontology1 = pd.Series({'ontology_id': 2,
                           'documentation_id': 'obofoundry.org/ontology/CLO',
                           'ontology_name': "Cell Line Ontology",
                           'ontology_string': "CO"})
ontology2 = pd.Series({'ontology_id': 3,
                           'documentation_id': 'obofoundry.org/ontology/DIOD',
                           'ontology_name': "Disiease Ontology",
                           'ontology_string': "DIOD"})
ontology3 = pd.Series({'ontology_id': 4,
                           'documentation_id': 'obofoundry.org/ontology/PATO',
                           'ontology_name': "Phenotype and Trait Ontology",
                           'ontology_string': "PATO"})
ONTO = pd.concat([ONTO, ontology1.to_frame().T])
ONTO = pd.concat([ONTO, ontology2.to_frame().T])
ONTO = pd.concat([ONTO, ontology3.to_frame().T])
SEATemplates[6] = ONTO.set_index('ontology_id')


GROUP = SEATemplates[10]
GROUP['group_id'] = oadata['experimental_group']
GROUP['experiment_id'] = 66 # Must be user defined.
GROUP['reference_id'] = oadata['experimental_group']
GROUP['reference_source'] = 'CellxGene'
GROUP = GROUP.drop_duplicates(subset='group_id')

ORGO = SEATemplates[7]
ORGO['organism_id'] = oadata['donor_id']
ORGO['group_id'] = oadata['experimental_group']
ORGO['species_id'] = oadata['organism_ontology_term_id']
ORGO['sex'] = oadata['sex']
ORGO['sex_id'] = oadata['sex_ontology_term_id']
ORGO['age'] = oadata['Age_in_days']

ORGO['age_unit'] = 'Days'
#viget['study_id'] = viget['reference_id']

# intervention Table is complete but does not generate linking _id

INTER= SEATemplates[3]
INTER['experiment_id']  = oadata['experimental_group']
INTER['material_id'] = '2733526' #PubChem CID 
INTER['material'] = 'Tamoxifen'
INTER['intervention_time'] =  oadata['Tamoxifen_start']
INTER['intervention_unit'] = viget['Days']
INTER['intervention_time_unit_id'] = "UO_0000035"
INTER['reference_id'] = "VIGET"
INTER['T0_definition'] = viget['day_0_def']
INTER['reference_source'] = 'ImmPort'
INTER['organism_id'] = viget['immport_subject_accession']

INTER['experiment_id'] = INTER['experiment_id'].map(EXPER.set_index('experiment_name')['experiment_id'])
INTER['organism_id'] = INTER['organism_id'].map(ORGO.set_index('reference_id')['organism_id'])
INTER['intervention_type'] =  'drug treatment'
INTER['intervention_route_id'] = 'VO_0000574'
INTER['dosage_unit_id'] = 'OBI_0000984'

INTER = INTER.drop_duplicates(subset='organism_id')


ZINTER = INTER
ZINTER['material_id'] = 
INTER['intervention_id'] = INTER.index+1


SEATemplates[3] = INTER.drop_duplicates()


#.reset_index(drop=True, inplace=True)





# siget = pd.merge(siget, STUDY, left_on="immport_study_accession", right_on="reference_id", how='outer')





#df_binary = np.where(df > 0, 1, 0)
#df = pd.DataFrame(df_binary, index=df.index, columns=df.columns)


SEATemplates[2] = STUDY.drop_duplicates()

#df[['age', 'age_unit']] = df['age'].str.extract(r'(\d+)-([a-zA-Z]+)-old')





SAMP=SEATemplates[9]
#SAMP['reference_id'] = viget['gsm']

#SAMP['organism_id'] = viget['organism_id']
SAMP['sample_id'] = oadata['sample_id']
SAMP['biosample_id'] = oadata['sample_id']
SAMP['group_id'] = oadata['experimental_group']
SAMP['biosample_type'] = oadata['tissue_type']
SAMP['expsample_type'] =  oadata['suspension_type']
SAMP['collection_time'] = oadata['sacrifice_day']
SAMP['collection_time_unit'] = oadata['Day']

#SAMP['biosample_reference_id'] = oadata['sample_id']
SAMP['expsample_reference_id'] = oadata.index
#SAMP['reference_id']
SEATemplates[9] = SAMP.drop_duplicates()
SEATemplates[9]['biosample_reference_name'] = 'cellxgene'
SAMP['expsample_source'] = 'cellxgene'
SEATemplates[9] = SAMP

# 25 Samples
# 52,900 Results

# Generate REsults, does not includ mapping of appropriate _ids
RESULT = SEATemplates[5]
RESULT["result_id"] = oadata.['index']
RESULT["sample_id"] = oadata["sample_id"]
#RESULT["data_dimensions"] = 22343
RESULT["datatype"] = "h5aD"
RESULT["file_access"] = "cellxgene"
RESULT["file_type"] = "h5ad"
RESULT["document_id"] = "8c64b76f-6798-43b4-9e22-a4c69be77325.h5ad"
RESULT["analysis_name"] = "CellxGene Processing" # Not sure if correct
RESULT["original_assay_type"] = "Gene Expression Assay"
RESULT["replications"] = 1
SEATemplates[5] = RESULT

MATS = SEATemplates[11]


assay = pd.Series({'assay_id': zi,
                       'assay_name': '10x 3 v3',
                       'documentation_id': 1,
                       'assay_type': 'Experimental Assay',
                       'assay_type_id': 'ECO_0000097',
                       'organism': True,
                       'reagents': 'mRNA',
                       'platform': f'{platform}'})
ASSAY = pd.concat([ASSAY, assay.to_frame().T])

    SEA_Assay = pd.DataFrame(columns=['assay_id','assay_name','documentation_id','assay_type', 'assay_type_id', 'organism', 'reagents', 'platform'])
    SEA_Rslt  = pd.DataFrame(columns=['results_id','experiment_id','group_id','sample_id','analysis_name','analysis_id', 
                                  'original_assay_type', 'assay_id', 'analysis_type',
                                  'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',  'comments' ])
    SEA_Anal  = pd.DataFrame(columns=['analysis_id', 'documentation_id', 'group_id', 'analysis_name', 'analysis_name_id', 'input_data', 'input_data_id' 'reference_id', 'reference_source', 'comments'])


ALYS = SEATemplates[12]



SEATemplates[11] = MATS

save_list(SEATemplates)
print("All tables saved.")
#test = pd.DataFrame(list(range(10)))

#STUDY['study_id'] = pd.DataFrame([list(range(test['study_name'].size))])
#.drop_duplicates() 



#dummy_id = = []
#for i in range(viget.shape[0]):
#        append.





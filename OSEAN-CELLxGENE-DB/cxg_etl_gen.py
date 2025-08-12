# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 07:50:45 2025

@author: huffmaar

if len(sys.argv) > 1:
   filename = sys.argv[1]
else:
   print("Please provide the absolute path of the ann_data file as a command-line argument.")


"""
# Implementation is only based on cellxgene.
# This is very rough cataegory for ETL that is meant to just query experiments and results data.

import pandas as pd
import numpy as np
import sys
import anndata as ad


if len(sys.argv) > 1:
   filename = sys.argv[1]
else:
   print("Please provide the absolute path of the cellxgene a5hd file as a command-line argument.")



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
    SEA_Study  = pd.DataFrame(columns=['study_id','study_type', 'study_focus', 'study_subject', 'study_type_id', 'study_name', 'study_description',
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


def save_list(df_list):
    try:
        for i in df_list:
            zeq = i.columns[0][0:-2]+"h5ad.csv"
            i.to_csv(zeq)
    except:
        print("Could not save list.")
    return 0

def _source_keys(df1, df2, col1, col2):
    #df1 should have column joined be lost.
    outer_join_df = pd.merge(df1, df2, left_on=col1, right_on=col2, how='outer')

    return outer_join_df

from collections import Counter



SEATemplates = SEA_INIT()
cellxgene = filename
h5ad = read_cxg(cellxgene)


vadata = h5ad[1]




SEATemplates = SEA_INIT()

STUDY = SEATemplates[0]
STUDY['study_name'] = vadata['study_name'].unique()
STUDY['study_type_id'] = 'OBI_0003697'
STUDY['study_focus'] = vadata['disease'] # True only for this

STUDY['reference_source'] = 'CellxGene'
STUDY['study_id'] = STUDY.index+1
SEATemplates[0] = STUDY.set_index('study_id')

EXPER =  SEATemplates[2]
#Placeholder for Experiments.
EXPER['experiment_id'] = vadata['study_name'] + vadata['disease']
EXPER['reference_source'] = 'CellxGene'
EXPER = EXPER.drop_duplicates(subset='experiment_id')

SEATemplates[2] = EXPER
 

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
GROUP['group_id'] = vadata['disease'] + vadata['study_name'] + vadata['development_stage']
GROUP['experiment_id'] = vadata['study_name'] + vadata['disease']
GROUP['reference_source'] = 'CellxGene'
GROUP['group_type'] = 'Organism'
GROUP = GROUP.drop_duplicates(subset='group_id')
SEATemplates[10] = GROUP


ORGO = SEATemplates[7]
ORGO['reference_id'] = vadata['donor_id'] 
ORGO['organism_id'] = 'ORGO'+vadata['donor_id']
ORGO['group_id'] = vadata['disease'] + vadata['study_name'] + vadata['development_stage']
ORGO['sex'] = vadata['sex']
ORGO['sex_id'] = vadata['sex_ontology_term_id']
SEATemplates[7] = ORGO.drop_duplicates(subset='organism_id')



INTER= SEATemplates[3]
INTER['intervention_id'] = vadata['study_name']+vadata['donor_id']
INTER['organism_id'] = vadata['donor_id']
INTER['material'] = vadata['disease']
INTER[INTER['material'] == 'influenza']['material_id'] == "NCBITaxon_11309"
INTER['intervention_type'] = 'immune response'
SEATemplates[3] = INTER.drop_duplicates(subset='intervention_id')



SAMP=SEATemplates[9]
SAMP['expsample_reference_id'] =  vadata.index
SAMP['expsample_reference_source'] = 'CellxGene'
SAMP['organism_id'] = vadata['donor_id'].values
SAMP['group_id'] = vadata['disease'].values + vadata['study_name'].values + vadata['development_stage'].values
SAMP['biosample_type'] = vadata['tissue'].values
SAMP['expsample_type'] =  vadata['cell_type'].values + ' ' + vadata['suspension'].values
SAMP['sample_id'] = 'SAMP'+vadata.index
#SAMP['reference_id']
SEATemplates[9] = SAMP

ASSAY=SEATemplates[4]
ASSAY["assay_id"]  = vadata['study_name'] + vadata['assay'] +' ' + vadata['cell_type'] + ' assay'
ASSAY["platform"]  = vadata['assay']

SEATemplates[4]=ASSAY.drop_duplicates(subset='assay_id')

# Generate Results, does not includ mapping of appropriate _ids
RESULT = SEATemplates[5]
RESULT['result_id'] =  'RSLT'+vadata.index
RESULT['sample_id'] = 'SAMP'+vadata.index
RESULT['experiment_id'] = vadata['study_name'].values + vadata['disease'].values
RESULT['group_id'] = vadata['disease'].values + vadata['study_name'].values + vadata['development_stage'].values
RESULT["assay_name"]  = vadata['study_name'].values + vadata['assay'].values + ' assay'
#RESULT["data_dimensions"] = 22343
RESULT['assay_type'] = 'single ' + vadata['suspension'].values +' RNA-seq'
RESULT["datatype"] = "h5aD"
RESULT["file_access"] = "CellxGene"
RESULT["file_type"] = "h5ad"
RESULT["analysis_name"] = "CellxGene Processing" # Not sure if correct
SEATemplates[5] = RESULT

MATS = SEATemplates[11]


ALYS = SEATemplates[12]



SEATemplates[11] = MATS

save_list(SEATemplates)
print("All tables saved.")


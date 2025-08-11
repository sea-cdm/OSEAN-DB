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


#C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/ETL_TestCases/CellGene UseCase/8c64b76f-6798-43b4-9e22-a4c69be77325.h5ad
#python VIGET_ETL.py /Users/huffmaar/Documents/SEA-CDM-SQL-Imports/ImmuneExposureGeneExpression_020922_Raw.csv

cellxgene = "C:/Users/huffmaar/Documents_Local/8655aff7-44c7-4904-8719-7dd75ec20fcd.h5ad"
pathway = 'C:/Users/huffmaar/Documents_Local/'
filename1 = 'a3ef98b7-5eec-45e0-ae73-db13324bac22.h5ad'
filename2 = 'bd572490-8f80-4044-9d00-db07a68fb6ec.h5ad'
filename3 = '8655aff7-44c7-4904-8719-7dd75ec20fcd.h5ad'
filename4 = '983bd800-e655-4c76-ad9a-20ae0257fc0b.h5ad'
filename5 = '65cf7371-bbf3-4d41-9250-2d30bd048125.h5ad'
filenames = [filename1, filename2, filename3, filename4, filename5]
pathways = []
for name in filenames:
    pathways.append(pathway+name)


#cellxgene = 
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



# Intialize SEATEmplates
SEATemplates = SEA_INIT()
# Strings for filenames, to be changed lagter.

# "Users\huffmaar\Documents\SEA-CDM-SQL-Imports\CellGene UseCase\8c64b76f-6798-43b4-9e22-a4c69be77325.h5ad"
cellxgene = pathways[0]
h5ad = read_cxg(cellxgene)


vadata0 = read_cxg(pathways[0])[1]
vadata1 = read_cxg(pathways[1])[1]
vadata2 = read_cxg(pathways[2])[1]
vadata3 = read_cxg(pathways[3])[1]
vadata4 = read_cxg(pathways[4])[1]

vadata0['study_name'] = 'Mouse Post-Flu Time Series'
vadata1['study_name'] = 'Immunophenotyping of COVID-19 and influenza highlights the role of type I interferons in development of severe COVID-19'
vadata2['study_name'] = 'A total of 27,092 droplet-based single-nucleus transcriptomes profiled across 11 cell types in the choroid plexus'
vadata3['study_name'] = 'COMBAT project: single cell gene expression data from COVID-19, sepsis and flu patient PBMCs'
vadata4['study_name'] = 'A total of 38,217 droplet-based single-nucleus transcriptomes profiled across 14 cell types in the frontal cortex'

vadata5 = pd.concat([vadata1, vadata2, vadata3, vadata4, vadata0])
vadata = vadata5.loc[:, ['observation_joinid', 'study_name', 'experimental_group', 'donor_id', 'tissue_type', 'tissue_ontology_term_id', 'assay_ontology_term_id', 'sex_ontology_term_id',  'disease_ontology_term_id', 'assay', 'disease', 'sex', 'tissue', ]]

# Gather all column names from all dataframes
all_columns = (
    list(vadata1.columns) +
    list(vadata2.columns) +
    list(vadata3.columns) +
    list(vadata4.columns) +
    list(vadata0.columns)
)

# Count occurrences and convert to get column entries that work.
column_counts = Counter(all_columns)
column_counts_df = pd.DataFrame.from_dict(column_counts, orient='index', columns=['count']).sort_values('count', ascending=False)
vcolumns = column_counts_df[column_counts_df['count'] >= 2]
#vadata = vadata5.loc[:, vcolumns.index]
vadata = vadata5[vadata5['disease'].isin(['normal', 'influenza'])].loc[:, vcolumns.index]


#vadata = h5ad[0]
#oadata = h5ad[1]




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

#viget['study_id'] = viget['reference_id']

# intervention Table is complete but does not generate linking _id

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

# Generate REsults, does not includ mapping of appropriate _ids
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
#test = pd.DataFrame(list(range(10)))

#STUDY['study_id'] = pd.DataFrame([list(range(test['study_name'].size))])
#.drop_duplicates() 


#dummy_id = = []
#for i in range(viget.shape[0]):
#        append.


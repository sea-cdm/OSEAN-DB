# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 10:41:46 2025

@author: huffmaar
"""

import pandas as pd
import numpy as np
import sys
    

# Dummy variables for testing....
VIGET = "/Users/huffmaar/Documents/SEA-CDM-SQL-Imports/ImmuneExposureGeneExpression_020922_Raw.csv"
VIGETGENE = "a"
gene_exp = "/Users/huffmaar/OneDrive - Michigan Medicine/Documents/immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv"


if len(sys.argv) == 3:
   VIGET = sys.argv[1]
   gene_exp = sys.argv[2]
else:
   try:
       VIGET = sys.argv[2]
       gene_exp = sys.argv[1]   
   except:
       print("Please provide the absolute path of the VIGET metadata file and gene expression file as a command-line argument.")
       sys.exit()

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
    SEA_Study  = pd.DataFrame(columns=['study_id','study_type', 'study_type_id', 'study_name', 'study_description',
                                       'reference_id','reference_source','comments'])
    SEA_Docu =  pd.DataFrame(columns=['documentation_id','study_id','document_name','document_type','document_type_id','documentation_source', 'reference_id', 'reference_source', 'citation', 'citation_style','person_id', 'person_id_type','honorific','first_name','middle_name','last_name','person_role', 'comments'])
    SEA_Exper = pd.DataFrame(columns=['experiment_id', 'study_id',
                                      'experiment_type','experiment_type_id','experiment_control','reference_id','reference_source','comments'])
    SEA_Inter = pd.DataFrame(columns=['intervention_id','experiment_id','organism_id','material', 'material_id', 'dosage', 'dosage_unit', 'dosage_unit_id', 'intervention_type', 'intervention_type_id',
                                      'intervention_route','intervention_route_id', 'T0_defintion', 'intervention_time', 'intervention_unit', 'intervention_time_unit_id', 'reference_id', 'reference_source', 'comments'])
    SEA_Assay = pd.DataFrame(columns=['assay_id','assay_name','documentation_id','assay_type', 'assay_type_id', 'organism', 'reagents', 'platform'])
    SEA_Rslt  = pd.DataFrame(columns=['results_id','experiment_id','group_id','sample_id','analysis_name','analysis_id', 
                                  'original_assay_type', 'assay_id', 'analysis_type',
                                  'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',  'comments' ])
    SEA_Onto  = pd.DataFrame(columns=['ontology_id','documentation_id','ontology_name','ontology_string'])
    SEA_Orgo =  pd.DataFrame(columns=['organism_id','group_id','experiment_id','species','species_id','lineage', 'type_id',
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
    nomen = SEA_INIT()
    for ziz in range(len(df_list)):
        try:
            zeq = df_list[ziz].index.name[0:-3]+".csv"
            print(zeq)
            #df_list[ziz].to_csv(zeq)
            print(f"Successfuly saved {zeq}")
        except:
            print("Could not save list.")
        
    return 0



def indexed(df):
    index_series = df.index.to_series()
    indexed = df
    df['index_id'] = index_series
    return df

def fix_id(df, dfs, ref, refs):
    mapping = ref
    df_replaced = df.replace(mapping)
    return df_replaced



def _source_keys(df1, df2, col1, col2):
    outer_join_df = pd.merge(df1, df2, left_on=col1, right_on=col2, how='outer')

    return outer_join_df

# Intialize SEATEmplates
SEATemplates = SEA_INIT()
viget = read_VIGET(VIGET)


STUDY = SEATemplates[0]
STUDY['reference_id'] = viget['immport_study_accession']
STUDY['reference_source'] = 'ImmPort'
STUDY['study_description'] = viget['study_brief_desc']
STUDY['study_name'] = viget['study_title']
STUDY = STUDY.drop_duplicates()
STUDY['study_type'] = 'Clinical Investigation'
STUDY['study_type_id'] = 'OBI_0003697'
STUDY['study_id'] = STUDY.index+1
study_viget = pd.Series({'study_id': 3,
                      'study_name' :"VIGET:Vaccine Immune Gemone Expression Tool",
                      'study_type': 'Hypothesis-Generating Investigation',
                      'study_type_id': 'OBI_0000356',
                      'reference_id': '37180100',
                      'reference_source':"PUBMED"})
STUDY = pd.concat([STUDY, study_viget.to_frame().T])
SEATemplates[0] = STUDY.set_index('study_id')


# Early Documenation set up relational identification to repeat for study.
DOCU = SEATemplates[1]
big_list = [["Mr", "Anthony", "Robert", "Huffman"], ["Mr", "Timothy", "", "Burson"], ["Mrs", "Naseem", "", "Sanati"]]
document_list = [['VIGET:Vaccine Immune Gemone Expression Tool', 'Research', '37180100', 'PUBMED'], ['ImmuneExposureGeneExpression_020922.csv', 'Research Supplement', '37180100', 'PUBMED'], ['immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv', 'Research Supplement', '37180100', 'PUBMED']]
documentation_ids = 1

for names in big_list:
    honorific = names[0]
    personal = names[1]
    middle = names[2]
    surname = names[3]
    for documents in document_list:
        doc_name = documents[0]
        doc_type = documents[1]
        doc_id  = documents[2]
        doc_source = documents[3]
        document1 =  pd.Series({'documentation_id': documentation_ids,
                              'study_id': 2,
                              'document_name': f'{doc_name}',
                              'document_type': f'{doc_type}',
                              'honorific': f'{honorific}',
                              'first_name': f'{personal}',
                              'middle_name': f'{middle}',
                              'last_name': f'{surname}',
                              'reference_id': f'{doc_id}',
                              'person_role': 'First Author',
                              'documentation_source':'immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv',
                              'reference_source': f'{doc_source}'})
        DOCU =  pd.concat([DOCU, document1.to_frame().T])
        documentation_ids +=1

GEXP = read_VIGET(gene_exp)
SEATemplates[1] = DOCU.set_index('documentation_id')


EXPER =  SEATemplates[2]
EXPER['study_id'] = viget['immport_study_accession']
EXPER['experiment_name'] = viget['immport_study_accession']+' '+viget['vaccine']
EXPER['experiment_type'] = 'vaccination response'
EXPER['experiment_type_id'] = 'VO_0000002'
EXPER['experiment_control'] = 0
EXPER['reference_source'] = 'VIGET'
EXPER = EXPER.drop_duplicates()
EXPER['experiment_id'] = EXPER.index+1
EXPER['study_id'] = EXPER['study_id'].map(STUDY.set_index('reference_id')['study_id'])
SEATemplates[2] = EXPER.set_index('experiment_id')


ONTO = SEATemplates[6]
ontology = pd.Series({'ontology_id': 1,
                           'documentation_id': 'obofoundry.org/ontology/vo',
                           'ontology_name': "Vaccine_Ontology",
                           'ontology_string': "VO"})
ONTO = pd.concat([ONTO, ontology.to_frame().T])
SEATemplates[6] = ONTO

GROUP = SEATemplates[10]
GROUP['experiment_id'] = viget['immport_study_accession']+' '+viget['vaccine']
GROUP['min_age'] = viget['study_min_age']
GROUP['max_age'] = viget['study_max_age']
GROUP['reference_id'] = viget['immport_study_accession']+' '+viget['batch_factor']
GROUP['reference_source'] = 'VIGET'
GROUP['group_type'] = 'organism'
GROUP['group_id'] = GROUP.index+1
GROUP = GROUP.drop_duplicates(subset='experiment_id')
GROUP['experiment_id'] = GROUP['experiment_id'].map(EXPER.set_index('experiment_name')['experiment_id'])

SEATemplates[10] = GROUP.set_index('group_id')


ORGO = SEATemplates[7]
ORGO['reference_source'] = 'ImmPort'
ORGO['species'] = 'human'
ORGO['species_id'] = 'NCBITaxon_9606'
ORGO['group_id'] = viget['immport_study_accession']+' '+viget['batch_factor']
ORGO['sex'] = viget['gender']
ORGO['sex_id'] = 'PATO_0001894'
ORGO['sex_id'][ORGO['sex']=='Male'] = 'PATO_0000384'
ORGO['sex_id'][ORGO['sex']=='Female'] = 'PATO_0000383'
ORGO['experiment_id'] = viget['immport_study_accession']+' '+viget['vaccine']
ORGO['lineage_or_ethnicity'] = viget['race']
ORGO['experiment_id'] = ORGO['experiment_id'].map(EXPER.set_index('experiment_name')['experiment_id'])
ORGO['reference_id'] = viget['immport_subject_accession']
ORGO['reference_source'] = 'ImmPort'
ORGO['age_unit_id'] = 'UO_0000001'
ORGO = ORGO.drop_duplicates(subset = 'reference_id')
ORGO['organism_id'] = ORGO.index+1

SEATemplates[7] = ORGO.set_index('organism_id')



INTER= SEATemplates[3]
INTER['experiment_id'] = viget['immport_study_accession']+' '+viget['vaccine']
INTER['material_id'] = viget['immport_immune_exposure_material_id']
INTER['material'] = viget['vaccine']
INTER['intervention_time'] = 0
INTER['intervention_unit'] = viget['immport_vaccination_time_unit']
INTER['intervention_time_unit_id'] = "UO_0000035"
INTER['reference_id'] = "VIGET"
INTER['T0_definition'] = viget['day_0_def']
INTER['reference_source'] = 'ImmPort'
INTER['organism_id'] = viget['immport_subject_accession']
INTER['experiment_id'] = INTER['experiment_id'].map(EXPER.set_index('experiment_name')['experiment_id'])
INTER['organism_id'] = INTER['organism_id'].map(ORGO.set_index('reference_id')['organism_id'])
INTER['intervention_type'] =  'vaccination'
INTER['intervention_type_id'] =  'VO_0000001'
INTER['intervention_route_id'] = 'VO_0000574'
INTER['dosage_unit_id'] = 'OBI_0000984'
INTER = INTER.drop_duplicates(subset='organism_id')
INTER['intervention_id'] = INTER.index+1
SEATemplates[3] = INTER.set_index('intervention_id')


SAMP=SEATemplates[9]
SAMP['organism_id'] = viget['immport_subject_accession']
SAMP['group_id'] = viget['immport_study_accession']+' '+viget['batch_factor']

SAMP['biosample_type'] = viget['biosample_type']
SAMP['expsample_type'] =  viget['type_subtype']
SAMP['expsample_source'] = viget['expsample_repository_name']
SAMP['biosample_reference_id'] = viget['immport_biosample_accession']
SAMP['expsample_reference_id'] = viget['gse']
SAMP['expsample_reference_name'] = viget['gsm']
SAMP['collection'] = 'blood draw'
SAMP['collection_id'] = 'EFO_0009121'
SAMP['collection_time'] = viget['immport_vaccination_time']
SAMP['collection_time_unit'] = viget['immport_vaccination_time_unit']
SAMP['collection_time_unit_id'] = "UO_0000035"

#Assignment of additional metadata data.
SAMP['biosample_type_id'] = 'NCIT_C43412'
SAMP['biosample_type_id'][SAMP['biosample_type'] == 'PBMC'] = 'NCIT_C12519'
SAMP['biosample_type_id'][SAMP['biosample_type'] == 'B cell'] = 'CL_0000236'
SAMP['biosample_type_id'][SAMP['biosample_type'] == 'Whole Blood'] = 'NCIT_C12434'

SAMP['group_id'] = SAMP['group_id'].map(GROUP.set_index('group_id')['reference_id'])
SAMP['organism_id'] = SAMP['organism_id'].map(ORGO.set_index('reference_id')['organism_id'])
SAMP['sample_id'] = SAMP.index+1

SEATemplates[9] = SAMP.set_index('sample_id')



 
# Asay and Analysis follow this loop.
ASSAY = SEATemplates[4]
ALYS = SEATemplates[12]

zi = 0
for z in viget['gpl'].unique():
    platform = z
    zi += 1
    assay = pd.Series({'assay_id': zi,
                       'assay_name': 'Blood.RNA-Microarray',
                       'documentation_id': 1,
                       'assay_type': 'Experimental Assay',
                       'assay_type_id': 'ECO_0000097',
                       'organism': True,
                       'reagents': 'mRNA',
                       'platform': f'{platform}'})
    ASSAY = pd.concat([ASSAY, assay.to_frame().T])
    alys = pd.Series({'analysis_id': zi,  
                   'assay_name': f'LIMMA usng f{platform}',
                   'assay_type': 'LIMMA',
                   'assay_type_id':'EFO_0001456',
                   'documentation_id': 7,
                   'organism': True,
                   'imput_data': 'VIGET',
                   'reference_id': 1,
                   'reference_source': 'ImmPort',
                   'reagents': 'RNA',
                   'platform': f'{platform}'
                   })
    ALYS = pd.concat([ALYS, alys.to_frame().T])
SEATemplates[12] = ALYS.set_index('analysis_id')
SEATemplates[4] = ASSAY.set_index('assay_id')

RESULT = SEATemplates[5]

RESULT["sample_id"] = SAMP['sample_id']
RESULT['group_id'] = viget['immport_study_accession']+viget['batch_factor']
RESULT['experiment_id'] = viget['immport_study_accession']+' '+viget['vaccine']
RESULT['experiment_id'] =  RESULT['experiment_id'].map(EXPER.set_index('experiment_name')['experiment_id'])
RESULT["analysis_id"] = viget['gpl']
RESULT['original_assay_type'] = viget['gpl']
RESULT['assay_id'] = viget['gpl']
RESULT["datatype"] = "VIGET"
# Information on result categories.
RESULT["file_access"] = "Zenodo"
RESULT["file_type"] = "csv"
RESULT["document_id"] = "immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv"
RESULT["original_assay_type"] = "Blood.RNA Expression Assay"
RESULT["analysis_name"] = "RNA Microarray of " + RESULT['group_id']
RESULT["analysis_type"] = "LIMMA"
RESULT["replications"] = 1
RESULT['original_assay_type_id'] = RESULT['assay_id'].map(ASSAY.set_index('platform')['assay_id'])
RESULT['analysis_id'] = RESULT['analysis_id'].map(ALYS.set_index('platform')['analysis_id'])
RESULT["results_id"] = RESULT.index+1
SEATemplates[5] = RESULT.set_index('results_id')



MATS = SEATemplates[11]
MATS['reference_id'] = viget['immport_immune_exposure_material_id']
MATS['material_name_id'] = viget['immport_immune_exposure_material_id']
MATS['reference'] = 'VIGET'
MATS['material_name'] = viget['vaccine']
MATS = MATS.drop_duplicates(subset='reference_id')
MATS['material_id'] = MATS.index+1
SEATemplates[11] = MATS.set_index('material_id')


save_list(SEATemplates)
print("All tables saved.")


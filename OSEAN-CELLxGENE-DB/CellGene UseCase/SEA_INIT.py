# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:46:23 2025

@author: huffmaar
"""

import pandas as pd

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


def SEA_Export(export, excep):
    try:
        for i in export:
            zeq = i.columns[0][0:-2]+".csv"
            i.to_csv(zeq)
            print("All tables saved.")
    except:
        print("Could not save list.")
    # export should be list of files in SEA template
    # excep should define which tables to be export in format.    
    return 0
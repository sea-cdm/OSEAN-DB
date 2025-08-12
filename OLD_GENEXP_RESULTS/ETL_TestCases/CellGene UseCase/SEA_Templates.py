# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:57:25 2025

@author: huffmaar
"""

# Commands should be.
# Update all terms as df if given static value.
# Update all terms as table is converted in SEA Format.
# Retrieve all values of a type....

# Classes or functions should be defined as a set of values that ar elinked.
# This should be common name, specific ID, and ????
# Specific IDs should not be worked out for what is going on.

import pandas as pd


def dataload (filename, filetype):
    try:
        input_data = pd.read_csv(filename, filetype)
        return input_data
    except:
        return 0



class Study:
    def __init__(self, name):
        self.name = name
        self.template =  pd.DataFrame(columns=['study_id','study_type', 'study_type_id', 'study_name', 
                                               'reference_id','reference_source','comments'])

              
        def type(self):
            return()
        
class Experiment:
    def __init__(self, name, exp_name, exp_id,  ref_id, ref_source, study_type, exp_control, study_id = "None"):
        self.name = name
        self.table = pd.DataFrame(columns=['experiment_id', 'study_id',
                                                  'experiment_type','experiment_type_id','experiment_control','reference_id','reference_source','comments'])
        def export (self):
            return 0
        

#   SEA_Docu =         SEA_Onto  = 


class Assay:
    def __init__(self, name):
        self.name = name
        self.template  = pd.DataFrame([
            'assay_id','assay_name','documentation_id','sea_assay','sea_assay_id','assay_type_id',
            'organism', 'reagents', 'platform', 'parameters', 'parameter_values', 'input_data' ])

class Documentation:
    def __init__(self, name, ref_id, ref_source,study_type, study_id, comments):
        self.name = name
        self.template = pd.DataFrame(columns=['documentation_id','study_id','document_name','document_type','document_type_id',
                                              'documentaiton_source', 'source_id', 'reference_source',  'citation', 'citation_style',
                                              'person_id', 'person_id_type','honorific','first_name','middle_name','last_name','person_role', 'comments'])

        
        def study(self):
            return()
        
        def type(self):
            return()

class Organism:
    def __init__(self, name, ref_id, ref_source,study_type, study_id, comments):
        self.name = name
        self.template = pd.DataFrame(columns=['organism_id','Group_id','experiment_id','species','species_id','type', 'type_id'
                                     'age', 'age_unit','age_unit_id','sex','sex_id', 'source_id' , 'reference_source' , 'comments'  ])
        
        def study(self):
            return()
        
        def type(self):
            return()
class Occurence:
    def __init__(self, name, ref_id, ref_source,study_type, study_id, comments):
        self.name = name
        self.template = pd.DataFrame(columns=['occurence_id','organism_id','occurence_Name','occurence_id','occurence_severity','occurence_start_time','occurence_start_unit', 'occurence_start_id', 
                                     'occurence_end_time','occurence_end_unit', 'occurence_end_id', 'source_id', 'reference_source', 'comments' ])
        
        def study(self):
            return()
        
        def type(self):
            return()

class Group:
    def __init__(self, name, ref_id, ref_source,study_type, study_id, comments):
        self.name = name
        self.template  = pd.DataFrame(columns=['group_id','experiment_id','consistency','group_size','reference_id','reference_source','comments'])
        
        def study(self):
            return()
        
        def type(self):
            return()

class Intervention:
    def __init__(self, name, ref_id, ref_source,study_type, study_id, comments):
        self.name = name
        self.template = pd.DataFrame(columns=['intervention_id','experiment_id','organism_id','material', 'material_id', 'dosage', 'dosage_unit', 'dosage_unit_id', 
                                             'intervention_route','intervention_route_id', 'T0 Defintion', 'intervention_time', 'intervention_unit', 'intervention_time_unit_id', 'source_id', 'reference_source', 'comments'])

        def type(self):
            return()

class Samples:
    def __init__(self, name):
        self.name = name
        self.template = pd.DataFrame(columns=['sample_id','group_id','organism_id', 'collection',
                                  'expsample_type','expsample_type_id', 'expsample_reference_id', 'expsample_reference_name',
                                  'biosampl_type', 'biosample_type_id', 'biosample_reference_id', 'biosample_reference_name',
                                  'expsample_source','expsamplesource_id', 'replicates' ])
   

class Materials:
    def __init__(self, name):
        self.name = name
        self.template  = pd.DataFrame(columns=['material_id','material_name','ontology_id','Organization','reference_id','reference_source','comments'])
        
    def type(self):
            return()

class Results:
    def __init__(self, name):
        self.name = name
        self.template = pd.DataFrame(columns=['results_id','experiment_id','Group_id','sample_id','assay_name','assay_id', 
                              'original_assay_type', 'original_assay_type_id', 'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',  'comments' ])
        def type(self):
            return()

class Ontology:
    def __init__(self, name, ref_id, ref_source,study_type, study_id, comments):
        self.name = name
        self.template = pd.DataFrame(columns=['ontology_id','documentation_id','ontology_name','ontology_string'])
        def study(self):
            return()
        
        def type(self):
            return()
        
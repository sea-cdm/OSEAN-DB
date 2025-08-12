# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 16:09:38 2025

@author: huffmaar
"""
import numpy as np
import pandas as pd
import sys

# Set up an excel document or tool to enable mapping between categories within SEA CDM category

# four arguments are needed to be assigned for each mapping....
# or generate code to set up details for mapping.



import os
import sys
import shutil
import argparse
import multiprocessing

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


def main( self ):
            parser = argparse.ArgumentParser( description="SEA CDM ETL converts files into SEA CDM format." )
            parser.add_argument("--input_format", '-i', dest='filename', required=True)
            parser.add_argument("--output", '-o', dest='export', required=True)
            parser.add_argument("--convertor", '-c', dest='converstion', required=True)
            args = parser.parse_args()
            self.check_args (args)
            SEA_Templates = SEA_INIT
            
            





def main( self ):
        try:
            parser = argparse.ArgumentParser( description="Vaxign-ML predicts bacterial protective antigens." )
            parser.add_argument( "--input", '-i', dest='inputFasta', required=True )
            parser.add_argument( "--output", '-o', dest='outputDir', required=True )
            parser.add_argument( "--organismtype", '-t', dest='organism', required=True)
            parser.add_argument( "--savedModel", '-s', dest='savedModel', default=MODEL_PATH )
            parser.add_argument( "--multi", '-m', dest='multiFlag', default="True" )
            parser.add_argument( "--process", '-p', dest='process', type=int, default=int(multiprocessing.cpu_count()/2) )
            parser.add_argument( "--raw", '-r', dest='rawFlag', default="False" )
            args = parser.parse_args()
            self.check_args( args )
            
            featureDir = os.path.join( args.outputDir, "_FEATURE" )
            if not os.path.exists( featureDir ):
                os.mkdir( featureDir )
            if args.organism.lower() in ["gram+","g+","gram-","g-"]:
                incFeatures = []
                incFeatures.append( "psortb" )
                Feature.run_psortb( args.inputFasta, featureDir, args.organism, args.multiFlag, args.process, args.rawFlag )
                incFeatures.append( "spaan" )
                Feature.run_spaan( args.inputFasta, featureDir, args.rawFlag )
                incFeatures.append( "signalp" )
                Feature.run_signalp( args.inputFasta, featureDir, args.organism, args.multiFlag, args.process, args.rawFlag )
                incFeatures.append( "tmhmm" )
                Feature.run_tmhmm( args.inputFasta, featureDir, args.multiFlag, args.process, args.rawFlag )
                incFeatures.append( "imgen" )
                Feature.run_immugen( args.inputFasta, featureDir, args.rawFlag )
                incFeatures.append( "mdesc" )
                Feature.run_descriptor( args.inputFasta, featureDir, args.rawFlag )
                
                self.makeInput( args.inputFasta, args.outputDir, args.organism, incFeatures )
                
                if args.rawFlag.lower() in ['f','false']:
                    shutil.rmtree( featureDir )
                
                self.predict( args.inputFasta, args.outputDir, args.savedModel, model="bacteria" )
            elif args.organism.lower() in ["virus","v"]:
                incFeatures = []
                incFeatures.append( "spaan" )
                Feature.run_spaan( args.inputFasta, featureDir, args.rawFlag )
                incFeatures.append( "tmhmm" )
                Feature.run_tmhmm( args.inputFasta, featureDir, args.multiFlag, args.process, args.rawFlag )
                incFeatures.append( "imgen" )
                Feature.run_immugen( args.inputFasta, featureDir, args.rawFlag )
                incFeatures.append( "mdesc" )
                Feature.run_descriptor( args.inputFasta, featureDir, args.rawFlag )
                
                self.makeInput( args.inputFasta, args.outputDir, args.organism, incFeatures )
                
                if args.rawFlag.lower() in ['f','false']:
                    shutil.rmtree( featureDir )
                
                self.predict( args.inputFasta, args.outputDir, args.savedModel, model="virus" )
            
        except:
            print( sys.exc_info() )
        

if __name__ == "__main__":
    VaxignML().main()


if (len(sys.argv) > 4):
    sys.argv[0] = SEAClass
    sys.argv[1] = SEAEntry
    sys.argv[2] = InputClass
    sys.argv[3] = InputEntry
        
    


if len(sys.argv) > 1:
   filename = sys.argv[1]
else:
   print("Please provide the absolute path of the ann_data file as a command-line argument.")

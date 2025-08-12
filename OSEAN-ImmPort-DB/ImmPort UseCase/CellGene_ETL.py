# -*- coding: utf-8 -*-
"""
Created on Tue Apr 1 10:41:48 2025

@author: huffmaar
"""

import pandas as pd
import numpy as np

kap = 'Users/huffmaar/Documents/Control_Proteins.xlsx'

#kap = pd.read_excel('C:/Users/huffmaar/Documents/Control_Proteins.xlsx')

#df = pd.DataFrame(columns=['A','B','C','D','E','F','G'])

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
    SEA_Study  = pd.DataFrame(columns=['StudyID','StudyType', 'StudyTypeID', 'StudyName', 
                                       'ForeignID','ForeignSource','Comments'])
    SEA_Docu =  pd.DataFrame(columns=['DocumentationID','StudyID','DocumentName','DocumentType','DocumentTypeID','DocumentationSource', 'ForeignID', 'ForeignSource', 'Citation', 'CitationStyle','PersonID', 'PersonIDType','Honorific','FirstName','MiddleName','LastName','PersonRole', 'Comments'])
    SEA_Exper = pd.DataFrame(columns=['ExperimentID','ExperimentType','ExperimentTypeID','ExperimentControl','ForeignID','ForeignSource','Comments'])
    SEA_Inter = pd.DataFrame(columns=['InterventionID','ExperimentID','OrganismID','Material', 'MaterialID', 'Dosage', 'DosageUnit', 'DosageUnitID', 
                                      'InterventionRoute','InterventionRouteID', 'T0 Defintion', 'InterventionTime', 'InterventionUnit', 'InterventionTimeUnitID', 'ForeignID', 'ForeignSource', 'Comments'])
    SEA_Assay  = pd.DataFrame(columns=['AssayID','AssayName','DocumenationID','SEAAssay','SEAAssayID','AssayTypeID','Organism', 'Reagents', 'Platform', 'Parameters', 'ParameterValues', 'InputData' ])
    SEA_Rslt  = pd.DataFrame(columns=['ResultsID','ExperimentID','GroupID','SampleID','DocumentID','AssayName','AssayID', 
                                      'OriginalAssay', 'OriginalAssayID', 'DataType', 'DataTypeID', 'DataDimensions', 'Replications',  'Comments' ])
    SEA_Onto  = pd.DataFrame(columns=['OntologyID','DocumentationID','OntologyName','OntologyString'])
    SEA_Orgo =  pd.DataFrame(columns=['OrganismID','GroupID','ExperimentID','OntologyString', 'Species','SpeciesID','Type', 'TypeID'
                                      'Age', 'AgeUnit','AgeUnitID','Sex','SexID', 'ForeignID' , 'ForeignSource' , 'Comments'  ])
    SEA_Occr  = pd.DataFrame(columns=['OccurenceID','OrganismID','OccurenceName','OccurenceID','OccurenceSeverity','OccurenceStartTime','OccurenceStartUnit', 'OccurenceStartID', 
                                      'OccurenceEndTime','OccurenceEndUnit', 'OccurenceEndID', 'ForeignID', 'ForeignSource', 'Comments' ])
    SEA_Samp  = pd.DataFrame(columns=['SampleID','GroupID','OrganismID', 'SampleType','SampleTypeID','SampleSource','SampleSourceID','OriginalSample', 'Replicates', 'ForeignID', 'ForeignSource', ])
    SEA_Grop  = pd.DataFrame(columns=['GroupID','ExperimentID','Consistency','GroupSize','ForeignID','ForeignSource','Comments'])
    SEA_Mats  = pd.DataFrame(columns=['MaterialID','MaterialName','OntologyID','Organization','ForeignID','ForeignSource','Comments'])
    export = [SEA_Study, SEA_Docu, SEA_Exper, SEA_Inter, SEA_Assay, SEA_Rslt, SEA_Onto, SEA_Orgo, SEA_Occr, SEA_Samp, SEA_Grop, SEA_Mats]
    print("All tables initialized.")
    return export

SEATemplates = SEA_INIT()


VIGET = "/Users/huffmaar/Documents/SEA-CDM-SQL-Imports/ImmuneExposureGeneExpression_020922_Raw.csv"
VIGET = pd.read_csv("/Users/huffmaar/Documents/SEA-CDM-SQL-Imports/ImmuneExposureGeneExpression_020922_Raw.csv")


def read_VIGET(VIGET):
    try: 
        dfVIGET = file_reader(VIGET)
    except:
        print("File could not be found")
        return  0
    return dfVIGET

viget = read_VIGET(VIGET)

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
            zeq = "examplefile" + "i"
            pd.csv()
    
    return 0


pd.
#Drop duplicate IDs in tables after making sure mapping does not go.

STUDY = SEATemplates[0]
STUDY['ForeignID'] = viget['immport_study_accession']
STUDY['StudyName'] = viget['study_title']

ORGO = SEATemplates[7]
ORGO['OrganismID'] = viget['immport_subject_accession']
#ORGO['GroupID'] = viget['']
#ORGO['Organism'] = 
ORGO['Sex'] = viget['gender']
ORGO['Type'] = viget['race']
#ORGO['ExperimentID'] = viget['']
ORGO['ForeignID'] = viget['immport_subject_accession']

INTER= SEATemplates[3]
INTER['ForeignID'] = viget['gpl']
INTER['MaterialName'] = viget['platform_desc']


SAMP=SEATemplates[9]

MATS = SEATemplates[11]

test = pd.DataFrame(list(range(10)))

#STUDY['StudyID'] = pd.DataFrame([list(range(test['StudyName'].size))])
#.drop_duplicates() 




def read_CELLXGENE():
    VIGET = 0
    return VIGET

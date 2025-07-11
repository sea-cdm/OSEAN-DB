# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 16:08:34 2025

@author: huffmaar
"""

import pandas as pd

def SEA_Templates():
    SEA_Study  = pd.DataFrame(columns=['study_id','study_type', 'study_type_id', 'study_name', 
                                       'reference_id','reference_source','comments'])
    SEA_Docu =  pd.DataFrame(columns=['documentation_id','study_id','document_name','document_type','document_type_id','documentation_source', 'source_id', 'reference_source', 'citation', 'citation_style','person_id', 'person_id_type','honorific','first_name','middle_name','last_name','person_role', 'comments'])
    SEA_Exper = pd.DataFrame(columns=['experiment_id', 'study_id',
                                      'experiment_type','experiment_type_id','experiment_control','source_id','reference_source','comments'])
    SEA_Inter = pd.DataFrame(columns=['intervention_id','experiment_id','organism_id','material', 'material_id', 'dosage', 'dosage_unit', 'dosage_unit_id', 
                                      'intervention_route','intervention_route_id', 'T0_defintion', 'intervention_time', 'intervention_unit', 'intervention_time_unit_id', 'source_id', 'reference_source', 'comments'])
    SEA_Assay  = pd.DataFrame(columns=['assay_id','assay_name','documentation_id','sea_assay','sea_assay_id','assay_type_id','organism', 'reagents', 'platform', 'parameters', 'parameter_values', 'input_data' ])
    SEA_Rslt  = pd.DataFrame(columns=['results_id','experiment_id','Group_id','sample_id','analysis_name','analysis_id', 
                                  'original_assay_type', 'original_assay_type_id', 'datatype', 'datatype_id', 'file_access', 'file_type', 'replications',  'comments' ])
    SEA_Onto  = pd.DataFrame(columns=['ontology_id','documentation_id','ontology_name','ontology_string'])
    SEA_Orgo =  pd.DataFrame(columns=['organism_id','Group_id','experiment_id','species','species_id','type', 'type_id'
                                      'age', 'age_unit','age_unit_id','sex','sex_id', 'source_id' , 'reference_source' , 'comments'  ])
    SEA_Occr  = pd.DataFrame(columns=['occurence_id','organism_id','occurence_Name','occurence_id','occurence_severity','occurence_start_time','occurence_start_unit', 'occurence_start_id', 
                                      'occurence_end_time','occurence_end_unit', 'occurence_end_id', 'source_id', 'reference_source', 'comments' ])
    SEA_Samp  = pd.DataFrame(columns=['sample_id','group_id','organism_id', 'collection', 'collection_time', 'collection_time_unit', 'collection_time_unit_id', 'T0_definition'
                                      'expsample_type','expsample_type_id', 'expsample_reference_id', 'expsample_reference_name',
                                      'biosampl_type', 'biosample_type_id', 'biosample_reference_id', 'biosample_reference_name',
                                      'expsample_source','expsamplesource_id', 'replicates' ])
    SEA_Grop  = pd.DataFrame(columns=['group_id','experiment_id','composition','group_size','reference_id','reference_source','comments'])
    SEA_Anal  = pd.DataFrame(columns=['analysis_id', 'analysis_name', 'paramaters', 'parameter_values', 'protocol' , 'comments'])
    SEA_Mats  = pd.DataFrame(columns=['material_id','material_name','ontology_id','Organization','reference_id','reference_source','comments'])
    export = [SEA_Study, SEA_Docu, SEA_Exper, SEA_Inter, SEA_Assay, SEA_Rslt, SEA_Onto, SEA_Orgo, SEA_Occr, SEA_Samp, SEA_Grop, SEA_Mats, SEA_Anal]
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

pathway = 'C:/Users/huffmaar/Downloads/ALLSTUDIES-DR54.2_Metadata'

#ir = pathway+'/immune_exposure.txt'
ir = pathway+'/immune_exposure.txt'
ar = pathway+'/arm_2_subject.txt'
ae = pathway+'/adverse_event.txt'
a2s = pathway+'/study_2_condition_or_disease.txt'
sub = pathway+'/subject.txt'
bios = pathway+'/biosample.txt'
exp = pathway+'/expsample.txt'
#trt = pathway+'/treatment.txt'
b2e = pathway+'/expsample_2_biosample.txt'
lab = pathway+'/lab_test.txt'
expr = pathway+'/experiment.txt'
vis = pathway+'/planned_visit.txt'
sdy = pathway+'/study.txt'

files='/standard_curve.txt'
paths = pathway+files
df_head = pd.read_csv(paths, sep = '\t').head(500)


# Load all data as needed
df_ir = pd.read_csv(ir, sep = '\t')
df_arm = pd.read_csv(ar , sep = '\t')
df_ae = pd.read_csv(ae, sep = '\t')
df_sub = pd.read_csv(sub, sep = '\t')
df_ir = df_ir[df_ir['EXPOSURE_PROCESS_REPORTED'] == 'vaccination']
df_a2s = pd.read_csv(a2s, sep = '\t')
df_exp = pd.read_csv(exp, sep = '\t')
df_expr = pd.read_csv(expr, sep = '\t')
df_vis = pd.read_csv(vis, sep = '\t')
df_sdy = pd.read_csv(sdy, sep = '\t')

tables = SEA_Templates()


# Vaccine Fork
STUDYVAX = df_a2s[df_a2s['CONDITION_PREFERRED'] == 'influenza']
INTERVAX = tables[3]
#INTERVAX = INTERVAX[INTERVAX['EXPOSURE_MATERIAL_REPORTED'].isin(['Shield iFerr',  'Seasonal influenza, unspecified formulation 2018-2019', 'IIV, Product Name: IIV_cH5_1HA',  'LAIV-Replication deficient, Product Name: LAIV8_IIV5',  'IIV, Product Name: IIV_cH8_1HA',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: HA-negative IAV',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: WT IAV',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: NC/99',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Brisb/07',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: CA/09',  'Whole virus vaccine, Product Name: B/Lee/1940',  'Whole live virus vaccine, Product Name: B/Yamagata/16/1988',  'Whole live virus vaccine, Product Name: B/Harbin/7/1994',  'Whole virus vaccine, Product Name: B/Sichuan/379/1999',  'Whole virus vaccine, Product Name: B/Shanghai/361/2002',  'Whole virus vaccine, Product Name: B/Florida/4/2006',  'Whole live virus vaccine, Product Name: B/Wisconsin/01/2010',  'Whole live virus vaccine, Product Name: B/Texas/06/2011',  'Whole live virus vaccine, Product Name: B/Massachusetts/02/2012',  'Whole live virus vaccine, Product Name: B/Phuket/3073/2013',  'Whole live virus vaccine, Product Name: B/Hong Kong/330/2001',  'Whole live virus vaccine, Product Name: B/Malaysia/2506/2004',  'Whole live virus vaccine, Product Name: B/Brisbane/60/2008',  'Whole live virus vaccine, Product Name: B/Colorado/06/2017',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_BC1_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_BC3_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_WT_MY04-YIC',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_WT_FL06-YAM',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_WT_CO17-VIC',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_WT_PH13-YAM',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_BC2_HA_VLP',  'Recombinant protein-HA vaccine, Product Name: scrHA-Mut1-9',  'Recombinant protein-HA vaccine, Product Name: scrHA-Mut10-18',  'Recombinant protein-HA vaccine, Product Name: scrHA-Mut1-18',  'Recombinant protein-HA vaccine, Product Name: WT-HA',  'Recombinant protein-Hyperglycosylated protein vaccine, Product Name: H3HK68 hgHA_RBS,cys',  'Recombinant protein-Hyperglycosylated protein vaccine, Product Name: H3HK68 hgHA_RBS',  'Recombinant protein-Hyperglycosylated protein vaccine, Product Name: H3HK68 hgHA_shield,cys',  'Recombinant protein-Hyperglycosylated protein vaccine, Product Name: H3HK68 hgHA_shield', 'Trivalent inactivated influenza',  'Influenza A H1N1 2009 Monovalent Vaccine Novartis' 
#'Fluzone Intradermal Trivalent',  '2011-2012 trivalent inactivated vaccine (A/California/7/09 (H1N1), A/Perth /16/2009 (H3N2), and B/Brisbane/60/2008)',  '2011-2012 trivalent inactivated vaccine',  'LAIV, Product Name: pH1N1 LAIV',  'LAIV, Product Name: pH1N1 PB2 WT PB1 L319Q',  'LAIV, Product Name: pH1N1 PB2 WT PB1 LAIV',  'LAIV, Product Name: pH1N1 PB2 WT PB1 LAIV plus L319Q',  'LAIV, Product Name: pH1N1 WT',  'LAIV, Product Name: pH1N1 PB2 LAIV PB1 LAIV plus L319Q',  'Fluzone',  'Influenza virus vaccine',  'live attenuated influenza vaccine', 'Low dose live influenza vaccine, Product Name: PR/8' 
# 'FluMist' 
#'Adjuvant Name: AddaVax' 'Measles-rubella vaccine',  'Recombinant protein-Neuraminidase vaccine, Product name: N1-MPP',  'Recombinant protein-Neuraminidase vaccine, Product name: N1-VASP',  'Seasonal influenza, unspecified formulation, CVX Code: 150',  'Seasonal influenza, unspecified formulation, CVX Code: 150, 158',  'Seasonal influenza, unspecified formulation, CVX Code: 150, 158, 161',  'Seasonal influenza, unspecified formulation, CVX Code: 171, 186',  'Seasonal influenza, unspecified formulation, CVX Code: 185', '2016 Fluarix quadrivalent seasonal influenza vaccine',  'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_Z1_HA_RC',  'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_Z5_HA_RC',  'Recombinant protein-Full length protein vaccine, Product Name: Mal/NL/01',  'Recombinant protein-Full length protein vaccine, Product Name: Mal/WI/08',  'Seasonal influenza, unspecified formulation 2018-2019, CVX Code: 88',  'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_Y2_HA_RC',  'Flucelvax Quadrivalent 2018-2019, CVX Code: 171, 186',  'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_J4_HA_RC',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ1_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Fujian02',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Wis05',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Bris07',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Perth09',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Vic',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Tx12',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Switz13',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: HK14',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Sing16',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_T8_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_TJ2_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_T11_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ3_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ4_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_TJ5_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ6_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ7_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ8_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ9_HA_VLP', 'H1 reassortant virus vaccine, Product Name: Brisb07',  'H1 reassortant virus vaccine, Product Name: CA/09',  'H1 reassortant virus vaccine, Product Name: Chile/83',  'H1 reassortant virus vaccine, Product Name: NC/99',  'H1 reassortant virus vaccine, Product Name: PR/34',  'H1 reassortant virus vaccine, Product Name: Sing/86',  'H1 reassortant virus vaccine, Product Name: UGA_COBRA_P1_HA_RA',  'H1 reassortant virus vaccine, Product Name: UGA_COBRA_X3_HA_RA',  'H1 reassortant virus vaccine, Product Name: UGA_COBRA_X6_HA_RA',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: CA/09_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_P1_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Brisb07_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_X6_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Brisb18_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_Y2_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_Y4_HA_VLP',  'Recombinant protein-HA vaccine, Product Name: Bris18',  'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_P1_HA_RC',  'Recombinant protein-HA vaccine, Product Name: CA09',  'Recombinant protein-HA vaccine, Product Name: Bris07',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_X6_HA_RC',  'Recombinant protein-COBRA vaccine, Product Name: COBRA_Y4_HA_RC', 'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_NG2_HA_RC',  'Fluad 2017-2018, CVX Code: 168',  'Fluzone High-Dose 2016-2017, CVX Code: 135',  'Recombinant protein-COBRA vaccines, Product Name: COBRA_IAN-8_HA_RC, Product Name: COBRA_Q6_HA_RC, Product Name: UGA_COBRA_Z1_HA_RC',  'mRNA vaccine, Vaccine Name: M2' 'mRNA vaccine, Vaccine Name: H3ss-TM',  'mRNA vaccine, Vaccine Name: NA' 'mRNA vaccine, Vaccine Name: NP',  'Recombinant Protein-NA vaccine, Product Name: CA09_NA_RC',  'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_N1-I_NA_RC',  'Recombinant Protein-NA vaccine, Product Name: Viet/04_NA_RC',  'Recombinant Protein-NA vaccine, Product Name: Bris/07_NA_RC',  'Fluzone Quadrivalent 2022-2023, CVX Code: 150, 150, 158, 161',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_TX_12_HA_VLP',  'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_Wisc_05_HA_VLP',  'Seasonal influenza, intranasal, CVX Code: 151',  'A/Ruddy turnstone/Delaware/300/2009 (H1N1)',  'mRNA vaccine, Product Name: 20 mRNA-LNP vaccine',  'mRNA vaccine, Product Name: H1 mRNA-LNP (Hensley)',  'mRNA vaccine, Product Name: H3 mRNA-LNP (Hensley)',  'mRNA vaccine, Product Name: IBV mRNA-LNP (Hensley)',  'mRNA vaccine, Product Name: CA09_mRNA',  'mRNA vaccine, Product Name: Kan17_mRNA',  'mRNA vaccine, Product Name: UGA_COBRA_NG2_HA_mRNA',  'mRNA vaccine, Product Name: UGA_COBRA_Y2_HA_mRNA',  
# 'Fluarix' 
#'Fluvirin',  'Influvac',  '2008-2009 trivalent influenza vaccine',  'inactivated influenza vaccine',  'A/California/7/2009', 'mRNA vaccine, Product Name: Furin mut',  'mRNA vaccine, Product Name: Monomeric sRBD',  'Viral vector vaccine, Product Name: PRD_NDV_004, Target Antigen: OTH-Spike Protein (ectodomain) Strain Name: SARS-CoV-2/human/China/Wuhan-Hu-1/2019',  'Viral vector vaccine, Product Name: PRD_NDV_001, Target Antigen: OTH-Spike Protein (transmembrane) Strain Name: SARS-CoV-2/human/China/Wuhan-Hu-1/2019',  'NDV expressing the SARS-CoV-2 spike-F chimera consisting of the spike protein ectodomain without the polybasic cleavage site and the TM domain and cytoplasmic tail of the NDV F protein (NDV_LS_S-F)',  'Viral vector vaccine, Product Name: PRD_NDV, Target Antigen: OTH-Not Applicable Strain Name: OTH-Wild type NDV LaSota',  'Recombinant protein-NA vaccine, Product Name: B-Mal, Target Antigen: NA, Strain Name: B/Malaysia/2506/2004',  'Recombinant protein-NA vaccine, Product Name: A-Mich-N1, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)',  'Fluzone Quadrivalent 2017-2018', 'mRNA vaccine, Product Name: iNA, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: M1, Target Antigen: M1, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: M2, Target Antigen: M2, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: M2e, Target Antigen: M2, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: M2i, Target Antigen: M2, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: HA-cleave, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: Mem-MiniHA, Target Antigen: HA, conserved stalk domain, Strain Name: A/Brisbane/59/2007 (H1N1)',  'mRNA vaccine, Product Name: HA-RBS, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: WT-HA, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: NA, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: NP, Target Antigen: NP, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: sHA-cleave, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: siNA, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: MiniHA, Target Antigen: HA, conserved stalk domain, Strain Name: A/Brisbane/59/2007 (H1N1)',  'mRNA vaccine, Product Name: sNA, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: sHA-RBS, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)',  'mRNA vaccine, Product Name: sHA, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)',  'Fluarix 2014-2015' 'Influenza A (H1N1) 2009 Monovalent',  'Seasonal influenza, unspecified formulation 2009-2010',  'Seasonal influenza, unspecified formulation 2010-2011',  'Seasonal influenza, unspecified formulation 2013-2014',  'IIV, Product Name: IIV_cH5_1HA, Target Antigen: HA head domain, conserved epitopes',  'IIV, Product Name: IIV_cH8_1HA, Target Antigen: HA head domain, conserved epitopes',  'LAIV, Product Name: LAIV8_IIV5, Target Antigen: HA head domain, conserved epitopes'
#])]



# INTERVAX = INTERVAX[INTERVAX['EXPOSURE_PROCESS_REPORTED'] == 'vaccination']

STUDY = tables[0]
STUDY['description'] = df_sdy['BRIEF_TITLE']
STUDY['study_id'] = df_sdy['STUDY_ACCESSION']
STUDY['reference_id'] = df_sdy['STUDY_ACCESSION']
STUDY['']
tables[0] = STUDY

EXPER = tables[2]
EXPER['experiment_id'] = pd.concat([df_vis['PLANNED_VISIT_ACCESSION'], df_exp['EXPERIMENT_ACCESSION']])
EXPER['study_id'] =  pd.concat([df_vis['STUDY_ACCESSION'], df_exp['STUDY_ACCESSION']])

list_1d = ['Visit'] * df_vis.shape[0]
list_2d = ['Experiment'] * df_exp.shape[0]                  
EXPER['experiment_type'] = pd.concat([pd.DataFrame(list_1d, columns=['a']), pd.DataFrame(list_2d, columns=['a'])]) 
          
                            
INTER = tables[3]
#INTER = INTERVAX
INTER['organism_id'] = pd.concat([df_ir['SUBJECT_ACCESSION']])
INTER['material_id'] = pd.concat([df_ir['EXPOSURE_MATERIAL_REPORTED']])


ORGO = tables[7]
ORGO['organism_id'] = df_sub['SUBJECT_ACCESSION']
ORGO['species'] = df_sub['SPECIES']
ORGO['race'] = df_sub['RACE']
ORGO['sex'] = df_sub['GENDER']
df_sub = None
ORGO = ORGO.dropna()

OCCUR = tables[8]
OCCUR['organism_id'] = pd.concat([df_ir['SUBJECT_ACCESSION'], df_ae['SUBJECT_ACCESSION']])
OCCUR['occurence_id'] = pd.concat([df_ir['EXPOSURE_ACCESSION'], df_ae['ADVERSE_EVENT_ACCESSION']])
OCCUR['occurence_Name'] = pd.concat([df_ir['DISEASE_PREFERRED'], df_ae['NAME_REPORTED']])

occur = OCCUR[(OCCUR.occurence_Name !='healthy') & (OCCUR.occurence_Name !='Not Applicable') & (OCCUR.occurence_Name !='NA')]

RESULTS = tables[5]
RESULTS['result_id'] = df_exp['EXPERIMENT_ACCESSION']
RESULTS['experiment_type'] = df_exp['RESULT_SCHEMA']

#Sample Generation
df_bios = pd.read_csv(bios, sep = '\t')
df_b2e = pd.read_csv(b2e, sep = '\t')
df_exp =  pd.read_csv(exp, sep = '\t')
df_bios = df_bios.merge(df_b2e, on='BIOSAMPLE_ACCESSION')
df_bios = df_bios.merge(df_exp, on='EXPSAMPLE_ACCESSION') 
SAMPLES = tables[9]
SAMPLES['biosample_reference_id'] = df_bios['BIOSAMPLE_ACCESSION']
SAMPLES['biosample_type'] = df_bios['SUBTYPE']
SAMPLES['expsample_reference_id'] = df_bios['BIOSAMPLE_ACCESSION']
SAMPLES['expsample_type'] = df_bios['NAME_y']
SAMPLES['experiment_id'] = df_bios['PLANNED_VISIT_ACCESSION']
SAMPLES['collection_time'] = df_bios['STUDY_TIME_COLLECTED']
SAMPLES['collection_time_unit'] = df_bios['STUDY_TIME_COLLECTED_UNIT']
SAMPLES['T0_definition'] = df_bios['STUDY_TIME_T0_EVENT_SPECIFY']
SAMPLES['biosample_reference_name'] = 'ImmPort'
SAMPLES['expsample_refence_name'] = 'ImmPort'


#Results Generation



#df_exp = None

# .head(10)  a = df_b2e.head(5)

tables[0] = STUDY
tables[2] = EXPER
tables[3] = INTER
tables[7] = ORGO
tables[8] = OCCUR
tables[9] = SAMPLES
tables[10]
SEA_Export(tables, '.csv')

INTERVAX = INTER

wrong = INTERVAX[INTERVAX['material_id'].isin(['Shield iFerr', 'Seasonal influenza, unspecified formulation 2018-2019','IIV, Product Name: IIV_cH5_1HA', 'LAIV-Replication deficient, Product Name: LAIV8_IIV5', 'IIV, Product Name: IIV_cH8_1HA', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: HA-negative IAV', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: WT IAV', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: NC/99', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Brisb/07', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: CA/09', 'Whole virus vaccine, Product Name: B/Lee/1940', 'Whole live virus vaccine, Product Name: B/Yamagata/16/1988', 'Whole live virus vaccine, Product Name: B/Harbin/7/1994', 'Whole virus vaccine, Product Name: B/Sichuan/379/1999', 'Whole virus vaccine, Product Name: B/Shanghai/361/2002', 'Whole virus vaccine, Product Name: B/Florida/4/2006', 'Whole live virus vaccine, Product Name: B/Wisconsin/01/2010', 'Whole live virus vaccine, Product Name: B/Texas/06/2011', 'Whole live virus vaccine, Product Name: B/Massachusetts/02/2012', 'Whole live virus vaccine, Product Name: B/Phuket/3073/2013', 'Whole live virus vaccine, Product Name: B/Hong Kong/330/2001', 'Whole live virus vaccine, Product Name: B/Malaysia/2506/2004', 'Whole live virus vaccine, Product Name: B/Brisbane/60/2008', 'Whole live virus vaccine, Product Name: B/Colorado/06/2017', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_BC1_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_BC3_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_WT_MY04-YIC', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_WT_FL06-YAM', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_WT_CO17-VIC', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_WT_PH13-YAM', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_BC2_HA_VLP', 'Recombinant protein-HA vaccine, Product Name: scrHA-Mut1-9', 'Recombinant protein-HA vaccine, Product Name: scrHA-Mut10-18', 'Recombinant protein-HA vaccine, Product Name: scrHA-Mut1-18', 'Recombinant protein-HA vaccine, Product Name: WT-HA', 'Recombinant protein-Hyperglycosylated protein vaccine, Product Name: H3HK68 hgHA_RBS,cys', 'Recombinant protein-Hyperglycosylated protein vaccine, Product Name: H3HK68 hgHA_RBS', 'Recombinant protein-Hyperglycosylated protein vaccine, Product Name: H3HK68 hgHA_shield,cys', 'Recombinant protein-Hyperglycosylated protein vaccine, Product Name: H3HK68 hgHA_shield','Trivalent inactivated influenza', 'Influenza A H1N1 2009 Monovalent Vaccine Novartis' 'Fluzone Intradermal Trivalent', '2011-2012 trivalent inactivated vaccine (A/California/7/09 (H1N1), A/Perth /16/2009 (H3N2), and B/Brisbane/60/2008)', '2011-2012 trivalent inactivated vaccine', 'LAIV, Product Name: pH1N1 LAIV', 'LAIV, Product Name: pH1N1 PB2 WT PB1 L319Q', 'LAIV, Product Name: pH1N1 PB2 WT PB1 LAIV', 'LAIV, Product Name: pH1N1 PB2 WT PB1 LAIV plus L319Q', 'LAIV, Product Name: pH1N1 WT', 'LAIV, Product Name: pH1N1 PB2 LAIV PB1 LAIV plus L319Q', 'Fluzone', 'Influenza virus vaccine', 'live attenuated influenza vaccine','Low dose live influenza vaccine, Product Name: PR/8'  'FluMist' 'Adjuvant Name: AddaVax' 'Measles-rubella vaccine', 'Recombinant protein-Neuraminidase vaccine, Product name: N1-MPP', 'Recombinant protein-Neuraminidase vaccine, Product name: N1-VASP', 'Seasonal influenza, unspecified formulation, CVX Code: 150', 'Seasonal influenza, unspecified formulation, CVX Code: 150, 158', 'Seasonal influenza, unspecified formulation, CVX Code: 150, 158, 161', 'Seasonal influenza, unspecified formulation, CVX Code: 171, 186', 'Seasonal influenza, unspecified formulation, CVX Code: 185','2016 Fluarix quadrivalent seasonal influenza vaccine', 'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_Z1_HA_RC', 'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_Z5_HA_RC', 'Recombinant protein-Full length protein vaccine, Product Name: Mal/NL/01', 'Recombinant protein-Full length protein vaccine, Product Name: Mal/WI/08', 'Seasonal influenza, unspecified formulation 2018-2019, CVX Code: 88', 'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_Y2_HA_RC', 'Flucelvax Quadrivalent 2018-2019, CVX Code: 171, 186', 'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_J4_HA_RC', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ1_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Fujian02', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Wis05', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Bris07', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Perth09', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Vic', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Tx12', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Switz13', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: HK14', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Sing16', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_T8_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_TJ2_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_T11_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ3_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ4_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_TJ5_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ6_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ7_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ8_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_TJ9_HA_VLP', 'H1 reassortant virus vaccine, Product Name: Brisb07', 'H1 reassortant virus vaccine, Product Name: CA/09', 'H1 reassortant virus vaccine, Product Name: Chile/83', 'H1 reassortant virus vaccine, Product Name: NC/99', 'H1 reassortant virus vaccine, Product Name: PR/34', 'H1 reassortant virus vaccine, Product Name: Sing/86', 'H1 reassortant virus vaccine, Product Name: UGA_COBRA_P1_HA_RA', 'H1 reassortant virus vaccine, Product Name: UGA_COBRA_X3_HA_RA', 'H1 reassortant virus vaccine, Product Name: UGA_COBRA_X6_HA_RA', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: CA/09_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_P1_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Brisb07_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_X6_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: Brisb18_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_Y2_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: COBRA_Y4_HA_VLP', 'Recombinant protein-HA vaccine, Product Name: Bris18', 'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_P1_HA_RC', 'Recombinant protein-HA vaccine, Product Name: CA09', 'Recombinant protein-HA vaccine, Product Name: Bris07', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_X6_HA_RC', 'Recombinant protein-COBRA vaccine, Product Name: COBRA_Y4_HA_RC', 'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_NG2_HA_RC', 'Fluad 2017-2018, CVX Code: 168', 'Fluzone High-Dose 2016-2017, CVX Code: 135', 'Recombinant protein-COBRA vaccines, Product Name: COBRA_IAN-8_HA_RC, Product Name: COBRA_Q6_HA_RC, Product Name: UGA_COBRA_Z1_HA_RC', 'mRNA vaccine, Vaccine Name: M2' 'mRNA vaccine, Vaccine Name: H3ss-TM', 'mRNA vaccine, Vaccine Name: NA' 'mRNA vaccine, Vaccine Name: NP', 'Recombinant Protein-NA vaccine, Product Name: CA09_NA_RC', 'Recombinant protein-COBRA vaccine, Product Name: UGA_COBRA_N1-I_NA_RC', 'Recombinant Protein-NA vaccine, Product Name: Viet/04_NA_RC', 'Recombinant Protein-NA vaccine, Product Name: Bris/07_NA_RC', 'Fluzone Quadrivalent 2022-2023, CVX Code: 150, 150, 158, 161', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_TX_12_HA_VLP', 'Recombinant subunit VLP (non-fusion) vaccine, Product Name: UGA_COBRA_Wisc_05_HA_VLP', 'Seasonal influenza, intranasal, CVX Code: 151', 'A/Ruddy turnstone/Delaware/300/2009 (H1N1)', 'mRNA vaccine, Product Name: 20 mRNA-LNP vaccine', 'mRNA vaccine, Product Name: H1 mRNA-LNP (Hensley)', 'mRNA vaccine, Product Name: H3 mRNA-LNP (Hensley)', 'mRNA vaccine, Product Name: IBV mRNA-LNP (Hensley)', 'mRNA vaccine, Product Name: CA09_mRNA', 'mRNA vaccine, Product Name: Kan17_mRNA', 'mRNA vaccine, Product Name: UGA_COBRA_NG2_HA_mRNA', 'mRNA vaccine, Product Name: UGA_COBRA_Y2_HA_mRNA', 'Fluarix' 'Fluvirin', 'Influvac', '2008-2009 trivalent influenza vaccine', 'inactivated influenza vaccine', 'A/California/7/2009', 'mRNA vaccine, Product Name: Furin mut', 'mRNA vaccine, Product Name: Monomeric sRBD', 'Viral vector vaccine, Product Name: PRD_NDV_004, Target Antigen: OTH-Spike Protein (ectodomain) Strain Name: SARS-CoV-2/human/China/Wuhan-Hu-1/2019', 'Viral vector vaccine, Product Name: PRD_NDV_001, Target Antigen: OTH-Spike Protein (transmembrane) Strain Name: SARS-CoV-2/human/China/Wuhan-Hu-1/2019', 'NDV expressing the SARS-CoV-2 spike-F chimera consisting of the spike protein ectodomain without the polybasic cleavage site and the TM domain and cytoplasmic tail of the NDV F protein (NDV_LS_S-F)', 'Viral vector vaccine, Product Name: PRD_NDV, Target Antigen: OTH-Not Applicable Strain Name: OTH-Wild type NDV LaSota', 'Recombinant protein-NA vaccine, Product Name: B-Mal, Target Antigen: NA, Strain Name: B/Malaysia/2506/2004', 'Recombinant protein-NA vaccine, Product Name: A-Mich-N1, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)', 'Fluzone Quadrivalent 2017-2018', 'mRNA vaccine, Product Name: iNA, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: M1, Target Antigen: M1, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: M2, Target Antigen: M2, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: M2e, Target Antigen: M2, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: M2i, Target Antigen: M2, Strain Name: A/Michigan/45/2015 (H1N1)''mRNA vaccine, Product Name: HA-cleave, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: Mem-MiniHA, Target Antigen: HA, conserved stalk domain, Strain Name: A/Brisbane/59/2007 (H1N1)', 'mRNA vaccine, Product Name: HA-RBS, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: WT-HA, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: NA, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: NP, Target Antigen: NP, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: sHA-cleave, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: siNA, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: MiniHA, Target Antigen: HA, conserved stalk domain, Strain Name: A/Brisbane/59/2007 (H1N1)',  'mRNA vaccine, Product Name: sNA, Target Antigen: NA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: sHA-RBS, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)', 'mRNA vaccine, Product Name: sHA, Target Antigen: OTH-HA, Strain Name: A/Michigan/45/2015 (H1N1)', 'Fluarix 2014-2015' 'Influenza A (H1N1) 2009 Monovalent',  'Seasonal influenza, unspecified formulation 2009-2010',  'Seasonal influenza, unspecified formulation 2010-2011',  'Seasonal influenza, unspecified formulation 2013-2014', 'IIV, Product Name: IIV_cH5_1HA, Target Antigen: HA head domain, conserved epitopes', 'IIV, Product Name: IIV_cH8_1HA, Target Antigen: HA head domain, conserved epitopes', 'LAIV, Product Name: LAIV8_IIV5, Target Antigen: HA head domain, conserved epitopes'])]


                   #Drop duplicates of names OCCUR.drop()
#occur = OCCUR.head(200)
#zoccur = occur.merge(df_ir, how = 'left', left_on='comments', right_on='ARM_ACCESSION')
#zoccur = pd.concat([df_ir['EXPOSURE_ACCESSION'], df_ae['ADVERSE_EVENT_ACCESSION']])

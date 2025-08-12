# -*- coding: utf-8 -*-
"""
Created on Wed May 7 14:37:40 2025

@author: Huffmaar
"""


import pandas as pd
import numpy as np
import sys

pathway = 'C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/ETL_TestCases/ImmPort UseCase/'
template = ''

#'immport_study_accession',	'study_title', 'study_brief_desc',	'study_min_age',	'study_max_age',	'immport_subject_accession',	'gender',	'race',	'immport_immune_exposure_material_id',	'vaccine',	biosample_id	immport_vaccination_time	immport_vaccination_time_unit	day_0_def	biosample_type	subtype	immport_biosample_accession	expsample_repository_name	gsm	expsample_to_multiple_gsm_flag	gse	gpl	platform_desc	batch_factor	type_subtype	age_group


STY = "ImmPortstudy_.csv"
ORGO = "ImmPortorgo_.csv"
SAMP = "ImmPortsample_.csv"
INTER = "ImmPortintervention_.csv"
pinter = 'C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/ETL_TestCases/ImmPort UseCase/intervention_.csv'
pinter = pathway+INTER
psamp = pathway+SAMP
pstudy = pathway+ "/study_.csv"
pexp = pathway+ "/experiment_.csv"
pd_i = pd.read_csv(pinter, sep = ',')
pd_s = pd.read_csv(psamp, sep = ',')
pd_y = pd.read_csv(pstudy, sep = ',')
pd_e = pd.read_csv(pexp, sep = ',')


# -*- coding: utf-8 -*-
"""
Created on Tue Jun 3 10:04:31 2025

@author: huffmaar
"""

# This code is meant to load in data from MYSQL and then generate two tables of results.





def twinned_studdies (study1, study2):
    lists = [study1, study2]
    for studyn in lists:
        test_s = STUDY['study_id'] == ids_study
        test_e = EXPER[EXPER['study_id'].isin(test_s['study_id'])].drop(columns=['A_right', 'B_right'])
        test_o = ORGO[ORGO['experiment_id'].isin(test_e['experiment_id'])]
        test_i = INTER[INTER['experiment_id'].isin(test_e['experiment_id'])]
        test_p = SAMP[SAMP['organism_id'].isin(test_o['organism_id'])]
        test_r = RESULT[RESULT['sample_id'].isin(test_p['sample_id'])]
        
        test_se = test_s.merge(test_e, on='experiment_id')
        test_pr = test_p.merge(test_r, on='sample_id')
        test_oi = test_i.merge(test_o, on='organism_id')
        test_proi = test_oi.merge(test_pr, on='organism_id')
        
        sallies = test_proi.to_json(indent=4)
        
        test_sproit = test_oi.merge(test_proi)
        test_eproi = test_e.merge(test_proi, left_on='experiment_id', right_on='experiment_id')
        test_seproi = test_s.merge(test_eproi, on='study_id')
        print(test_proi)
        to_json(orient= 'index', indent=4)



test_s = STUDY['study_id'] == ids_study
test_e = EXPER[EXPER['study_id'].isin(test_s['study_id'])].drop(columns=['A_right', 'B_right'])
test_o = ORGO[ORGO['experiment_id'].isin(test_e['experiment_id'])]
test_i = INTER[INTER['experiment_id'].isin(test_e['experiment_id'])]
test_p = SAMP[SAMP['organism_id'].isin(test_o['organism_id'])]
test_r = RESULT[RESULT['sample_id'].isin(test_p['sample_id'])]

test_se = test_s.merge(test_e, on='experiment_id')
test_pr = test_p.merge(test_r, on='sample_id')
test_oi = test_i.merge(test_o, on='organism_id')
test_proi = test_oi.merge(test_pr, on='organism_id')

json_data_proi = test_proi.to_json(indent=4)


test_sproit = test_oi.merge(test_proi)
test_eproi = test_e.merge(test_proi, left_on='experiment_id', right_on='experiment_id')
test_seproi = test_s.merge(test_eproi, on='study_id')

import json

json_data_proi = test_proi.to_json(orient='index', indent=4)

json_data_s = test_s.to_json(orient='index', indent=4)
json_data_e = test_e.to_json(orient='index', indent=4)
json_data_o = test_o.to_json(orient='index', indent=4)
json_data_i = test_i.to_json(orient='index', indent=4)
json_data_p = test_p.to_json(orient='index', indent=4)
json_data_r = test_r.to_json(orient='index', indent=4)

json_data_se = test_se.to_json(orient='index', indent=4)

def twinned_studdies (study1, study2):
    lists = [study1, study2]
    for studyn in lists:
        test_s = STUDY['study_id'] == ids_study
        test_e = EXPER[EXPER['study_id'].isin(test_s['study_id'])].drop(columns=['A_right', 'B_right'])
        test_o = ORGO[ORGO['experiment_id'].isin(test_e['experiment_id'])]
        test_i = INTER[INTER['experiment_id'].isin(test_e['experiment_id'])]
        test_p = SAMP[SAMP['organism_id'].isin(test_o['organism_id'])]
        test_r = RESULT[RESULT['sample_id'].isin(test_p['sample_id'])]
        
        test_se = test_s.merge(test_e, on='experiment_id')
        test_pr = test_p.merge(test_r, on='sample_id')
        test_oi = test_i.merge(test_o, on='organism_id')
        test_proi = test_oi.merge(test_pr, on='organism_id')
        
        sallies = test_proi.to_json(indent=4)
        
        test_sproit = test_oi.merge(test_proi)
        test_eproi = test_e.merge(test_proi, left_on='experiment_id', right_on='experiment_id')
        test_seproi = test_s.merge(test_eproi, on='study_id')
        print(test_proi)
        to_json(orient= 'index', indent=4)



test_s = STUDY['study_id'] == ids_study
test_e = EXPER[EXPER['study_id'].isin(test_s['study_id'])].drop(columns=['A_right', 'B_right'])
test_o = ORGO[ORGO['experiment_id'].isin(test_e['experiment_id'])]
test_i = INTER[INTER['experiment_id'].isin(test_e['experiment_id'])]
test_p = SAMP[SAMP['organism_id'].isin(test_o['organism_id'])]
test_r = RESULT[RESULT['sample_id'].isin(test_p['sample_id'])]

test_se = test_s.merge(test_e, on='experiment_id')
test_pr = test_p.merge(test_r, on='sample_id')
test_oi = test_i.merge(test_o, on='organism_id')
test_proi = test_oi.merge(test_pr, on='organism_id')

json_data_proi = test_proi.to_json(indent=4)


test_sproit = test_oi.merge(test_proi)
test_eproi = test_e.merge(test_proi, left_on='experiment_id', right_on='experiment_id')
test_seproi = test_s.merge(test_eproi, on='study_id')

import json

json_data_proi = test_proi.to_json(orient='index', indent=4)

json_data_s = test_s.to_json(orient='index', indent=4)
json_data_e = test_e.to_json(orient='index', indent=4)
json_data_o = test_o.to_json(orient='index', indent=4)
json_data_i = test_i.to_json(orient='index', indent=4)
json_data_p = test_p.to_json(orient='index', indent=4)
json_data_r = test_r.to_json(orient='index', indent=4)

json_data_se = test_se.to_json(orient='index', indent=4)
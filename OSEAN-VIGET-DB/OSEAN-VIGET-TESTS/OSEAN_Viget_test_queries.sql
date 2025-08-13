SELECT expsample_reference_id, organism_id,  collection_time FROM seacdm.sample 
WHERE 
organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = 'Female') AND
organism_id IN (SELECT intervention_id FROM seacdm.intervention 
WHERE  intervention_type = 'vaccination' AND material = 'Fluarix') AND
sample_id IN ( SELECT sample_id FROM seacdm.results 
WHERE original_assay_type = 'Blood.RNA Expression Assay');

SELECT organism_id, intervention_id FROM seacdm.intervention;

SELECT expsample_reference_name, organism_id, collection_time, expsample_type FROM seacdm.sample 
WHERE 
organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = 'Female') AND
organism_id IN (SELECT organism_id FROM seacdm.intervention 
WHERE  intervention_type = 'vaccination' AND material  = 'Fluzone' AND T0_definition = 'Time of initial vaccine administration') AND
sample_id IN ( SELECT sample_id FROM seacdm.results 
WHERE original_assay_type = 'Blood.RNA Expression Assay');

SELECT expsample_reference_name, organism_id, collection_time FROM seacdm.sample WHERE organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = 'Female') AND organism_id IN (SELECT organism_id FROM seacdm.intervention WHERE  intervention_type = 'vaccination' AND (material  = 'FluMist') or (material = 'live attenuated influenza vaccine')) AND sample_id IN ( SELECT sample_id FROM seacdm.results WHERE original_assay_type = 'Blood.RNA Expression Assay');

SELECT organism_id FROM seacdm.intervention 
WHERE  intervention_type = 'vaccination' AND material  = 'Fluzone' AND T0_definition = 'Time of initial vaccine administration';

SELECT expsample_reference_id, organism_id, collection_time FROM seacdm.sample 
WHERE 
organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = 'Female') AND
organism_id IN (SELECT intervention_id FROM seacdm.intervention 
WHERE  intervention_type = 'vaccination' AND material = 'Fluarix') AND
sample_id IN ( SELECT sample_id FROM seacdm.results 
WHERE original_assay_type = 'Blood.RNA Expression Assay');

select * from experiment;

SELECT DISTINCT s.expsample_reference_name, s.organism_id, s.collection_time, e.experiment_id
FROM sample s
JOIN organism o ON s.organism_id = o.organism_id
JOIN intervention i ON s.organism_id = i.organism_id
JOIN results r ON s.sample_id = r.sample_id
JOIN experiment e ON o.organism_id = e.experiment_id
WHERE
    o.sex = 'Female' AND
    i.intervention_type = 'vaccination' AND
    i.material = 'Fluarix' AND
    r.original_assay_type = 'Blood.RNA Expression Assay';

SELECT DISTINCT s.expsample_reference_name, s.organism_id, s.collection_time
FROM sample s
JOIN organism o ON s.organism_id = o.organism_id
JOIN intervention i ON s.organism_id = i.organism_id
JOIN results r ON s.sample_id = r.sample_id
WHERE
    o.sex = 'Female' AND
    i.intervention_type = 'vaccination' AND
    i.material = 'Fluarix' AND
    r.original_assay_type = 'Blood.RNA Expression Assay';

SELECT expsample_reference_name, organism_id, collection_time FROM seacdm.sample 
WHERE 
organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = 'Female') AND
organism_id IN (SELECT intervention_id FROM seacdm.intervention 
WHERE  intervention_type = 'vaccination' AND material = 'Trivalent inactivated influenza') AND
sample_id IN ( SELECT sample_id FROM seacdm.results 
WHERE original_assay_type = 'Blood.RNA Expression Assay');

SELECT expsample_reference_name, organism_id, collection_time FROM seacdm.sample 
WHERE 
organism_id IN ( SELECT organism_id FROM seacdm.organism WHERE sex = 'Female') AND
organism_id IN (SELECT intervention_id FROM seacdm.intervention 
WHERE  intervention_type = 'vaccination' AND material_id = 'Trivalent inactivated influenza') AND
sample_id IN ( SELECT sample_id FROM seacdm.results 
WHERE original_assay_type = 'Blood.RNA Expression Assay');


SELECT * from sample where expsample_reference_name = 'GSM1147760' ;

SELECT * FROM seacdm.sample 
WHERE 
organism_id IN (SELECT intervention_id FROM seacdm.intervention 
WHERE  intervention_type = 'vaccination' AND material = 'Fluarix') AND
sample_id IN ( SELECT sample_id FROM seacdm.results 
WHERE original_assay_type = 'Blood.RNA Expression Assay');
select distinct material, material_id from intervention;


SELECT organism_id FROM intervention
WHERE material_id IN ('VO_0000044', 'VO_0000045', 'VO_0000046', 'VO_0000047', 'VO_0000642', 'VO_0001178',  'VO_004809', 'VO_0004810');

select reference_id from seacdm.group;

SELECT DISTINCT 
    s.expsample_reference_name, 
    s.organism_id, 
    s.collection_time, 
    s.expsample_type, 
    g.reference_id
FROM seacdm.sample s
JOIN seacdm.organism o ON s.organism_id = o.organism_id
JOIN seacdm.intervention i ON s.organism_id = i.organism_id
JOIN seacdm.results r ON s.sample_id = r.sample_id
JOIN seacdm.experiment e ON o.experiment_id = e.experiment_id
JOIN seacdm.group g ON g.experiment_id = e.experiment_id
WHERE
    o.sex IN ({sex_ids_sql}) AND
    i.intervention_type = 'vaccination' AND
    i.material_id IN ({vaccine_ids_sql}) AND
    r.original_assay_type = 'Blood.RNA Expression Assay';




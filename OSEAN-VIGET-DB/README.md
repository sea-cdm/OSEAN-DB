### OSEAN-VIGET-DB

OSEAN-VIGET-DB is an OSEAN DB for VIGET.

VIGET is the Vaccine Immune Genetic Expression Tool
Ref: Brunson, T. et al. VIGET: A web portal for study of vaccine-induced host responses based on Reactome pathways and ImmPort data. Front Immunol 14, 1141030 (2023).

## Database Schema
Database Schema uses the general one stored in sea-cdm.sql

## Data used 

The first OSEAN DB developed was called OSEAN-VIGET, which converted the data from the VIGET (Vaccine Immune Gene Expression Tool) program to the SEA CDM format. Specifically, two VIGET input files were extracted from the VIGET Zenodo website (https://zenodo.org/records/7407195), with one file about the metadata of 28 vaccine immune studies (download: https://zenodo.org/records/7407195/files/immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv?download=1) about the metadata of 28 vaccine immune studies, and the other file (download: https://zenodo.org/records/7407195/files/ImmuneExposureGeneExpression_020922.csv?download=1). A Python ETL program was developed to process the metadata file to the SEA CDM format. The gene expression data file was downloaded to a local directory pointed by the SEA CDM documentation.

## ETL

ETL: The ETL is found with OSEAN_Viget_ETL.py.

## PELAGIC Methods 

The Pelagic_SQL_Wrapper.py program under the [PELAGIC Module](https://github.com/sea-cdm/OSEAN-DB/tree/main/PELAGIC%20Module) provides functions and templates for creating Python code to query the OSEAN DB (MySQL) relational database for specific questions. 


## Applications of OSEAN VIGET DB  

Several application programs can be found under the [OSEAN-VIGET-TESTS directory](https://github.com/sea-cdm/OSEAN-DB/tree/main/OSEAN-VIGET-DB/OSEAN-VIGET-TESTS). 

Specifically, OSEAN_Viget_test_queries.sql queries  for sex-specific vaccine immune responses. 

OSEAN_Viget_comparison.py compares OSEAN VIGET DB gene expression studies.

OSEAN_Viget_export.py exports the results from the OSEAN DB studies into json format.

OSEAN_Viget_queries.py looks at different tables within the OSEAN VIGET DB and the VIGET gene expression file. Note that the VIGET gene expression file can be found here from the VIGET Zenodo website https://zenodo.org/records/7407195. 


### Tracker link:  
https://github.com/sea-cdm/OSEAN-DB/issues 

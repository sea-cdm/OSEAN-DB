### OSEAN-VIGET-DB

OSEAN-VIGET-DB is an OSEAN DB for VIGET.

VIGET is the Vaccine Immune Genetic Expression Tool
Ref: 

## Database Schema
Database Schema uses the general one stored in sea-cdm.sql

## Data used 

The first OSEAN DB developed was called OSEAN-VIGET, which converted the data from the VIGET (Vaccine Immune Gene Expression Tool) program to the SEA CDM format. Specifically, two VIGET input files were extracted from the VIGET Zenodo website (https://zenodo.org/records/7407195), with one about the metadata of 28 vaccine immune studies, and the other being the normalized gene expression data file. A Python ETL program was developed to process the metadata file to the SEA CDM format. The gene expression data file was downloaded to a local directory pointed by the SEA CDM documentation.

## ETL

ETL: The ETL is found with VIGET_ETL.py.

## PELAGIC Methods 

PELAGIC's PURE_SPARQL function provides template for creating python code to query the oseandb database format. 


## Applications of OSEAN VIGET DB  

Query for sex-specific vaccine immune responses can be found in Test_Query.sql.
Resulting data can be found as part of the non-ETL functions.
VIGET_Comparison.py to compare OSEAN VIGET DB  gene expression studies.

VIGET_Export.py to export OSEAN DB studies into json format.

VIGET_QUERIES.py to look 


### Tracker link:  
https://github.com/sea-cdm/OSEAN-DB/issues 

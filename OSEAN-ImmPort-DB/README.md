# OSEAN-ImmPort-DB
OSEAN-VIGET-DB is an OSEAN DB for VIGET.

This folder contains OSEAN-ImmPort-DB ETL.
Please provide the full path name as an argument to generate files to load into SQL. The OSEAN-CellxGene-DB was generated using the DR 56.0 All Metadata downloaded from ImmPort website.


## Database Schema
Database Schema uses the general one stored in sea-cdm.sql

## Data used 

The second OSEAN DB developed was called OSEAN-ImmPort, which converted the data from the ImmPort program to the SEA CDM format. Specifically, the all metadata file was converted into SEA-CDM.

## ETL

ETL: The ETL is found with ImmPort_ETL_Gen.py. Include the absolute path of the metadata files to have it function.

## PELAGIC Methods 

PELAGIC's PURE_SPARQL function provides template for creating python code to query the oseandb database format. 

### Tracker link:  
https://github.com/sea-cdm/OSEAN-DB/issues 

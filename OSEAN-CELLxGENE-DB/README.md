## OSEAN-CellxGene-DB

This contains the ETL used to generate CellxGene-DB using the generic ETL. The OSEAN-CellxGene-DB used the following h5ad to load in the files.



# OSEAN-ImmPort-DB

OSEAN-CellxGene-DB is an OSEAN DB for VIGET.

This folder contains OSEAN-CELLxGENE-DB ETL.
Please provide the full path name as an argument to generate files to load into SQL.


## Database Schema

Database Schema uses the general one stored in sea-cdm.sql

## Data used

The second OSEAN DB developed was called OSEAN-ImmPort, which converted the data from the ImmPort program to the SEA CDM format. Specifically, the OSEAN-CellxGene-DB was generated using the DR 56.0 All Metadata downloaded from ImmPort website (https://www.immport.org/browser/?path=ALLSTUDIES%2Farchive%2FALLSTUDIES-DR56\_Metadata\&page=1).

The OSEAN-CellxGene-DB was generated using the following five databases obtained from the CZ CELLxGENE website (https://cellxgene.cziscience.com/datasets) after filtering for Influenza vaccines:
    - 'A total of 38,217 droplet-based single-nucleus transcriptomes profiled across 14 cell types in the frontal cortex': 'bd572490-8f80-4044-9d00-db07a68fb6ec.h5ad'
    - 'A total of 27,092 droplet-based single-nucleus transcriptomes profiled across 11 cell types in the choroid plexus': '8655aff7-44c7-4904-8719-7dd75ec20fcd.h5ad'
    - 'COMBAT project: single cell gene expression data from COVID-19, sepsis and flu patient PBMCs': '983bd800-e655-4c76-ad9a-20ae0257fc0b.h5ad'
    - 'Immunophenotyping of COVID-19 and influenza highlights the role of type I interferons in development of severe COVID-19': 'a3ef98b7-5eec-45e0-ae73-db13324bac22.h5ad'
    - 'Mouse Post-Flu Time Series': '65cf7371-bbf3-4d41-9250-2d30bd048125.h5ad'

## ETL

ETL: The ETL is found with Osean_ImmPort_ETL.py. Include the absolute path of the metadata files to have it function.

## PELAGIC Methods

PELAGIC's library provides template for creating python code to query the oseandb database format.

### Tracker link:

https://github.com/sea-cdm/OSEAN-DB/issues

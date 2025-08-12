# OSEAN-DB
OSEAN-DB: OSEAN database

OSEAN stands for Ontology-based Study-Experiment-Assay Newtwork. OSEAN DB is a relational database system built on the ontology-supported SEA CDM.

Currently OSEAN-DB contains prototypes for SEA-CDM file conversion.

## Database Schema

Database Schema: Contains the schema for OSEAN-DB as a .sql file. 


## ETLs

ETL: An Export-Transform-Loard pipeline are found within each use case for generic models. Certain studies or tables with author or table-specific metadat columns have to be changed.

## PELAGIC 

PELAGIC is a module that queries a local OSEAN DB for results. There are two variations of PELAGIC, the Pure SQL was used by the paper to generate the file; whiel PELAGIC is used a template to input code into a function.


## Use cases  

Three use cases are provided with appropriate ETLs:
- OSEAN VIGET DB: This contains the appropriate ETL for VIGET DB and the actual metadata and gene expression file used. The readme contains the link for all files used for this use case as part of the SEA CDM paper.
- OSEAN ImmPort DB: This contains the appropriate ETL. The readme contains the link for all files used for this use case as part of the SEA CDM paper.
- OSEAN CellxGene DB: This contains the appropriate ETL. The readme contains the link for all files used for this use case as part of the SEA CDM paper.
  


### Tracker link:  
https://github.com/sea-cdm/OSEAN-DB/issues 


## Developers 

Anthony Huffman is responsible for code.
Yongqun He is responsible for aid in setting up Git-Hub.

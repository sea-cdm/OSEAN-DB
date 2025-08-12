# OSEAN-DB
OSEAN-DB: OSEAN database

OSEAN stands for Ontology-based Study-Experiment-Assay Newtwork. 

OSEAN DB is a relational database system built on the ontology-supported SEA CDM. MySQL is our default relational database management system. 

This directory includes three examples of OSEAN databases.

## Database Schema

The SEA-CDM.sql file under the directory DB-Schema provides the database schema for generating an OSEAN database using MySQL.

## ETLs

The Extract-Transform-Load (ETL) pipelines are found within each use case for generic models. Users may update specific ETL programs depending on specific studies or use cases. 

## PELAGIC 

PELAGIC is a Python Engine for Linking, Analyzing, and Gleaning Insightful Context from the SEA CDM-based OSEAN databases. 

PELAGIC is a module in the SEA CDM system that performs queries and analyses on a specific OSEAN DB. 

The 

There are two types of PELAGIC programs: 
- Direct SQL scripts that can be used to directly query a specific OSAEN DB. 
- while PELAGIC is used a template to input code into a function.


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

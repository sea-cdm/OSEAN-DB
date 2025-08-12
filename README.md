# OSEAN-DB
OSEAN-DB: OSEAN database

OSEAN stands for Ontology-based Study-Experiment-Assay Newtwork. OSEAN is set up as an integrative database system based on the SEA CDM. When we all use the SEA CDM to generate the OSEAN databases, we basically are able to seamlessly integrate biological and biomedical datasets from different resources in different domains.  

OSEAN DB is a relational database system built on the ontology-supported SEA CDM. MySQL is our default relational database management system. 

This directory includes three examples of OSEAN databases.

## Database Schema

The SEA-CDM.sql file under the directory DB-Schema provides the database schema for generating an OSEAN database using MySQL.

## ETLs

The Extract-Transform-Load (ETL) pipelines are found within each use case for generic models. Users may update specific ETL programs depending on specific studies or use cases. 

## PELAGIC 

PELAGIC is a Python Engine for Linking, Analyzing, and Gleaning Insightful Context from the SEA CDM-based OSEAN databases. 

PELAGIC is a module in the SEA CDM system that performs queries and analyses on a specific OSEAN DB. This module contains a Python SQL wrapper that implements specific SQL scripts for querying specific OSAEN DB and a Python PELAGIC program that includes a library of functions that can be used to process specific data. 

## Use cases  

Three use cases are provided:
- OSEAN VIGET DB: An OSEAN DB that contains data from the VIGET (Vaccine-induced gene expression analysis tool) system:
  - Data downloaded: Two VIGET input files were extracted from the VIGET Zenodo website (https://zenodo.org/records/7407195), with one about the metadata of 28 vaccine immune studies, and the other being the normalized gene expression data file. 
  - VIGET paper ref: Brunson T, Sanati N, Huffman A, Masci AM, Zheng J, Cooke MF, Conley P, He Y, Wu G. VIGET: A web portal for study of vaccine-induced host responses based on Reactome pathways and ImmPort data. Front Immunol 14, 1141030 (2023). PMID: [37180100](https://pubmed.ncbi.nlm.nih.gov/37180100/) PMCID: [PMC10172660](https://pmc.ncbi.nlm.nih.gov/articles/PMC10172660/).  
  - VIGET website: https://viget.violinet.org/. 

- OSEAN ImmPort DB: An OSEAN DB that contains ImmPort data:
  - ImmPort data:
  - ImmPort website:
       
- OSEAN CellxGene DB: An OSEAN DB that contains a part of CellxGene data. As a demonstration, only influenza-related data are included.
  -  Data source: ... 

  
### Tracker link:  
https://github.com/sea-cdm/OSEAN-DB/issues 


## Developers 

- Anthony Huffman is responsible for generating the code. 
- Yongqun "Oliver" He is responsible for design, testing, editing, and documentation.
  

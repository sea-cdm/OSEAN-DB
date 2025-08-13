# OSEAN-ImmPort-DB

OSEAN-VIGET-DB is an OSEAN DB for VIGET.

This folder contains OSEAN-ImmPort-DB ETL.
Please provide the full path name as an argument to generate files to load into SQL.



## Database Schema

Database Schema uses the general one stored in sea-cdm.sql

## Data used

The second OSEAN DB developed was called OSEAN-ImmPort, which converted the data from the ImmPort program to the SEA CDM format. Specifically, the OSEAN-CellxGene-DB was generated using the DR 56.0 All Metadata downloaded from ImmPort website (https://www.immport.org/browser/?path=ALLSTUDIES%2Farchive%2FALLSTUDIES-DR56\_Metadata\&page=1).

## ETL

ETL: The ETL is found with Osean_ImmPort_ETL.py. Include the absolute path of the metadata files to have it function.

## PELAGIC Methods

PELAGIC's library provides template for creating python code to query the oseandb database format.

### Tracker link:

https://github.com/sea-cdm/OSEAN-DB/issues


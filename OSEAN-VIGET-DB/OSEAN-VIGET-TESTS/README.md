# OSEAN-DB
OSEAN-DB: OSEAN database

OSEAN is a relational database system built on the ontology-supported SEA CDM.

Currently OSEAN-DB contains files to query and compare the results of the data in SEA CDM.

OSEAN_Viget_test_queries.sql contains example SQL queries to be used in the database.
OSEAN_Viget_export.py contains a script to export information from OSEAN_VIGET_DB into a json file format.
OSEAN_Viget_queries.py contains a script to retreive a list of sample_ids in OSEAN and gene expresssion data from a VIGET file according to some restriction criteria.
OSEAN_Viget_comparison.py contains a script to retreive two sets of samples from two different studies.


Database Schema: Uses SEA-CDM db format.

ETL: Uses data loaded from Osean_Viget_ETL.py.

PELAGIC: Shares functions from PELAGIC, functions define locally to avoid issues or need to download packages.

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 17:07:14 2025

@author: huffmaar
"""

import sys
    
if len(sys.argv) > 1:
   name = sys.argv[1]
   print(f"Hello, {name}!")
else:
   print("Please provide a name as a command-line argument.")
   
   #VIGET = "/Users/huffmaar/Documents/SEA-CDM-SQL-Imports/ImmuneExposureGeneExpression_020922_Raw.csv"

# Strings for filenames, to be changed lagter.
VIGET = "/Users/huffmaar/Documents/SEA-CDM-SQL-Imports/ImmuneExposureGeneExpression_020922_Raw.csv"
VIGETGENE = "a"
gene_exp = "/Users/huffmaar/OneDrive - Michigan Medicine/Documents/immport_vaccine_expression_matrix_mapped_merged_approved_genes_091421.csv"


GEXP = read_VIGET(gene_exp)
GEXP = GEXP.T

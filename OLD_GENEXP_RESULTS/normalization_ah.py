# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 21:54:53 2025

@author: Huffmaar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ===== Configuration =====
input_path = "/Users/cc/Desktop/He_lab/CellCards/cellxgene-census-main/api/python/notebooks/api_demo/male_genes_normal_by_celltype.csv"
output_path = input_path.replace(".csv", "_lognorm.csv")

# ===== Load data =====
df = pd.read_csv(input_path)

# ===== Scanpy-style normalization: total count scaling + log1p =====

# Scale expression per Cell_Type so that the total expression per group sums to 1e4
df["Norm_Scaled"] = df.groupby(["Cell_Type", "Disease"])["Mean_Expression"].transform( 
    lambda x: (x / x.sum()) * 1e4)
# Apply natural log transformation
df["Mean_Expression_LogNorm"] = np.log1p(df["Norm_Scaled"])

# ===== Save result =====
df.to_csv(output_path, index=False)
print(f"[INFO] Log-normalized data saved to: {output_path}")


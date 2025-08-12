# -*- coding: utf-8 -*-
"""
Created on Fri May 16 14:53:19 2025

@author: Huffmaar
"""

import GEOparse
import pandas as pd
GSM = 'GSM26818'
gse = GEOparse.get_GEO(geo=GSM, destdir="./")


pathway ='C:/Users/huffmaar'

gpath = pathway + '/' + GSM + '.txt'
zed = pd.read_csv(gpath, sep = '\t', skipfooter=1, skiprows=41)


print("GSM example:")
for gsm_name, gsm in gse.gsms.items():
    print("Name: ", gsm_name)
    print("Metadata:",)
    for key, value in gsm.metadata.items():
        print(" - %s : %s" % (key, ", ".join(value)))
    print ("Table data:",)
    print (gsm.table.head())
    break

print()
print("GPL example:")
for gpl_name, gpl in gse.gpls.items():
    print("Name: ", gpl_name)
    print("Metadata:",)
    for key, value in gpl.metadata.items():
        print(" - %s : %s" % (key, ", ".join(value)))
    print("Table data:",)
    print(gpl.table.head())
    break
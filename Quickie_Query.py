# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 23:18:13 2025

@author: Huffmaar
"""

import pandas as pd

path = 'C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/VIGET_OSEAN_2025_USECASE/'
str1 = '/Fluvirin-All-7.0-0.0--GeneExpression.csv'
str2 = '/Fluarix-All-7.0-0.0--GeneExpression.csv'
str3 = '/Fluzone-All-28.0-0.0--GeneExpression.csv'
str4 = '/Fluzone-All-7.0-0.0--GeneExpression.csv'


path1 = path+str1
path2 = path+str2
path3 = path+str3
path4 = path+str4

db1 = pd.read_csv(path1)
db2 = pd.read_csv(path2)
db3 = pd.read_csv(path3)
db4 = pd.read_csv(path4)
dball = pd.concat([db1, db2, db3, db4])

#db1 = pd.read_csv('C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/VIGET_OSEAN_2025_USECASE/Fluvirin-Male-7.0-0.0--GeneExpression.csv', sep=',')
#db2 = pd.read_csv('C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/VIGET_OSEAN_2025_USECASE/FluMist-Male-28.0-0.0--GeneExpression.csv', sep=',')
#db3 = pd.read_csv('C:/Users/huffmaar/OneDrive - Michigan Medicine/Documents/GitHub/OSEAN-DB/VIGET_OSEAN_2025_USECASE/FluMist-All-7.0-0.0--GeneExpression.csv', sep=',')
#db4
#db5
#dball = pd.concat([db1, db2, db3], axis=0)
print(dball['gene_name'].unique())
print(len(dball['gene_name'].unique()))

str11 = '/Fluvirin-Female-7.0-0.0--GeneExpression.csv'
str21 = '/Fluarix-Female-7.0-0.0--GeneExpression.csv'
str31 = '/Fluzone-Female-28.0-0.0--GeneExpression.csv'
str41 = '/Fluzone-Female-7.0-0.0--GeneExpression.csv'

db11 = pd.read_csv(path+str11)
db21 = pd.read_csv(path+str21)
db31 = pd.read_csv(path+str31)
db41 = pd.read_csv(path+str41)
dball1 = pd.concat([db11, db21, db31, db41])


str12 = '/Fluvirin-Male-7.0-0.0--GeneExpression.csv'
str22 = '/Fluarix-Male-7.0-0.0--GeneExpression.csv'
str32 = '/Fluzone-Male-28.0-0.0--GeneExpression.csv'
str42 = '/Fluzone-Male-7.0-0.0--GeneExpression.csv'

db12 = pd.read_csv(path+str12)
db22 = pd.read_csv(path+str22)
db32 = pd.read_csv(path+str32)
db42 = pd.read_csv(path+str42)
dball22 = pd.concat([db12, db22, db32, db42])




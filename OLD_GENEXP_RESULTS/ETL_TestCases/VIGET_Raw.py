# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 06:59:12 2025

@author: Huffmaar
"""
import numpy as np

import pandas as pd
import pymysql
import json
from collections import defaultdict

def read_VIGET(VIGET):
    try: 
        dfVIGET = file_reader(VIGET)
    except:
        print("File could not be found")
        return  0
    return dfVIGET


def load_VIGET(VIGET):
    try:
        VIGET = read_VIGET(VIGET)
    except:
        print("File could not be loaded.")
    template = SEA_INIT()
    STUDY = template[0]
    
    "All files are loaded."
    return 0
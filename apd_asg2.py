# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 00:14:20 2022

@author: User
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st

def data_(filename):
    """
    The function data_ takes filename as argument
    read the data file into argument read the dataframes
    and returns datas,d_t
    
    """
    data = pd.read_excel(filename)
    data = pd.DataFrame(data)
    print(data.info)
    # Statistical function returnns description of data on the data frame
    print(data.describe())
    # drop null values in rows as part of data cleaning
    data["Series Name"] = data["Series Name"].dropna(axis=0)
    # drop unwanted names in rows as part of data cleaning
    data = data.drop([684,685,686,687,688])
    # drop columns as part of data cleaning
    d = data.drop(columns=["Series Name","Series Code","Country Code"])
    # transposing the dataframe
    d_t = np.transpose(d)
    datas = data.drop(columns=["Series Code","Country Code"])
    # Statistical function returnns description of data on the data frame
    print(datas.describe())
    # Statistical function returnns description of data on the data frame
    print(d_t.describe())
    return datas,d_t
# calling the function dat_ and assinging in to two variables data and d_transpose
data,d_transpose = data_("D:\\a\\new_data.xlsx")
print(data)
print(d_transpose)
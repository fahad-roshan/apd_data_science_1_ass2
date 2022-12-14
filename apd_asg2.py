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
def co2(data,d_transpose):
    """
    the function co2 takes data and d_transpose as 
    argument 

    """
    # grouping the datas of Series Name by groupby() function
    dt1 = data.groupby(["Series Name"])
    # getting a specific group by get_group() function
    data1 = dt1.get_group("CO2 emissions (kt)")
    print(data1.columns)
    # CO2 emissions (kt) bar graph
    width = 0.17
    plt.figure(figsize=(30,17))
    plt.title("CO2 emissions (kt)",size=40)
    tm = np.arange(len(data1["Country Name"]))
    plt.bar(tm-0.2,data1["1990 [YR1990]"],width,label="1990",align="edge")
    plt.bar(tm-0.1,data1["2000 [YR2000]"],width,label="2000",align="edge")
    plt.bar(tm+0.0,data1["2012 [YR2012]"],width,label="2012",align="edge")
    plt.bar(tm+0.1,data1["2013 [YR2013]"],width,label="2013",align="edge")
    plt.bar(tm+0.2,data1["2014 [YR2014]"],width,label="2014",align="edge")
    plt.bar(tm+0.3,data1["2015 [YR2015]"],width,label="2015",align="edge")
    plt.xticks(tm,data1["Country Name"],fontsize=22)
    plt.xlabel("Countries",size=20)
    plt.legend(prop={"size":25})
    plt.show()
    print(data1)
    d_transpose = data1.drop(columns=["Country Name","Series Name"])
    # slicing the years using loc
    d_transpose = d_transpose.loc[:,"2000 [YR2000]":"2019 [YR2019]"]
    d_transpose1 = np.transpose(d_transpose)
    print(d_transpose1)
    # renaming the column number with thier country name 
    d_transpose1= d_transpose1.rename(columns={270:"Angola",271:"Benin",272:"Albania",273:"Ecuador",274:"India",275:"Pakistan",276:"Serbia",277:"Saudi Arabia",278:"Russia"})
    india["CO2 emissions (kt)"]= d_transpose1["India"]
    benin["CO2 emissions (kt)"]= d_transpose1["Benin"]
    angola["CO2 emissions (kt)"]= d_transpose1["Angola"]

def access_electricity(data,d_transpose):
    """
    the function  access_electricty takes data and d_transpose as 
    argument 

    """
    # grouping the datas of Series Name by groupby() function
    dt1 = data.groupby(["Series Name"])
    # getting a specific group by get_group() function
    data1 = dt1.get_group("Access to electricity (% of population)")
    d_transpose = data1.drop(columns=["Country Name","Series Name"])
    print(d_transpose)
    # slicing the years using loc
    d_transpose = d_transpose.loc[:,"2000 [YR2000]":"2019 [YR2019]"]
    d_transpose1 = np.transpose(d_transpose)
    print(d_transpose1)
    # renaming the column number with thier country name 
    d_transpose1= d_transpose1.rename(columns={117:"Angola",118:"Benin",119:"Albania",120:"Ecuador",121:"India",122:"Pakistan",123:"Serbia",124:"Saudi Arabia",125:"Russia"})
    # Access to electricity (% of population) line plot 
    plt.figure(figsize=(34,19))
    plt.title("Access to electricity (% of population)",fontsize=(29))
    plt.plot(d_transpose1.index,d_transpose1["Angola"],"--",label="Angola")
    plt.plot(d_transpose1.index,d_transpose1["Benin"],"--",label="Benin")
    plt.plot(d_transpose1.index,d_transpose1["Albania"],"--",label="Albania")
    plt.plot(d_transpose1.index,d_transpose1["Ecuador"],"--",label="Ecuador")
    plt.plot(d_transpose1.index,d_transpose1["India"],"--",label="India")
    plt.plot(d_transpose1.index,d_transpose1["Pakistan"],"--",label="Pakistan")
    plt.plot(d_transpose1.index,d_transpose1["Serbia"],"--",label="Serbia")
    plt.plot(d_transpose1.index,d_transpose1["Saudi Arabia"],"-.",label="Saudi Arabia")
    plt.plot(d_transpose1.index,d_transpose1["Russia"],":",label="Russia")
    plt.xticks(d_transpose1.index,fontsize=21)
    plt.xlabel("Years",fontsize=30)
    plt.legend(fontsize=28)
    plt.show()
    india["Access to electricity (% of population)"]= d_transpose1["India"]
    benin["Access to electricity (% of population)"]= d_transpose1["Benin"]
    angola["Access to electricity (% of population)"]= d_transpose1["Angola"]

def electric_cons(data,d_transpose):
    """
    the function electric_cons takes data and d_transpose as 
    argument 

    """
    # grouping the datas of Series Name by groupby() function
    dt1 = data.groupby(["Series Name"])
    # getting a specific group by get_group() function
    data1 = dt1.get_group("Electric power consumption (kWh per capita)")
    d_transpose = data1.drop(columns=["Country Name","Series Name"])
    # slicing the years using loc
    d_transpose = d_transpose.loc[:,"2000 [YR2000]":"2019 [YR2019]"]
    d_transpose1 = np.transpose(d_transpose)
    print(d_transpose1)
    d_transpose1= d_transpose1.rename(columns={216:"Angola",217:"Benin",218:"Albania",219:"Ecuador",220:"India",221:"Pakistan",222:"Serbia",223:"Saudi Arabia",224:"Russia"})
    india["Electric power consumption (kWh per capita)"]= d_transpose1["India"]
    benin["Electric power consumption (kWh per capita)"]= d_transpose1["Benin"]
    angola["Electric power consumption (kWh per capita)"]= d_transpose1["Angola"]
    
def renew_energy(data,d_transpose):
    """
    the function renew_energy takes data and d_transpose as 
    argument 

    """
    # grouping the datas of Series Name by groupby() function
    dt1 = data.groupby(["Series Name"])
    # getting a specific group by get_group() function
    data1 = dt1.get_group("Renewable energy consumption (% of total final energy consumption)")
    d_transpose = data1.drop(columns=["Country Name","Series Name"])
    # slicing the years using loc
    d_transpose = d_transpose.loc[:,"2000 [YR2000]":"2019 [YR2019]"]
    d_transpose1 = np.transpose(d_transpose)
    print(d_transpose1)
    # renaming the column number with thier country name 
    d_transpose1= d_transpose1.rename(columns={198:"Angola",199:"Benin",200:"Albania",201:"Ecuador",202:"India",203:"Pakistan",204:"Serbia",205:"Saudi Arabia",206:"Russia"})
    # Renewable energy consumption (% of total final energy consumption) line plot
    plt.figure(figsize=(34,19))
    plt.title("Renewable energy consumption (% of total final energy consumption)",fontsize=(29))
    plt.plot(d_transpose1.index,d_transpose1["Angola"],"--",label="Angola")
    plt.plot(d_transpose1.index,d_transpose1["Benin"],"--",label="Benin")
    plt.plot(d_transpose1.index,d_transpose1["Albania"],"--",label="Albania")
    plt.plot(d_transpose1.index,d_transpose1["Ecuador"],"--",label="Ecuador")
    plt.plot(d_transpose1.index,d_transpose1["India"],"--",label="India")
    plt.plot(d_transpose1.index,d_transpose1["Pakistan"],"--",label="Pakistan")
    plt.plot(d_transpose1.index,d_transpose1["Serbia"],"--",label="Serbia")
    plt.plot(d_transpose1.index,d_transpose1["Saudi Arabia"],"-.",label="Saudi Arabia")
    plt.plot(d_transpose1.index,d_transpose1["Russia"],":",label="Russia")
    plt.xticks(d_transpose1.index,fontsize=21)
    plt.xlabel("Years",fontsize=30)
    plt.legend(fontsize=28)
    plt.show()
    india["Renewable energy consumption"]= d_transpose1["India"]
    benin["Renewable energy consumption"]= d_transpose1["Benin"]
    angola["Renewable energy consumption"]= d_transpose1["Angola"]
    
def urban_population(data,d_transpose):
    """
    the function urban_population takes data and d_transpose as 
    argument 

    """
    # grouping the datas of Series Name by groupby() function
    dt1 = data.groupby(["Series Name"])
    # getting a specific group by get_group() function
    data1 = dt1.get_group("Urban population (% of total population)")
    print(data1)
    d_transpose = data1.drop(columns=["Country Name","Series Name"])
    print(d_transpose)
    # slicing the years using loc
    d_transpose = d_transpose.loc[:,"2000 [YR2000]":"2019 [YR2019]"]
    d_transpose1 = np.transpose(d_transpose)
    print(d_transpose1)
    # renaming the column number with thier country name 
    d_transpose1= d_transpose1.rename(columns={594:"Angola",595:"Benin",596:"Albania",597:"Ecuador",598:"India",599:"Pakistan",600:"Serbia",601:"Saudi Arabia",602:"Russia"})
    india["Urban population (% of total population)"]= d_transpose1["India"]
    benin["Urban population (% of total population)"]= d_transpose1["Benin"]
    angola["Urban population (% of total population)"]= d_transpose1["Angola"]
    
def population_total(data,d_transpose):
    """
    the function population_total takes data and d_transpose as 
    argument 

    """
    # grouping the datas of Series Name by groupby() function
    dt1 = data.groupby(["Series Name"])
    # getting a specific group by get_group() function
    data1 = dt1.get_group("Population, total")
    print(data1)
    #Population, total bargraph
    width = 0.17
    plt.figure(figsize=(30,17))
    plt.title("Population, total",size=40)
    tm = np.arange(len(data1["Country Name"]))
    plt.bar(tm-0.2,data1["1990 [YR1990]"],width,label="1990",align="edge",color="red")
    plt.bar(tm-0.1,data1["2000 [YR2000]"],width,label="2000",align="edge",color="green")
    plt.bar(tm+0.0,data1["2012 [YR2012]"],width,label="2012",align="edge",color="blue")
    plt.bar(tm+0.1,data1["2013 [YR2013]"],width,label="2013",align="edge",color="pink")
    plt.bar(tm+0.2,data1["2014 [YR2014]"],width,label="2014",align="edge",color="yellow")
    plt.bar(tm+0.3,data1["2015 [YR2015]"],width,label="2015",align="edge",color="orange")
    plt.xticks(tm,data1["Country Name"],fontsize=22)
    plt.xlabel("Countries",size=20)
    plt.legend(prop={"size":25})
    plt.show()
    d_transpose = data1.drop(columns=["Country Name","Series Name"])
    print(d_transpose)
    # slicing the years using loc
    d_transpose = d_transpose.loc[:,"2000 [YR2000]":"2019 [YR2019]"]
    d_transpose1 = np.transpose(d_transpose)
    print(d_transpose1)
    # renaming the column number with thier country name 
    d_transpose1= d_transpose1.rename(columns={567:"Angola",568:"Benin",569:"Albania",570:"Ecuador",571:"India",572:"Pakistan",573:"Serbia",574:"Saudi Arabia",575:"Russia"})
    print(d_transpose1)
    india["Population, total"]= d_transpose1["India"]
    benin["Population, total"]= d_transpose1["Benin"]
    angola["Population, total"]= d_transpose1["Angola"]
def corr_india(data_):
    """
    the function  corr_india takes data_ argument 

    """
    plt.figure(figsize=(15,11))
    plt.title("india",size=30)
    # correlating the data using corr()
    cor = data_.corr()
    # printing the shape of cor
    print(cor.shape)
    # plotting the heatmap
    sns.heatmap(data=cor,annot=True,cmap="coolwarm")
    plt.show()
def corr_benin(data_):
    """
    the function corr_benin takes data_ as argument 

    """
    plt.figure(figsize=(15,11))
    plt.title("Benin",size=30)
    # correlating the data_ using corr() function
    cor = data_.corr()
    # plotting the heatmap
    sns.heatmap(data=cor,annot=True,cmap="inferno")
    plt.show()
def corr_angola(data_):
    """
    the function corr_angola takes data_ as argument

    """
    plt.figure(figsize=(15,11))
    plt.title("Angola",size=30)
    # correlating the data_ using corr() function
    cor = data_.corr()
    # plotting the heatmap
    sns.heatmap(data=cor,annot=True,cmap="plasma")
    plt.show()    
# calling the function dat_ and assinging in to two variables data and d_transpose
data,d_transpose = data_("D:\\a\\new_data.xlsx")
print(data)
print(d_transpose)
# creating a dataframe india
india = pd.DataFrame()
# creating a dataframe benin
benin = pd.DataFrame()
# creating a dataframe angola
angola = pd.DataFrame()
#calling function co2
co2(data,d_transpose)
#calling function access_electricity
access_electricity(data,d_transpose)  
#calling function electric_cons
electric_cons(data,d_transpose) 
#calling function renew_energy 
renew_energy(data,d_transpose)
#calling function urban_population 
urban_population(data,d_transpose)  
#calling function population_total
population_total(data,d_transpose)
#calling function corr_india 
corr_india(india)
#calling function corr_benin
corr_benin(benin)    
#calling function corr_angola
corr_angola(angola)
# using scipy.stats to check pearson relation between dataframe
print(st.pearsonr(india["Population, total"],india["CO2 emissions (kt)"]))
print(st.pearsonr(angola["Access to electricity (% of population)"],angola["CO2 emissions (kt)"]))
print(st.pearsonr(benin["Renewable energy consumption"],benin["CO2 emissions (kt)"]))
print(st.pearsonr(india["Population, total"],benin["CO2 emissions (kt)"]))
print(st.pearsonr(benin["Renewable energy consumption"],benin["Urban population (% of total population)"]))
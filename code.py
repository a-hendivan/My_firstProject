# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:58:56 2022

@author: Andivan Ahmad
"""

# Modules     
import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
%matplotlib inline 
sns.set(color_codes=True)

#Data frame 

df = pd.read_csv('Death Cause Reason by Country.csv',header =0)
print(df)

df.head(5)

# Check Data Types 
df.dtypes


# Dropping irrelevant columns
df = df.drop([‘Engine Fuel Type’, ‘Market Category’, ‘Vehicle Style’, ‘Popularity’, ‘Number of Doors’, ‘Vehicle Size’], axis=1)
df.head(5)



# Total number of rows and columns
df.shape
# Out[53]: (191, 33)


# Rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

# Used to count the number of rows before removing the data
df.count() 


# Dropping the duplicates 
df = df.drop_duplicates()
df.head(5)

df.count()


# Finding the null values.
print(df.isnull().sum())


sns.boxplot(x=df['Covid-19 Deaths'])

sns.boxplot(x=df['Nutritional deficiencies'])


print(df['Country Name'])

sum_Stats = df[:].describe()

sum_Stats = df.agg(["min", "max", "median","mean", "skew"] )


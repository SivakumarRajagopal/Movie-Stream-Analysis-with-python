### Best Streaming Service Analysis

# import libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('moviestreams.csv')
# print(df.head())

cols = df.columns.tolist()
# print(cols)

df.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True)
cols = df.columns.to_list()
#  print(cols)

###Check for Missing Values

#  print(df.isna().sum())

# print(df['Age'])


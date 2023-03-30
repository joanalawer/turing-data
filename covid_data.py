# Python Data Analysis Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

# Overview of Dataset
covid_df = pd.read_csv("covid_data.csv")
print(covid_df.head(), '\n')

print(covid_df.shape, '\n')

print(covid_df.info(), '\n')

print(covid_df.describe(), '\n')

# Numerical analysis and visualisation
#Analyse on a column


# Categorical analyses and visualisation
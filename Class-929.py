# file for class 9/29

import pandas as pd

small = pd.read_csv("wdi_small_tidy_2015.csv")

small.columns

subet_small = small[["Mortality rate, infant (per 1,000 live births)", "GDP per capita (constant 2010 US$)", "Country Name"]]

print(subet_small)
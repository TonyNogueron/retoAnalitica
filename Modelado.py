import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sn
import statsmodels.api as sm 

tabla =  pd.read_csv("data.csv", low_memory=False) #Created data frame from our dataset
tabla = tabla[["year","transmission_type", "fuel_type", "co_emissions", "co2","engine_capacity","noise_level"]] #Filters dataframe by given columns
tabla.dropna(inplace=True) #Deletes rows when it is empty

#print(tabla.head(10)) #prints first 10 rows

tabla["transmission_type"].replace({"Manual": 0, "Automatic": 1}, inplace=True)
tabla["fuel_type"].replace({"Diesel": 0, "Petrol": 1, "LPG": 2, "CNG": 3, "Petrol Hybrid": 4, "Diesel Electric": 5, "Electricity": 6, "Electricity/Diesel":7,"Electricity/Petrol":8, "LPG / Petrol": 9, "Petrol / E85":10, "Petrol / E85 (Flex Fuel)":11, "Petrol Electric": 12}, inplace=True)
#holi te amo
#print(tabla.head(10)) #prints first 10 rows
#print(tabla.dtypes)

x = tabla[["year","transmission_type","engine_capacity","noise_level"]]

y = tabla["co2"]
x = sm.add_constant(x)
modelo = sm.OLS(y, x).fit()

predictions = modelo.predict(x)  # Con el modelo, se calculan las Y´s
#print(predictions)
print("==============================================================================")

print(modelo.summary())
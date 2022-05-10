import pandas as pd
import numpy as np

tabla =  pd.read_csv("data.csv", low_memory=False) #Created data frame from our dataset
tabla = tabla[["year","manufacturer","transmission_type", "fuel_type", "co_emissions", "co2","engine_capacity","noise_level"]] #Filters dataframe by given columns
tabla.dropna(inplace=True) #Deletes rows when it is empty
print(tabla.head(10)) #prints first 10 rows 
print(tabla.dtypes) #Prints the data type of our data frame columns
print(tabla.describe()) #Prints statistics from our dataframe

for column in tabla:
    try:
        print("Rango de "+str(column)+":" , tabla[column].max()-tabla[column].min())
    except:
        print("Rango de "+str(column)+": No existe rango para este tipo de dato")
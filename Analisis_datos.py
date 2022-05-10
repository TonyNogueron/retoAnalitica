import pandas as pd
import numpy as np

tabla =  pd.read_csv("data.csv")
tabla = tabla[["manufacturer","transmission_type", "fuel_type", "co_emissions"]]
tabla.dropna(inplace=True)
print(tabla)
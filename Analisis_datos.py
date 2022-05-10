import pandas as pd
import numpy as np


tabla = pd.read_csv("./data.csv", low_memory=False)
carTable = tabla[["manufacturer","transmission_type", "fuel_type", "co_emissions"]]
carTable.replace("", np.nan, inplace=True)
carTable = carTable.dropna(inplace=True)
#print(carTable)


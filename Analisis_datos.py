import pandas as pd
tabla = pd.read_csv("./data.csv", low_memory=False)
carTable = tabla[["manufacturer","transmission_type", "fuel_type", "co_emissions"]]
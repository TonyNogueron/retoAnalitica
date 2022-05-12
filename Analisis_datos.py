import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

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

fig, ax = plt.subplots(figsize=(6,4))

tabla_CO2 = tabla["co2"]
tabla_CO = tabla["co_emissions"]

ax.hist(tabla_CO2,ec='black')

plt.xlabel('Emisiones de CO2')
plt.ylabel('Frecuencia')
plt.show()

fig, ax = plt.subplots(figsize=(6,4), sharey=True )

sns.boxplot(x = tabla["co_emissions"])

plt.show()

#Creamos un heatmap con otros datos porque creemos que no se ajusta a nuestra base de datos, no son datos reales

datos = {'ciudades': np.tile (['Londres', 'Glasgow', 'Westminster', 'Birmingham', 'Cambridge'], 5),
        'anio': np.repeat ([2000, 2001, 2002, 2003, 2004], 5),
        'ventas': np.random.randint (100, 500, size = 25)
        }

df = pd.DataFrame(datos, columns = ['ciudades', 'anio', 'ventas'])
df = df.pivot ('ciudades', 'anio', 'ventas')

sns.heatmap(df, linewidths = .5, annot = True, fmt="d")

plt.show()

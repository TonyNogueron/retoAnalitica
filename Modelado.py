import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm 
from sklearn.model_selection import train_test_split

tabla =  pd.read_csv("data.csv", low_memory=False) #Created data frame from our dataset
tabla = tabla[["year","transmission_type", "fuel_type", "co_emissions", "co2","engine_capacity","noise_level"]] #Filters dataframe by given columns
tabla.dropna(inplace=True) #Deletes rows when it is empty

tabla["transmission_type"].replace({"Manual": 0, "Automatic": 1}, inplace=True)
tabla["fuel_type"].replace({"Diesel": 0, "Petrol": 1, "LPG": 2, "CNG": 3, "Petrol Hybrid": 4, "Diesel Electric": 5, "Electricity": 6, "Electricity/Diesel":7,"Electricity/Petrol":8, "LPG / Petrol": 9, "Petrol / E85":10, "Petrol / E85 (Flex Fuel)":11, "Petrol Electric": 12}, inplace=True)

train, test = train_test_split(tabla, test_size=0.2) #Split our data in 80 / 20 ratio for training and testing of our model

x = train[["year","transmission_type","engine_capacity","noise_level"]]

y = train["co2"]
x = sm.add_constant(x)
modelo = sm.OLS(y, x).fit()

predictions = modelo.predict(x)  # Con el modelo, se calculan las Y´s
print("==============================================================================")
print(modelo.summary())

tabla2 = test.assign(calculated_co2 = lambda x: 8849.3913 -4.4589 * x.year + 11.2728 * x.transmission_type + 0.0469 * x.engine_capacity + 2.5492 * x.noise_level)
tabla2 = tabla2[["year","transmission_type","engine_capacity","noise_level", "co2", "calculated_co2"]]
tabla2 = tabla2.assign(error = lambda x: abs(((x.co2 - x.calculated_co2)/x.co2)))
print("==============================================================================")
print(tabla2.head())
print("==============================================================================")
print("El error promedio es: ", np.mean(tabla2["error"]))


tabla2 = tabla2.head(20)
y1 = tabla2["co2"]
y2 = tabla2["calculated_co2"]
independiente = np.arange(len(y1))

plt.plot(independiente,y1, c="b", label = "Real")
plt.plot(independiente,y2, c="r", label = "Calculado")
plt.xlabel("Valores en X")
plt.ylabel("Valores en Y")
plt.title("Valor real vs Calculado")
plt.legend(loc='upper left');
plt.show()

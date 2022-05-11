- ¿Qué datos hay que seleccionar? Por qué.
	
	Vamos a seleccionar las columnas de:
	- year
	- manufacturer
	- transmission_type
	- fuel_type
	- co_emissions
	- co2  
	- engine_capacity 
	- noise_level

	Por que son las columnas que queremos analizar para después crear
	nuestro modelo de regresión que describa las emisiones de co2. Esto 
	previamente planeado.	

- ¿Hay que eliminar o reemplazar valores en blanco? Sí / No / Por qué.
	
	Si, es necesario eliminar aquellas filas donde alguna columna de 
	interés tenga alguna celda vacía, esto se hace para el filtrado de
	los datos, y mejoramiento de la efectividad del modelo.

	Esto se logra con la función de pandas:
		dataFrame.dropna(inplace=True)	

- ¿Es posible agregar más datos? Sí / No / Por qué.

	Si, es posible añadir más datos a nuestro data frame, en nuestro caso
	no consideramos que sea necesario hacerlo, ya que nuestra base de datos
	es bastante completa.

- ¿Hay qué integrar o fusionar datos de varias fuentes? Sí / No / Por qué.

	Para nuestro análisis no, la base de datos ya filtrada tiene un total
	de 48,849 filas y consideramos que son suficientes para la creación
	de nuestro modelo y que puede darnos buena información.

- ¿Es necesario ordenar los datos para el análisis? Sí / No / Por qué.
	
	No, no es necesario ordenar los datos para el tipo de análisis
	que queremos realizar. Como queremos averiguar la correlación 
	de los regresores, no es fundamental tener los datos ordenados.

- ¿Tengo que hacer conjuntos de datos para entrenamiento y prueba? Sí / No / Por qué.

	Si, para el entrenamiento de nuestro modelo, podríamos entrenar
	con el 80% de los datos, dejando un restante 20% para corroborar
	el modelo y darnos una idea de su precisión.

	También podemos hacer varios modelos con distintas combinaciones
	de regresores  y sería necesario hacer conjuntos de datos.

- ¿Qué ajustes se tuvieron que hacer a los datos (agregar, integrar, modificar registros (filas), cambiar atributos (columnas)?

	A nuestra base de datos, le quitamos aquellas filas con alguna
	celda vacía y eliminamos aquellas columnas que no consideramos
	necesarias para nuestro análisis. Además tendremos que agregar
	una columna para las variables cualitativas que convertiremos 
	a valores numéricos.

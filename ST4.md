1. ¿Cuántos intentos o corridas realizaste para obtener los resultados sin errores? Porqué
   Realizamos cerca de 5 intentos, aquí los problemas que se presentaron fueron que no se habían tomado
   los regresores necesarios y que no se acotaron correctamente.
2. ¿Cómo los resolviste los problemas que se presentaron?
  Los problemas que tuvimos fueron por seleccionar mal los rangos de la información que cargábamos al modelo,
  entonces solo fue poner más atención a como se acotaban los datos. Al igual se limpiaron los regresores que se
  iban a utilizar para el análisis.
3. ¿Qué resultados arrojó el análisis? Incluye imagen de cada resultado y explica cada uno de los resultados:
  - Estadística descriptiva
           year                transmission_type  engine_capacity   noise_level     fuel_type
    count  35396.000000        35396.00000        35396.000000      35396.000000    35396.000000
    mean    2007.286191            0.40352        2179.205616       72.141523       0.612442
    std        3.816540            0.49061        889.965819        1.817418        0.487200
    min     2000.000000            0.00000        599.000000        0.200000        0.000000
    25%     2004.000000            0.00000        1598.000000       71.000000       0.000000
    50%     2008.000000            0.00000        1985.000000       72.000000       1.000000
    75%     2010.000000            1.00000        2402.000000       73.300000       1.000000
    max     2013.000000            1.00000        8285.000000       83.000000       1.000000
  - Coeficientes de regresión
      y = 7479.5115 + -3.7683*x<sub>1</sub> + 9.3768*x<sub>2</sub> + 0.0463*x<sub>3</sub> + 2.1364*x<sub>4</sub> + 25.7168*x<sub>5</sub>
  - Valores actuales y de predicción
      190 - 197.90
      149 - 167.55
      184 - 167.11
      211 - 217.92
      259 - 251.21
  - Coeficiente de determinación r2
      0.784
  - Gráficas
      Ver carpeta de recursos gráficos
4. ¿Cuáles son tus conclusiones de la modelación?
    Al final tuvimos un modelo que al compararlo con los datos de prueba nos dan valores
    muy cercanos, tenemos un error promedio de 10%. Nuestro modelo sugiere que sí hay una 
    correlación bastante fuerte entre los regresores seleccionados y la variable dependiente
    que es la emisión de CO2.

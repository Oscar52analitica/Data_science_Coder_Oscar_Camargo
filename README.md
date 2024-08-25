# Data_science_Coder_Oscar_Camargo
Repositorio de curso 

# Pre entrega n°1 - Oscar Orlando Camrgo Vargas

1.   Elemento de la lista
2.   Elemento de la lista

## Análisis de impacto del precio de fabricaicón de diferentes modelos de autos según su año de fabricación: Estudio de Datos

## ABSTRACT

### Resumen:
#### Este proyecto se centra en el análisis  de los datos el csv Cars_Database, examinando diversas características como:
- Precio.
- Año de Fabricación.
- Tamaño de Motor.
- Consumo por millas.
- Millaje.
- Gasto de combustible.

 ###  Hipótesis de interés:
#### Basándonos en un análisis previo del dataset, planteamos las siguientes hipótesis:
- Relación entre año y precio: ¿Cómo afecta el año de fabricación al precio de los automóviles? Hipótesis: Los autos más nuevos tienden a ser más caros.
- Impacto de la transmisión en el precio: ¿Es la transmisión automática más cara que la manual?
- Influencia del tipo de combustible: ¿Los autos que utilizan combustible más eficiente tienen un precio más alto?
- Costo por milla vs. Años de circulación: ¿Los autos que han circulado más años tienen un costo por milla más bajo?
- Se iniciara conociendo valores estadisticos que permiten conocer medidas para generar graficos y analisis que generen la respuesta de la hipotesis y las preguntas de interes planteadas
  ### Objetivos:

- Validar las hipótesis formuladas a través de análisis estadísticos y representaciones gráficas.
- Descubrir patrones y tendencias dentro del conjunto de datos.
- Crear un modelo predictivo para calcular la relación entre el año de fabriación de un auto y su precio.

### Impacto:
#### Los resultados de este estudio permitirán:

- Determinar los factores que influyen en el precio de un vehiculo.
- Crear informes para la toma de desiciones a la hora de la compra de un vehiculo si es mas combeniente uno sobre otro analisando diferentes variables.
- Construir un modelo que permita comparar diferentes variables a una persona a fin de simplificar conceptos y predecir cual vehiculo es mas combeniente para difernetes presupuestos.

- Resultados de la matriz

precio y año : 0.52

precio y engeniesize: 0.63

precio y impuestos: 0.27

año y consumo de combustible: -0.75

año y millas: -0.75

millage y cosnumo por galon: 0.94

Con los resultados se puede inferir que el precio del auto es mayor si el año del vehiculo es mas reciente al igual que su precio aumenta segun el tamaño del motor y sus impuestos aumentan segun el precio del auto,  en cuanto a consumos si el modelo es resiente el consumo es menor entre mas nuevo se el modelo menos consumo tiene, y se detecto que entre mas millas tenga el vehiculo mayor es el consumo por galon, son datos que son encontrados gracias a la matriz de correlacion


**Resultado**

Relación Directa:  los gráficos muestran que los autos más nuevos tienden a tener precios más altos, esto confirmaría la hipótesis de que el año de fabricación es un factor importante en la determinación del precio.

Variabilidad por Marca: Al segmentar por marca, se sabe  que algunas marcas retienen mejor su valor con el tiempo que otras.

Diferencias de Precio: La transmisión automática muestra precios significativamente más altos, puede concluir que los autos automáticos son percibidos como más valiosos o que su fabricación es más costosa.

Distribución de Precios: El boxplot permite ver QUE  hay mayor variabilidad en los precios de los autos automáticos en comparación con los manuales.

Influencia del Tamaño del Motor: los gráficos muestran que los autos con motores más grandes tienden a ser más caros, esto confirmaría que el tamaño del motor es un factor importante en el precio del vehículo.

Impacto del Tipo de Combustible: los autos que usan combustible más caro (como diésel) también tienen precios más altos, lo que podría indicar una relación entre el tipo de combustible y el valor percibido del vehículo.

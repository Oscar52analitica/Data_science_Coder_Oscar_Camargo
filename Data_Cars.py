import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# Se creó la ruta del archivo 
Ruta = 'C:/Users/oscar/OneDrive/Escritorio/CODER/Data Science I Fundamentos para la Ciencia de Datos/Data_science_Coder_Oscar_Camargo/BASES_DE_DATOS'
Datos_de_autos = Ruta + "/Cars_database.xlsx"

#Creación del Dataframe 

df_cars = pd.read_excel(Datos_de_autos)

# Información general del Data frame

print(df_cars.info())
print(df_cars.describe())
print(df_cars.head(10))
print(df_cars.tail(10))
print(df_cars.columns)

print(df_cars['price'].describe())

#     Calculos de la columna Precio:

''' Información relevante para la columna de precio '''


media_price = df_cars['price'].mean()
print(f'La media es: {media_price}')

#Valor minimo
min_price=df_cars['price'].min()
print(f'el minimo es : {min_price}')

#Valor maximo
max_price=df_cars['price'].max()
print(f'el maximo es: {max_price}')

#Desviacion Estandandar
desest=df_cars['price'].std()
print(f'la desviasion estadar es :{desest}')


# algunos filtros para conocer aspectos relevantes del df_cars


#Promedio de precios por marca
precio_por_marca= df_cars.groupby('Make')['price'].mean().sort_values(ascending=False)
print(f'El precio promedio por marca es :{precio_por_marca}')

# cantidad de autos por marca 

Cantidad_de_autos_por_marca= df_cars['Make'].value_counts()
print(f' la Cantidad_de_autos_por_marca :{Cantidad_de_autos_por_marca}')

# cantidad de autos =

total_autos= len(df_cars)
print(f"La cantidad total de autos es: {total_autos}")

#Precio Maximo y minimo por marca

precio_max_min_por_marca = df_cars.groupby('Make')['price'].agg(['max', 'min'])
print("Precio máximo y mínimo por marca:")
print(precio_max_min_por_marca)


'''
Algunas graficas propuestas 
'''
# Visualización de precios por marca

plt.figure(figsize=(10, 6))
precio_por_marca.plot(kind='bar', color='skyblue')
plt.title('Precio Promedio por Marca')
plt.xlabel('Marca')
plt.ylabel('Precio Promedio')
plt.xticks(rotation=45)
plt.show()


plt.clf()
# Distribución de precios según la transmisión (automática o manual)

plt.figure(figsize=(8, 6))
sns.boxplot(x='transmission', y='price', data=df_cars, palette='Set2')
plt.title('Distribución de Precios según Transmisión')
plt.xlabel('Transmisión')
plt.ylabel('Precio')
plt.show()

plt.clf()

# SCATTER PLOT

plt.figure(figsize=(10, 6))
sns.scatterplot(x='year', y='price', data=df_cars, hue='Make', palette='Set2', alpha=0.7)
plt.title('Relación entre Año y Precio de los Autos por Marca')
plt.xlabel('Año')
plt.ylabel('Precio')
plt.grid(True)
plt.show()
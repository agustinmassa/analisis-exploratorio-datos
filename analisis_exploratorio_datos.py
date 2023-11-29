"""
ANALISIS EXPLORATORIO DE LOS DATOS DEL DATASET diamonds.csv

1)Cargar el archivo como una DataFrame de pandas, asignado a una variable de nombre df 
¿Hay que importar algún paquete para hacerlo?

2)¿Cuántas filas tiene el dataset? 
¿Cuáles son las unidades de este conjunto de datos? En otras palabras, ¿de qué habla este dataset?

3)¿Cuántas columnas tiene el dataset? ¿Corresponden todas a atributos de las unidades?

4)Describir a qué tipo pertenece cada una de las variables

5)Hay datos faltantes. ¿Cuántos y para qué variables?

6)¿Cuántos tipos de cortes (cut) existen? ¿Cuántos diamantes de cada tipo hay en el dataset?

7)¿Cuántos tipos de claridad (clarity) existen? ¿Cuántos diamantes de cada tipo hay en el dataset?

8)¿Cómo depende el valor medio del precio del tipo de corte?

9)Realizar un gráfico que permita ver esto.

10)Calcular el coeficiente de correlación entre el precio y todas los demás atributos. 
¿Qué atributo presenta un coeficiente mayor con el precio? Si no conociéramos el precio de los diamantes, 
¿qué atributo permitiría obtener mayor información sobre el precio?

11)Graficar la matriz de correlación entre todos los parámetros y colorearla. 
Identificar grupos de variables que tienen fuerte correlación o cualquier otro patrón.
"""
#1

import pandas as pd
import matplotlib.pyplot as plt

ARCHIVO = 'F:\Agu\Diplomatura.UNSAM\Practica\Analisis Exploratorio de datos\diamonds.csv'
df = pd.read_csv(ARCHIVO)

#2

#num_filas = df.shape[0]
num_filas2 = format(len(df)) #Otra opción
print('Número de filas en el dataset:', num_filas2)

primeras_filas=df.head()
print('Primeras filas del dataset:\n', primeras_filas)

#3

#num_columnas = df.shape[1]
num_columnas2 = format(len(df.columns)) #Otra opción
print('Número de columnas en el dataset:', num_columnas2)

columnas = df.columns
print('Todas estas corresponden a atributos de los diamantes', columnas)

#4

variables = df.info()
print(variables)
print('Como se puede observar tiene 6 flotantes, 1 entero y 3 cadenas de texto')

tipos_de_varibles = df.dtypes #Otra forma
print(tipos_de_varibles)

#5

datos_faltantes = df.isnull().sum()
print(datos_faltantes)
print('Como se puede ver no hay datos faltantes, esto tambien ya se pudo ver en el inciso 4 cuando hacemos el info')

#6

tipos_de_corte = df['cut'].unique()
print('Tipos de corte de diamantes:', tipos_de_corte)

cantidad_diamantes_por_corte = df['cut'].value_counts()
print('Cantidad de diamantes por tipo de corte:')
print(cantidad_diamantes_por_corte)

#7

tipos_de_claridad = df['clarity'].unique()
print('Tipos de claridad de diamantes:', tipos_de_claridad)

cantidad_diamantes_por_claridad = df['clarity'].value_counts()
print('Cantidad de diamantes por tipo de claridad:')
print(cantidad_diamantes_por_claridad)

#8

valor_medio_por_corte = df.groupby('cut')['price'].mean()
#valor_medio_por_corte = df.groupby(by='cut').price.mean().round(2) #Otra forma redondeando a dos cifras
print('Valor medio del precio por tipo de corte:') 
print(valor_medio_por_corte)

#9

#Opcion 1 - diagrama de barras 
df.groupby(by='cut').price.mean().plot(kind='bar',
                                       ylabel='Precio medio [USD]',
                                        title='Cambio del precio medio con el tipo de corte')

#Otra opcion del mismo grafico 
#valor_medio_por_corte = df.groupby('cut')['price'].mean()
#plt.bar(valor_medio_por_corte.index, valor_medio_por_corte)
#plt.xlabel('Tipo de Corte')
#plt.ylabel('Valor Medio del Precio')
#plt.title('Relación entre Tipo de Corte y Valor Medio del Precio')

#plt.show()

# Opción 2 - diagrama de caja y bigote
df.plot(kind='box', by='cut', column='price',
        ylabel='Precio [USD]',
        title='Cambio de la *distribución* de los precios con el tipo de corte')

#plt.show()

#10

corr_price = df.corr(numeric_only=True).price
print(corr_price.abs().sort_values(ascending=False))

print("""La variable carat tiene una fuerte correlación con el precio. 
Podríamos usarla para predecir el precio de los diamantes.""")

#11

df_num = df.drop(columns=['cut', 'clarity', 'color'])
corr_matrix = df_num.corr()

plt.figure(figsize=(6,6))
plt.imshow(corr_matrix, cmap='seismic') 
xt = plt.xticks(range(len(df_num.columns)), 
                df_num.columns, 
                rotation=45, ha='right', va='top')
yt = plt.yticks(range(len(df_num.columns)), 
                df_num.columns, 
                rotation=0, ha='right', va='center')
plt.colorbar(label='Pearson CC')

plt.show()

print('Las variables depth y table están correlacionadas. Además, todas demás variables están correlacionads entre sí.')
print('Por otro lado, las variables price, carat, x e y tienen una anticorrelación con depth.')
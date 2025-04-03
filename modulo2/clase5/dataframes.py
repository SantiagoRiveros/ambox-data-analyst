import pandas as pd

#Datos para diccionario
datos = {
    "Nombre": ["Ana", "Juan", "Pedro", "Lucia", "Carlos"],
    "Edad": [25,30,35,40,45],
    "Ciudad": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "Tucuman"],
    "Salario": [3000, 4000, 5000, 6000, 7000]
}

df = pd.DataFrame(datos)

print(df)

datos2 = {
    "Nombre": ["Ana", "Juan", "Pedro", "Lucia", "Carlos", "Sofia", "Diego", "Mariana", "Luis", "Valeria", "Fernando", "Gabriela", "Ricardo", "Camila", "Andres"],
    "Edad": [25, 30, 35, 40, 45, 28, 33, 38, 43, 48, 27, 32, 37, 42, 47],
    "Ciudad": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "Tucuman", "Salta", "Santa Fe", "Mar del Plata", "Neuquen", "San Luis", "La Plata", "Bahia Blanca", "San Juan", "Jujuy", "Chaco"],
    "Salario": [3000, 4000, 5000, 6000, 7000, 3500, 4500, 5500, 6500, 7500, 3200, 4200, 5200, 6200, 7200]
}

dataframe = pd.DataFrame(datos2)

# Metodos utiles de dataframes
print(dataframe.head()) # Muestra las primeras 5 entradas
print(dataframe.tail()) # Muestra las ultimas 5 entradas
print(dataframe.shape) # Muestra la cantidad de filas y columnas
print(dataframe.info()) # Muestra informacion sobre el dataframe

# Acceder a una columna
print(dataframe["Nombre"])

# Acceder a una fila
print(dataframe.iloc[2])

# Datos estadisticos
print(dataframe.describe()) # Estadisticas GENERALES para columnas numericas

""" 
count: Cantidad total de datos en esa columna (15 valores en este caso).

mean: Promedio (media aritmética) de los valores de la columna.

std (standard deviation): Desviación estándar, que mide cuánto varían los datos respecto a la media.

min: Valor mínimo encontrado en la columna.

25% (1er cuartil): El 25% de los valores son menores o iguales a este número.

50% (mediana): La mitad de los valores están por debajo de este número.

75% (3er cuartil): El 75% de los valores son menores o iguales a este número.

max: Valor máximo encontrado en la columna.

"""

# Sacar promedio de un valor

print(dataframe["Salario"].mean())
print(df["Edad"].max()) 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic_corregido.csv")

# Distribuciones por grupo
sns.histplot(data=titanic, x="Age", hue="Survived", kde=True)
plt.title("Distribucion de edad por supervivencia")
plt.show()

# Comparar variables categoricas
sns.countplot(data=titanic, x="Pclass", hue="Survived")
plt.title("Supervivencia por clase")
plt.show()

# Relaciones entre variables numericas
sns.scatterplot(data=titanic, x="Age", y="Fare", hue="Survived")
plt.title("Relacion entre edad y tarifa")
plt.show()

# Deteccion de outliers y anomalias
sns.boxplot(data=titanic, x="Pclass", y="Fare")
plt.title("Boxplot de tarifa por clase")
plt.show()

# Localizar valores extremos manualmente

# Un outlier, es un valor, que se aleja significativamente, del resto de los datos.
# Puede ser un error, una excepcion, o un dato interesante que conviene estudiar aparte

# IQR = El IQR o rango intercuartilico, es una medida estadistica de dispersion
# Se calcula asi:
""" 
IQR = Q3 - Q1

-Q1 = Primer cuartil (percentil 25%)
-Q3 = tercer cuartil (percentil 75%)

Se usa para encontrar valores extremos:
-Los valores menores a Q1 - 1.5 * IQR son outliers bajos
-Los valores mayores a Q3 + 1.5 * IQR son outliers altos
"""

""" 
Los cuartiles son valores que dividen un conjunto de datos ordenados en cuatro partes iguales, donde cada parte representa el 25% de los datos.

Se utilizan para entender la dispersión y distribución de los datos, y son fundamentales en EDA para detectar asimetrías, valores atípicos (outliers) y comparar grupos.
"""

""" 
📐 Tipos de Cuartiles
En un conjunto de datos ordenados:

Q1 (Primer cuartil o cuartil inferior): El 25% de los datos están por debajo de este valor.

Q2 (Segundo cuartil o mediana): El 50% de los datos están por debajo de este valor.

Q3 (Tercer cuartil o cuartil superior): El 75% de los datos están por debajo de este valor.
"""
#         |Q1 |Q2 |Q3
# Ej: [1,2,3,4,5,6,7,8,9,10]

# EJ 2:
# [3, 5, 7, 8, 9, 10, 12, 13, 14, 18]
# Q2 (Mediana) = (9 + 10)/2 = 9.5
# Q1: Mediana de la mitad inferior: [3, 5, 7, 8, 9] → Q1 = 7
# Q3: Mediana de la mitad superior: [10, 12, 13, 14, 18] → Q3 = 13

# Obtiene el valor del primer cuartil (Q1), es decir, el valor bajo el cual está el 25% más barato de las tarifas (Fare).
q1 = titanic["Fare"].quantile(0.25)

# Obtiene el valor del tercer cuartil (Q3), es decir, el valor bajo el cual está el 75% más barato. El 25% más caro está arriba de esto.
q3 = titanic["Fare"].quantile(0.75)
# Calcula el IQR (InterQuartile Range). Es la distancia entre Q3 y Q1. Este valor mide la "dispersión central" de los datos.
iqr = q3 - q1
# Filtra el DataFrame para quedarnos solo con los pasajeros que pagaron una tarifa mayor al límite superior permitido. Ese límite se calcula como:
outliers = titanic[titanic["Fare"] > (q3 + 1.5 * iqr)]
# límite superior = Q3 + 1.5 * IQR
# Esto te da los outliers altos, o sea, los pasajeros que pagaron mucho más que el promedio.
print(outliers[["Fare", "Pclass", "Survived"]])
""" 
 Muestra solo las columnas Fare, Pclass y Survived de los pasajeros detectados como outliers. Así podés ver:

Cuánto pagaron
En qué clase estaban
Si sobrevivieron
"""

# Visualizá la relación entre edad y supervivencia para hombres y mujeres por separado.
sns.violinplot(data=titanic, x="Sex", y="Age", hue="Survived", split=True)
plt.show()

# Detectá qué variables están más correlacionadas.
sns.heatmap(titanic.select_dtypes("number").corr(),
            annot=True, cmap="coolwarm")
plt.show()

# ¿Qué edad promedio tienen los pasajeros que sobrevivieron por clase?
print(titanic.groupby(["Pclass", "Survived"])["Age"].mean())

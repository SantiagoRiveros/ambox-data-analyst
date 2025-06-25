import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe = sns.load_dataset('titanic')

# 1 - Conteo de pasajeros por clase

sns.countplot(x='pclass', data=dataframe)
# countplot cuenta la cantidad de registros por categoría. En este caso, por clase social (1ra, 2da, 3ra).
plt.title('Cantidad de pasajeros por clase')
plt.savefig('pasajeros_por_clase.png')
plt.show()

""" 
-Muestra:
El eje X tiene las clases (pclass): 1, 2 y 3
El eje Y muestra la cantidad de pasajeros en cada clase
Altura de la barra = cantidad de registros con ese valor pclass

-Para que sirve:
Ver la distribucion de frecuencia de una variable
Por ejemplo: Si la barra de la clase 3 es mas alta, significa que la mayoria viajaba en tercera clase.
"""

# 2 - Supervivencia por sexo

sns.barplot(x='sex', y='survived', data=dataframe)
# barplot calcula automáticamente el promedio de survived por cada categoría de sex.
plt.title('Tasa de supervivencia por sexo')
plt.ylabel('Proporcion que sobrevivio')
plt.savefig('supervivencia_por_sexo.png')
plt.show()

""" 
-Muestra:
survived tiene valores 0 = no sobrevivio, 1 si sobrevivio
barplot calcula el promedio de survived para cada grupo de 'sex'
Por eso:
    Si el promedio es 0.74 para mujeres, significa que el 74% de las mujeres sobrevivio
    Si es el 0.19 para hombres, significa que el 19% de hombre sobrevivio
    
-Para que sirve:
Compara tasas(promedios) entre grupos
Es util cuando una columna es categorica, y la otra numerica binaria (por ejemplo, survived)
"""

# 3 - Edad por clase 

sns.boxplot(x='pclass', y='age', data=dataframe)
# Ideal para ver la mediana, cuartiles y valores atípicos (outliers) de edad por clase social.
plt.title('Distribucion de edad por clase')
plt.savefig('edad_por_clase.png')
plt.show()

""" 
-Muestra:
Para cada cada clase (pclass), muestra un boxplot de edades:
    Linea central del cuadro: Mediana (50% de los datos estan por encima, 50% de los datos estan por debajo)
    Caja: del 25% (Q1) al 75% (Q3) de los datos = rango intercuatilico.
    "Bigotes" (whiskers): hasta 1.5 * rango intercualitico desde Q1 y Q3.
    Puntos fuera de los bigotes: outliers (datos atipicos)
    
-Para que sirve:
Comparar la distribucion y dispersion, de valores numericos segun categorias
Identificar outliers, asimetrias, o diferencias de edad entre clases    
"""


# 4 - Relacion entre edad y tarifa

sns.scatterplot(x='age', y='fare', hue='sex', data=dataframe)
# Usamos hue para colorear los puntos según sexo.
plt.title('Relacion entre edad y tarifa')
plt.savefig('relacion_edad_tarifa.png')
plt.show()

""" 
-Muestra:
Cada punto representa una persona
Eje X: edad
Eje Y: tarifa (fare) que pago
hue='sex' diferencia los puntos de color segun sexo.

-para que sirve:
Analizar relaciones entre variables numericas
visualizar agrupamientos, outliers o correlaciones

"""

# 5 - Mapa de calor de correlaciones

#Seleccionar solo las columnas numericas
df_numerico = dataframe.select_dtypes(include=['float64', 'int64'])

sns.heatmap(df_numerico.corr(), annot=True, cmap='coolwarm')
# dataframe.corr() calcula la correlación entre variables numéricas. Se visualiza como un mapa de calor con colores.
plt.title('Mapa de correlaciones')
plt.savefig('mapa_correlaciones.png')
plt.show()

""" 
-muestra:
df_numerico.corr() calcula la correlacion de Pearson entre columnas numericas
El calor muestra:
                Valores cercanos a 1: Correlacion pósitiva fuerte
                Valores cercanos a -1: Correlacion negativa fuerte
                Valores cercanos a 0: sin correlacion
annot=True muestra los numeros sobre cada celda
cmap='coolwarm' colores rojos para correlaciones positivas, azules para negativas
"""

# 6 - Pairplot para varias variables

sns.pairplot(dataframe[['age','fare','survived','pclass']], hue='survived')
# Permite ver todas las combinaciones posibles entre variables numéricas. hue='survived' colorea por categoría.
plt.savefig('pairplot.png')
plt.show()

# 7 - Violin plot por sexo

sns.violinplot(x='sex', y='age', data=dataframe)
# Similar al boxplot, pero muestra la densidad de la distribución.
plt.title('Distribucion de edad por sexo')
plt.savefig('violinplot.png')
plt.show()

# 8 - Histograma de edad

sns.histplot(dataframe['age'].dropna(), bins=20, kde=True)
# Combina histograma con curva KDE (estimación de densidad).
plt.title('Distribucion de edades')
plt.savefig('histograma.png')
plt.show()
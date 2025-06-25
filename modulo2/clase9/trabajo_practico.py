import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('titanic.csv')

# Otro Metodo para leer csv
# dataframe = pd.read_csv(r, 'C:\Users\santi\OneDrive\Escritorio\Curso Analisis de datos\modulo2\clase9\titanic.csv')

# Leer las primeras 5 filas
#print(dataframe.head())

""" 
¿Cuántas personas hay registradas?

¿Qué columnas tienen datos faltantes?
"""

# personas registradas
print('Cantidad de personas registradas:', len(dataframe))

# ¿Que columnas tienen datos faltantes?

# Cuantos valores faltan por columna
print("Datos faltantes por columna")
print(dataframe.isnull().sum())

# Columnas con faltantes
print('Columnas con faltantes')
print(dataframe.isnull().sum()[dataframe.isnull().sum() > 0])


""" 
paso 1:
dataframe.isnull()
Este metodo devuelve un dataframe Booleano del mismo tamaño que el dataframe original, donde cada celda tiene:
True: si el valor es NaN(faltante)
False: Si el valor no esta vacio
"""

""" 
Paso 2:
dataframe.isnull().sum()
Cuando lo aplicas sobre este dataframe booleano, cuenta los True por columna, y los suma (Recordemos que True = 1 y False = 0)
"""

""" 
Paso 3:
[dataframe.isnull().sum() > 0]
Esta parte es un filtro: Te quedas solamente con las columnas que tienen al menos 1 dato faltante
"""

# LIMPIEZA DE DATOS
dataframe = dataframe.drop(columns=['Cabin', 'Ticket', 'Name'])

# Rellenar datos faltantes
dataframe['Age'] = dataframe['Age'].fillna(dataframe['Age'].median())

""" 
🔍 Paso a paso
1. dataframe['Age']
Selecciona la columna llamada "Age" del DataFrame dataframe.

2. dataframe['Age'].median()
Calcula la mediana de los valores en la columna "Age".

La mediana es el valor que está en el medio cuando ordenás todos los números. Se usa frecuentemente para reemplazar datos faltantes porque no se ve tan afectada por valores extremos (outliers) como el promedio.

3. dataframe['Age'].fillna(...)
Esta parte reemplaza todos los valores NaN (faltantes) en la columna "Age" con el valor que le pasemos entre paréntesis.

En este caso, le estamos pasando la mediana.

4. dataframe['Age'] = ...
Sobrescribimos la columna "Age" del DataFrame con la versión que ya no tiene valores NaN, sino que esos valores fueron reemplazados por la mediana.

"""

#reemplazar los nulos de embarked por "Unknown"

dataframe['Embarked'] = dataframe['Embarked'].fillna('Unkown')

# Convertí la columna 'Sex' en lowercase (str.lower()).
dataframe['Sex'] = dataframe['Sex'].str.lower()

print(dataframe)

#ANALISIS ESTADISTICO

#Tasa de Supervivencia

#print(dataframe['Survived'].value_counts(normalize=True))
tasa_supervivencia = dataframe['Survived'].value_counts(normalize=True).round(4) * 100

# Extraemos los valores
fallecidos = tasa_supervivencia[0]
sobrevivientes = tasa_supervivencia[1]

# Tasa de supervivencia
print(f'Sobrevivio un {sobrevivientes.round(4)}% de los pasajeros')
print(f'Fallecio un {fallecidos.round(4)}% de los pasajeros')

#Edad promedio
print('Edad promedio:',dataframe['Age'].mean().round(4))

#Supervivencia por sexo

supervivencia_sexo = dataframe.groupby('Sex')['Survived'].mean()



# Supervivencia por sexo

print("Supervivencia por sexo")

print(f'Sobrevivio un {supervivencia_sexo['female'].round(2) * 100}% de mujeres')
print(f'Sobrevivio un {supervivencia_sexo['male'].round(2) * 100}% de hombres')

#Supervivencia por clase
print('Supervivencia por clase')

print(f'Sobrevivio un {dataframe.groupby('Pclass')['Survived'].mean()[1].round(2) * 100}% de Primera Clase')
print(f'Sobrevivio un {dataframe.groupby('Pclass')['Survived'].mean()[2].round(4) * 100}% de Segunda Clase')
print(f'Sobrevivio un {dataframe.groupby('Pclass')['Survived'].mean()[3].round(2) * 100}% de Tercera Clase')



""" 
¿Cuál es el promedio de tarifa (Fare) por clase?

¿Cuál es la edad media por sexo?

Graficar un histograma de las tarifas (Fare)

Graficar la cantidad de sobrevivientes por sexo (df['Sex'].value_counts().plot(kind='bar'))

"""

# Promedio Tarifas por clase
promedio_tarifa = dataframe.groupby('Pclass')['Fare'].mean()
print('Promedio de tarifa por clase')
print(f'El promedio del boleto en Primera clase es de ${promedio_tarifa[1].round(2)}')
print(f'El promedio del boleto en Segunda clase es de ${promedio_tarifa[2].round(2)}')
print(f'El promedio del boleto en Tercera clase es de ${promedio_tarifa[3].round(2)}')

#Edad promedio por sexo
edad_media_sexo = dataframe.groupby('Sex')['Age'].mean()
print('Edad media Sexo')
print(f'La edad promedio de mujeres es de {edad_media_sexo['female'].round(2)} Años')
print(f'La edad promedio de hombrees es de {edad_media_sexo['male'].round(2)} Años')

# Histograma de tarifas
plt.figure(figsize=(8, 5))
dataframe['Fare'].plot(kind='hist', bins=200, color='skyblue', edgecolor='black')
plt.title('Distribucion de tarifas (Fare)')
plt.xlabel('Tarifa')
plt.ylabel('Cantidad de pasajeros')
plt.grid(True)
plt.show()

""" 
kind='hist': tipo histograma

bins=20: cuántos grupos agrupa (puedes modificarlo)

edgecolor: color del borde de las barras

plt.grid(True): agrega una cuadrícula para mejor lectura
"""

# Graficar cantidad de sobrevivientes por sexo
plt.figure(figsize=(6, 4))
dataframe['Sex'].value_counts().plot(kind='bar', color=['lightcoral', 'lightblue'])
plt.title('Cantidad de pasajeros por sexo')
plt.xlabel('Sexo')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
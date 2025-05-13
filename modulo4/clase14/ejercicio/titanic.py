import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('titanic.csv')

df['Sex'] = df['Sex'].str.lower()
df['Embarked'] = df['Embarked'].fillna('Unknown')
df['Fare'] = df['Fare'].fillna(0)
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Supervivencia por clase

sobrevivientes = df[df['Survived'] == 1]['Pclass'].value_counts().sort_index()

""" 
 df[df['Survived'] == 1]
 Esto es filtrado de filas de dataframe
 df['Survived'] == 1 devuelve una serie booleana que es True para las filas donde el valor en la columna
 Survived es 1 (Es decir, sobreviviente)
 df[...] Usa ese filtro para devolver solo las filas donde Survived es 1
 -Resultado: un nuevo DataFrame que contiene solo los pasajeros que sobrevivieron.
 
 ['Pclass']
 Luego de filtrar por sobrevivientes, esto selecciona solo la columna Pclass del dataframe resultante
 Resultado: Una serie con las clases (1, 2, 3) de los pasajeros sobrevivientes
 
 .value_counts()
 Este metodo cuenta cuantas veces aparece cada clase (1, 2, 3) entre los sobrevivientes.
 Por ejemplo:
 3    50
 1    40
 2    30 
 
 .sort_index()
 Esto ordena la serie por el indice, es decir por el numero de clase (Pclass), en vez de la cantidad
 (que es lo que hace value_counts() por defecto)
"""

plt.bar(sobrevivientes.index, sobrevivientes.values)
plt.title("Supervivencia por clase")
plt.xlabel("Clase")
plt.ylabel("Cantidad")
plt.xticks([1, 2, 3])
plt.savefig("supervivencia_por_clase.png")
plt.show()

# Distribución de edad de los que sobrevivieron

plt.hist(df[df['Survived'] == 1]['Age'].dropna(), bins=20)
plt.title("Edad de sobrevivientes")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.savefig("supervivencia_por_edad.png")
plt.show()

# Supervivencia por sexo (gráfico de torta)

sexos = df[df["Survived"] == 1]['Sex'].value_counts()
plt.pie(sexos, labels=sexos.index, autopct='%1.1f%%')
plt.title("Sobrevivientes por sexo")
plt.savefig("supervivencia_por_sexo.png")
plt.show()

# Scatter entre tarifa y edad (color según supervivencia)

plt.scatter(df['Age'], df['Fare'].dropna(), c=df['Survived'], cmap='viridis')
plt.title('Edad vs Tarifa (Color segun supervivencia)')
plt.xlabel('Edad')
plt.ylabel('Tarifa')
plt.colorbar(label='0 = No sobrevivio, 1 = Sobrevivio')
plt.savefig('supervivencia_tarifa_vs_edad.png')
plt.show()

# ¿Qué clase tenía más mujeres?

mujeres_por_clase = df[df['Sex'] ==
                       'female']['Pclass'].value_counts().sort_index()

plt.bar(mujeres_por_clase.index, mujeres_por_clase.values)
plt.title('Cantidad de mujeres por clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad de mujeres')
plt.xticks([1, 2, 3])
plt.savefig('mujeres_por_clase.png')
plt.show()

# ¿Cuál es la distribución de tarifas para los pasajeros de 3ra clase?

tarifas_3ra = df[df['Pclass'] == 3]['Fare']

plt.hist(tarifas_3ra, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribucion de tarifas (3ra clase)')
plt.xlabel('Tarifa')
plt.ylabel('Cantidad de pasajeros')
plt.savefig('distribucion_tarifas_3raclase.png')
plt.show()

# ¿Cuál es la edad promedio de los pasajeros que embarcaron en cada puerto?

edad_promedio_embarque = df.groupby('Embarked')['Age'].mean()

plt.bar(edad_promedio_embarque.index, edad_promedio_embarque.values, color='salmon', edgecolor='skyblue')
plt.title('Edad promedio por puerto de embarque')
plt.xlabel('Puerto de embarque')
plt.ylabel('Edad promedio')
plt.savefig('edad_promedio_puerto.png')
plt.show()

# Crear un gráfico de barras que muestre la edad promedio de los pasajeros del Titanic según su clase social (Pclass).

edad_promedio_clase = df.groupby('Pclass')['Age'].mean()

plt.bar(edad_promedio_clase.index, edad_promedio_clase.values, color='cornflowerblue')

plt.title('Edad promedio por clase social')
plt.xlabel('Clase social')
plt.ylabel('Edad promedio')
plt.xticks([1, 2, 3])
plt.savefig('edad_promedio_clase.png')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

empleados = pd.read_csv("empleados.csv")

#Definir el tamaño del grafico
plt.figure(figsize=(10, 5))

# Es decir va a tener 10 de ancho por 5 de alto (pulgadas)

#Vamos a crear el grafico de barras

plt.bar(empleados["Nombre"], empleados["Salario"], color="skyblue")

""" 
plt.bar(): Genera un gráfico de barras.

df["Nombre"]: Define los valores en el eje X (nombre de los empleados).

df["Salario"]: Define los valores en el eje Y (salario de cada empleado).

color="skyblue": Cambia el color de las barras a azul claro.
"""

# Agregando etiquetas alos ejes y el titulo
plt.xlabel("Empleado") # Etiqueta eje X
plt.ylabel("Salario") # Etiqueta eje Y
plt.title("Salario de cada empleado") # Titulo del grafico

#Ajustando la rotacion de los nombres
plt.xticks(rotation=45)

# Linea de codigo para mostrarlo corriendo python
plt.show()
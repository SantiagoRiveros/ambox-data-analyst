import matplotlib.pyplot as plt
import numpy as np

datos = np.random.normal(loc=50, scale=10, size=100)

# Esta línea genera 100 datos aleatorios que siguen una distribución normal (gaussiana). 
""" 
np.random.normal(...)
Es una función de numpy que genera números aleatorios con distribución normal (campana de Gauss)
loc=50: es la media (valor central) de la distribución.

scale=10: es la desviación estándar, que define cuánto varían los datos respecto a la media.

size=100: indica que se generen 100 valores.

"""
plt.hist(datos, bins=10)

# datos: es la lista de datos que generaste en la línea anterior.

# bins=10: indica que querés dividir los datos en 10 intervalos (o "cajones") para contar cuántos valores caen en cada uno.
plt.title("Distribucion de datos")
plt.savefig("grafico_histograma.png")
plt.show()
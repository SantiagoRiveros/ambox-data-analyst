import numpy as np

""" 
Se proporcionará el siguiente problema:

Crea un array con 1 millón de números aleatorios entre 0 y 100.

Calcula la media, el máximo, el mínimo y la desviación estándar.

Luego, filtra (sin bucles explícitos) todos los valores mayores a la media y cuenta cuántos son.
"""

# Generar 1 millon de numeros aleatorios
datos = np.linspace(0, 100, 1000000)

# Calcular las estadisticas

media = np.mean(datos)
maximo = np.max(datos)
minimo = np.min(datos)
std_dev = np.std(datos)

# Prints

print("Media: ", media)
print("Maximo: ", maximo)
print("Minimo: ", minimo)
print("Desviacion estandar: ", std_dev)

# Filtrar los valores mayores a la media
valores_mayores = datos[datos > media]
# Imprimimos y mostramos la cantidad de valores
print("Cantidad de valores mayores a la media: ", len(valores_mayores))
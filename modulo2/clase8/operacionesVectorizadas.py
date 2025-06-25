import numpy as np

# Operaciones vectorizadas

arr = np.array([10, 20, 30, 40])
print("Array original: ", arr)
print("Array sumado 5: ", arr + 5)
print("Array multiplicado por 2: ", arr * 2)

# Funciones estadisticas

print("Suma: ", np.sum(arr))
print("Media: ", np.mean(arr))
print("Desviacion Estandar: ", np.std(arr))
print("Maximo: ", np.max(arr))
print("Minimo: ", np.min(arr))
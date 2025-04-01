import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr + 10) # Suma 10 a cada elemento
print(arr * 2) # Multiplica todo por 2
print(arr ** 2) # Elevado al cuadrado
print(np.sqrt(arr)) # raiz cuadrada

# Ejercicio 1 = Calcula la suma total y el promedio de un array [4, 8, 12, 16]

ejercicio1 = np.array([4,8,12,16])

suma_total = np.sum(ejercicio1) # Calcula la suma total
promedio = np.mean(ejercicio1) # Calcula el promedio

# PRINTS
print(suma_total)
print(promedio)
import numpy as np

# Ejercicio 1 = Crear un array del 1 al 10

ejercicio1 = np.array([1,2,3,4,5,6,7,8,9,10])

# Ejercicio 2 = Acceder al primer elemento
ejercicio2 = ejercicio1[0]
print(ejercicio2)

#Ejercicio 3 = Acceder al ultimo elemento
# (Suponiendo que no se cual es el ultimo, cual es su ultimo numero de indice)

ejercicio3 = ejercicio1[-1]
print(ejercicio3)

# Quiero mostrar del segundo al quinto elemento
# aca usamos el SLICING
ejercicio4 = ejercicio1[1:7]
print(ejercicio4)


import numpy as np

# Usando listas de Python
lista = [1, 2, 3, 4, 5]
resultado_lista = [x * 2 for x in lista]

# Usando Numpy
arr = np.array([1, 2, 3, 4, 5])
resultado_np = arr * 2

print(resultado_lista)
print(resultado_np)
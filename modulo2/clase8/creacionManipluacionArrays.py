import numpy as np

# Creacion de un array unidimensional (o 1D)
arr = np.array([1, 2, 3, 4, 5])
print("Array 1D:")
print(arr)

# Creacion de una matriz (o array bidimensional, o 2D)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:")
print(matriz)

# Acceder a elementos y slicing
print("Primer elemento:", arr[0]) # Acceso
print("Elementos del indice 1 al 3:", arr[1:4]) # Slice
print("Elemento en la fila 2, columna 3 de la matriz:", matriz[1, 2]) # acceso matriz

# Explicacion de como acceder o hacer slice o acceder a matrices

""" 
1. arr[0] - Acceso por indice
Esto accede al primer elemento del array unidimensional(arr)

Reglas
- Los indices empiezan en 0
- arr[0] -> primer elemento
- arr[1] -> segundo elemento
- arr[2] -> tercero
...etcetera

-----------------------------------------------------------------

2. arr[1:4] - Slice (rebanada)
Esto selecciona un subconjunto del array desde el indice 1 hasta el indice 4 SIN INCLUIRLO

Reglas
- Incluye el elemento del inicio
- No incluye el elemento del fin
- Siempre toma: fin - inicio elementos
- Si cuesta entenderlo, pensarlo como unr ango: range(1, 4) -> 1, 2, 3

EJEMPLO:
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])  # Output: [20 30 40]

---------------------------------------------------

3. matriz [1, 2] - Acceso a matrices (2D arrays)
En NumPy, las matrices son arrays bidimensionales. 
El formato matriz[fila, columna] te permite acceder directamente
al valor en esa posicion

Reglas:
- Primer numero -> Indice de fila
- Segundo numero -> Indice de columna
- Igual que en excel, primero bajas, despues te moves a la derecha.

Ejemplo:

matriz = np.array([
    [1, 2, 3],   # fila 0
    [4, 5, 6],   # fila 1
    [7, 8, 9]    # fila 2
])
print(matriz[1, 2])  # Output: 6 (segunda fila, tercera columna)


"""
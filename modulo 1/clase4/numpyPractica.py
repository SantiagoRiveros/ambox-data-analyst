# Como importamos una libreria en un archivo de python?
# import NOMBRELIBRERIA as ALIASLIBRERIA

import numpy as np # Aca importamos numpy y para utilizarlo vamos a llamarlo desde la variable "np"

# Creando un array 1D [0,1,2,3,4,5,6,7,8,9] <- 1 Dimension
# array 2D [[0,1,2,3,4,5],[6,7,8,9]]



"""   [       [
    [ 0  ,     6  ]
      1        7
      2        8
      3        9
      4
      5
      6
      7
      ]

"""


#Sin Numpy

lista = [1,2,3,4,5]

resultado = [x * 2 for x in lista]
print(resultado)

# Con Numpy

arr = np.array([1,2,3,4,5])
print(arr)

resultadoNumpy = arr * 2

print(resultadoNumpy)


# Como creamos un array en Numpy?

arrayNumpy = np.array([10,20,30,40,50]) # Array 1D
print(arrayNumpy)

# ¿Y que es una matriz?

matriz = np.array([[1,2,3],[4,5,6]])
print("MATRIZ")
print(matriz)



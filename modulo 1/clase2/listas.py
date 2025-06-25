""" 
¿Que es una lista? (o array, o arreglo)
Una lista, es un conjunto de datos, ordenados, y encadenados
La sintaxis de las listas son: lista = [0,1,2,3,4]
["Messi", "Dibu Martinez", "Scaloni"] es desigual a  ["Dibu Martinez", "Scaloni", "Messi"]

"""

# Vamos a declarar unas listas y "jugar" con ellas

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

frutas = ["manzana", "banana", "cereza"]

# Hay un elemento importantisimo en las listas, que son los INDICES
# ¿Que es un indice? Es basicamente la posicion de X elemento en la lista
# Como se cuentan los indices? El primer dato, basicamente es indice 0, el siguiente indice 1, el siguiente indice 2, y asi

""" 
frutas = ["manzana", "banana", "cereza"]
indices      0           1          2
 
"""

# Yo quiero mostrar en consola "cereza"
print(frutas[2])

# Supongamos que no se el numero de indice de "cereza" pero quiero mostrarlo
indiceCereza = frutas.index("cereza")

print(indiceCereza)
print(frutas[indiceCereza])

# metodos utiles para listas

# supongamos que a frutas quiero sumarle "uvas"

frutas.append("uva")

print(frutas)

# ahora supongamos que quiero remover "banana" de la lista de frutas

frutas.remove("banana")

print(frutas)

# Esto me devuelve el largo de la lista de frutas
largoListaFrutas = len(frutas)

print(largoListaFrutas)

""" 
Crear una lista con 5 ciudades, agregar otra ciudad y remover la tercera

"""

ciudades = ["Berazategui", "Quilmes", "Florencio Varela", "La Plata"]

# Elimino a Florencio Varela

ciudades.remove(ciudades[2])

print(ciudades)

ciudades.append("Avellaneda")

print(ciudades)

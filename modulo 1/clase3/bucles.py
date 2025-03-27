"""  
El bucle basicamente es algo que se repite, hasta que se llegue a X condicion, o hasta que repita todas las veces posibles
"""

# Imprimir los números del 1 al 10 con un for.

# Estructura for

""" 
el for es una estructura de bucle, que puede ser usada de diversas maneras, en este caso, lo usamos con la variable i
la variable i, al estar declarada en el for, se toma como si fuera cada uno de los elementos
range es para determinar un rango, donde se especifican 2 numeros
"""
for i in range(1, 11):
    print(i)

# Ejercicio 2: Pedir un número al usuario y usar un while para contar desde ese número hasta 0.

numero = int(input("Ingrese un numero: "))


# La estructura del while, se declara de la siguiente manera: while CONDICION:
# Cada vez que se ejecuta, consulta si la condicion es verdadera
# Deja de ejecutarse una vez la condicion deja de ser verdadera

while numero >= 0:
    print(numero)
    # numero = numero - 1
    numero -= 1

# Ejercicio 3: Dada una lista de nombres, recórrela con un for e imprime cada nombre en mayúsculas.

nombres = ["Ana", "Juan", "María", "Pedro", "Luis"]

# El for tambien se puede usar para recorrer toda una lista de esta manera

for nombre in nombres:
    print(nombre.upper())

# Ejercicio 4: Imprimir los números pares del 1 al 20 usando un for.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

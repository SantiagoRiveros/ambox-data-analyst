""" 
Para hablar de funciones, tenemos que entender que es un modulo, o como hacer codigo "repetible"
Un modulo, es "algo" que podemos llamar desde otras partes del codigo, y podemos reutilizarlo cuantas veces queramos
Es decir, una funcion, es algo, que puede o no recibir datos, y que devuelve algo
"""

# Ejercicio 1: Crear una función que reciba un nombre y una edad, y retorne un mensaje indicando si la persona es mayor de edad o no.

# Vamos a usar la palabra clave reservada "def"
# La sintaxis es: def NOMBRE_DE_LA_FUNCION(ARGUMENTO1, ARGUMENTO2):
# Algo importante tambien es el uso del "return"+
# UNa vez que una funcion llega al return, ejecuta esa linea, y ya no continua ejecutandose


# Aca lo declaro (tal cual como se declararia una variable), antes de declararlo, "no existe"
def verificar_edad(nombre, edad):
    if edad >= 18:
        return f"{nombre} es mayor de edad"
    else:
        return f"{nombre} es menor de edad"
    print("HOLA")


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Como llamamos a la funcion y la ejecutamos?
# NOMBRE_DE_LA_FUNCION(ARGUMENTO1, ARGUMENTO2)

print(verificar_edad(nombre, edad))

# Las propiedades NO SON OBLIGATORIAS, es decir, no todas las funciones deben recibir propiedades
# La ejecucion de la funcion es igual a su retorno

# Ejercicio 2: Crear una función que reciba una lista de números y devuelva la suma de los números pares.


def suma_pares(listaNumeros):
    sumaNumeros = 0
    for i in listaNumeros:
        if i % 2 == 0:
            sumaNumeros += i
    return sumaNumeros


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(
    f"La suma de los numeros pares es: {suma_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")

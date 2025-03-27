""" 
Los condicionales que ya vimos es if y else
ahora vamos a agregarle uno mas que es elif
es como un "else if" o "sino si" sirve para concatenar condiciones y ademas darle una nueva condicion
"""

# Solicitar al usuario un número y verificar si es positivo, negativo o cero.

# Cuando uno ingresa algo en la consola, siempre lo toma como string, por ende uso el metodo int para transformarlo en un integer
numero = int(input("Ingrese un numero: "))

# Con el metodo float podemos transformar un string a float o flotante (o decimal)

# numeroDecimal = float(input("Ingrese el numero decimal"))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
elif numero == 0:
    print("El numero es cero")


# Ejercicio 2
#  Pedir dos números y decir cuál es mayor o si son iguales.

numeroA = int(input("Ingrese el primer numero: "))
numeroB = int(input("Ingrese el segundo numero: "))

if numeroA > numeroB:
    print("El primer numero es mayor")
elif numeroB > numeroA:
    print("El segundo numero es mayor")
elif numeroA == numeroB:
    print("Ambos numeros son iguales")

numeroC = int(input("Ingrese otro numero: "))

if numeroC > 0:
    if numeroC > 10:
        if numeroC > 20:
            print("El numero es mayor a 20")
        else:
            print("El numero es mayor a 10")
    else:
        print("El numero es mayor a 0")
else:
    print("El numero es negativo")

# No es necesario acompañar siempre al if de un else, pero el else siempre es "consecuencia" del if, lo mismo con el elif
if numeroC < 0:
    print("El numero es negativo")

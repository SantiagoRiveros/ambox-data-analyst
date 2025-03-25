# Tipos de datos

entero = 32  # variable de tipo integer (o entero)
decimal = 0.5  # variable de tipo float (o decimal)
string = "hola"  # variable de tipo string
# variable de tipo bool, admite solo dos valores True o False (verdadero/falso)
booleano = True

print(string)

# para navegar entre carpetas por la consola, debes utilizar el siguiente comando: cd NOMBRE_DE_LA_CARPETA
# si queres volver para atras, ejecutamos: cd ..
numero1 = 3
numero2 = 30

# Operadores matematicos
print(numero1 + numero2)  # Suma = 33
print(numero1 - numero2)  # Resta = -27
print(numero1 * numero2)  # Multiplicacion = 90
print(numero1 / numero2)  # Division = 10
print(numero2 % numero1)  # Modulo, es la resta de la division, en este caso 0
print(numero1 ** numero2)  # Potencia

# supongamos que divido 10 / 3 = 3

numeroA = 10
numeroB = 3

print("Aca va explicacion de modulo")
print(numeroA / numeroB)
print((30 % 3) == 0)
# numeroB (3) * 3 = 9 --------------- numeroA - 9 = 1


# if - else (condicionales)
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")

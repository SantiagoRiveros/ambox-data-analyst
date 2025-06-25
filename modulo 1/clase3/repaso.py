# Completa el código para obtener la capital de un país desde un diccionario.
paises = {"Argentina": "Buenos Aires", "México": "CDMX", "España": "Madrid"}

pais = input("Ingrese el nombre de un país: ")
# Agregar lógica para mostrar la capital del país ingresado

if pais in paises:
    print(f"La capital de {pais} es {paises[pais]}.")
else:
    print("Pais no encontrado")

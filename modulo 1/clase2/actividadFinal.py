""" Crear un programa que almacene una lista de estudiantes en un diccionario y permita consultar datos """

estudiantes = {
    "001": {"nombre": "Juan", "apellido": "Perez", "curso": "Python"},
    "002": {"nombre": "Jose", "apellido": "Gomez", "curso": "Javascript"}
}

estudiantesLista = [{"nombre": "Juan", "apellido": "Perez", "curso": "Python"}, {
    "nombre": "Jose", "apellido": "Gomez", "curso": "Javascript"}]

codigo = input("Ingrese el id del estudiante: ")

""" Iteracion es basicamente una forma de recorrer o repetir un comando especialmente utiles en estructuras de datos """

if codigo in estudiantes:
    print(estudiantes[codigo])
else:
    print("Estudiante no encontrado")

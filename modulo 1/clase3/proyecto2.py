empleados = {
    "E001": {"nombre": "Juan Pérez", "puesto": "Analista", "salario": 45000},
    "E002": {"nombre": "María López", "puesto": "Desarrollador", "salario": 55000},
    "E003": {"nombre": "Carlos Díaz", "puesto": "Gerente", "salario": 75000}
}

# consultar empleado


def consultar_empleado(codigo):
    if codigo in empleados:
        print(f"nombre:{empleados[codigo]["nombre"]}")
        print(f"puesto:{empleados[codigo]["puesto"]}")
        print(f"salario:{empleados[codigo]["salario"]}")
    else:
        print("No existe empleado")


consultar_empleado(input("Ingrese codigo del empleado:").upper())

# modificar salario


def actualizar_salario(codigo, salario):
    if codigo in empleados:
        empleados[codigo]["salario"] = salario
        print(
            f"el nuevo salario del empleado es: {empleados[codigo]["salario"]}")
    else:
        print("No existe empleado")


codigo = input("ingrese codigo del empleado:")
nuevo_salario = int(input("Ingrese nuevo salario: "))

actualizar_salario(codigo.upper(), nuevo_salario)

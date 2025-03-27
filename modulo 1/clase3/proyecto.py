# Agregar funciones para actualizar el stock y agregar productos.

inventario = {
    "A101": {"nombre": "Laptop", "precio": 800, "stock": 5},
    "B202": {"nombre": "Mouse", "precio": 25, "stock": 20},
    "C303": {"nombre": "Teclado", "precio": 45, "stock": 15}
}

# Consulta de producto


def consultar_producto(codigo):
    if codigo in inventario:
        producto = inventario[codigo]
        print(f"Nombre: {producto["nombre"]}")
        print(f"Precio: {producto["precio"]}")
        print(f"Stock: {producto["stock"]}")
    else:
        print("Producto no encontrado")

# Actualizar stock

# inventario[codigo] accedo a por ejemplo: {"nombre": "Laptop", "precio": 800, "stock": 5}
# inventario[codigo]["stock"] accedo al valor de stock


def actualizar_stock(codigo, cantidad, operacion):
    if codigo in inventario:
        if operacion == "suma":
            inventario[codigo]["stock"] += cantidad
        elif operacion == "resta":
            inventario[codigo]["stock"] -= cantidad
        print(
            f"Stock actualizado. Nuevo stock: {inventario[codigo]["stock"]}")
    else:
        print("Producto no encontrado")

# Agregar producto


def agregar_producto(codigo, nombre, precio, stock):
    if codigo in inventario:
        print("Producto ya existente")
    else:
        inventario[codigo] = {"nombre": nombre,
                              "precio": precio, "stock": stock}
        print("Producto agregado con exito")


# Pruebas de las funciones
codigo = input("Ingrese el codigo del producto a consultar: ")
consultar_producto(codigo)

codigo = input("Ingrese el codigo del producto para actualizar stock: ")
cantidad = int(input("Ingrese la cantidad de stock a reformar: "))
operacion = input(
    "Ingrese la operacion a efectuarse, puede ser suma o resta: ")

actualizar_stock(codigo, cantidad, operacion)

nuevo_codigo = input("Ingrese el codigo del nuevo producto: ")
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = input("Ingrese el precio del nuevo producto: ")
nuevo_stock = input("Ingrese el stock del nuevo producto: ")

agregar_producto(nuevo_codigo, nuevo_nombre, nuevo_precio, nuevo_stock)

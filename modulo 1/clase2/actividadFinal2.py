""" Crear un programa que almacene información sobre productos en un inventario y permita consultar detalles por su código. """

inventario = {

    "B202": {"nombre": "Mouse", "precio": 25, "stock": 20},
    "C303": {"nombre": "Teclado", "precio": 45, "stock": 15},
    "A101": {"nombre": "Laptop", "precio": 800, "stock": 5},
}

codigo = input("Ingrese el codigo de producto: ")

if codigo in inventario:
    producto = inventario[codigo]
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: {producto['precio']}")
    print(f"Stock: {producto['stock']}")
else:
    print("Producto no encontrado")

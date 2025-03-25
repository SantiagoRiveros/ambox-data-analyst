""" 
Es una estructura de datos que se caracteriza por tener pares clave-valor

"""

persona = {"nombre": "Santiago", "edad": 32, "ciudad": "Berazategui"}

print(persona["nombre"])

# Como hago para modificar un valor del diccionario?

persona["nombre"] = "Anselmo"

print(persona)

# Agregarle un nuevo valor

persona["profesion"] = "Developer / Project Manager / Data Analyst"

print(persona)


# Metodos practicos y utiles de diccionarios

# metodo keys - muestra lista de claves
print(persona.keys())

# metodo values - muestra lista de valores
print(persona.values())

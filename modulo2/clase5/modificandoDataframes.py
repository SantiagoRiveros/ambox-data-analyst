import pandas as pd

datos = {
    "Nombre": ["Ana", "Juan", "Pedro", "Lucia", "Carlos", "Sofia", "Diego", "Mariana", "Luis", "Valeria", "Fernando", "Gabriela", "Ricardo", "Camila", "Andres"],
    "Edad": [25, 30, 35, 40, 45, 28, 33, 38, 43, 48, 27, 32, 37, 42, 47],
    "Ciudad": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "Tucuman", "Salta", "Santa Fe", "Mar del Plata", "Neuquen", "San Luis", "La Plata", "Bahia Blanca", "San Juan", "Jujuy", "Chaco"],
    "Salario": [3000, 4000, 5000, 6000, 7000, 3500, 4500, 5500, 6500, 7500, 3200, 4200, 5200, 6200, 7200]
}

dataframe = pd.DataFrame(datos)

# Agregar una nueva columna
dataframe["Años de experiencia"] = [2, 4, 1, 5, 6, 9, 0, 7, 12, 4, 20, 4, 9, 8, 0]
print(dataframe)

# Modificar una columna
dataframe["Salario"] = dataframe["Salario"] * 10
print(dataframe)


# Guardando un dataframe en un archivo CSV
dataframe.to_csv("datos.csv")
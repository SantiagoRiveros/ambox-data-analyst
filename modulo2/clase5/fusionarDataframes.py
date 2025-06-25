import pandas as pd

df_empleados = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "Pedro", "Lucía", "Carlos"],
    "Edad": [28, 45, 40, 32, 35],
    "Salario": [4500, 7000, 6000, 5200, 5000]
})

df_bonos = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "Pedro", "Lucía"],
    "Bono": [500, 800, 600, 700]
})

df_completo = df_empleados.merge(df_bonos, on="Nombre", how="left")
print(df_completo)

""" 
merge(df_bonos, on="Nombre", how="left") une los DataFrames utilizando la columna común "Nombre".

how="left" hace una unión por la izquierda, es decir, mantiene todos los empleados aunque algunos no tengan bono.
"""
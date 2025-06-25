import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "Pedro"],
    "Edad": [25, 30, 35],
    "Salario": [3000, 4000, 5000]
})

print(df)

mayores_30 = df[df["Edad"] > 30]

print(mayores_30)

print(df["Edad"])

#Acceder a fila especifica

print(df.iloc[1])

#Extraer la columna edades

edades = df["Edad"]

print(edades)

# Como modificamos algo?

df["Salario"] = df["Salario"] * 1.1  # Aumento del 10%
print(df)

df["Edad"] = df["Edad"] * 2

print(df)
import pandas as pd

dataframe_nuevo = pd.read_csv("datos.csv")
print(dataframe_nuevo)

# Ordenando dataframe
dataframe_ordenado = dataframe_nuevo.sort_values("Edad")
print(dataframe_ordenado)

# Como hago para ordenarlos en orden Descendente?

df_descendente = dataframe_nuevo.sort_values("Edad", ascending=False)
print(df_descendente)

# Como puedo mostrar los salarios de mayor a menor?

df_salarios_descendente = dataframe_nuevo.sort_values("Salario", ascending=False)
print(df_salarios_descendente)

# Ordenar alfabeticamente
df_nombres_alfabeticos = dataframe_nuevo.sort_values(by="Nombre")
print(df_nombres_alfabeticos)
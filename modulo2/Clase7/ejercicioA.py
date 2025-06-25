import pandas as pd

""" 
Crea dos DataFrames:

Ventas: con columnas ID, Producto, Cantidad

Precios: con columnas ID y Precio

Realiza un inner merge sobre ID para obtener un 
DataFrame combinado que incluya Producto, Cantidad y Precio.

"""

df_ventas = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Producto': ['A', 'B', 'C', 'D'],
    'Cantidad': [10, 15, 20, 5]
})

df_precios = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Precio': [100, 200, 150, 250]
})

df_combinado = pd.merge(df_ventas, df_precios, on='ID', how='inner')
print(df_combinado)
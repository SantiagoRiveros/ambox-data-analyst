import pandas as pd

""" 
Crea tres DataFrames cada uno con la misma estructura 
(por ejemplo: registros de empleados de distintas sucursales) 
y concaténalos verticalmente.

Verifica que el índice se reasigne de forma secuencial.
"""

df_suc1 = pd.DataFrame({
    'ID': [1, 2],
    'Nombre': ['Ana', 'Juan']
})
df_suc2 = pd.DataFrame({
    'ID': [3, 4],
    'Nombre': ['Pedro', 'Lucía']
})
df_suc3 = pd.DataFrame({
    'ID': [5, 6],
    'Nombre': ['Carlos', 'Sofía']
})

df_total = pd.concat([df_suc1, df_suc2, df_suc3], axis=0, ignore_index=True)
print(df_total)
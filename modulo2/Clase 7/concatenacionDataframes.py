import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2],
    'Nombre': ['Ana', 'Juan']
})

df2 = pd.DataFrame({
    'ID': [3, 4],
    'Nombre': ['Pedro', 'Lucía']
})

#¿Como concateno un dataframe a otro?
# ¿Que es concantenar?
# Basicamente, es unir dos elementos
# Ejemplo "Ho" + "la" = "Hola"

df_concatenado = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df_concatenado)

""" 
ignore_index=False :
   ID Nombre
0   1    Ana
1   2   Juan
0   3  Pedro
1   4  Lucía
"""
""" 
ignore_index=True :
   ID Nombre
0   1    Ana
1   2   Juan
2   3  Pedro
3   4  Lucía


"""


# Con axis 0:

""" 
   ID Nombre
0   1    Ana
1   2   Juan
2   3  Pedro
3   4  Lucía

"""

# Con axis 1

""" 
   ID Nombre  ID Nombre
0   1    Ana   3  Pedro
1   2   Juan   4  Lucía

"""
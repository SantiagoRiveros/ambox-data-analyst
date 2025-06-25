# Metodos para manipular datos faltantes

import pandas as pd

data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Juan', None],
    'Edad': [25, 30, None, 25, 40],
    'Ciudad': ['Bs As', 'Córdoba', 'Mendoza', 'Bs As', 'La Plata']
}

dataframe = pd.DataFrame(data)

# Ver valores Nulos

print(dataframe.isnull())

# Eliminamos filas con datos faltantes

dataframe_sin_nulos = dataframe.dropna()

print(dataframe_sin_nulos)

# Rellenamos los datos faltantes de edad, con la media de edad
dataframe['Edad'].fillna(dataframe['Edad'].mean(), inplace = True)

# inplace, significa de que va a realizar los cambios sobre el dataframe original, es un argumento de pandas

print(dataframe)

# Como ponerle un nombre "Anonimo" cuando le falta el nombre
dataframe['Nombre'].fillna('Anonimo', inplace = True)

print(dataframe)

""" 
isnull() → Devuelve True donde hay nulos.

notnull() → Devuelve True donde hay datos válidos.

dropna() → Elimina filas/columnas con valores nulos.

fillna() → Rellena nulos con un valor (media, 0, "Desconocido", etc.).

"""

# DATOS DUPLICADOS

# Como sabemos que datos estan duplicados?

data = {
    'Nombre': ['Juan  ', 'Ana', 'Pedro', 'Juan  ', 'Pedro', 'Ana', 'Juan  '],
    'Edad': ["25", "30", 22, 25, 22, 30, 25],
    'Ciudad': ['Bs As', 'Córdoba', 'Mendoza', 'Bs As', 'Mendoza', 'Córdoba', 'Bs As']
}

dataframeDuplicados = pd.DataFrame(data)

# Mostrando duplicados:

print(dataframeDuplicados.duplicated())

# Como eliminar datos duplicados:

print(dataframeDuplicados.drop_duplicates())

""" 
duplicated() → Devuelve True para filas duplicadas.

drop_duplicates() → Elimina duplicados.

"""

# Reemplazos en limpieza de datos

# Como reemplazamos las ciudades en siglas por el nombre completo?

dataframeDuplicados['Ciudad'] = dataframeDuplicados['Ciudad'].replace('Bs As', 'Buenos Aires')

dataframeDuplicados = dataframeDuplicados.drop_duplicates()

print("----------------")
print(dataframeDuplicados)

# Ahora supongamos que queremos pasar a minuscula todos los nombres, y borrarle los espacios extra
dataframeDuplicados['Nombre'] = dataframeDuplicados['Nombre'].str.lower().str.strip()

print(dataframeDuplicados)

# Queremos pasar los valores de Edad a tipo integer (o entero)

dataframeDuplicados['Edad'] = dataframeDuplicados['Edad'].astype(int)

dataframeDuplicados = dataframeDuplicados.drop_duplicates()

print(dataframeDuplicados.drop_duplicates())

""" 
replace('viejo', 'nuevo') → Reemplaza valores.

Métodos de string en columnas: str.lower(), str.strip(), str.title()

astype() → Cambia el tipo de dato (por ejemplo de float a int).
"""

# ---------------------------------

# Renombrando Columnas

#Quiero pasar todas las columnas a minuscula

dataframeDuplicados.rename(columns={
    'Nombre': 'nombre',
    'Edad': 'edad',
    'Ciudad': 'ciudad'
}, inplace=True)

print(dataframeDuplicados)

""" 
df.rename(columns={'ViejoNombre': 'NuevoNombre'})

"""
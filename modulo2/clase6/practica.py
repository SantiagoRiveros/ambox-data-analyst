import pandas as pd

data = {
    'Nombre': [' Juan ', 'ANA', 'Pedro', 'ANA', None],
    'Edad': [25, None, 35, 25, 40],
    'Ciudad': ['Bs As', 'CÓRDOBA', 'Mendoza', 'Bs As', 'La Plata']
}
df = pd.DataFrame(data)

""" 
Actividades:
1. Detectar nulos y reemplazarlos con la media de la columna.

2. Eliminar duplicados.

3. Reemplazar “Bs As” por “Buenos Aires”.

4. Normalizar nombres (lower() + strip()).

5. Convertir la columna Edad a int.

6. Renombrar todas las columnas.

"""

# parte 1 - Detectar Nulos

media_edad = df['Edad'].mean()
df['Edad'] = df['Edad'].fillna(media_edad)

#  Esto reemplaza el None (que es un NaN) en 'Edad' por el promedio (31.25 en este caso).

# Parte 2 - Eliminar Duplicados

df = df.drop_duplicates()
print(df)

# Parte 3 - Reemplazar "Bs As" por "Buenos Aires"

df['Ciudad'] = df['Ciudad'].replace('Bs As', 'Buenos Aires')

# Parte 4 - Normalizar nombres

df['Nombre'] = df['Nombre'].str.lower().str.strip()
df['Ciudad'] = df['Ciudad'].str.lower().str.strip()

# Parte 5 - Convertir la columna edad a int

df['Edad'] = df['Edad'].astype(int)

# Parte 6 - Renombrar todas las columnas

nombre = 'nombre'

#df.columns[nombre, 'edad', 'ciudad']
#EJEMPLO SABIENDO EL NOMBRE DE LAS COLUMNAS

#Como hago si no se el nombre de las columnas?

df.columns = df.columns.str.lower()


# Resultado:

print(df)


""" 
df.columns accede a todos los nombres de las columnas.

.str.lower() convierte cada nombre a minúscula.

Se lo reasignás con df.columns = para actualizar el DataFrame.

"""
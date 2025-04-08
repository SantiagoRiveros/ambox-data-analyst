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

Normalizar nombres (lower() + strip()).

Convertir la columna Edad a int.

Renombrar todas las columnas.

"""
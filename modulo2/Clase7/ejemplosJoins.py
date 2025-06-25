import pandas as pd

# Dataframe de empleados
empleados = pd.DataFrame({
    'id': [1,2,3,4],
    'nombre': ['Ana', 'Luis', 'Carlos', 'Maria']
})

# Dataframe de salarios
salarios = pd.DataFrame({
    'id': [2,3,4,5],
    'salario': [50000, 60000, 55000, 70000]
})

# Inner Join
resultadoInnerJoin = pd.merge(empleados, salarios, on='id', how='inner')
print(resultadoInnerJoin)

# Solo muestra los empleados que tienen un salario registrado (coincidencia en ambas tablas).

# LEFT JOIN

resultadoLeftJoin = pd.merge(empleados, salarios, on='id', how='left')
print(resultadoLeftJoin)

# RIGHT JOIN

resultadoRightJoin = pd.merge(empleados, salarios, on='id', how='right')
print(resultadoRightJoin)

# OUTER JOIN

resultadoOuterJoin = pd.merge(empleados, salarios, on='id', how='outer')
print(resultadoOuterJoin)
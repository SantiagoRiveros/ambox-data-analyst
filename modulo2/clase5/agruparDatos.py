import pandas as pd

dataframe = pd.read_csv("datos.csv")

# Como agrupar datos
dataframe_agrupado = dataframe.groupby("Ciudad")["Salario"].mean()
print(dataframe_agrupado)
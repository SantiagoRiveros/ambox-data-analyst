import pandas as pd

dataframe = pd.read_csv("datos.csv")

def categorizar_edad(edad):
    if edad < 30:
        return "Joven"
    elif edad < 40:
        return "Adulto"
    else:
        return "Mayor"
    
dataframe["Categoria Edad"] = dataframe["Edad"].apply(categorizar_edad)
print(dataframe)
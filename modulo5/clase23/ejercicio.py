import pandas as pd

titanic = pd.read_csv("titanic.csv")

# Ver datos Nulos
print(titanic.isnull().sum())

# Aca ya sabemos que, age tiene 177 nulos, cabin 687 y embarked 2

# Rellenar o eliminar nulos
# Rellenamos los nulos de edad, con la mediana
titanic['Age'].fillna(titanic["Age"].median(), inplace=True)
# muchos nulos en cabin, por eso lo bajamos
titanic.drop(columns=["Cabin"], inplace=True)

print(titanic.isnull().sum())

# Ahora solo me quedan 2 nulos en embarked, voy a reemplazarlos por "Unknown"

titanic['Embarked'].fillna("Unknown", inplace=True)

print(titanic.isnull().sum())

# Ahora ya no tengo datos nulos

# Cambiamos todos los Sex a minuscula
titanic["Sex"] = titanic["Sex"].str.lower()

# Reemplazar valores de survived por True o False
titanic["Survived"] = titanic["Survived"].map({0: False, 1: True})

# Dejo comentado porque ya guarde lo que queria guardar
# titanic.to_csv("titanic_corregido.csv", index=False)

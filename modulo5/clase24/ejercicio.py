import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic.head())
print(titanic.tail())
print(titanic.info())
print(titanic.describe(include="all"))
print(titanic.isnull().sum())

# Limpieza y tratamiento

# Eliminamos cabin porque demasiados nulos, y ticket porque no lo uso
titanic.drop(columns=["Ticket", "Cabin"], inplace=True)
# reemplazo nulos con la mediana
titanic["Age"].fillna(titanic["Age"].median(), inplace=True)
titanic["Embarked"].fillna("Unknown", inplace=True)
titanic["Sex"] = titanic["Sex"].map({"male": "M", "female": "F"})
# Vamos a crear un par de columnitas mas
titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"] + 1
titanic["IsAlone"] = (titanic["FamilySize"] == 1).astype(int)

print(titanic)

print(titanic.head())
print(titanic.tail())
print(titanic.info())
print(titanic.describe(include="all"))
print(titanic.isnull().sum())

print(titanic["Sex"])

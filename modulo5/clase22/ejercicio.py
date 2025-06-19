import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("titanic.csv")

# Histograma
sns.histplot(data=dataframe, x="Age", bins=20, kde=True)

plt.show()

# Boxplot
# Muestra la mediana, cuartiles y outliers
sns.boxplot(data=dataframe, x="Pclass", y="Age")

plt.show()

# Correlaciones
# Scatter plot (Grafico de dispersion)
sns.scatterplot(data=dataframe, x="Age", y="Fare")

plt.show()

# Heatmap de correlaciones
# Muestra matriz de correlaciones (de -1 a 1)
# Solo tiene sentido con valores numericos

corr = dataframe.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.show()

# Histograma de tarifas

sns.histplot(data=dataframe, x="Fare", bins=100, kde=True)

plt.title("Distribucion de tarifas")
plt.xlabel("Tarifa")
plt.ylabel("Frecuencia")
plt.show()

# Boxplot de tarifas vs clase

sns.boxplot(data=dataframe, x="Pclass", y="Fare")
plt.title("Distribucion de tarifas por clase")
plt.xlabel("Clase")
plt.ylabel("Tarifa")
plt.show()

# Scatter plot de edad vs supervivencia

sns.stripplot(data=dataframe, x="Survived", y="Age", jitter=True)
plt.title("Relacion entre edad y supervivencia")
plt.xlabel("¿Sobrevivio?")
plt.ylabel("Edad")
plt.show()

# Violin plot de edad por sexo y sueprvivencia


sns.violinplot(data=dataframe, x="Sex", y="Age", hue="Survived", split=True)
plt.title("Distribucion de edad por sexo y supervivencia")
plt.show()

# Countplot de sobrevivientes por clase y sexo
sns.countplot(data=dataframe, x="Pclass", hue="Sex")
plt.title("Cantidad de pasajeros por clase y sexo")
plt.show()

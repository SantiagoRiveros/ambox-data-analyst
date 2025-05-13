import matplotlib.pyplot as plt

plt.pie([60,30,10], labels=["A", "B", "C"], autopct='%1.1f%%')

""" 
plt.pie
Llama a la funcion pie() de matplotlib.pyplot para generar un grafico torta

[60, 30, 10]
Es una lista de valores numericos que representan la proporcion de cada porcion de la torta.
En este caso: 60% la primera porcion, 30% la segunda porcion, 10% la tercera

labels=["A", "B", "C"]
Especifica la etiqueta de cada porcion.
Es decir, el 60% se etiqueta como "A", el 30% como "B" y el 10% como "C"

autopct='%1.1f%%'
Este parametro muestra el porcentaje de cada porcion del grafico.
'%1.1f%%' significa:
%1.1f: mostrar el numero con 1 decimal (ej: 23.5)
%%: el doble % es para mostrar el simbolo '%' literal.
es decir, con el ejemplo anterior mostraria 23.5%
"""

plt.title("Distribucion de categorias")
plt.savefig("grafico_de_torta.png")
plt.show()

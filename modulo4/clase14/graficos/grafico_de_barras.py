import matplotlib.pyplot as plt

etiquetas = ['A', 'B', 'C', 'D']
valores = [10, 25, 5, 15]

plt.bar(etiquetas, valores)
plt.title("Comparacion de categorias")
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.savefig('grafico_de_barras.png')
plt.show()
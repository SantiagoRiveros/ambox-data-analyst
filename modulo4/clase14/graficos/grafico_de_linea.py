import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x,y) # Dibuja una linea usando los puntos definidos por X e Y
plt.title("Crecimiento") # Agregamos titulo al grafico
plt.xlabel("Tiempo") # Etiqueta el eje X con el titulo "Tiempo"
plt.ylabel("Valor") # Etiqueta el eje Y con el titulo "Valor"

# Aca guardamos el grafico
plt.savefig('grafico_de_linea.png')

plt.show() # Muestra el grafico
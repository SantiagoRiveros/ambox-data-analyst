import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = x + np.random.normal(0, 0.1, 50)

plt.scatter(x, y)
plt.title("Relacion entre variables")
plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.savefig("grafico_dispersion.png")
plt.show()
import math
import time

# Crear 100.000 valores entre 0 y 10
x_vals = [i * 10 / 99999999 for i in range(100000000)]

# Medir el tiempo
start = time.time()

# Calcular f(x) = e^(-x) * sin(x) para cada valor
y_vals = []
for x in x_vals:
    y = math.exp(-x) * math.sin(x)
    y_vals.append(y)

# Medimos el tiempo cuando termina
end = time.time()

print("Tiempo de calculo vectorizado:", end - start, "segundos")

# Tiempo de calculo vectorizado: 0.04399585723876953 segundos <- 100.000
# Tiempo de calculo vectorizado: 30.4851336479187 segundos <- 100.000.000
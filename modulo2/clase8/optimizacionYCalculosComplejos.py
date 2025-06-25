""" 
Supongamos que queremos calcular la función
f(x)=e 
−x
 sin(x)
 para 100,000 valores entre 0 y 10.
"""

import numpy as np
import time

# Generar 100.000 valores entre 0 y 10
x = np.linspace(0, 10, 100000000)

# Inicio del tiempo
start = time.time()

# Calcular f(x) vectorizado
y = np.exp(-x) * np.sin(x)

# Medir el tiempo
end = time.time()

print("Tiempo de calculo vectorizado:", end - start, "segundos")

""" 
np.linspace(0, 10, 100000) 
genera un array de 100,000 valores equidistantes entre 0 y 10.

La operación vectorizada en y = np.exp(-x) * np.sin(x) 
se aplica a todos los valores de x sin usar bucles explícitos, lo que es mucho más rápido.
"""

# Tiempo de calculo vectorizado: 0.0019998550415039062 segundos <- 100.000
# Tiempo de calculo vectorizado: 1.9579963684082031 segundos <- 100.000.000
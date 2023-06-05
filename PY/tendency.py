import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np
from scipy.stats import linregress

# Leer los datos del archivo resultados.csv
data = pd.read_csv("resultados.csv")

velocidad_subida = data["up"]
velocidad_bajada = data["down"]

# Cálculos estadísticos de subida
media_subida = statistics.mean(velocidad_subida)
moda_subida = statistics.mode(velocidad_subida)
desviacion_subida = statistics.stdev(velocidad_subida)

# Cálculos estadísticos de bajada
media_bajada = statistics.mean(velocidad_bajada)
moda_bajada = statistics.mode(velocidad_bajada)
desviacion_bajada = statistics.stdev(velocidad_bajada)

# Gráfica de dispersión de velocidad de subida y bajada
plt.figure(figsize=(8, 6))
plt.scatter(velocidad_subida, velocidad_bajada)
plt.xlabel("Velocidad de subida (Mbps)")
plt.ylabel("Velocidad de bajada (Mbps)")
plt.title("Velocidad de Subida vs Velocidad de Bajada")

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(
    velocidad_subida, velocidad_bajada
)

# Generate points for the trend line
x = np.linspace(min(velocidad_subida), max(velocidad_subida), 100)
y = slope * x + intercept

# Plot the trend line
plt.plot(x, y, color="red")

# Print the trendline equation and r-value
equation = f"y = {slope:.2f}x + {intercept:.2f}"
r_squared = f"r = {r_value:.2f}"

plt.text(40, 260, equation, fontsize=12)
plt.text(40, 250, r_squared, fontsize=12)

# Resultados de subida
print("Estadísticas de Velocidad de Subida:")
print("Media:", media_subida)
print("Moda:", moda_subida)
print("Desviación estándar:", desviacion_subida)

# Resultados de bajada
print("\nEstadísticas de Velocidad de Bajada:")
print("Media:", media_bajada)
print("Moda:", moda_bajada)
print("Desviación estándar:", desviacion_bajada)

print()
print(equation)
print(r_squared)

plt.show()

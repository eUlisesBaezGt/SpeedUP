import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Leer los datos del archivo resultados.csv
data = pd.read_csv("resultados.csv")

velocidad_subida = data["up"]
velocidad_bajada = data["down"]

# Cálculos estadísticos de subida
media_subida = statistics.mean(velocidad_subida)
desviacion_subida = statistics.stdev(velocidad_subida)

# Cálculos estadísticos de bajada
media_bajada = statistics.mean(velocidad_bajada)
desviacion_bajada = statistics.stdev(velocidad_bajada)

# Gráfica de dispersión de velocidad de subida y bajada
plt.figure(figsize=(10, 5))
plt.scatter(velocidad_subida, velocidad_bajada)
plt.xlabel("Velocidad de subida (Mbps)")
plt.ylabel("Velocidad de bajada (Mbps)")
plt.title("Velocidad de Subida vs Velocidad de Bajada")

# Resultados de subida
print("Estadísticas de Velocidad de Subida:")
print("Media:", media_subida)
print("Desviación estándar:", desviacion_subida)

# Resultados de bajada
print("\nEstadísticas de Velocidad de Bajada:")
print("Media:", media_bajada)
print("Desviación estándar:", desviacion_bajada)

plt.tight_layout()
plt.show()

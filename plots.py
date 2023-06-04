import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Leer los datos del archivo resultados.txt
data = pd.read_csv('resultados.txt', delimiter=': ', engine='python', skip_blank_lines=True)
velocidad_subida = data['Velocidad de subida'].str.split().str[0].astype(float)
velocidad_bajada = data['Velocidad de bajada'].str.split().str[0].astype(float)

# Cálculos estadísticos
media_subida = statistics.mean(velocidad_subida)
media_bajada = statistics.mean(velocidad_bajada)
moda_subida = statistics.mode(velocidad_subida)
moda_bajada = statistics.mode(velocidad_bajada)
desviacion_subida = statistics.stdev(velocidad_subida)
desviacion_bajada = statistics.stdev(velocidad_bajada)

# Tabla de frecuencia
tabla_subida = velocidad_subida.value_counts().reset_index().sort_values('index')
tabla_subida.columns = ['Velocidad', 'Frecuencia']
tabla_subida['Frecuencia Relativa'] = tabla_subida['Frecuencia'] / tabla_subida['Frecuencia'].sum()
tabla_subida['Frecuencia Acumulada'] = tabla_subida['Frecuencia'].cumsum()

tabla_bajada = velocidad_bajada.value_counts().reset_index().sort_values('index')
tabla_bajada.columns = ['Velocidad', 'Frecuencia']
tabla_bajada['Frecuencia Relativa'] = tabla_bajada['Frecuencia'] / tabla_bajada['Frecuencia'].sum()
tabla_bajada['Frecuencia Acumulada'] = tabla_bajada['Frecuencia'].cumsum()

# Gráficas
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(tabla_subida['Velocidad'], tabla_subida['Frecuencia'], width=0.5)
plt.xlabel('Velocidad de subida (Mbps)')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de Velocidad de Subida')

plt.subplot(1, 2, 2)
plt.bar(tabla_bajada['Velocidad'], tabla_bajada['Frecuencia'], width=0.5)
plt.xlabel('Velocidad de bajada (Mbps)')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de Velocidad de Bajada')

plt.tight_layout()
plt.show()

# Resultados
print("Media de Velocidad de Subida:", media_subida)
print("Media de Velocidad de Bajada:", media_bajada)
print("Moda de Velocidad de Subida:", moda_subida)
print("Moda de Velocidad de Bajada:", moda_bajada)
print("Desviación estándar de Velocidad de Subida:", desviacion_subida)
print("Desviación estándar de Velocidad de Bajada:", desviacion_bajada)

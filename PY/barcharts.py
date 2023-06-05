import pandas as pd
import matplotlib.pyplot as plt
import statistics
import math

# Leer los datos del archivo resultados.csv
data = pd.read_csv("resultados.csv")

velocidad_subida = data["up"]
velocidad_bajada = data["down"]

# Cálculos estadísticos de subida
media_subida = statistics.mean(velocidad_subida)
moda_subida = statistics.mode(velocidad_subida)
desviacion_subida = statistics.stdev(velocidad_subida)

# Rangos de velocidad de subida
rango_min_subida = math.floor(min(velocidad_subida) / 10) * 10
rango_max_subida = math.ceil(max(velocidad_subida) / 10) * 10
rangos_subida = list(range(rango_min_subida, rango_max_subida + 10, 10))

# Tabla de frecuencia de velocidad de subida
tabla_subida = (
    pd.cut(velocidad_subida, bins=rangos_subida, include_lowest=True)
    .value_counts()
    .sort_index()
)
tabla_subida = tabla_subida.reset_index()
tabla_subida.columns = ["Rango de Velocidad (Subida)", "Frecuencia"]
tabla_subida["Frecuencia Relativa"] = (
    tabla_subida["Frecuencia"] / tabla_subida["Frecuencia"].sum()
)
tabla_subida["Frecuencia Acumulada"] = tabla_subida["Frecuencia"].cumsum()

# Convertir los intervalos de subida a formato de cadena
tabla_subida["Rango de Velocidad (Subida)"] = tabla_subida[
    "Rango de Velocidad (Subida)"
].astype(str)

# Gráfica de frecuencia de velocidad de subida
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.bar(
    tabla_subida["Rango de Velocidad (Subida)"], tabla_subida["Frecuencia"], width=0.8
)
plt.xlabel("Rango de Velocidad de subida (Mbps)")
plt.ylabel("Frecuencia")
plt.title("Frecuencia de Velocidad de Subida")
plt.xticks(rotation=45, ha="right")

# Resultados de subida
print("Estadísticas de Velocidad de Subida:")
print("Media:", media_subida)
print("Moda:", moda_subida)
print("Desviación estándar:", desviacion_subida)

# Handle empty download speed data
if velocidad_bajada.isnull().all():
    print("\nNo hay datos de Velocidad de Bajada.")
else:
    # Cálculos estadísticos de bajada
    media_bajada = statistics.mean(velocidad_bajada)
    moda_bajada = statistics.mode(velocidad_bajada)
    desviacion_bajada = statistics.stdev(velocidad_bajada)

    # Rangos de velocidad de bajada
    rango_min_bajada = math.floor(min(velocidad_bajada) / 10) * 10
    rango_max_bajada = math.ceil(max(velocidad_bajada) / 10) * 10
    rangos_bajada = list(range(rango_min_bajada, rango_max_bajada + 10, 10))

    # Tabla de frecuencia de velocidad de bajada
    tabla_bajada = (
        pd.cut(velocidad_bajada, bins=rangos_bajada, include_lowest=True)
        .value_counts()
        .sort_index()
    )
    tabla_bajada = tabla_bajada.reset_index()
    tabla_bajada.columns = ["Rango de Velocidad (Bajada)", "Frecuencia"]
    tabla_bajada["Frecuencia Relativa"] = (
        tabla_bajada["Frecuencia"] / tabla_bajada["Frecuencia"].sum()
    )
    tabla_bajada["Frecuencia Acumulada"] = tabla_bajada["Frecuencia"].cumsum()

    # Convertir los intervalos de bajada a formato de cadena
    tabla_bajada["Rango de Velocidad (Bajada)"] = tabla_bajada[
        "Rango de Velocidad (Bajada)"
    ].astype(str)

    # Gráfica de frecuencia de velocidad de bajada
    plt.subplot(1, 2, 2)
    plt.bar(
        tabla_bajada["Rango de Velocidad (Bajada)"],
        tabla_bajada["Frecuencia"],
        width=0.8,
    )
    plt.xlabel("Rango de Velocidad de bajada (Mbps)")
    plt.ylabel("Frecuencia")
    plt.title("Frecuencia de Velocidad de Bajada")
    plt.xticks(rotation=45, ha="right")

    # Resultados de bajada
    print("\nEstadísticas de Velocidad de Bajada:")
    print("Media:", media_bajada)
    print("Moda:", moda_bajada)
    print("Desviación estándar:", desviacion_bajada)

plt.tight_layout()
plt.show()

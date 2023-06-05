import pandas as pd
import math

# Leer los datos del archivo resultados.csv
data = pd.read_csv("resultados.csv")

velocidad_subida = data["up"]
velocidad_bajada = data["down"]

# Definir los intervalos de clase
rango_min = math.floor(min(min(velocidad_subida), min(velocidad_bajada)) / 10) * 10
rango_max = math.ceil(max(max(velocidad_subida), max(velocidad_bajada)) / 10) * 10
rangos = list(range(rango_min, rango_max + 10, 10))

# Tabla de frecuencia de velocidad de subida
tabla_subida = (
    pd.cut(velocidad_subida, bins=rangos, include_lowest=True)
    .value_counts()
    .sort_index()
)
tabla_subida = tabla_subida.reset_index()
tabla_subida.columns = ["Rango de Velocidad", "Frecuencia"]
tabla_subida["Frecuencia Relativa"] = (
    tabla_subida["Frecuencia"] / tabla_subida["Frecuencia"].sum()
)
tabla_subida["Frecuencia Acumulada"] = tabla_subida["Frecuencia"].cumsum()

# Convertir los intervalos de subida a formato de cadena
tabla_subida["Rango de Velocidad"] = tabla_subida["Rango de Velocidad"].astype(str)

# Filtrar filas con frecuencia diferente de 0
tabla_subida = tabla_subida[tabla_subida["Frecuencia"] != 0]

# Tabla de frecuencia de velocidad de bajada
tabla_bajada = (
    pd.cut(velocidad_bajada, bins=rangos, include_lowest=True)
    .value_counts()
    .sort_index()
)
tabla_bajada = tabla_bajada.reset_index()
tabla_bajada.columns = ["Rango de Velocidad", "Frecuencia"]
tabla_bajada["Frecuencia Relativa"] = (
    tabla_bajada["Frecuencia"] / tabla_bajada["Frecuencia"].sum()
)
tabla_bajada["Frecuencia Acumulada"] = tabla_bajada["Frecuencia"].cumsum()

# Convertir los intervalos de bajada a formato de cadena
tabla_bajada["Rango de Velocidad"] = tabla_bajada["Rango de Velocidad"].astype(str)

# Filtrar filas con frecuencia diferente de 0
tabla_bajada = tabla_bajada[tabla_bajada["Frecuencia"] != 0]

# Imprimir la tabla de frecuencia de velocidad de subida
print("Tabla de Frecuencia de Velocidad de Subida:")
print(tabla_subida)

# Imprimir la tabla de frecuencia de velocidad de bajada
print("\nTabla de Frecuencia de Velocidad de Bajada:")
print(tabla_bajada)

import csv
import os

# Directorio donde se encuentran los archivos CSV
directorio = "./"

# Nombre del archivo de salida
archivo_salida = "results.csv"

# Lista para almacenar los datos de los archivos CSV
datos_totales = []

# Recorre todos los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".csv"):
        ruta_archivo = os.path.join(directorio, archivo)
        with open(ruta_archivo, "r", newline="") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            # Ignora la primera fila si contiene encabezados
            encabezados = next(lector_csv, None)
            # Agrega los datos restantes del archivo CSV a la lista
            for fila in lector_csv:
                datos_totales.append(fila)

# Escribe los datos combinados en el archivo de salida
with open(archivo_salida, "w", newline="") as archivo_salida:
    escritor_csv = csv.writer(archivo_salida)
    # Escribe los encabezados
    escritor_csv.writerow(encabezados)
    # Escribe los datos
    escritor_csv.writerows(datos_totales)

print("Archivos CSV combinados correctamente en", archivo_salida)

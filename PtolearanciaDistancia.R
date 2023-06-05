# Cargar el paquete necesario para leer archivos CSV
library(readr)

# Leer el archivo CSV
datos <- read_csv("resultados.csv")

# Obtener el vector de distancias
distancia <- datos$distancia

# Definir la tolerancia como una desviación estándar de la media
tolerancia <- sd(distancia, na.rm = TRUE)

# Calcular el número de distancias dentro y fuera de tolerancia
dentro_tolerancia <- sum(abs(distancia - mean(distancia, na.rm = TRUE)) <= tolerancia)
fuera_tolerancia <- sum(abs(distancia - mean(distancia, na.rm = TRUE)) > tolerancia)

cat("Media distancia --> ",  mean(distancia, na.rm = TRUE))
cat("Desviación distancia --> ", sd(distancia, na.rm = TRUE))

# Calcular las probabilidades
p_distancia <- dentro_tolerancia / length(distancia)
q_distancia <- fuera_tolerancia / length(distancia)

# Imprimir los resultados
cat("Probabilidad de distancias dentro de tolerancia P:", p_distancia, "\n")
cat("Probabilidad de distancias fuera de tolerancia Q:", q_distancia, "\n")

# Cargar el paquete necesario para leer archivos CSV
library(readr)

# Leer el archivo CSV
datos <- read_csv("results.csv")

# Obtener los vectores de velocidad de subida y bajada
velocidad_subida <- datos$up
velocidad_bajada <- datos$down

# Definir la tolerancia como una desviación estándar de la media
tolerancia_subida <- sd(velocidad_subida, na.rm = TRUE)
tolerancia_bajada <- sd(velocidad_bajada, na.rm = TRUE)

# Calcular el número de velocidades dentro y fuera de tolerancia
dentro_tolerancia_subida <- sum(abs(velocidad_subida - mean(velocidad_subida, na.rm = TRUE)) <= tolerancia_subida)
fuera_tolerancia_subida <- sum(abs(velocidad_subida - mean(velocidad_subida, na.rm = TRUE)) > tolerancia_subida)
dentro_tolerancia_bajada <- sum(abs(velocidad_bajada - mean(velocidad_bajada, na.rm = TRUE)) <= tolerancia_bajada)
fuera_tolerancia_bajada <- sum(abs(velocidad_bajada - mean(velocidad_bajada, na.rm = TRUE)) > tolerancia_bajada)

# Calcular las probabilidades
p_subida <- dentro_tolerancia_subida / length(velocidad_subida)
q_subida <- fuera_tolerancia_subida / length(velocidad_subida)
p_bajada <- dentro_tolerancia_bajada / length(velocidad_bajada)
q_bajada <- fuera_tolerancia_bajada / length(velocidad_bajada)

cat("\nMedia subida --> " , mean(velocidad_subida, na.rm = TRUE))
cat("\nDesviación subida--> ", sd(velocidad_subida, na.rm = TRUE))

cat("\nMedia bajada --> " , mean(velocidad_bajada, na.rm = TRUE))
cat("\nDesviación bajada --> ",sd(velocidad_bajada, na.rm = TRUE))

# Imprimir los resultados
cat("Probabilidad de velocidades de subida dentro de tolerancia P1:", p_subida, "\n")
cat("Probabilidad de velocidades de subida fuera de tolerancia Q1:", q_subida, "\n")
cat("Probabilidad de velocidades de bajada dentro de tolerancia P2: ", p_bajada, "\n")
cat("Probabilidad de velocidades de bajada fuera de tolerancia Q2: ", q_bajada, "\n")

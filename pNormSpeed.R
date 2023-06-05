# Cargar el paquete necesario para leer archivos CSV
library(readr)

# Leer el archivo CSV
datos <- read_csv("resultados.csv")

# Obtener los vectores de velocidad de subida y bajada
velocidad_subida <- datos$up
velocidad_bajada <- datos$down

# Calcular la media y desviación estándar de las velocidades de subida
media_subida <- mean(velocidad_subida, na.rm = TRUE)
desviacion_subida <- sd(velocidad_subida, na.rm = TRUE)

# Calcular la media y desviación estándar de las velocidades de bajada
media_bajada <- mean(velocidad_bajada, na.rm = TRUE)
desviacion_bajada <- sd(velocidad_bajada, na.rm = TRUE)

cat("Media de velocidades de subida:", media_subida, "\n")
cat("Desviación estándar de velocidades de subida:", desviacion_subida, "\n")
cat("Media de velocidades de bajada:", media_bajada, "\n")
cat("Desviación estándar de velocidades de bajada:", desviacion_bajada, "\n")

# Definir las tolerancias como múltiplos de la desviación estándar
multiplo_tolerancia <- 1
tolerancia_subida <- multiplo_tolerancia * desviacion_subida
tolerancia_bajada <- multiplo_tolerancia * desviacion_bajada

# Calcular las probabilidades utilizando la función pnorm
probabilidad_dentro_tolerancia_subida <- pnorm(media_subida + tolerancia_subida, mean = media_subida, sd = desviacion_subida) - pnorm(media_subida - tolerancia_subida, mean = media_subida, sd = desviacion_subida)
probabilidad_fuera_tolerancia_subida <- 1 - probabilidad_dentro_tolerancia_subida

probabilidad_dentro_tolerancia_bajada <- pnorm(media_bajada + tolerancia_bajada, mean = media_bajada, sd = desviacion_bajada) - pnorm(media_bajada - tolerancia_bajada, mean = media_bajada, sd = desviacion_bajada)
probabilidad_fuera_tolerancia_bajada <- 1 - probabilidad_dentro_tolerancia_bajada

# Imprimir los resultados
cat("Probabilidad de velocidades de subida dentro de tolerancia P1:", probabilidad_dentro_tolerancia_subida, "\n")
cat("Probabilidad de velocidades de subida fuera de tolerancia Q1:", probabilidad_fuera_tolerancia_subida, "\n")
cat("Probabilidad de velocidades de bajada dentro de tolerancia P2: ", probabilidad_dentro_tolerancia_bajada, "\n")
cat("Probabilidad de velocidades de bajada fuera de tolerancia Q2: ", probabilidad_fuera_tolerancia_bajada, "\n")

# Cargar el paquete necesario para leer archivos CSV
library(readr)

# Leer el archivo CSV
datos <- read_csv("results.csv")

# Obtener los vectores de velocidad de subida y bajada
velocidad_subida <- datos$up
velocidad_bajada <- datos$down

# Obtener el vector de distancia
distancia <- datos$distancia

# Calcular la media y desviación estándar de las velocidades de subida
media_subida <- mean(velocidad_subida, na.rm = TRUE)
desviacion_subida <- sd(velocidad_subida, na.rm = TRUE)

# Calcular la media y desviación estándar de las velocidades de bajada
media_bajada <- mean(velocidad_bajada, na.rm = TRUE)
desviacion_bajada <- sd(velocidad_bajada, na.rm = TRUE)

# Calcular la media y desviación estándar de la distancia
media_distancia <- mean(distancia, na.rm = TRUE)
desviacion_distancia <- sd(distancia, na.rm = TRUE)

cat("Media de velocidades de subida:", media_subida, "\n")
cat("Desviación estándar de velocidades de subida:", desviacion_subida, "\n")
cat("Media de velocidades de bajada:", media_bajada, "\n")
cat("Desviación estándar de velocidades de bajada:", desviacion_bajada, "\n")

cat("Media de distancia:", media_distancia, "\n")
cat("Desviación estándar de distancia:", desviacion_distancia, "\n")

# Definir las tolerancias como múltiplos de la desviación estándar
multiplo_tolerancia <- 1
tolerancia_subida <- multiplo_tolerancia * desviacion_subida
tolerancia_bajada <- multiplo_tolerancia * desviacion_bajada
tolerancia_distancia <- multiplo_tolerancia * desviacion_distancia

probabilidad_dentro_tolerancia_subida <- pnorm(media_subida + tolerancia_subida, mean = media_subida, sd = desviacion_subida) - pnorm(media_subida - tolerancia_subida, mean = media_subida, sd = desviacion_subida)
probabilidad_fuera_tolerancia_subida <- 1 - probabilidad_dentro_tolerancia_subida

probabilidad_dentro_tolerancia_bajada <- pnorm(media_bajada + tolerancia_bajada, mean = media_bajada, sd = desviacion_bajada) - pnorm(media_bajada - tolerancia_bajada, mean = media_bajada, sd = desviacion_bajada)
probabilidad_fuera_tolerancia_bajada <- 1 - probabilidad_dentro_tolerancia_bajada

probabilidad_dentro_tolerancia_distancia <- pnorm(media_distancia + tolerancia_distancia, mean = media_distancia, sd = desviacion_distancia) - pnorm(media_distancia - tolerancia_distancia, mean = media_distancia, sd = desviacion_distancia)
probabilidad_fuera_tolerancia_distancia <- 1 - probabilidad_dentro_tolerancia_distancia

# Calcula la probabilidad de necesitar más de 150 mediciones para encontrar 10 mediciones fuera de tolerancias (subida)
# Número de mediciones fuera de tolerancia deseado
exitos_deseados_subida <- 10
# Número máximo de mediciones totales
intentos_maximos_subida <- 150
# Probabilidad de una medición fuera de tolerancia en la velocidad de subida (ya calculada)
probabilidad_subida <- 1 - pnbinom(intentos_maximos_subida - exitos_deseados_subida, exitos_deseados_subida, probabilidad_fuera_tolerancia_subida)
cat("Probabilidad de necesitar más de 150 mediciones para encontrar 10 mediciones fuera de tolerancias (subida):", probabilidad_subida, "\n")

# Calcula la probabilidad de necesitar más de 300 mediciones para encontrar 20 mediciones fuera de tolerancias (bajada)
# Número de mediciones fuera de tolerancia deseado
exitos_deseados_bajada <- 20
# Número máximo de mediciones totales
intentos_maximos_bajada <- 300
# Probabilidad de una medición fuera de tolerancia en la velocidad de bajada (ya calculada)
probabilidad_bajada <- 1 - pnbinom(intentos_maximos_bajada - exitos_deseados_bajada, exitos_deseados_bajada, probabilidad_fuera_tolerancia_bajada)
cat("Probabilidad de necesitar más de 300 mediciones para encontrar 20 mediciones fuera de tolerancias (bajada):", probabilidad_bajada, "\n")

# Calcula la probabilidad de necesitar más de 200 mediciones para encontrar 15 mediciones fuera de tolerancias (distancia)
# Número de mediciones fuera de tolerancia deseado
exitos_deseados_distancia <- 15
# Número máximo de mediciones totales
intentos_maximos_distancia <- 200
# Probabilidad de una medición fuera de tolerancia en la distancia (ya calculada)
probabilidad_distancia <- 1 - pnbinom(intentos_maximos_distancia - exitos_deseados_distancia, exitos_deseados_distancia, probabilidad_fuera_tolerancia_distancia)
cat("Probabilidad de necesitar más de 200 mediciones para encontrar 15 mediciones fuera de tolerancias (distancia):", probabilidad_distancia, "\n")

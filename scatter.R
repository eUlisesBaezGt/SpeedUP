library(ggplot2)
library(stats)

# Leer los datos del archivo resultados.csv
data <- read.csv("resultados.csv")

velocidad_subida <- data$up
velocidad_bajada <- data$down

# Cálculos estadísticos de subida
media_subida <- mean(velocidad_subida)
desviacion_subida <- sd(velocidad_subida)

# Cálculos estadísticos de bajada
media_bajada <- mean(velocidad_bajada)
desviacion_bajada <- sd(velocidad_bajada)

# Gráfica de dispersión de velocidad de subida y bajada
ggplot(data, aes(x = up, y = down)) +
  geom_point() +
  labs(x = "Velocidad de subida (Mbps)", y = "Velocidad de bajada (Mbps)",
       title = "Velocidad de Subida vs Velocidad de Bajada")

# Resultados de subida
cat("Estadísticas de Velocidad de Subida:\n")
cat("Media:", media_subida, "\n")
cat("Desviación estándar:", desviacion_subida, "\n")

# Resultados de bajada
cat("\nEstadísticas de Velocidad de Bajada:\n")
cat("Media:", media_bajada, "\n")
cat("Desviación estándar:", desviacion_bajada, "\n")


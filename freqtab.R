library(dplyr)
library(tidyr)

# Leer los datos del archivo resultados.csv
data <- read.csv("resultados.csv")

velocidad_subida <- data$up
velocidad_bajada <- data$down

# Definir los intervalos de clase
rango_min <- floor(min(velocidad_subida, na.rm = TRUE) / 10) * 10
rango_max <- ceiling(max(velocidad_subida, na.rm = TRUE) / 10) * 10
rangos <- seq(rango_min, rango_max, by = 10)

# Tabla de frecuencia de velocidad de subida
tabla_subida <- data.frame(Rango_de_Velocidad = cut(velocidad_subida, breaks = rangos, include.lowest = TRUE, na.include = TRUE)) %>%
  count(Rango_de_Velocidad, .drop = FALSE) %>%
  arrange(Rango_de_Velocidad) %>%
  rename(Frecuencia = n) %>%
  mutate(Frecuencia_Relativa = Frecuencia / sum(Frecuencia, na.rm = TRUE),
         Frecuencia_Acumulada = cumsum(Frecuencia))

# Convertir los intervalos de subida a formato de cadena
tabla_subida$Rango_de_Velocidad <- as.character(tabla_subida$Rango_de_Velocidad)

# Tabla de frecuencia de velocidad de bajada
tabla_bajada <- data.frame(Rango_de_Velocidad = cut(velocidad_bajada, breaks = rangos, include.lowest = TRUE, na.include = TRUE)) %>%
  count(Rango_de_Velocidad, .drop = FALSE) %>%
  arrange(Rango_de_Velocidad) %>%
  rename(Frecuencia = n) %>%
  mutate(Frecuencia_Relativa = Frecuencia / sum(Frecuencia, na.rm = TRUE),
         Frecuencia_Acumulada = cumsum(Frecuencia))

# Convertir los intervalos de bajada a formato de cadena
tabla_bajada$Rango_de_Velocidad <- as.character(tabla_bajada$Rango_de_Velocidad)

# Imprimir la tabla de frecuencia de velocidad de subida
cat("Tabla de Frecuencia de Velocidad de Subida:\n")
print(tabla_subida)

# Imprimir la tabla de frecuencia de velocidad de bajada
cat("\nTabla de Frecuencia de Velocidad de Bajada:\n")
print(tabla_bajada)

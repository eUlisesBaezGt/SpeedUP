library(ggplot2)
library(dplyr)
library(tidyr)

Mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

# Leer los datos del archivo resultados.csv
data <- read.csv("results.csv")

distancia <- as.numeric(data$distancia)

# Cálculos estadísticos de distancia
media_distancia <- mean(distancia, na.rm = TRUE)
moda_distancia <- Mode(distancia)
desviacion_distancia <- sd(distancia, na.rm = TRUE)

# Rangos de distancia
rango_min_distancia <- floor(min(distancia) / 10) * 10
rango_max_distancia <- ceiling(max(distancia) / 10) * 10
rangos_distancia <- seq(rango_min_distancia, rango_max_distancia, by = 10)

# Tabla de frecuencia de distancia
tabla_distancia <- data.frame(Rango_de_Distancia = cut(distancia, breaks = rangos_distancia, include.lowest = TRUE)) %>%
  count(Rango_de_Distancia) %>%
  arrange(Rango_de_Distancia) %>%
  rename(Frecuencia = n) %>%
  mutate(Frecuencia_Relativa = Frecuencia / sum(Frecuencia),
         Frecuencia_Acumulada = cumsum(Frecuencia))

# Convertir los intervalos de distancia a formato de cadena
tabla_distancia$Rango_de_Distancia <- as.character(tabla_distancia$Rango_de_Distancia)

# Gráfica de frecuencia de distancia
plt_distancia <- ggplot(tabla_distancia, aes(x = Rango_de_Distancia, y = Frecuencia)) +
  geom_bar(stat = "identity", width = 0.8) +
  labs(x = "Rango de Distancia", y = "Frecuencia", title = "Frecuencia de Distancia") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  coord_flip()

# Resultados de distancia
cat("Estadísticas de Distancia:\n")
cat("Media:", media_distancia, "\n")
cat("Moda:", moda_distancia, "\n")
cat("Desviación estándar:", desviacion_distancia, "\n")

plt_distancia

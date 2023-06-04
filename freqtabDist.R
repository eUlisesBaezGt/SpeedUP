data <- read.csv("resultados.csv")

data$distancia <- as.numeric(data$distancia)

# Definir los intervalos de clase
rango_min <- floor(min(data$distancia) / 10) * 10
rango_max <- ceiling(max(data$distancia) / 10) * 10
rangos <- seq(rango_min, rango_max, by = 10)

# Tabla de frecuencia de distancia
tabla_distancias <- data %>%
  mutate(Rango_de_Distancia = cut(distancia, breaks = rangos, include.lowest = TRUE)) %>%
  count(Rango_de_Distancia) %>%
  arrange(Rango_de_Distancia) %>%
  rename(Frecuencia = n) %>%
  mutate(Frecuencia_Relativa = Frecuencia / sum(Frecuencia),
         Frecuencia_Acumulada = cumsum(Frecuencia)) %>%
  filter(Frecuencia != 0)

# Convertir los intervalos de distancias a formato de cadena
tabla_distancias$Rango_de_Distancia <- as.character(tabla_distancias$Rango_de_Distancia)

# Imprimir la tabla de frecuencia de distancia
cat("Tabla de Frecuencia de Distancia:\n")
print(tabla_distancias)

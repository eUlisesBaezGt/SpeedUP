library(ggplot2)
library(stats)

# Leer los datos del archivo resultados.csv
data <- read.csv("results.csv")

velocidad_subida <- data$up
velocidad_bajada <- data$down

# Cálculos estadísticos de subida
media_subida <- mean(velocidad_subida)
moda_subida <- as.numeric(names(table(velocidad_subida))[table(velocidad_subida) == max(table(velocidad_subida))])
desviacion_subida <- sd(velocidad_subida)

# Cálculos estadísticos de bajada
media_bajada <- mean(velocidad_bajada)
moda_bajada <- as.numeric(names(table(velocidad_bajada))[table(velocidad_bajada) == max(table(velocidad_bajada))])
desviacion_bajada <- sd(velocidad_bajada)

# Gráfica de dispersión de velocidad de subida y bajada
ggplot(data, aes(x = up, y = down)) +
  geom_point() +
  labs(x = "Velocidad de subida (Mbps)", y = "Velocidad de bajada (Mbps)",
       title = "Velocidad de Subida vs Velocidad de Bajada") +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  geom_text(x = 40, y = 260, label = paste("y =", round(coef(lm(down ~ up, data))["up"], 2), "x +",
                                           round(coef(lm(down ~ up, data))["(Intercept)"], 2)), size = 4) +
  geom_text(x = 40, y = 250, label = paste("r =", round(cor(velocidad_subida, velocidad_bajada), 2)), size = 4)

# Resultados de subida
cat("Estadísticas de Velocidad de Subida:\n")
cat("Media:", media_subida, "\n")
cat("Moda:", moda_subida, "\n")
cat("Desviación estándar:", desviacion_subida, "\n")

# Resultados de bajada
cat("\nEstadísticas de Velocidad de Bajada:\n")
cat("Media:", media_bajada, "\n")
cat("Moda:", moda_bajada, "\n")
cat("Desviación estándar:", desviacion_bajada, "\n")

# Perform linear regression
lm_model <- lm(down ~ up, data)
slope <- coef(lm_model)["up"]
intercept <- coef(lm_model)["(Intercept)"]
r_value <- cor(velocidad_subida, velocidad_bajada)

# Print the trendline equation and r-value
cat("\n")
cat("y =", round(slope, 2), "x +", round(intercept, 2), "\n")
cat("r =", round(r_value, 2), "\n")

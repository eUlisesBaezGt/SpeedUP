# Carga los datos
data <- read.csv("results.csv")

# Extrae las velocidades de subida y bajada
velocidad_subida <- data$up
velocidad_bajada <- data$down

cat("Mediana de la subida: ", median(velocidad_subida), "\n")
cat("Mediana de la bajada: ", median(velocidad_bajada), "\n")

# Realiza la prueba de Mann-Whitney U
resultado <- wilcox.test(velocidad_subida, velocidad_bajada)

# Imprime el resultado de la prueba
print(resultado)

# Decide si se acepta la hipótesis nula o la alternativa
if (resultado$p.value < 0.05) {
  cat("Como el valor p es menor que 0.05, rechazamos la hipótesis nula. Esto significa que hay una diferencia significativa entre las medianas de la velocidad de subida y la velocidad de bajada, por lo que aceptamos la hipótesis alternativa de que las medianas son diferentes.\n")
} else {
  cat("Como el valor p es mayor que 0.05, no rechazamos la hipótesis nula. Esto significa que no hay una diferencia significativa entre las medianas de la velocidad de subida y la velocidad de bajada, por lo que aceptamos la hipótesis nula de que las medianas son iguales.\n")
}

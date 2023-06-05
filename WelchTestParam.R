# Carga los datos
data <- read.csv("resultados.csv")

# Pide al usuario los nombres de los dos salones que quiere comparar
salon1 <- readline(prompt="Introduce el nombre del primer salón: ")
salon2 <- readline(prompt="Introduce el nombre del segundo salón: ")

# Filtra los datos para obtener solo las mediciones de la velocidad de subida para los dos salones
data_salon1 <- data[data$salon == salon1, "down"]
data_salon2 <- data[data$salon == salon2, "down"]

# Realiza la prueba t
resultado <- t.test(data_salon1, data_salon2)

# Imprime el resultado de la prueba
print(resultado)

# Calcula la diferencia de las medias
diferencia_medias <- mean(data_salon1) - mean(data_salon2)

# Imprime la diferencia de las medias
cat("La diferencia entre las medias es:", diferencia_medias, "\n")

# Realizaremos una prueba t para comparar las medias de la velocidad de subida en dos salones diferentes.
# La hipótesis nula sería que las medias de la velocidad de subida son iguales en los dos salones, y la hipótesis alternativa sería que las medias son diferentes.
# Decide si se acepta la hipótesis nula o la alternativa
if (resultado$p.value < 0.05) {
  cat("Como el valor p es menor que 0.05, rechazamos la hipótesis nula. Esto significa que hay una diferencia significativa entre las medias de la velocidad de subida en los dos salones, por lo que aceptamos la hipótesis alternativa.\n")
} else {
  cat("Como el valor p es mayor que 0.05, no rechazamos la hipótesis nula. Esto significa que no hay una diferencia significativa entre las medias de la velocidad de subida en los dos salones, por lo que aceptamos la hipótesis nula de que las medias son iguales.\n")
}

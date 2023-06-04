library(ggplot2)
library(dplyr)
library(tidyr)

daa <- read.csv("resultados.csv")


# Scatter plot of distance values
plt_distancia <- ggplot(data, aes(x = salon, y = distancia)) +
  geom_point() +
  labs(x = "Salón", y = "Distancia", title = "Valores de Distancia")

plt_distancia



import socket
import netifaces
import speedtest


def obtener_direccion_ip():
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    return direccion_ip


def obtener_direccion_router():
    gateways = netifaces.gateways()
    direccion_router = gateways["default"][netifaces.AF_INET][0]
    return direccion_router


def calcular_distancia(ip1, ip2):
    distancia = abs(int(ip1.split(".")[-1]) - int(ip2.split(".")[-1]))
    return distancia


def encontrar_ubicacion_optima(ip_computadora, puntos_acceso):
    distancia_minima = float("inf")
    ubicacion_optima = None

    for ap in puntos_acceso:
        distancia = calcular_distancia(ip_computadora, ap)
        if distancia < distancia_minima:
            distancia_minima = distancia
            ubicacion_optima = ap

    return ubicacion_optima


def medir_velocidad():
    st = speedtest.Speedtest()
    velocidad_subida = st.upload() / 1000000  # Convertir a Mbps
    velocidad_bajada = st.download() / 1000000  # Convertir a Mbps

    return velocidad_subida, velocidad_bajada


def main():
    resultados = []
    lugar = ""

    for i in range(200):
        if i % 10 == 0:
            lugar = input("Ingrese el nombre del salón: ")

        # Obtener dirección IP de la computadora
        ip_computadora = obtener_direccion_ip()

        # Obtener dirección IP del router
        ip_router = obtener_direccion_router()

        distancia_router = calcular_distancia(ip_router, ip_computadora)
        velocidad_subida, velocidad_bajada = medir_velocidad()

        print(
            f"Salón {lugar}: Velocidad: up {velocidad_subida}, down {velocidad_bajada}, distancia {distancia_router}"
        )
        # Añadir a la lista de resultados
        resultados.append((lugar, distancia_router, velocidad_subida, velocidad_bajada))

    # Guardar resultados en un archivo CSV
    with open("resultados.csv", "w") as archivo:
        archivo.write("salon,distancia,up,down\n")
        for resultado in resultados:
            archivo.write(
                f"{resultado[0]},{resultado[1]},{resultado[2]},{resultado[3]}\n"
            )


if __name__ == "__main__":
    main()

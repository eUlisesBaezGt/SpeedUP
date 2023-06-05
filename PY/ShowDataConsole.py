import speedtest
import socket
import netifaces


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
    # Obtener dirección IP de la computadora
    ip_computadora = obtener_direccion_ip()

    # Obtener dirección IP del router
    ip_router = obtener_direccion_router()

    # Simular varios puntos de acceso en la red
    puntos_acceso = ["192.168.1.100", "192.168.1.200", "192.168.1.300"]

    distancia_router = calcular_distancia(ip_router, ip_computadora)
    ubicacion_optima = encontrar_ubicacion_optima(ip_computadora, puntos_acceso)
    velocidad_subida, velocidad_bajada = medir_velocidad()

    print("Dirección IP de la computadora:", ip_computadora)
    print("Dirección IP del router:", ip_router)
    print("Distancia entre la computadora y el router:", distancia_router)
    print("Ubicación óptima para el punto de acceso:", ubicacion_optima)
    print("Velocidad de subida:", velocidad_subida, "Mbps")
    print("Velocidad de bajada:", velocidad_bajada, "Mbps")


if __name__ == "__main__":
    main()

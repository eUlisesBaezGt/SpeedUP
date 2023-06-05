import csv
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
    writer = None

    for i in range(200):
        if i % 20 == 0:
            # Close the previous file if it's open
            if writer:
                archivo.close()

            # Get a new salon name and create a new CSV file
            lugar = input("Ingrese el nombre del salón: ")
            archivo = open(f"{lugar}_resultados.csv", "a", newline="")
            writer = csv.writer(archivo)
            writer.writerow(["salon", "distancia", "up", "down"])

        # Obtain the computer's IP address
        ip_computadora = obtener_direccion_ip()

        # Obtain the router's IP address
        ip_router = obtener_direccion_router()

        distancia_router = calcular_distancia(ip_router, ip_computadora)
        velocidad_subida, velocidad_bajada = medir_velocidad()

        print(
            f"Salón {lugar}: Velocidad: up {velocidad_subida}, down {velocidad_bajada}, distancia {distancia_router}"
        )
        # Add to the list of results
        resultado = (lugar, distancia_router, velocidad_subida, velocidad_bajada)
        resultados.append(resultado)

        # Write to CSV
        writer.writerow(resultado)

    # Close the last file
    archivo.close()


if __name__ == "__main__":
    main()

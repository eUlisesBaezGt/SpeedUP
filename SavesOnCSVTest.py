import socket
import netifaces
import subprocess
import re

def obtener_direccion_ip():
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    return direccion_ip

def obtener_direccion_router():
    gateways = netifaces.gateways()
    direccion_router = gateways['default'][netifaces.AF_INET][0]
    return direccion_router

def calcular_distancia(ip1, ip2):
    distancia = abs(int(ip1.split(".")[-1]) - int(ip2.split(".")[-1]))
    return distancia

def encontrar_ubicacion_optima(ip_computadora, puntos_acceso):
    distancia_minima = float('inf')
    ubicacion_optima = None

    for ap in puntos_acceso:
        distancia = calcular_distancia(ip_computadora, ap)
        if distancia < distancia_minima:
            distancia_minima = distancia
            ubicacion_optima = ap

    return ubicacion_optima

def medir_velocidad():
    try:
        output = subprocess.check_output(["speedtest-cli", "--json"], timeout=10)
        result = output.decode("utf-8")
        speed_data = re.search(r'"upload": (\d+\.\d+), "download": (\d+\.\d+)', result)
        if speed_data:
            velocidad_subida = float(speed_data.group(1))
            velocidad_bajada = float(speed_data.group(2))
            return velocidad_subida, velocidad_bajada
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass

    return None, None

def main():
    resultados = []

    for _ in range(500):
        # Obtener dirección IP de la computadora
        ip_computadora = obtener_direccion_ip()

        # Obtener dirección IP del router
        ip_router = obtener_direccion_router()

        # Simular varios puntos de acceso en la red
        puntos_acceso = ["192.168.1.100", "192.168.1.200", "192.168.1.300"]

        distancia_router = calcular_distancia(ip_router, ip_computadora)
        ubicacion_optima = encontrar_ubicacion_optima(ip_computadora, puntos_acceso)
        velocidad_subida, velocidad_bajada = medir_velocidad()

        resultado = [ip_computadora, ip_router, distancia_router, ubicacion_optima, velocidad_subida, velocidad_bajada]
        resultados.append(resultado)

    with open('resultados.txt', 'w') as archivo_txt:
        for resultado in resultados:
            archivo_txt.write(f"Dirección IP de la computadora: {resultado[0]}\n")
            archivo_txt.write(f"Dirección IP del router: {resultado[1]}\n")
            archivo_txt.write(f"Distancia entre la computadora y el router: {resultado[2]}\n")
            archivo_txt.write(f"Ubicación óptima para el punto de acceso: {resultado[3]}\n")
            archivo_txt.write(f"Velocidad de subida: {resultado[4]} Mbps\n")
            archivo_txt.write(f"Velocidad de bajada: {resultado[5]} Mbps\n\n")

    print("Datos guardados en el archivo resultados.txt")

if __name__ == '__main__':
    main()
    

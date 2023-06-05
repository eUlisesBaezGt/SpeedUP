import csv

def main():
    resultados = []
    lugar = ""
    writer = None

    for i in range(200):
        if i % 10 == 0:
            # Close the previous file if it's open
            if writer:
                archivo.close()

            # Get a new salon name and create a new CSV file
            lugar = input("Ingrese el nombre del salón: ")
            archivo = open(f"{lugar}_resultados.csv", "w", newline='')
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

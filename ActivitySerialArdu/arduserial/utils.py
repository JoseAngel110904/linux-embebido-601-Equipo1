import os

def find_available_serial_ports() -> list:
    try:
        # Sacar la lista de puertos disponibles
        file_names = os.listdir("/dev")
        #Filtrar a solo los puertos con terminación ttyA
        available_ports = [file for file in file_names if file.startswith("ttyA")]
        return available_ports
    
    except OSError as e:
        # En caso de tener error al encontrar los puertos disponibles, printear en la terminal:
        print("Error al obtener la lista de puertos:", e)
        return []
    
if __name__ == '__main__':
    # Ejemplo de uso:
    available_ports = find_available_serial_ports()
    print("Puertos disponibles:", available_ports)

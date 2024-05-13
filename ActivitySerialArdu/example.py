import time
import serial

PORT = '/dev/ttyACM0'
BAUDRATE = 115200

arduino = serial.Serial(
    port = PORT,
    baudrate = BAUDRATE,
    timeout=2.
)

time.sleep(3)
arduino.write(b'hola')
time.sleep(.5)
recived = arduino.readline()
print(recived)
time.sleep(.5)
recived = arduino.readline()
print(recived)

for i in range(1, 4):
    to_send = f"Prueba {i}"
    arduino.write(to_send.encode(encoding="utf-8"))
    print(f"Enviado: {to_send}")
    time.sleep(0.5)
    recived = arduino.readline()
    print(f"Recibido: {recived}")
    
arduino.close()
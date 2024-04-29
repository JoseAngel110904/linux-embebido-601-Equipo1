# Limpiar archivos generados
clean:
	echo 3 > /sys/class/gpio/unexport

# Definir el objetivo predeterminado
all: export_gpio

# Regla para exportar el pin GPIO
export_gpio:
	echo 3 > /sys/class/gpio/export
	echo out > /sys/class/gpio/gpio3/direction
	cat gpio3
	echo 1 > /sys/class/gpio/gpio3/value

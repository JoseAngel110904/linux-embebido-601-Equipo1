PRG = LEDS
SOURCE = LEDS.C

MCU = atmega328p

CC = avr-gcc


CFLAGS			= -g -Wall -Os -mmcu=$(MCU)

OBJCOPY			= avr-objcopy
OBJDUMP			= avr-OBJDUMP

all: ofile text


clean:
	rm -rf *.o $(PRG)
	rm -rf *.hex


ofile:
	$(CC) $(SOURCE) -o $(PRG) -Wall -Os -mmcu=$(MCU) -I.

text: hex

hex: $(PRG).hex


%.hex:
	$(OBJCOPY) -O ihex $(PRG) $(PRG).hex
install:
	sudo avrdude -p $(MCU) -c usbtiny -v -U flash:w:$(PRG).hex:i
PRG = LEDS
SOURCE = LEDS.c
PROGRAMMER = usbasp

MCU = atmega328p

CC = avr-gcc


CFLAGS			= -g -Wall -Os -mmcu=$(MCU)

OBJCOPY			= avr-objcopy
OBJDUMP			= avr-OBJDUMP

clean:
	rm -rf *.o $(PRG)
	rm -rf *.hex

ofile:
	$(CC) $(SOURCE) -o $(PRG) -Wall -Os -mmcu=$(MCU) -I.

text: hex

hex: $(PRG).hex

%.hex:
	$(OBJCOPY) -O ihex $(PRG) $(PRG).hex

all: ofile text

install:
	sudo avrdude -p $(MCU) -c $(PROGRAMMER) -v -U flash:w:$(PRG).hex:i
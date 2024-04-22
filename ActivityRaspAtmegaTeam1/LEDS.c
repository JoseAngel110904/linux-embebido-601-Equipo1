#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
int main (void){
    DDRC = 0x3E;  // Configurar PC1-PC5 como salidas
    
    while (1) {
        for (int i = 0; i <= 5; i++) {
            PORTC |= (1 << i);      // Enciende el LED i (i-ésimo bit)
            _delay_ms(500);         // Espera 500 ms
            PORTC &= ~(1 << i);     // Apaga el LED i
            _delay_ms(500);         // Espera 500 ms
        }
    }

    return 0;
}
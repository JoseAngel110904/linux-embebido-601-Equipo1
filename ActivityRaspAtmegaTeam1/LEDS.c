#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay>
int main (void){
    DDRB = (1<<PB2);
    PORTB = 0xFF;
    while(1){
        PORTB = (1<<PB2);
        _delay_ms(1500);
        PORTB &= 0xFB;
        _delay_ms(1500);
    }
}
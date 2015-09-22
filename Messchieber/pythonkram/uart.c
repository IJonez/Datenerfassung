#include <avr/io.h>
#include <avr/delay.h>

#define F_CPU 12000000L
#define BAUD 9600L

#define UBRR_VAL ((F_CPU+BAUD * 8)/(BAUD*16)-1)		//clever runde
#define BAUD_REAL (F_CPU/(16*(UBRR_VAL+1)))			//reale Baudrate

#define BAUD_ERROR ((BAUD_REAL*1000)/BAUD-1000)		//Fehler in Promille

#if ((BAUD_ERROR>10)||(BAUD_ERROR<-10))
#error Systematischer Fehler in der Baudrate größer 1% und damit zu hoch!
#endif
 

int main(void)
{	
	UBRRH = UBRR_VAL >> 8;
	UBRRL = UBRR_VAL & 0xFF;
	
	UCSRB = (1<<RXEN)|(1<<TXEN);		//UART TX einschalten
	UCSRC = (1<<URSEL)|(1<<USBS)|(3<<UCSZ0);		//Asynchron 8N1

	while (!(UCSRA & (1<<UDRE)))		//warten bis Senden möglich
	{
	}	

	UDR = 'x';							//schreibt das Zeichen x auf die Schnittstelle
	_delay_ms(100);

	return 0;	
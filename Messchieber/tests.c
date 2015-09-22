#include <avr/io.h>
#include <stdint.h>

uint32_t ms_data;

int main(void)
	{
	DDRB = 0Xff; \\ sets Port B as input (ff = 11111111)
	PORTB = 0x03; \\ sets pin 0 and 1 as "1" (03 = 11)
	
	while(1)
		{
		\\Nothing
		}
	return 0;
	}
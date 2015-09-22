#include <avr/io.h>
#include <stdlib.h>
#include <uart.c>
#include <stdint.h>


#define F_CPU 8000000
#define BAUD 38400L      // Baudrate


//Pins for the caliper
#define ms_vcc_line PD5
#define ms_clock_line PD7
#define ms_data PD6
#define ms_gnd_line PB0

uint32_t ms_daten;
uint8_t i;


// calcs for the uart
#define UBRR_VAL ((F_CPU+BAUD*8)/(BAUD*16)-1)   // clever runden
#define BAUD_REAL (F_CPU/(16*(UBRR_VAL+1)))     // Reale Baudrate
#define BAUD_ERROR ((BAUD_REAL*1000)/BAUD) // Fehler in Promille, 1000 = kein Fehler.

#if ((BAUD_ERROR<990) || (BAUD_ERROR>1010))
  #error Systematischer Fehler der Baudrate groesser 1% und damit zu hoch!
#endif



int main(void)
	{
	DDRD = (0xff);     //sets Port D as input (ff = 11111111)
	PORTB = 0x03;  //sets pin 0 and 1 as "1" (0x03 = 11)
	i = 0;
	while(1)
		{
		static char old_level = 0;
		  char new_level;

		  new_level = (PIND7 != 1);
		  if( !old_level && new_level )
		  {
			  if (i < 23)
			  			{
			  				i += 1;
			  				if (PIND & (1<<ms_clock_line))
			  				{
			  				    ms_daten (0<<1); //reverses the invert from the transistors
			  				}
			  				else
			  				{
			  				    ms_daten (1<<1); //reverses the invert from the transistors
			  				}
			  			}

			  			if (i == 24)
			  			{
			  				uart_puts(ms_daten);
			  				i = 0;
			  			}
		  }
		  old_level = new_level;
		}
	return 0;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

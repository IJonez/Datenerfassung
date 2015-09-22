/*
 * uart.h
 *
 *  Created on: 08.04.2011
 *      Author: mf5435s
 */


//#undef F_CPU

#ifndef F_CPU
#define F_CPU 16000000UL
#endif

#define BAUD 38400L      // Baudrate

// Berechnungen
#define UBRR_VAL ((F_CPU+BAUD*8)/(BAUD*16)-1)   // clever runden
#define BAUD_REAL (F_CPU/(16*(UBRR_VAL+1)))     // Reale Baudrate
#define BAUD_ERROR ((BAUD_REAL*1000)/BAUD) // Fehler in Promille, 1000 = kein Fehler.


#if ((BAUD_ERROR<990) || (BAUD_ERROR>1010))
  #error Systematischer Fehler der Baudrate grösser 1% und damit zu hoch!
#endif



#include <avr/interrupt.h>
#include <avr/pgmspace.h>
#include <ctype.h>




//Externe Funktionsprototypen
void uart_init(void);
void uart_puts (char *s);
void uart_putuint(uint8_t value);
int uart_putc(unsigned char c);
uint8_t uart_cmd_recieved(void);
uint8_t uart_cmd_len(void);
char * uart_cmd(void);
void uart_putc_hex(uint8_t b);
void uart_putw_hex(uint16_t w);
void uart_putdw_hex(uint32_t dw);
void uart_putw_dec(uint16_t w);
void uart_putdw_dec(uint32_t dw);
void uart_puts_p(PGM_P str);
void uart_put_int( const int val );
void uart_put_uint( const uint16_t val );

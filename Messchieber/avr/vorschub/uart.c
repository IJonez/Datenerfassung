/*
 * uart.c
 *
 *  Created on: 18.04.2011
 *      Author: Marco Feldmann
 */

#include "uart.h"
#include <avr/interrupt.h>
#include <ctype.h>
#include <stdlib.h>
#include <avr/pgmspace.h>
#include <avr/sfr_defs.h>




#define UART_MAXSTRLEN  200

volatile uint8_t char_count = 0;
volatile uint8_t cmd_len =  0;
volatile uint8_t cmd_buf_len = 0;
volatile char input_buffer[UART_MAXSTRLEN + 1] = "";
volatile char command_buffer[UART_MAXSTRLEN + 1] = "";
volatile struct {
   unsigned command_complete:1;
   unsigned cmd_in_process:1;
   unsigned buf_overflow:1;
   unsigned init_done:1;
   unsigned rec_status:1;
} uart_status;



//Bereitgestellte Funktionen:

//Initialisieren des UARTS
void uart_init(void){

	 UCSRC = (1<<URSEL)|(1<<UCSZ1)|(1<<UCSZ0);  // Asynchron 8N1
  	 UBRRH = UBRR_VAL >> 8;
     UBRRL = UBRR_VAL & 0xFF;
     UCSRB=(1<<RXEN)|(1<<TXEN)|(1<<RXCIE);
     sei();
     uart_status.init_done = 1;
     uart_status.command_complete = 0;
}






//Einzelnes Zeichen senden
int uart_putc(unsigned char c)
{
    while (!(UCSRA & (1<<UDRE)))  /* warten bis Senden moeglich */
    {
    }
    UDR = c;                      /* sende Zeichen */
    return 0;
}



//Zeichenkette senden
/* puts ist unabhaengig vom Controllertyp */
void uart_puts (char *s)
{
    while (*s)
    {   /* so lange *s != '\0' also ungleich dem "String-Endezeichen" */
        uart_putc(*s);
        s++;
    }
}


uint8_t uart_cmd_recieved(void){
	if(uart_status.command_complete==1){ //
		return 1;
	}
	else{
		return 0;
	}

}


uint8_t uart_cmd_len(void){
	return cmd_buf_len;

}




ISR(USART_RXC_vect) {
	uint8_t in_char;
	uint8_t l_i;
	in_char = UDR;
	//uart_putc(in_char);

	/* Das erste Zeichen eines neuen Kommandos wird überprüft.
	 * Falls das ein 'x' ist, wird das Kommando über die Zeichenlänge gesteuert und nicht
	 * mit dem LF beendet.
	 */
	if(char_count == 0){
		if(in_char==120){					//ASCII-Nummer für 'x'
			//Längengesteuerter Modus
			uart_status.rec_status = 1;
			cmd_len = 10;
		}
		else{
			//Terminatorzeichen-gesteuerter Modus, Default
			uart_status.rec_status = 0;
		}
	}


	if(uart_status.rec_status == 1){ //Längegesteuerte Modus
		input_buffer[char_count] = in_char;
		char_count++;

		if(char_count==4){
			cmd_len = in_char;
			cmd_len = cmd_len + 8;
		}
		if(char_count == cmd_len){
			char_count--;
			for(l_i = 0; l_i <= char_count;l_i++){
				command_buffer[l_i] = input_buffer[l_i];
				//uart_putc(command_buffer[l_i]);
			}
			//uart_putc('\n');
			cmd_buf_len = char_count;
			char_count = 0;
			//uart_puts("CMD-Buf_Len:");
			//uart_putuint(cmd_buf_len);
			uart_status.command_complete = 1;
			uart_status.rec_status = 0;


		}


	}
	else{ //Default-Mode: Terminatorzeichen beendet Kommando
		if(in_char == '\n')
		{
			for(l_i = 0; l_i <= char_count;l_i++){
				command_buffer[l_i] = input_buffer[l_i];
			}
			command_buffer[char_count] = '\0';
			char_count = 0;
			uart_status.command_complete = 1;
		}
		else{
			input_buffer[char_count] = in_char;
			char_count++;
		}
	}



}

void uart_putuint(uint8_t value){
	char out[3];
	uart_puts( itoa( value, out, 10 ));
	return;
}


char* uart_cmd(void){
	uart_status.command_complete = 0;
	return command_buffer;

}


void uart_put_int( const int val ){
	char buffer[10];
	uart_puts( itoa( val, buffer, 10 ) );
}

void uart_put_uint( const uint16_t val ){
	char buffer[10];
	uart_puts( utoa( val, buffer, 10 ) );
}

void uart_putc_hex(uint8_t b)
{
    /* upper nibble */
    if((b >> 4) < 0x0a)
        uart_putc((b >> 4) + '0');
    else
        uart_putc((b >> 4) - 0x0a + 'a');

    /* lower nibble */
    if((b & 0x0f) < 0x0a)
        uart_putc((b & 0x0f) + '0');
    else
        uart_putc((b & 0x0f) - 0x0a + 'a');
}

void uart_putw_hex(uint16_t w)
{
    uart_putc_hex((uint8_t) (w >> 8));
    uart_putc_hex((uint8_t) (w & 0xff));
}

void uart_putdw_hex(uint32_t dw)
{
    uart_putw_hex((uint16_t) (dw >> 16));
    uart_putw_hex((uint16_t) (dw & 0xffff));
}

void uart_putw_dec(uint16_t w)
{
    uint16_t num = 10000;
    uint8_t started = 0;

    while(num > 0)
    {
        uint8_t b = w / num;
        if(b > 0 || started || num == 1)
        {
            uart_putc('0' + b);
            started = 1;
        }
        w -= b * num;

        num /= 10;
    }
}

void uart_putdw_dec(uint32_t dw)
{
    uint32_t num = 1000000000;
    uint8_t started = 0;

    while(num > 0)
    {
        uint8_t b = dw / num;
        if(b > 0 || started || num == 1)
        {
            uart_putc('0' + b);
            started = 1;
        }
        dw -= b * num;

        num /= 10;
    }
}

void uart_puts_p(PGM_P str)
{
    while(1)
    {
        uint8_t b = pgm_read_byte_near(str++);
        if(!b)
            break;

        uart_putc(b);
    }
}

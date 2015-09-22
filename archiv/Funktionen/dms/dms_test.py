#!/usr/bin/python
import RPi.GPIO as GPIO
#import time
from string import maketrans
from time import clock

#for spi usage
#import spidev
import os

#for 1-wire-bus
import sys

def read_ADS1232(DRDY=29, SCLK=31):
	#std GPIO for DataReady is 29, for SerialClock 31
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	#declares which pin is In which is Out
	GPIO.setup(DRDY, GPIO.IN)
	GPIO.setup(SCLK, GPIO.OUT)
	a = 0

	#Data is retrieved once

	while GPIO.input(DRDY) == False:
		GPIO.OUT(SCLK, True)
		GPIO.OUT(SCLK, False)
		i = 0
		while i<24:
			a+= DRDY
			GPIO.OUT(SCLK, True)
			GPIO.OUT(SCLK, False)
			i += 1				
		#Forces DRDY to "high", so a data ready state can be recognized
		GPIO.OUT(SCLK, True)
		GPIO.OUT(SCLK, False)
		print(a)
	return(zwokompdez(a))
	
def zwokompdez(a):
#wandelt ein zweierkomplement in dezimal um
    a=str(a)
    a='0b'+a
    if a[2]=='0':
        return(int(a,2))
    else:
        b=len(a)
        a=int(a,2)        
        a=a-1
        a=bin(a)
        if len(a) < b:
            a=-(pow(2, len(a)-1)/2)
            return(int(a))
        else:    
            b='0b'
            i=2
            while i < len(a):
                if a[i] == '0':
                    b += '1'
                else:
                    b += '0'
                i+=1           
            a=b
            a=int(a,2)
            a=-a    
            return(a)

			
while True:
    
    dmswert = read_ADS1232()
    print(dmswert)
    
    
    
	

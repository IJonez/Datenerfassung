#!/usr/bin/python
#Datnerfassung zur Eisschraubenmessvorrichtung (Baugruppe 2.301.X-X) von ADS1232
#author db
#blandfort@fh-aachen.de
import RPi.GPIO as GPIO
import time
import os
import sys
import spidev

spi = spidev.SpiDev()
spi.open(0,0)


DRDY=21
SCLK=23

#std GPIO for DataReady is 29, for SerialClock 31
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#declares which pin is In which is Out
GPIO.setup(DRDY, GPIO.IN)
GPIO.setup(SCLK, GPIO.OUT)

ausgabe = ''
i = 0
actual = 0

def ISR_DRDY(channel):
    global ausgabe
    global i
    global actual
    spi.open(0,0)
    actual = time.time()
    #Data is retrieved once
    print('in der ISR')
    ausgabe = spi.readbytes(3)
    #spi.close()
    print('spi gelesen')				
    #Forces DRDY to "high", so a data ready state can be recognized
    #GPIO.output(SCLK, 1)
    #time.sleep(.0001)
    #GPIO.output(SCLK, 0)
    
    #print( actual - time.time() )
    print(ausgabe)
    ausgabe = str(ausgabe)
    #print(zwokompdez(ausgabe))
    print(ausgabe)
    ausgabe = ''

def zwokompdez(a):
#wandelt ein zweierkomplement in dezimal um
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




GPIO.output(SCLK, 1)
GPIO.output(SCLK, 0)	

GPIO.add_event_detect(DRDY, GPIO.FALLING, callback = ISR_DRDY)

try:
    while True:
        print('sleeping')
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()


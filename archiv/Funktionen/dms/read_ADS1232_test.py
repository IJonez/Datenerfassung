#!/usr/bin/python
#Datnerfassung zur Eisschraubenmessvorrichtung (Baugruppe 2.301.X-X) von ADS1232
#author db
#blandfort@fh-aachen.de
import RPi.GPIO as GPIO
import time
import os
import sys


DRDY=29
SCLK=31
#std GPIO for DataReady is 29, for SerialClock 31
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#declares which pin is In which is Out
GPIO.setup(DRDY, GPIO.IN)
GPIO.setup(SCLK, GPIO.OUT)
a = 0

def ISR_DRDY(channel):
    global ausgabe
    #Data is retrieved once
    while GPIO.input(DRDY) == False:
        actual = time()
        GPIO.OUT(SCLK, True)
        GPIO.OUT(SCLK, False)
        i = 0
        global a = 0
        while i<24:
            ausgabe += DRDY
            GPIO.OUT(SCLK, True)
            GPIO.OUT(SCLK, False)
            i += 1				
        #Forces DRDY to "high", so a data ready state can be recognized
        GPIO.OUT(SCLK, True)
        GPIO.OUT(SCLK, False)
        print( actual - time() )
        print(ausgabe)

GPIO.add_event_detect(DRDY, GPIO.Falling, callback ISR_DRDY)

try:
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    GPIO.cleanup()


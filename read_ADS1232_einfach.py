#!/usr/bin/python
#Datnerfassung zur Eisschraubenmessvorrichtung (Baugruppe 2.301.X-X) von ADS1232
#author db
#blandfort@fh-aachen.de
import RPi.GPIO as GPIO
import time
import os
import sys

DRDY = 29
SCLK = 31
PWDN = 15

#std GPIO for DataReady is 29, for SerialClock 31
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

#declares which pin is In which is Out
GPIO.setup(DRDY, GPIO.IN)
GPIO.setup(SCLK, GPIO.OUT)
GPIO.setup(PWDN, GPIO.OUT)

ausgabe = ''
i = 0



def ISR_DRDY(channel):
    #retrieves data from ADS1232
    global ausgabe
    global i
    ausgabe = ''

    #Data is retrieved once
    print('in der ISR')
    GPIO.remove_event_detect(DRDY)
    
    while i < 24:
        ausgabe = str(ausgabe)
        GPIO.output(SCLK, 1)
        time.sleep(.0001)
        ausgabe += str(GPIO.input(DRDY))
        GPIO.output(SCLK, 0)
        time.sleep(.0001)
        i += 1
       

    #Forces DRDY to "high", so a data ready state can be recognized
    GPIO.output(SCLK, 1)
    time.sleep(.0001)
    GPIO.output(SCLK, 0)
    
    print(ausgabe)
    i = 0
    ausgabe = ''
    GPIO.add_event_detect(DRDY, GPIO.FALLING, callback = ISR_DRDY)

GPIO.add_event_detect(DRDY, GPIO.FALLING, callback = ISR_DRDY)

#init der Messhardware
GPIO.output(PWDN, 0)
time.sleep(1)
GPIO.output(PWDN, 1)

GPIO.output(SCLK, 0)

try:
    while True:
        time.sleep(1)                        
except KeyboardInterrupt:
    GPIO.cleanup()


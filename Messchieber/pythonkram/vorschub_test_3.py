
#!/usr/bin/python

#Datenerfassung zur Eisschraubenmessvorrichtung ( Baugruppe 2.301.X-X)
#Necessary for time declerations and GPIO usage
import RPi.GPIO as GPIO
import time
#for spi usage
import os
print('start')
#for 1-wire-bus
import sys
counter = 0
ms_daten = 33
ms_clock = 35 
i = 0
data_in = 0
weg = 0
print('deklaration')
#std. GPIO for Data is 33, for Clock 35
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#declares which pin is In which is Out
GPIO.setup(ms_daten, GPIO.IN)
GPIO.setup(ms_clock, GPIO.IN)

GPIO.add_event_detect(ms_clock, GPIO.RISING)
print('vor der schleife')
while counter  < 3:
    print('aeussere schleife')
    while i < 24:
        #print('innere schleife')
        if GPIO.event_detected(ms_clock):
            data_in =str(GPIO.input(ms_daten)) + str(data_in)
            i += 1
            print(i)
            print(data_in)
        weg = str(data_in)[4:23]
    print('wieder draussen')
#weg = int(weg, 2)           
#   if str(data_in)[3] == True:
 #      weg = weg*(-1)
    weg = '0b' + weg
    print(int(weg, 2))
    print('--------------------------------------------------------')
    i=0
    data_in = 0
    weg = 0
    counter +=1
GPIO.cleanup()

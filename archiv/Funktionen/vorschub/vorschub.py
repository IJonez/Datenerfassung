#!/usr/bin/python

#Datenerfassung zur Eisschraubenmessvorrichtung ( Baugruppe 2.301.X-X)
#Erfassung des Messchiebers
#Necessary for time declerations and GPIO usage
import RPi.GPIO as GPIO
import time

#std. GPIO for Data is 33, for Clock 35
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#declares which pin is In which is Out
GPIO.setup(ms_daten, GPIO.IN)
GPIO.setup(ms_clock, GPIO.IN)

i = 0
data_in = '0'
ms_daten = 33
ms_clock = 35
weg = 0

def ISR(channel):
    global i
    global data_in
    global ms_daten

    actual_t = time.time()
    if actual_t - last_t > 0.0005:
        print('datapoint invalid')
        i = 0
    else:
        data_in = data_in.insert(0, GPIO.input(ms_daten))
        i += 1
        if i == 24:
            data_out = data_in
    last_t = time.time()    
     
# add rising edge detection on a the clock channel to trigger dta collection


GPIO.add_event_detect(ms_clock, GPIO.RISING, callback = ISR)  

while True:
    time.sleep(0.0001)
    print('sleeping')
    if i == 25:
        weg = data_out[4:23]
        if data_out[3] == True:
            weg *= (-1)
        else:
            print(weg)
    else:
        print('still awaiting data')



    


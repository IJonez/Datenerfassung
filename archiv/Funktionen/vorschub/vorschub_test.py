#!/usr/bin/python

#Datenerfassung zur Eisschraubenmessvorrichtung ( Baugruppe 2.301.X-X)
#Necessary for time declerations and GPIO usage
import RPi.GPIO as GPIO
import time

#std. GPIO for Data is 33, for Clock 35
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    #declares which pin is In which is Out
    GPIO.setup(ms_daten, GPIO.IN)
    GPIO.setup(ms_clock, GPIO.IN)

def ISR(channel)
    global i
    global data_in
    global ms_daten
    
    while i < 25:
        data_in = data_in.insert(0, GPIO.input(ms_daten))
        i += 1
    weg = data_in[4:23]
    if data_in[3] == True:
        weg *= (-1)
        
    # add rising edge detection on a the clock channel to trigger dta collection


GPIO.add_event_detect(ms_clock, GPIO.RISING, callback = ISR)  

while True:
    time.sleep(1)
    print('sleeping')
    
    for i < 25:
        if GPIO.event_detected(ms_clock):
            data_in = data_in.insert(0, GPIO.input(ms_daten))
            i+=1
    weg = data_in[4:23]           
    for data_in[3] == True:
        weg = weg*(-1)
    print(weg)

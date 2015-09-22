#!/usr/bin/python

#Datenerfassung zur Eisschraubenmessvorrichtung ( Baugruppe 2.301.X-X)
#Erfassung des Messchiebers
#Necessary for time declerations and GPIO usage
import RPi.GPIO as GPIO
import time

#std. GPIO for Data is 33, for Clock 35
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ms_daten = 33
ms_clock = 35

#declares which pin is In which is Out
GPIO.setup(ms_daten, GPIO.IN)
GPIO.setup(ms_clock, GPIO.IN)

i = 0
data_in = '0b'
data_out = '0b'
weg = 0
drdy_flag = 0
last_t = time.time()

def ISR(channel):
    global last_t
    global drdy_flag
    global data_out
    global data_in
    global i
    drdy_flag = 0
    ms_daten = 33
    
    #print('isr gestartet')
    actual_t = time.time()
    if actual_t - last_t > .0025:
        print('datapoint invalid')
        i = 0
        data_in = '0b'
    else:
        data_in += str(GPIO.input(33))
        #print(data_in)
        i += 1
        #print(i)
        if i == 23:
            data_out = data_in
            drdy_flag = 1
            i = 0
            data_in = '0b'
    last_t = time.time()    
     
# add rising edge detection on a the clock channel to trigger dta collection


GPIO.add_event_detect(ms_clock, GPIO.RISING, callback = ISR)  

while True:
    try:
        time.sleep(0.1)
        #print('sleeping')
        if drdy_flag == 1:
            #print(data_out)
            weg = data_out[4:]
            #print(data_out)
            #print(weg)
            if data_out[3] == True:
                weg *= (-1)
                print(weg)
            else:
                print(weg)
            drdy_flag = 0
        #else:
            #print('still awaiting data')
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()



        

    


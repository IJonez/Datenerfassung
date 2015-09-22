#!/usr/bin/python
#Datenerfassung zur Eisschraubenmessvorrichtung ( Baugruppe 2.301.X-X)
#author db
#infos? Fuck off!

import RPi.GPIO as GPIO
import time
import os
import sys

ms_daten = 33
ms_clock = 35 
clk_cntr = 0
data_in = ""
counter = 0
periode = 0
time_set_1 = time.clock()
time_set_2 = time.clock()

def ISR_CLK_RISE(channel):
    global time_set_2
    global time_set_1
    global period
    global data_in
    global ms_daten
    global ms_clock
    global clk_cntr
    
    time_set_2 = time.clock()
    periode = time_set_2 - time_set_1
    time_set_1 = time.clock()
    if periode > 0.000000000000026:
        if clk_cntr < 23:
            clk_cntr = 0
            data_in = ''
            #print('data aquisition error')
        else:
            data_in = str(GPIO.input(ms_daten)) + data_in
    else:
        data_in = str(GPIO.input(ms_daten)) + data_in
    if clk_cntr == 23:
        print(data_in)
        data_in = ''
        clk_cntr = 0
    else:
        clk_cntr +=1
        
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#declares which pin is In which is Out
GPIO.setup(ms_daten, GPIO.IN)
GPIO.setup(ms_clock, GPIO.IN)

GPIO.add_event_detect(ms_clock, GPIO.RISING, callback = ISR_CLK_RISE)

try:
    
    while True:
        time.sleep(100)
        
        
except KeyboardInterrupt:
    GPIO.cleanup()


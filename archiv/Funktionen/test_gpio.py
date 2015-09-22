#!/usr/bin/python
import RPi.GPIO as GPIO
ms_daten = 33
ms_clock = 35


GPIO.setmode(GPIO.BOARD)
GPIO.setup(ms_daten, GPIO.IN)
GPIO.setup(ms_clock, GPIO.IN)
data_in = 0
clock = 0
i = 0
 
while i < 15:
    data_in = GPIO.input(ms_daten)
    clock = GPIO.input(ms_clock)
    print(data_in)
    print(clock)
    i += 1

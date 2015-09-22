#!/usr/bin/python
#Datenerfassung zur Eisschraubenmessvorrichtung ( Baugruppe 2.301.X-X)
#Necessary for time declerations and GPIO usage
import RPi.GPIO as GPIO
import time
#std. GPIO for Data is 33, for Clock 35
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#declares which pin is In which is Out
GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)

j = 0
weg = '0b'

def isr:
    global bit
	global zeit
	    
	bit.insert(0, gpio.input(33))
	zeit.insert(0, time.time())

GPIO.add_event_detect(35, GPIO.RISING)

time.sleep(1)

try:	
    while True:
        if j+25 <= len(bit):
            delta_t[j] = zeit[j+1] - zeit[j]
		    if delta_t[j] >= t_pause_halbe:
	            weg = bit[j:j+25]
			    print(weg)
		    j += 1
	except KeyboardInterrupt:
	    GPIO.cleanup()
		exit()   
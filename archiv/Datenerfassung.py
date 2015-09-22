#!/usr/bin/python

#Datenerfassung zur Eisschraubenmessvorrichtung ( Baugruppe 2.301.X-X)
#Necessary for time declerations and GPIO usage
import RPi.GPIO as GPIO
import time
from string import maketrans

#for spi usage
import spidev
import os

#for 1-wire-bus
import sys
  
#Variablen
#GPIOs am Raspberry für Drehmomentmessung
pin_DRDY = 29
pin_SCLK = 31
#GPIO input der drehzahlmessung
pin_dreh = 0

        #Konstanten des Biegebalkens
I = 10000
E = 210000
l_Motor = 0.01
l_Balken = 0.01
  
# Open SPI bus
#spi = spidev.SpiDev()
#spi.open(0,0)

timestr = time.strftime("%Y-%m-%d-%H-%M")

fobj_out = open('messwert' + timestr+ '.txt',"w")
fobj_out.write('Time		Drehzahl		Moment		T1		T2		T3')
fobj_out.write('----------------------------------------------------------------------------------------------------------------------------')

while True:
    GPIO.add_event_detect(29, GPIO.FALLING)
    GPIO.add_event_detection(11, GPIO.RISING)
    if GPIO.event_detected(29):
        T_roh = read_ADS1232(pin_DRDY, pin_SCLK)
    Torque = torque(I, E, l_Motor, l_Balken)
    Temperaturen = read_DS1820
    drehzahl_regelung()
    fobj_out.write('%s        %d        %d        %s' %timestr, %drehzahl, %Torque, %Temperaturen)
    
    









		

     		
		


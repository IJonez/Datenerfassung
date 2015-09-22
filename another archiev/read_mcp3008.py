#!/usr/bin/python
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
#Function ton convert pressure from digital data

def ConvertPressure(data,places):
  pressure = ((data * 3.30)/float(1023))/0.2
  pressure = round(pressure,places)
  return temp
 
# Define sensor channels
p_channel_0 = 0
p_channel_1 = 1
p_channel_2 = 2
p_channel_3 = 3

# Define delay between readings
delay = 5
 
print "time	channel_0	channel_1	channel_2	channel_3"
 
while True:
 
   #read channels
   pressure_data = ReadChannel(p_channel_0)
   p_volt = ConvertVolts(pressure_data,2)
   pressure_0 = p_volt / 0.2
  
   pressure_data = ReadChannel(p_channel_1)
   p_volt = ConvertVolts(pressure_data,2)
   pressure_1 = p_volt / 0.2
  
   pressure_data = ReadChannel(p_channel_2)
   p_volt = ConvertVolts(pressure_data,2)
   pressure_2 = p_volt / 0.2
  
   pressure_data = ReadChannel(p_channel_3)
   p_volt = ConvertVolts(pressure_data,2)
   pressure_3 = p_volt / 0.2


   #get the timestamp as a tuple
   lt = localtime()		                                                                        
   stunde, minute, sekunde = lt[3:5] 
   
   # Print out results
   print "--------------------------------------------"
   print "%02i.%02i.%04i	%d	%d	%d	%d" %(stunde, minute, sekunde, pressure_0, pressure_1, pressure_2, pressure_3)
 
   # Wait before repeating loop
   time.sleep(delay)
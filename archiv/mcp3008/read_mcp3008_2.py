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
 
 
 # function: read and parse sensor data file
def read_sensor(path):
  value = "U"
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
  except (IOError), e:
    print time.strftime("%x %X"), "Error reading", path, ": ", e
  return value

# define pathes to 1-wire sensor data
pathes = (
  "/sys/bus/w1/devices/10-000801b5a7a6/w1_slave",
  "/sys/bus/w1/devices/10-000801b5959d/w1_slave"
)
 
 
 
# Define sensor channels
p_channel_0 = 0
p_channel_1 = 1
p_channel_2 = 2
p_channel_3 = 3
t_channel_1 = 4
t_channel_2 = 6
t_channel_3 = 5
d_channel_1 = 7

# define variables
p_volt_0 = 0.000
p_volt_1 = 0.000
p_volt_2 = 0.000
p_volt_3 = 0.000
t_volt_4 = 0.000
t_volt_5 = 0.000
t_volt_6 = 0.000
d_volt_7 = 0.000


#define sensitivity of pressure  sensor
Sensitivity = 2.000
sens_t = 0.0039083 #not the usual definition of a sensitivity!

#fefine reference voltage of MCP3008
vref = 5.000 

#define variables and set them zero

pressure_data = 0.000

pressure_0 = 0.000
pressure_1 = 0.000
pressure_2 = 0.000
pressure_3 = 0.000

temp_1 = 0.000
temp_2 = 0.000
temp_3 = 0.000

distance = 0.000
# Define delay between readings
delay = 2

#define a timestring for filename
timestr = time.strftime("%Y-%m-%d-%H-%M")

#open file for datastorage 
fobj_out = open('Data_'+timestr+'.txt', "w")




#write header on screen
print "time	channel_0	channel_1	channel_2	channel_3	channel_4	channel_5	channel_6	channel_7"

#write header in file 
fobj_out.write("time	channel_0	channel_1	channel_2	channel_3	channel_4	channel_5	channel_6	channel_7 \n") 

while True:
 
   #read pressure channels and convert to bar and volts
   pressure_data = ReadChannel(p_channel_0)
   p_volt_0 = pressure_data * vref / 1024
   pressure_0 = (p_volt_0 / Sensitivity)
  
   pressure_data = ReadChannel(p_channel_1)
   p_volt_1 = pressure_data * vref / 1024
   pressure_1 = (p_volt_1 / Sensitivity)

   pressure_data = ReadChannel(p_channel_2)
   p_volt_2 = pressure_data * vref / 1024
   pressure_2 = (p_volt_2 / Sensitivity)

   pressure_data = ReadChannel(p_channel_3)
   p_volt_3 = pressure_data * vref / 1024
   pressure_3 = (p_volt_3 / Sensitivity)

   #read temperature channels and convert to Celsius and Volt
   temperature_data = ReadChannel(t_channel_1)
   t_volt_4 = temperature_data * vref / 1024
   temp_1 = ((t_volt_4 / 50) - 0.1) / (sens_t * 0.1)
   
   temperature_data = ReadChannel(t_channel_2)
   t_volt_5 = temperature_data * vref / 1024
   temp_2 = ((t_volt_5 / 50) - 0.1) / (sens_t * 0.1)
   
   temperature_data = ReadChannel(t_channel_3)
   t_volt_4 = temperature_data * vref / 1024
   temp_3 = ((t_volt_6 / 50) - 0.1) / (sens_t * 0.1)
   
   #get onewire temps
   # read sensor data
   tow = 'N'
   tow += ':'
   tow += read_sensor(path)
   
   #get the timestamp as a tuple
   lt = time.localtime()		                                                                        
   
      
   # Print out results
   print "---------------------------------------------------------------------------------------------------"
   print time.strftime(("%c") ,lt),
   print "%8.4f		%8.4f	%8.4f	%8.4f	%8.4f	%8.4f	%8.4f" % (pressure_0, pressure_1, pressure_2, pressure_3, temp_1, temp_2, temp_3)
   print time.strftime(("%c") ,lt),
   print "%8.4f		%8.4f	%8.4f	%8.4f	%8.4f	%8.4f	%8.4f" % (p_volt_0, p_volt_1, p_volt_2, p_volt_3, t_volt_4, t_volt_5, t_volt_6, t_volt_7)
               
  
     
   #print in file
   fobj_out.write("------------------------------------------------------------------------------------------ \n")
   fobj_out.write(time.strftime(("%c") ,lt),)
   fobj_out.write("%8.4f		%8.4f	%8.4f	%8.4f	%8.4f	%8.4f	%8.4f" % (pressure_0, pressure_1, pressure_2, pressure_3, temp_1, temp_2, temp_3))
   fobj_out.write(time.strftime(("%c") ,lt),)
   fobj_out.write("%8.4f		%8.4f	%8.4f	%8.4f	%8.4f	%8.4f	%8.4f" % (p_volt_0, p_volt_1, p_volt_2, p_volt_3, t_volt_4, t_volt_5, t_volt_6, t_volt_7))
   
   # Wait before repeating loop
   time.sleep(delay)

#closing file
fobj_out.close()

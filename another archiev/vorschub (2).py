import RPi.GPIO as GPIO        																			## Import GPIO Library
import time, re, os                    																	## Import 'time' library (for 'sleep')
 
																										##dev variables
counter = 0
delta_l = 0
measurement_const = 1 																				    ## Constant depending of the measurement unit
inPin = 13                    																			## Input from distance measurement connected to pin 13
lt = localtime()																					    ## localtime as a tuple
jahr, monat, tag = lt[0:2]																				## Entpacken des Tupels, Datum
filename = "%02i.%02i.%04i" % (tag,monat,jahr)
target = open('filename.txt' 'w')

##initialise GPIO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

GPIO.setmode(GPIO.BOARD)      																			 ## Use BOARD pin numbering
GPIO.setup(inPin, GPIO.IN)                                                                               ## Set pin 13 to INPUT
 
																										 ## function: read and parse sensor data file
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
  "/sys/bus/w1/devices/10-000801b5a7a6/w1_slave",														##hier unbedingt die eigenen seriennummern eintragen
  "/sys/bus/w1/devices/10-000801b5959d/w1_slave"
)
 
 
while True:                     																		 ## Do this forever
    value = GPIO.input(inPin)  																			 ## Read input from switch
    if value:                																			 ## If switch is released
		counter = counter + 1																			 ## Count ticks 
		delta_l = delta_l + counter * measurement_const
		lt = localtime()		                                                                         ## localtime as a tuple
		stunde, minute, sekunde = lt[3:5]                                                                ## Entpacken des Tupels, Datum
	
# read sensor data
  data = 'N'
  for path in pathes:
  data += ':'
  data += read_sensor(path)
   
  target.write("%02i.%02i.%04i	delt_l= %d	temp=%s") % (stunde,minute,sekunde,delta_l,data)             ## Write a line with time and the datapoint
  time.sleep(1)
	 
 
GPIO.cleanup()               																			 ## Cleanup
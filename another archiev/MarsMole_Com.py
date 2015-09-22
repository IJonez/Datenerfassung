import serial #importing package to read serial data port
import io

#information on programming serialports from http://pyserial.sourceforge.net/shortintro.html

#open 7th serial port, must be adjusted for used port
ser=serial.Serial(7)

#define bauds (for MarsMole 38400)
ser.baudrate = 38400

#check which port has been opened
print ser.name 

ser.write("ping")
res = ser.read(20)

if res != pong
 
 print 'No connection established'
 
 else 
  print 'connection established'
  while True
	 ser.write("get_temps \n")
	 res = ser.read(200)
	 print '%s', %res
	 
	 ser.write("is_force")
	 res = ser.read(10)
	 print '%s', %res
	 
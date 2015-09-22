import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

i = 0
dutycycle = 0
p = GPIO.PWM(16,50)

p.start(0)


try:
    while True:
        try:
            dutycycle_input = float(input('Drehzahl? \n'))
            while i < 50:
                dutycycle += (dutycycle_input - dutycycle)*0.1
                i += 1
                time.sleep(.1)
                print(dutycycle)
            dutycycle = dutycycle_input
            i = 0
            if dutycycle < 0:
                GPIO.output(18, GPIO.HIGH)
                dutycycle = abs(dutycycle)
                
            else: 
                GPIO.output(18, GPIO.LOW)
            if GPIO.input(22) == True:
                print('stk fault')                
                exit()
       
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit()
        else:
            p.ChangeDutyCycle(dutycycle)
        
except KeyboardInterrupt:
           GPIO.cleanup()
           exit()
p.stop()
GPIO.cleanup
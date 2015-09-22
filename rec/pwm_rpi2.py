import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(40, GPIO.IN)

i = 0
dutycycle = 0
p = GPIO.PWM(16,50)
diff = 0.5

p.start(0)



try:
    while True:
        try:
            dutycycle_input = float(input('Drehzahl? \n'))
            if dutycycle_input == 200:
                p.ChangeDutyCycle(0)
                p.stop()
                GPIO.cleanup()
                exit()
            print('vor der schleife')
            diff = 0.5     
            while i < 50:
                print('in der shcleife')
                dutycycle += (dutycycle_input - dutycycle)*0.1
                time.sleep(.01)
                if dutycycle < 0:
                    GPIO.output(18, GPIO.HIGH)
                    dutycycle = abs(dutycycle)
                    print('in der verzweigung')
                else:
                   GPIO.output(18, GPIO.LOW)
                i += 1
                p.ChangeDutyCycle(dutycycle)
                             
            dutycycle = abs(dutycycle_input)
            p.ChangeDutyCycle(dutycycle)
            i = 0
                
            if GPIO.input(40) == True:
                print('stk fault')                
                exit()
       
        except KeyboardInterrupt:
            p.stop()
            GPIO.cleanup()
            exit()
                
except KeyboardInterrupt:
           p.stop()
           GPIO.cleanup()
           exit()

           
                   

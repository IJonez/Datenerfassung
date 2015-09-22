def read_ADS1232(DRDY=29, SCLK=31):
	#std GPIO for DataReady is 29, for SerialClock 31
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	
	#declares which pin is In which is Out
	GPIO.setup(DRDY, GPIO.IN)
	GPIO.setup(SCLK, GPIO.OUT)
	a = 0

	#Data is retrieved once

	while GPIO.input(DRDY) == False:
		GPIO.OUT(SCLK, True)
		GPIO.OUT(SCLK, False)
		i = 0
		while i<24:
			a+= DRDY
			GPIO.OUT(SCLK, True)
			GPIO.OUT(SCLK, False)
			i += 1				
		#Forces DRDY to "high", so a data ready state can be recognized
		GPIO.OUT(SCLK, True)
		GPIO.OUT(SCLK, False)
		print(a)
	return(zwokompdez(a))

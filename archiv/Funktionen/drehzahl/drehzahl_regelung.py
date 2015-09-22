def drehzahl_regelung(cycle = 20, pwm_out = 16, gran = 10, DMA = 0, energize = 18, fault = 22):

    from RPIO import PWM
    import RPI.GPIO as GPIO
    GPIO set.mode(GPIO.BOARD)
    GPIO.setup(pwm_out, GPIO.OUT)
    GPIO.setup(energize, GPIO.OUT)
    GPIO.setup(fault, GPIO.IN)
			
    fahrt=input('geschwindigkeit eingeben, 0=voll rück, 100=voll vorwärts, 50=stillstand \n')
#Überprüfung der Eingabe
    if fahrt >100:
        return('Ungültige Eingabe, Wert ist größer Einhundert')
    if fahrt < 0:
        return('Ungültige Eingabe, Wert ist kleiner Null')
#initialisierung des pwm kanals
    pwm.init_channel(DMA, cycle)
#regelung zum sanften anlaufen/abbremsen des Motors
    if fahrt < 50:
        GPIO.output(energize, GPIO.HIGH)
	for ed_soll != ed_ist:
            ed_soll = (fahrt / 50) * (cycle / gran)				
            ed_ist += (ed_soll-ed_ist)/10
	    clear_channel(DMA)
	    add_channel_pulse(DMA, pwm_out, 0, ed_ist)
    if fahrt > 50:
        for ed_soll != ed_list:
	    GPIO.output(energize, GPIO.LOW)
	    ed_soll = (fahrt / 50) * (cycle / gran)
	    ed_ist += (ed_soll-ed_ist)/10
	    clear_channel(DMA)
	    add_channel_pulse(DMA, pwm_out, 0, ed_ist)
    else:
        return('Ein Fehler ist aufgetreten')
#Regelung zum halten des eingestellten Bruchteils der Leerlaufdrehzahl
    rps_1 = ed_soll
    rps_2 = ed_soll
    rps_3 = ed_soll
    rps_4 = ed_soll
    rps_5 = ed_soll
	
#integrative regelung über die letzten fünf Messwerte
    while True:
        durchschnitt = (rps_1 + rps_2 + rps_3 + rps_4 + rps_5) / 5
	delta = (leerlauf / 50) * ed_soll) - durchschnitt
	delta = (leerlauf / 50) * ed_soll) - durchschnitt
        ed_ist += delta * 50 / ed_soll
        clear_channel(DMA)
	add_channel_pulse(DMA, pwm_out, 0, ed_ist)			
	rps_5 = rps_4
	rps_4 = rps_3
	rps_3 = rps_2
	rps_2 = rps_1
	rps_1 = drehzahl_messung()
	
	
		
		
	    
	    

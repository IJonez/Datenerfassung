#function to read turns per second of the motor (not the gear!)

def drehzahl_messung(turns_input = 11):
    start = time.time()
    while t < 1:
        actual = time.time()
        t = start - actual
        if (GPIO.input(turns_input)) == True:
            i=+1
    return(i/t)

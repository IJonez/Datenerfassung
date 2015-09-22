While True:
    from RPIO import PWM
    drehzahl=input('Drehzahl? \n')
    
    #Setup PWM and DMA channel 0
    #Be advised that BCM numbering of the GPIOs is obligatory to use this function
    PWM.setup()
    PWM.init_channel(0, 200)

    PWM.add_channel_pulse(0, 17


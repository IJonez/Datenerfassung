def torque(I, E, l_Motor, l_Balken):
        dms_wert = read_ADS1232()
        dms_wert = a/16777216 #24bit a/d wandler signal
        T = dms_wert*I*E*(l_Motor/l_Balken)
        return(T)

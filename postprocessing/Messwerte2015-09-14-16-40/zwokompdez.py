import time
import sys
from os import system 


def zwokompdez(a):
#wandelt ein zweierkomplement in dezimal um

    if a[0] == '0':
        return(int(a,2))
    else:
        a = '0b' + a
        b = len(a)
        a = int(a,2)
        a = a-1
        a = bin(a)
        if len(a) < b:
            a =- (pow(2, len(a)-1)/2)
            return(int(a))
        else:
            b = '0b'
            i = 2
            while i < len(a):
                if a[i] == '0':
                    b += '1'
                else:
                    b += '0'
                i += 1
            a = b
            a = int(bin(a),2)
            a =- a
            return(a)

fobj_in = open('Messwerte.txt')
fobj_out_m = open('Messwerte_m' + '.txt',"w")
fobj_out_dez = open('Messwerte_dez' + '.txt',"w")
n = 1

for line in fobj_in:
    #print('for_schleife')
                
    if n > 3:
	
        if len(line) >= 1:
            #print('ifverzweigung')
            line = str(line)
            ausgabe = str(zwokompdez(line))
            Moment = float(ausgabe) * 0.00037216558669
            
            print(str(ausgabe))
            fobj_out_dez.write(str(ausgabe) +'\n')
            fobj_out_m.write(str(Moment) + '\n')		
    n += 1



fobj_in.close()
fobj_out_dez.close()
fobj_out_m.close()
system('gnuplot -persist test_daten.gp')
input('ende')


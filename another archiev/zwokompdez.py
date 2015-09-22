import time
import sys


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

fobj_in = open('Messwerte_roh.txt')
fobj_out = open('Messwerte_dez' + 'txt',"w")
i = 1
for line in fobj_in:
    #print('for_schleife')
                
    if i > 3:
        if len(line) == 0:
            fobj_in.close()
            fobj_out.close()
            print('ende')
        #print('ifverzweigung')
        line = str(line)
        ausgabe = str(zwokompdez(line))
        Moment = (ausgabe / 8388608) *4,27*10**(-10)* 70*10**9*0,06/0,07/0,004
        print(ausgabe)
        fobj_out.write(ausgabe + Moment '\n')
    i += 1

fobj_in.close()
fobj_out.close()
input('ende')


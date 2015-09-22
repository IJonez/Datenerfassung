def zwokompdez(a):
#wandelt ein zweierkomplement in dezimal um
    a='0b'+a
    if a[2]=='0':
        return(int(a,2))
    else:
        b=len(a)
        a=int(a,2)        
        a=a-1
        a=bin(a)
        if len(a) < b:
            a=-(pow(2, len(a)-1)/2)
            return(int(a))
        else:    
            b='0b'
            i=2
            while i < len(a):
                if a[i] == '0':
                    b += '1'
                else:
                    b += '0'
                i+=1           
            a=b
            a=int(a,2)
            a=-a    
            return(a)


while True:
    a=input('Bitte zahl eingeben \n')
    a=zwokompdez(a)
    print(a)


	

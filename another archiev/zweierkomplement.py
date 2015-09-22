
print('Zahl eingeben')
b = input('zwoerkomplement eingeben')





def zwokompdez(a):
    if a[0] == 1:
        a= '0b' + a
        print(a)
    else:
        a = bin(a)
        a-=1
        i = 0
        print(a)
        for elements in a:
            print(i)
            if a[i] == 1:
                a[i] = 0
            else:
                a[i] = 1
            i+=1
            print(a)
        a = '0b' + a 
        a = -a 
    return(a)

b = zwokompdez(b)
print(b)

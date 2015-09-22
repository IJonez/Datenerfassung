#!/usr/bin/python

fobj = open("test.txt", "w")
a= 1
b=3
c=4
d= 'abc234'
eingabe = str(a)+str(b)+str(c) +'\n' + d
fobj.write('%d \t %d \t %d \t %s' %(a, b, c, d))
print(str(a), b, c, d)
print(eingabe)
fobj.close()



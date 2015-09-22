import numpy as np
import Gnuplot
import time
import matplolib

i = 0

    
x = i
y1 = x**2
y2 = 10*np.sin(np.pi*x)

g = Gnuplot.Gnuplot(persist = 1)
d1 = Gnuplot.Data(x,y1, with_= 'lp', title = 'd1')
d2 = Gnuplot.Data(x,y2, with_= 'l', title = 'd2')

g('set grid')
g('set key left ')

g.plot(d1, d2)

while True:
    
    x = i
    y1 = x**2
    y2 = 10*np.sin(np.pi*x)

    g = Gnuplot.Gnuplot(persist = 0)
    d1 = Gnuplot.Data(x,y1, with_= 'lp', title = 'd1')
    d2 = Gnuplot.Data(x,y2, with_= 'l', title = 'd2')

    g('set grid')
    g('set key left ')

    g.reread
    

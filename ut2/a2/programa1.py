import sys
import math
from math import sqrt

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

discriminante = (b**2-4*a*c)

if a == 0:
    x = -c / b
    print (x, 'ecuación ya no es de segundo grado')
elif discriminante < 0:
    print (discriminante, 'ecuación sin solucion')
else:
    x1 = (-b+sqrt(b**2-4*a*c))
    print (x1, 'resultado')

    x2 = (-b-sqrt(b**2-4*a*c))
    print (x2,'resultado')

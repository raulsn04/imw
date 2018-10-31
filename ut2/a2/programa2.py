import sys
import math
from math import sqrt

x1,x2,x3,y1,y2,y3 = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])

d = sqrt(((x1-x2)**2)+((y1-y2)**2))
d1 = sqrt(((x1-x3)**2)+((y1-y3)**2))

if d < d1:
    print(d, 'Está más cercano  a' (x1-x2), 'es' (y1-y2), 'y está a una distancia de', d)


else d1 < d:
    print(d1, 'El punto más cercano a' (x1-x3), 'es' (y1-y3), 'y está a una distancia de', d1)

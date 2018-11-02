import sys
import math

n = int(sys.argv[1])
s = 0
if n < 0:
    print(n, 'Error, número negativo')
    sys.exit('Cerrando programa')

for n in range(1, n+1):
    s+=n**2
print(s)

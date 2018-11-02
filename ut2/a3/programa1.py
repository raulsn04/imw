import sys
import math

n = int(sys.argv[1])

if n < 0:
    print(n, 'Error, número negativo')
    sys.exit('Cerrando programa')
for e in range (2, n):
    if n % e == 0:
        print('Es primo')
        break
else:
print('No es primo')

import sys
import math

calc, calc1 = int(sys.argv[1]), int(sys.argv[2])

if calc < 0 or calc1 < 0:
    print('Error, sin solución')
    sys.exit('Cerrando programa')
else:
    if calc < calc1:
        min = calc
    elif calc > calc1:
        min = calc1
    else:
        print('Máximo común divisor es', calc)
        sys.exit('Cerrando programa')

    for a in range(min, 0 , -1):
        if calc % a == 0 and calc1 % c == 0:
            print('el maximo comun divisor es', a)
            break

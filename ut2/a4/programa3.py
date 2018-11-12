import sys
import math

k, cadena = int(sys.argv[1]), sys.argv[2]
longitud = 0
if k < 0:
    print('Error, el número no es positivo')
    sys.exit()
else:
    palabras = cadena.split(' ')

    for i in palabras:
        if len(i) == k:
            longitud += 1
print('Hay esta cantidad', longitud, ' de palabras de', k, 'letras')

import sys
import math

k, cadena = int(sys.argv[1]), sys.argv[2]


if k < 0:
    print('Error, el número no es positivo')
    sys.exit()
else:
    cadena = sys.argv[2]
    palabras = cadena.split(' ')
    longentrada = 0

    for i in range(len(palabras)):
        longitud = len(palabras[i])
        if longitud == k:
            longentrada += 1

    if longentrada == 0:
        print(f'No cumple los requisitos {k}')
    elif longentrada == 1:
        print(f'La palabra es de tamaño {k}')
    else:
        print(f'Hay {longentrada} palabras de tamaño {k}')

import sys
import math

dni = int(sys.argv[1])
cadena = 'TRWAGMYFPDXBNJZSQVHLCKE'
resto = cadena [dni % 23]

print(str(dni)+resto)

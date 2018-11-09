import sys
import math

a = int(sys.argv[1])
cadena = 'TRWAGMYFPDXBNJZSQVHLCKE'
resto = cadena [a % 23]

print(str(a)+resto)

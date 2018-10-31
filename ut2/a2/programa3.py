import sys
import math

nota = float(sys.argv[1])

if nota <5:
    print('Suspenso')
if nota >= 5 and nota <7:
    print('Aprobado')
if nota >= 7 and nota <9:
    print('Notable')
if nota >= 9 and nota <10:
    print('Sobresaliente')
if nota == 10:
    print('Matricula de honor')

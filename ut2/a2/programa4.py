import sys
import math
from math import pi

r = float(sys.argv[1])

print('Menú')
print('(1)Calcular el díametro de la circunferencia')
print('(2)Calcular el perímetro de la circunferencia')
print('(3)Calcular el área del circulo')
print('(4)Salir')


calcula = input['Elija la opción:']

if calcula == '1':
    d = 2 * r
    print('El diámetro es', d)
elif calcula == '2':
    p = 2 * math.pi * r
    print('El perímetro es', p)
elif calcula == '3':
    a = math.pi * r ** 2
    print('El area es', a)
elif calcula == '4':
    print('Salir')
else:
    print('Se acabó el programa')

import sys

flotante = 0.0

for i in range(1, len(sys.argv)):
    valores = float(sys.argv[i])
    flotante += valores
media = flotante / (len(sys.argv) - 1)

print('La media de los valores es {media}')

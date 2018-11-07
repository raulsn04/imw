import sys
import math

a = int(sys.argv[1])
b = 1

if a < 0:
    print('Error, sin resultado')
else:
    for c in range(1, a+1):
        b *= c
        print(c, '!=', b)

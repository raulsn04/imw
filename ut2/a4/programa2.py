import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
Adenine = 0
Guanine = 0
Cytosine = 0
Thymine = 0

for var in sequence:
    if var == 'A':
        Adenine += 1
    elif var == 'T':
        Thymine += 1
    elif var == 'G':
        Guanine += 1
    else:
        Cytosine += 1


print('Thymine', Thymine)
print('Guanine', Guanine)
print('Cytosine', Cytosine)
print('Adenine:', Adenine)

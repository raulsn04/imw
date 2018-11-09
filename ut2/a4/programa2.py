import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
A = 0

for v in range(100):
    if sequence == 'A':
        A += 1
print('Adenine:', A)

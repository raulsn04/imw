import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])


for v in range(100):
    if sequence == NUCLEOBASES:
        NUCLEOBASES += 1
print('Adenine')

import sys

def count_words(sentence):

    repite = sentence.split()
    summary = {}
    contador = 0

    for buscar in repite:
        if buscar in summary:
            summary [buscar] += 1
        else:
            summary [buscar] = 1

    return summary
sentence = sys.argv[1]
for clave, valor in 

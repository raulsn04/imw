import sys


def num_vowels(text):

    letras = 0

    for a in text:
        if a == 'a':
            letras = letras + 1

    for e in text:
        if e == 'e':
            letras = letras + 1

    for o in text:
        if o == 'o':
            letras = letras + 1

    for i in text:
        if i == 'i':
            letras = letras + 1

    for u in text:
        if u == 'u':
            letras = letras + 1

    return letras

def num_whitespaces(text):

    espacio =" "
    numero = 0

    for i in text:
        if i in espacio:
            numero += 1
    return numero


def num_digits(text):

    numeros ="0123456789"
    digito = 0

    for i in text:
        if i in numeros:
            digito += 1
    return digito


def num_words(text):

    palabras = 0
    return


def reverse(text):

    reverso = 0

    for i in range (-1, 0):
        if i in reverso:

    return reverso


def length(text):

    longitud = 0

    for i in text:
        if len(text) == 0:
            longitud = len(text)
            longitud += 1

    return longitud


def halfs(text):
    # ...
    return


def upper_vowels(text):
    return


def sorted_by_words(text):
    # ...
    return


def length_of_words(text):
    # ...
    return


text = sys.argv[1]
print("Number of vowels:", num_vowels(text))
print("Number of whitespaces:", num_whitespaces(text))
print("Number of digits:", num_digits(text))
print("Number of words:", num_words(text))
print("Reverse of text:", reverse(text))
print("Length of text:", length(text))
print("Halfs of text:", halfs(text))
print("Text with uppercased vowels:", upper_vowels(text))
print("Sorted by words:", sorted_by_words(text))
print("Length of words:", length_of_words(text))

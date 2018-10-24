import sys

importe = int(sys.argv[1])

billetes50= importe // 50
resto50= importe % 50
billetes20 = resto50 // 20
resto20= importe % 20
billetes10 = resto20 // 10
resto10= importe % 10
billetes5= resto10 // 5
resto5= importe % 5

if importe !=0:
    if resto == 1:
        print(billetes50)
    if importe > 1:
        print(billetes20)

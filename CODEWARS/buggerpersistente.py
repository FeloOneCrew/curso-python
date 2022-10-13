"""
Escribe una función, persistence, que tome un parámetro positivo numy devuelva su persistencia multiplicativa, que es el número de veces que debes multiplicar los dígitos numhasta llegar a un solo dígito.

Por ejemplo (Entrada --> Salida) :

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number) 
"""
import operator
import functools

#Solucion 1
cont = 0
def persistence(n):
    global cont
    mult = 1
    # your code
    if len(str(n)) <= 1:
        return cont
    else:
        for i in str(n):
            mult *= int(i)
        cont += 1
        if len(str(mult)) > 1:
            return persistence(mult)
    return cont

#Solucion 2
def persistence1(n):
    cont1=0
    # your code
    while len(str(n)) > 1:
        Mul = 1
        for i in str(n):
            Mul*= int(i)
            n = Mul
        cont1 += 1
    return cont1

def persistence2(n):
    i = 0
    while n>=10:
        n=functools.reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i


print(persistence(999))
print(persistence1(999))
print(persistence2(999))



            
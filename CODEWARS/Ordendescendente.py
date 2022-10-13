"""
   Su tarea es crear una función que pueda tomar cualquier número entero no negativo como argumento y devolverlo con sus dígitos en orden descendente. Esencialmente, reorganiza los dígitos para crear el número más alto posible.

Ejemplos:
Entrada: 42145 Salida:54421
Entrada: 145263 Salida:654321
Entrada: 123456789 Salida:987654321
"""


from ast import Num


def descending_order(num):
    mayor = 0
    dato = ""
    #Creando la lista
    lista = []
    for i in str(num):
        lista.append(i)
    lista.sort(reverse=True)
    for x in lista:
        dato= dato + str(x)
    dato =int(dato)
    return dato


def descending_order2(num):
    return int("".join(sorted(str(num), reverse=True)))


def descending_order3(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        print('Non-negative integer expected')


numero = 1872
numero2 = 59861789
numero3 = -1

print(descending_order(numero))
print(descending_order2(numero2))
print(descending_order3(numero3))



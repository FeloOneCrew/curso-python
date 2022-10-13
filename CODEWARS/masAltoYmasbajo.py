"""
 En esta pequeña tarea, se le da una cadena de números separados por espacios y tiene que devolver el número más alto y el más bajo.

Ejemplos
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

"""
from operator import index


def high_and_low(numbers):
    # ...
    lista = []
    n = numbers.split(" ")
    for x in n:
        lista.append(int(x))
    num = str(max(lista)) + " " + str(min(lista))
    return num

felo = input("Ingresar varios numeros dejando un espacion encada uno: ")
print(high_and_low(felo))
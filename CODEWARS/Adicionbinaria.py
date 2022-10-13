"""
Implemente una función que sume dos números y devuelva su suma en binario. La conversión se puede hacer antes o después de la adición.

El número binario devuelto debe ser una cadena.

Ejemplos:(Entrada1, Entrada2 --> Salida (explicación)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""

def add_binary(a,b): 
    binario = bin(a+b).replace('0b','')
    return str(binario)

def add_binary2(a,b):
    return bin(a+b)[2:]

def add_binary3(a,b):
    return '{0:b}'.format(a + b)

print(add_binary2(1,1))
print(add_binary(1,1))
print(add_binary3(1,1))
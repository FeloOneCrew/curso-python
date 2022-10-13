"""
Bienvenidos. En este kata, se le pide que eleve al cuadrado cada dígito de un número y los concatene.

Por ejemplo, si ejecutamos 9119 a través de la función, saldrá 811181, porque 9 2 es 81 y 1 2 es 1.

Nota: La función acepta un número entero y devuelve un número entero 
"""

def square_digits(num):

    new_list = [str(int(i)**2) for i in str(num)]

    return int(''.join(new_list))
   
print(square_digits(3212))
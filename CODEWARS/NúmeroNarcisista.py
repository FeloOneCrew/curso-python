"""def multiply(a, b):
   mul = a * b
   return mul
    
print(multiply(2,4))
"""
"""
Un Número Narcisista es un número positivo que es la suma de sus propios dígitos, cada uno elevado
a la potencia del número de dígitos en una base dada. En este Kata, nos limitaremos al decimal (base 10).

Por ejemplo, tome 153 (3 dígitos), que es narcisista:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
y 1652 (4 dígitos), que no es:
 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
 
"""

num = 153

def narcissistic(num):
    numero = num
    suma = 0
    largo= len(str(numero))
    
    for n in str(numero):
        x = int(n)**largo
        suma += x
        
    return suma

dato = narcissistic(num)
if dato == num :
        print(True,"El numero es Narcisita")
else:
    print(False,"El numero NO es Narcisita")

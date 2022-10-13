"""
Algunos números tienen propiedades divertidas. Por ejemplo:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Dado un entero positivo n escrito como abcd... (a, b, c, d... siendo dígitos) y un entero positivo p

queremos encontrar un entero positivo k, si existe, tal que la suma de las cifras de n elevadas a las sucesivas potencias de p sea igual a k * n.
En otras palabras:

¿Existe un número entero k como: (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

Si es el caso devolveremos k, si no devolveremos -1.
 
"""

def dig_pow(n, p):
    # your code
    suma = 0
    potencia= p
    for i in str(n):
        suma+= int(i)**potencia
        potencia += 1
        
    valor = suma // n
    if  (valor*n) != suma:
        return -1
    return valor

def dig_pow1(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1

print(dig_pow(92, 1))
print(dig_pow1(92, 1))

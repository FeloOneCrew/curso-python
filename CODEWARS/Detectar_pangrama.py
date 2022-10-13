"""
Un pangrama es una oración que contiene todas las letras del alfabeto al menos una vez. Por ejemplo, la oración "El rápido zorro marrón salta sobre el perro perezoso" es un pangrama, porque usa las letras AZ al menos una vez (las mayúsculas y minúsculas son irrelevantes).

Dada una cadena, detectar si es o no un pangrama. Devuelve True si lo es, False si no. Ignora los números y la puntuación. 
"""

def is_pangram(s):
    
    lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for b in lista:
        s = s.lower()
        if  s.find(b) == -1:
            return False
    return True

def is_pangram1(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False
        
print(is_pangram("aBcdefghijklmnopqr1tuvWxyz"))
print(is_pangram1("aBcdefghijklmnopqr1tuvWxyz"))
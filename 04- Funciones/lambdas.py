"""
Pequeñas funciones anónimas pueden ser creadas con la palabra 
reservada lambda. Esta función retorna la suma de sus dos
argumentos: lambda a, b: a+b Las funciones Lambda pueden ser 
usadas en cualquier lugar donde sea requerido un objeto de tipo 
función. Están sintácticamente restringidas a una sola expresión. 
Semánticamente, son solo azúcar sintáctica para definiciones 
normales de funciones. Al igual que las funciones anidadas, 
las funciones lambda pueden hacer referencia a variables desde 
el ámbito que la contiene:
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
"""

sumar= lambda a,b: a+b
doble= lambda n: n*2
par= lambda n:n%2==0
impar= lambda n:n%2!=0
revertir= lambda cadena:cadena[::-1] # revertir un nombre o leerlo de manera inversa
print(sumar(20,6))
print(doble(6))
print(par(7))
print(impar(5))
nom= input("Ingrese la palabra a invertir: ")
print(f"La palabra a revertir {nom}",revertir(nom))


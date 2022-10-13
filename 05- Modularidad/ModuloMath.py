import math as m

felo=m.floor(4.99) #La instruccion m.floor redondea hacia abajo 
print(felo)

felo= m.ceil(4.99)#La instruccion m.floor redondea hacia arriba
print(felo)

#Sumar una lista

n=[0.99, 1, 2 , 3]
felo= m.fsum(n)

print(felo)

#Realizar un truncamiento
"""
En matemáticas, truncamiento es el término usado para referirse a reducir 
el número de dígitos a la derecha del separador decimal, descartando los menos 
significativos.
""" 

felo= m.trunc(46.745)
print(felo)

felo=m.pow(5,4) #Sacar la potencia de 5 a la 4, siempre imprime un float
felo= int(felo) #Convierto a un entero
print(felo)

felo= m.sqrt(25) #Raiz cuadradra de un numero, siempre imprime un float
print(felo)

#Obtener el valor de PI
felo= m.pi
print(felo)
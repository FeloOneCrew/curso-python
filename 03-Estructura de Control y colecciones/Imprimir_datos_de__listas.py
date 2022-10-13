datos= ["Andrés","Gómez",33,"Medellin","ROBLEDO", True,15]

"""
#Imprimir una lista con for
for dato in datos:
   print(dato)
"""
"""
#Imprimir una lista con While
c=0
""" 

"""
while c< len(datos): #'Len' me indica la cantidad de elementos que tiene la lista,
    print(datos[c])
    c+=1
"""

#range(desde donde inicia, hasta donde termina, cuanto saltos de datos (ejemplo de 2 en 2))
for n in range(0,len(datos),2):
    print(datos[n])



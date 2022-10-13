from collections import deque

#-----utilizar una lista como Cola
"""
ambién es posible usar una lista como una cola, 
donde el primer elemento añadido es el primer elemento 
retirado («primero en entrar, primero en salir»); sin embargo, 
las listas no son eficientes para este propósito. Agregar y 
sacar del final de la lista es rápido, pero insertar o sacar 
del comienzo de una lista es lento (porque todos los otros 
elementos tienen que ser desplazados por uno).

Para implementar una cola, utiliza collections.deque el cual 
fue diseñado para añadir y quitar de ambas puntas de forma rápida.
"""
'''
'''
print("Esto es una Cola")
datos=deque([1, 2, 3, 4, 5 , 6 , 7, 8]) #asi se crea una cola, con el deque. es parecida a una lista
print(datos)
p=0
y= int(len(datos))
while p < y:
    datos.popleft()#Con este eliminamos el primer registro de la cola popleft
    print(datos)
    p+=1
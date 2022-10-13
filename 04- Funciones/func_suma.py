"""
Se indica la *args por convencion para indicar argumentos
indeterminados por posición
"""
def sumar(*args):
    suma=0
    for n in args:
        suma +=n
    return suma


SumaTotal= sumar(1,2,3,4,5,6,7)
print("La suma  total es: ", SumaTotal)

#---------------------------------------------
"""
Se indica la **kwargs por convencion para indicar argumentos
indeterminados por nombre
*args = se convierten en una tupla
**kwargs =  se convierten en un diccionario
"""

def sumar(*args, **kwargs):
    suma=0
    for n in args:
        suma +=n
    return suma , kwargs


SumaTotal, datos= sumar(1,2,3,4,8,nombre ="felo", apellido= "Crew", edad= 33)
print("La suma  total es: ", SumaTotal)
print(datos)
#---------------------------------------------
"""
Generar una lista(el tamaño de la lista debe de generarse 
de manera automatica aleatoriamente entre 1 y 20)con numeros 
generados de manera automatica aleatoriamente entre 1 y 100 y
enviar esa lista creada a una funcion para que esta, halle el valor 
total de los los numeros de la lista generada.
"""
import random
def aleat(datos):
    suma=0
    for n in datos:
        suma +=n
    return suma 


datos=[]
felo= random.randint(1, 20)
print("El tamaño de la lista es: ",felo )
for n in range(felo):
    crew= random.randint(1, 100)
    datos.append(crew)

#datos= tuple(datos)
print(datos)
SumaT= aleat(datos)
print("La suma  total e s: ", SumaT)
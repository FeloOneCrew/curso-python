"""
Aplicación 02: Crear un sistema que detecte si un carácter es vocal o no
Enunciado: dado un carácter determinar si es una vocal.
Análisis: para la solución de este problema, se requiere que el usuario 
ingrese un carácter y el sistema verifique si es una vocal.

"""

v= ("a","e","i","o","u","A","E","I","O","U")
x= input("Ingresar cualquier caracter del teclado: ")
felo = x in v
if str(felo) == "True":
    print (f"El caracter {x} indicado es una VOCAL")
else:
    print (f"El caracter {x} indicado NO es una VOCAL")

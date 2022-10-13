"""
funcines, para declarar una funciones se indica la
palabra reservada "def"
"""
"""
“return”, en la declaración de una función, indica
 que “se ha terminado” de procesar lo que se estuviera 
 haciendo dentro de la función.
 y devuelve un valor.

La palabra reservada “return” en la declaración de una función 
es simple, pero guarda algunos secretos, sin ir más lejos podemos 
encontrar funciones declaradas que tengan uno o incluso varios 
de estos tipos de return:

- Return que devuelve un valor.
- Return que devuelve varios valores.
- Return None.
- Return vacío (en inglés, “return void”).
- Sin Return.

"""
def saludar():
    #global nombre
    nombre = "Felipe Gómez"
    edad= 33
    #print("Hola MUNDO,FUNCION SALUDAR")
    return "Hola MUNDO,FUNCION SALUDAR", nombre, edad
#saludar() #Llamamos la funciones para que se ejecute lo que est dentro de esta.
#print(saludar())
#valor=saludar()
#print(valor) #Distintas maneras de imprimir el resultado desde una funcion

saludo, nombre1, edad = saludar()
print(saludo)
print(nombre1, edad)
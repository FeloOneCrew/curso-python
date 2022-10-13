"""
Son las funciones que ya vienen predeterminadas o definidas en el 
lenguaje de programación y que solo reutilizamos
"""

from msilib.schema import Binary


felo = 15
print(felo)
felo = str(15) #Convierto un entero en string
print("El numero en string ",felo)
felo = float(15) #Convierto un entero en flotante
print(felo)
felo= "ONE CREW" # len Indica la longitud de una cadena de caracteres, incluyendo el espacio
print(len(felo))
felo= 48.55955959
print(round(felo,2))

"""
La función eval() se utiliza para evaluar cadenas de texto que 
pueden contener expresiones o distintos tipos de estructuras de 
datos que pueden utilizarse con Python, tales como listas, tuplas, 
diccionarios y otros objetos que admiten asignación.

"""
crew= eval('felo *2-7/8') #eval me evalua una cadena de caracteres y me hace la operación
print(round(crew,2))
num= 150
print(bin(num))
print(int(0b10010110)) #Convertir un binario a un entero
print(bin(254))

"""
Practica 01: Palíndromo
•	Crear un sistema que detecte si una palabra es palíndroma o no
•	Para solucionar este problema el usuario tiene que ingresar por 
    pantalla una palabra y el sistema verificas si es palíndromo o no.
•	Una palabra palíndroma se lee de igual formo como de la derecha 
    y de la izquierda.

"""
"""
rever= lambda cadena:cadena[::-1]
palabra= input("Ingrese una palabra para identificar si es Palíndroma: ")
#palabra = "ana"
p= rever(palabra)
#print(rever(palabra))
if palabra =="":
    print("Ingresar una palabra")
    
elif palabra== p:
    print(f"La palabra {palabra} es Políndroma")
else:
    print(f"La palabra {palabra} NO es Políndroma")
"""


def palindrimo(palabra):
    palabra= palabra.replace(" ","")
    palabra=palabra.lower()
    PInver=palabra[::-1]

    if palabra == PInver:

        return True
    else:
        return False

def main():
    palabra = input("Ingrese una palabra para identificar si es Palíndroma: ")
    es_palindroma= palindrimo(palabra)
    
    if palabra == "":
        print("Ingrese una palabra o frase")

    elif es_palindroma:
        print(f"La palabra {palabra} es Palíndroma")
    else:
        print(f"La palabra {palabra} NO es Palíndroma")

"""
if __name__== '__main__':
    menu()
 este es el entry point de una aplicacion
"""

if __name__== '__main__':
    main()
    
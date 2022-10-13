from io import open
from os import close, path #Para verificar si un archivo existe o no

def escribir_archivo():
    #Asi se abre un archivo, en caso de que no exista lo crea
    archivo = open('Texto.xls','w')
    archivo2 = open('Texto.txt','w')
    #Asi se escribe en el archivo
    archivo.write('Hola Mundo Python')
    archivo2.write('Hola Mundo Python')
    archivo.close()
    archivo2.close()

def leer_archivo():
    if path.isfile('Texto.txt'): #Verificar si el archivo existe
        archivo = open('Texto.txt','r') #Lo abre y lo lee r= ready
        #textos= archivo.read()
        """
        Para indicar que cada linea del archivo sea un elemento de una lista
        readline= para la primera linea del archivo.
        readlines = para toda la info del archivo
        """
        textos= archivo.readlines()
        archivo.close()
        print(textos)
    else:
        print('No existe el archivo')

def agrear_datos(): #funcion

    if path.isfile('Texto.txt'): #Verificar si el archivo existe
        archivo = open('Texto.txt','a') #Lo abre y lo actualiza a= actualizar
        archivo.write('\nHola Familia')
        archivo.close()
    else:
        print('No existe el archivo')

def modificar_datos():
    if path.isfile('Texto.txt'): #Verificar si el archivo existe
        archivo = open('Texto.txt','r+') #Lo abren, lo lee y lo modifica r+= leer y modifica
        textos= archivo.readlines()
        print(textos)
        textos[1]= '\nHola FELITO y a la familia ONE CREW'
        print(textos)
        archivo.seek(0) #Poner el puntero en que posicion del texto
        
        archivo.writelines(textos)
        archivo.close()
        print(textos)
    else:
        print('No existe el archivo')
        
def eliminar_datos():
    archivo= open('Texto.txt', 'w')
    archivo.close()
    
    
#escribir_archivo()
#leer_archivo()
#agrear_datos()
#leer_archivo()
#modificar_datos()
eliminar_datos()
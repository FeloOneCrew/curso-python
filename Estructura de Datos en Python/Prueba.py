'''
7.1 Escriba un programa que solicite un nombre de archivo, luego abra ese archivo y lea
 el archivo e imprima el contenido del archivo en mayúsculas. 
 Use el archivo words.txt para producir el resultado de abajo.
'''
fname = input("Ingresa un nombre de archivo: ")
fh = open(fname)

for leer in fh:
    leer=leer.rstrip()
    print(leer.upper())

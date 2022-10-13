'''
8.4 Abra el archivo romeo.txt y léalo línea por línea. Para cada línea, divídala en una lista
 de palabras usando el método split(). El programa debe construir una lista de palabras. 
 Para cada palabra en cada línea, verifique si la palabra ya está en la lista y, si no, añádala a la lista. 
 Cuando el programa se complete, ordene e imprima las palabras resultantes en orden alfabético.
Puede descargar los datos de muestra en http://es.py4e.com/code3/romeo.txt
'''
#fname = input("Ingresa un nombre de archivo: ")
fname = "romeo.txt"
fh = open(fname)
lst = list()
nlst = list()
for linea in fh:
    lst = linea.split()
    for palabra in lst:
        x = palabra in nlst
        if x == True: continue
        nlst.append(palabra)
nlst.sort()
print(nlst)

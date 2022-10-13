'''
8.5 Escribe un programa para leer mbox-short.txt Cuando encuentres una línea que 
comience con 'From' como la siguiente línea:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Analiza la línea From utilizando split() e imprime la segunda palabra en
la línea (es decir, la dirección completa de la persona que envió el mensaje). 
A continuación, imprime un recuento al final.
Sugerencia: asegúrate de no incluir las líneas que comienzan con 'From:'.

Puedes descargar los datos de muestra en http://es.py4e.com/code3/mbox-short.txt
'''

#fname = input("Ingresa un nombre de archivo: ")
fname = "mbox-short.txt"
lst = list()
count = 0
fh = open(fname)
for linea in fh:
    if not linea.startswith("From ") : continue #encontrar la palabra en la linea
    lst = linea.split()
    count += 1
    print(lst[1])
print("Hay", count, "lineas en el archivo con From como la primer palabra")
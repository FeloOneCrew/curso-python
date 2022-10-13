'''
10.2 Escriba un programa para leer mbox-short.txt y calcule la distribución
por hora del día para cada uno de los mensajes. Puede obtener la hora desde 
las líneas que comienzan con 'From' para encontrar el tiempo y luego dividir 
la cadena por segunda vez con dos puntos.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Una vez que haya acumulado los recuentos de cada hora, imprima los recuentos, 
ordenados por hora como se muestra a continuación.
'''
dicc= dict()
lst= list()
mayor = 0
#name = input("Ingresa un nombre de archivo:")
name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for linea in handle:
    if not linea.startswith("From ") : continue #encontrar la palabra en la linea
    lst= linea.split() #Me enlista lo que este en un texto
    f = lst[5]#Solo esto tomando en cuenta de la lista los datos de la posicion 1
    f = linea.find(":")
    f= linea[f-2:f]
    dicc[f]=dicc.get(f,0) + 1

for clave, valor in sorted(dicc.items()):
    print(clave,valor)
#print(dicc)

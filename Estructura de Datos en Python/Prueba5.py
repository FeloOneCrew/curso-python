'''
9.4 Escribe un programa para leer mbox-short.txt y encuentra quién ha enviado
la mayor cantidad de mensajes de correo. El programa busca líneas 'De' y toma 
la segunda palabra de esas líneas como la persona que envió el correo. El programa crea un 
diccionario Python que asigna la dirección de correo del remitente a un recuento 
de la cantidad de veces que aparecen en el archivo. Después de que se produce el diccionario, 
el programa lee a través del diccionario utilizando un bucle máximo para encontrar la dirección 
que más envíos tuvo.
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
    lst= linea.split()
    f = lst[1]#Solo esto tomando en cuenta de la lista los datos de la posicion 1
    dicc[f]=dicc.get(f,0) + 1

for clave, valor in dicc.items():
    if valor > mayor :
        user = clave
        mayor = valor

print(user,mayor)
#print(dicc)

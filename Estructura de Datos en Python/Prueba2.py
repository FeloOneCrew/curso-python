'''
7.2 Escribir un programa que solicita un nombre de archivo, a continuación, 
abre el archivo y lee a través del archivo, en busca de líneas de la forma:
X-DSPAM-Confidence:    0.8475
Cuenta estas líneas y extrae los valores de coma flotante de cada una de las 
líneas y calcula el promedio de esos valores y produce una salida como se muestra 
a continuación. No uses la función sum () o una variable llamada sum en tu solución.
Puedes descargar los datos de muestra en http://es.py4e.com/code3/mbox-short.txt 
para probar la función, ingrese mbox-short.txt como el nombre del archivo.
'''
# Usa mbox-short.txt como el nombre de archivo
fname = input("Ingresa un nombre de archivo: ")
fh = open(fname)
count = 0
su=0
for linea in fh:
    if not linea.startswith("X-DSPAM-Confidence:") : continue
    f = linea.find(" ")
    e = linea[f+1:]
    e = float(e.rstrip())
    su = su + e
    count += 1
    print(linea)

prom = su / count
print('Average spam confidence:', prom)
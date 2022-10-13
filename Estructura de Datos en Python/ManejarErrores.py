
fname = input("Ingresar el nombre del archivo: ")
fname = fname + ".txt"

try:
    fhand = open(fname)
except:
    print('El archivo',fname,'no se pudo abrir, por favor verificar')
    quit()

count = 0
palabra= 'one'
for line in fhand:
    x=len(line)-1 #Cuantas caracteres tiene un linea de texto
    # line.startswith = solo encuentra la palabra si esta en el inicio si
    if line.startswith(palabra):
        count += 1
print('Hay', count, 'linea(s) con la palabra "',palabra, '" en ', fname)
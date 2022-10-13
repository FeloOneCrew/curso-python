from tkinter.tix import Tree


xfile = open('Felito.txt')
count= 0
for ciclo in xfile: #Leer las lineas de un archivo plano
    felo =ciclo.find("crew") #Buscar la posicion en la cual esta la palabra
    if bool(felo) == True:
        print(ciclo[felo:felo+4])
    #Contar cuantas veces esta la letra deseada en este caso la "e"
    for letter in ciclo:#Empieza a leer letra por letra sobre el contenido del archivo plano
        if letter == 'e':
            count += 1
    print(ciclo) #Cuenta las letras que yo necesito
print(count)#Imprime el numero de letras que encontro.
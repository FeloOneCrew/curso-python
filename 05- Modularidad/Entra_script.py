import sys #Reutilizar el modulo sys para recuperar datos que le podemos enviar desde script

if len(sys.argv)==3:
    texto= sys.argv[1]
    cantidad = int(sys.argv[2])

    c=0
    while c < cantidad:
        print(texto)
        c+=1
else:
    print("Error, ingrese los argumentos correctamente")
    print('Ejemplo: Entra_script "texto" 5')


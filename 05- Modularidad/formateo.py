from sys import argv   #Reutilizar el modulo sys para recuperar datos que le podemos enviar desde script

if len(argv)==4:
    Nombre= argv[1]
    edad = int(argv[2])
    Altura= float(argv[3])
    
    print('Nombre: {} \nedad: {} \nAltura: {}'.format(Nombre,edad,Altura))

else:
    print("Error, ingrese los argumentos correctamente")
    print('Ejemplo: Entra_script "Nombre" 5 1.80')


#Ingreso de datos
#x= int(input("Ingresar un número menor  o igual a 10: \n"))
#p = 0
#while p < x:
#    x -= 1
#    p += 1
#    print("ASI SE CODIFICA UN WHILE", p)

x= int(input("Ingresar un número: \n"))

suma=0 
n_menor=0

while n_menor<x:
    suma+=n_menor
    n_menor+=1

print("La suma de los numeros anteriores a ",x, "es", suma)
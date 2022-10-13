#Guardar resultados de pares e impares
"""
Practica 03: Guardar resultados de pares e impares
Crea 2 listas y una tupla que tendrá números de 1 a 9. La primera lista 
se llamará pares y el segundo impar, ambos estarán vacíos. 
Después multiplica cada uno de los números de la tupla por un número 
aleatorio entre 1 y 100, si el resultado es par guarda ese número en la 
lista de pares y si es impar en la lista  de impares. Muestra por consola: 
-la multiplicación que se produce junto con su resultado con el formato 2 x 3 = 6 
y la lista de pares e impares

"""
#ENTRADA
import random
tupla=(1,2,3,4,5,6,7,8,9,10)
Par=[]
ImPar=[]

for num in tupla:
    Alea = random.randint(1, 100)
    #print("El numero aleatorio es:", Alea )
    r= Alea * num
    d= r%2
    if d > 0:
        ImPar.append(r)
        print(num," x ",Alea," = ",r)
        #print("La lista PAR es: ",Par)
        #print("La lista IMPAR es: ",ImPar)
    else:
        Par.append(r)
        print(num," x ",Alea," = ",r)
        #print("La lista PAR es: ",Par)
        #print("La lista IMPAR es: ",ImPar)
print("------------------------------------------------------------------")
print("-------------------RESULTADO FINAL DE LAS LISTA-------------------")
print("La lista PAR es: ",sorted(Par)) #El sorted me ayuda a organizar los # de mayor a menor
print("La lista IMPAR es: ",ImPar)


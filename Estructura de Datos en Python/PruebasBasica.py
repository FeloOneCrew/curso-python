''' 
#Entrada
n1 = int(input("Por favor ingrese el primer número entero: "))
n2 = int(input("Por favor ingrese el segundo número entero: "))

#Operación
s = n1 + n2

#Salida
print(s)
#-----------------------------------------------------------------------------------------

#Entrada
a = int(input("Por favor ingrese la base: "))
n = int(input("Por favor ingrese el exponente: "))

#Operación
p = a**n
p1 = pow(a,n)

#Salida
print("La potencia es: ",p)
print("La potencia es: ",p1)

'''
#-----------------------------------------------------------------------------------------
#PROBLEMA: Dado un número de 5 dígitos, devolver el número en orden inverso.
#Entrada
n = list()
x = int(input("Por favor ingrese un numero de n digitos (Ejemplo: 12345): "))
i = int(len(str(x))) #Contar los digitos de un numero.

#Operación
for contar in range(i-1):
    c = x
    t = c// 10 #Cociente
    r = c % 10  #Residuo
    n.append(r)
    x = t
n.append(t) 

#Salida
print("Lista del numero",list(reversed(n))) #Mostrar una lista inversa
print("Lista Numero invertido",n) #Mostrar una lista inversa
ni = " "
for conc in n:
    ni = ni + str(conc)
    
print("Numero Invertido:", int(ni))

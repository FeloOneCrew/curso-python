"""
Práctica 01: Calcular el cociente y residuo.
Enunciado: Hallar el cociente y el residuo(Resto) de dos numero enteros.
Análisis: Para la solucion de este problema, se requiere que el usuario ingrese
dos numero enteros y el sistema realice el calculo respectivo para hallar
el cociente y el residuo.
"""
#Entrada de datos
print("Hallar el cociente y el residuo")
a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))

#Operacion
#c= a/b
#c= int(c)
#r=  int(a -(c*b))

c= a // b #Cociente
r= a % b  #Residuo
print(type(a))
print(type(b))
print(type(c))
print(type(r))
#Salida
print(f"El cociente es {c} y el residuo es {r}")

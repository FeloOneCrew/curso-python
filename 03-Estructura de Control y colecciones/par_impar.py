"""
Aplicación 01: Crear un sistema que detecte si número 
es par positivos o par negativo y también si es impar 
positivo o negativos y si el numero ingresado es 0 
que detecte si es neutro.
Enunciado: determinar si un número entero es par positivo, 
impar positivo, par negativo, impar negativo o neutro.
Análisis: para la solución de este problema, se requiere 
que el usuario ingrese un número entero y el sistema 
verifique si es par positivo, impar positivo, par negativo, impar negativo o neutro.

"""
print ("="*50)
print ("Crear un sistema que detecte si un número entero es:")
print ("- Par positivos o par negativo")
print ("- Impar positivos o par negativo")
print ("- si es 0 es neutro")
print ("="*50)

num= int(input("Por favor ingresar un numero: "))
r= num % 2 
if num ==0:
    print(f"El número {num} es NEUTRO")
else:
    if r>0: #TRUE
        if num<0:
            print(f"El número {num} es IMPAR NEGATIVO")
        else:
             print(f"El número {num} es IMPAR POSITIVO")

    else: #FALSE
        if num<0:
            print(f"El número {num} es PAR NEGATIVO")
        else:
             print(f"El número {num} es PAR POSITIVO")
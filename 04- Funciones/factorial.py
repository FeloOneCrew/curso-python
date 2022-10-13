
"""
en la funcion factorial(n):, al ejecutarse esta parte 
n= n* factorial(n - 1) es una funcion recursiva, que se ejecuta
asi misma.

"""
def factorial(n):
    print("valor inicial =>", n)
    if n > 1:
        n= n* factorial(n - 1)

    #print("valor final =>", n)
    return n

n= int(input("Ingrese un número entero: "))
f= factorial(n)
print(f"Su factorial de {n} es: ", f)
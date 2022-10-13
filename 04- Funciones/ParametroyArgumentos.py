"""
funcines, para declarar una funciones se indica la
palabra reservada "def"
"""
"""
Parametro:
Un parámetro es un valor que la función espera recibir cuando 
sea llamada (invocada), a fin de ejecutar acciones en base al mismo. 
Una función puede esperar uno o más parámetros 
(que irán separados por una coma) o ninguno.

def mi_funcion(nombre, apellido): 
"""

nom= input("Ingresar solo el nombre: \n")
num1= int(input("Ingresar primer numero entero mayor a 0: \n"))
num2= int(input("Ingresar segundo numero entero mayor a 0: \n"))
def saludar(nombre):
    if nombre == "":
        print("ERROR, Por favor indicar un nombre")
        return
    return f"Hola,{nombre}, desde la FUNCION SALUDAR"

def sumar(a, b):
    return a+b

def restar(a,b):
    return a-b

saludo= saludar(nom)
suma= sumar(num1, num2)
resta= restar(num1, num2)
print(f"{saludo}, hola")
print("La suma de los numero es: ",suma)
print("La resta de los numero es: ",resta)


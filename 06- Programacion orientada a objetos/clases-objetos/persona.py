#El molde de un objeto

class Persona:
#El nombre de la clase siempre inicia con Mayuscula ejemplo Curso
   # nombre = None # cuando tenemos constructor ya no necesitamos esto
   #edad= None

    def __init__(self, nombre, edad): #constructor
        self.nombre= nombre
        self.edad= edad


    def mostrar_datos(self): #Metodo dentro de una clase
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

    def __str__(self): #Imprimir el estado de un objeto
        return f'Nombre: {self.nombre} \nedad: {self.edad}'

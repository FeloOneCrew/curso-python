
class Persona:

    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    

    def detalle_persona(self):
        print(f'Nombre: {self.nombre} \nedad: {self.edad}')

    def __str__(self): #Imprimir el estado de un objeto
        return f'Nombre: {self.nombre} \nedad: {self.edad}'

#Clase cliente que hereda de Persona
class Cliente (Persona):
    pass

#Clase Empleado que hereda de Persona
class Empleado (Persona):
    def __init__(self, nombre, edad, sueldo):
        #super().__init__(nombre, edad) # super() Heredamos todo el constructor de la clase persona
        Persona.__init__(self, nombre, edad)
        self.sueldo=sueldo
    
    def detalle_Empleado(self):
       #super().detalle_persona()
        Persona.detalle_persona(self)
        print('El sueldo', self.sueldo)
    
    def __str__(self):
            #return super().__str__() + f'\nSueldo:{self.sueldo}' # super() Heredamos todo el constructor de la clase persona
            #print('El sueldo', self.sueldo)
            return Persona.__str__(self) + f'\nSueldo:{self.sueldo}'


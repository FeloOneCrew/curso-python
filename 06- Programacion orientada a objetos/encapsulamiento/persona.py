class Persona:

    #Para tener un atributo privado lo hacemos con doble barra baja "__nombre"

    __nombre= None
    __edad= None

    def __init__(self, nombre, edad):
        self.__nombre= nombre
        self.__edad= edad

    def __metodo_Privado(self):
        print('Soy un metodo privado')
    
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre= nombre

    def set_edad(self, edad):
        self.__edad= edad

    
    def __str__(self): #Imprimir el estado de un objeto
        return f'Nombre: {self.__nombre} \nedad: {self.__edad}'
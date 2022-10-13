import math

class Figura(object):

    def __init__(self,nombre):
        self.nombre = nombre
        

    def area(self):
        pass

    def perimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.nombre =__class__.__name__ #Capturar el nombre de la clase
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura )

    def __str__(self): #Imprimir el estado de un objeto
        return f'{self.nombre}[base:{self.base} altura:{self.altura}]'

class Circulo(Figura):
    def __init__(self, radio):
        self.nombre =__class__.__name__ #Capturar el nombre de la clase
        self.radio = radio

    def area(self):
        return math.pi* (self.radio)**2
    
    def perimetro(self):
        return 2* math.pi* self.radio

    def __str__(self): #Imprimir el estado de un objeto
        return f'{self.nombre}[radio:{self.radio}]'

class Cuadrado(Figura):
    def __init__(self, lado):
        self.nombre = __class__.__name__
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4

    def __str__(self): #Imprimir el estado de un objeto
        return f'{self.nombre}[Lado:{self.lado}]'


def probar_figura(figura):
    print(figura) # Va a la clase para mostrar el estado del objeto
    print('Area: ', figura.area())
    print('Perimetro: ', figura.perimetro())
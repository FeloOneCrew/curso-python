from persona import Persona as P

persona1= P('Felo', 33)
print(persona1)
persona1.set_nombre('crew') #De esta manera se modifica un dato privado
print(persona1.get_nombre()) #Mostrar el dato privado actual
print(persona1)

from persona import Persona as P

p1= input('Insertar su nombre:\n')
e1= input('Insertar su edad:\n')

p2= input('Insertar su nombre:\n')
e2= input('Insertar su edad:\n')

persona1= P(p1,e1) #creando un objeto - instanciar



persona1.nombre = p1
persona1.edad = e1

#persona1.nombre = "Felipe"
#persona1.edad = 33

persona2= P(p2,e2)
#persona2.nombre = "Andres"
#persona2.edad = 30

persona1.mostrar_datos()
persona2.mostrar_datos()
print(persona1)
print(persona2)
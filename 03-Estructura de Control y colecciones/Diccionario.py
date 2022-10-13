"""
Los diccionarios se encuentran a veces en otros lenguajes 
como «memorias asociativas» o «arreglos asociativos». A diferencia
 de las secuencias, que se indexan mediante un rango numérico, 
 los diccionarios se indexan con claves, que pueden ser cualquier
  tipo inmutable; las cadenas y números siempre pueden ser claves. 
  Las tuplas pueden usarse como claves si solamente contienen cadenas,
números o tuplas; si una tupla contiene cualquier objeto mutable 
directa o indirectamente, no puede usarse como clave. No podés usar 
listas como claves, ya que las listas pueden modificarse usando 
asignación por índice, asignación por sección, o métodos como 
append() y extend().

Es mejor pensar en un diccionario como un conjunto de pares 
clave:valor con el requerimiento de que las claves sean únicas 
(dentro de un diccionario). Un par de llaves crean un diccionario 
vacío: {}. Colocar una lista de pares clave:valor separada por comas
 dentro de las llaves agrega, de inicio, pares clave:valor al 
 diccionario; esta es, también, la forma en que los diccionarios 
 se muestran en la salida.

"""
#Diccionario numeros
numeros = {'uno':1 ,'dos':2 ,'tres':3 , 'cuatro':4 , 'cinco':5 }
print(numeros)
numeros['seis'] = 6 # Añadir un nuevo elemento al diccionario
print(numeros)
print(numeros['tres'])#Imprimir un valor segun la clave.
FELO=numeros.get('cinco',"NO SE ENCONTRO")# Buscar un elemento en el diccionario
print(FELO)
FELO=numeros.get('siete',"NO SE ENCONTRO")# Buscar un elemento en el diccionario
print(FELO)
claves= numeros.keys() #Para obtener solo las claves del diccionario. 
print(claves)
valores= numeros.values()
print(valores) #Para obtener solo los valores del diccionario. 
LosItems= numeros.items()
print(LosItems) #Para obtener toda la info del diccionario
Eliminar= numeros.pop('tres')
print(Eliminar) #Para eliminar un elemento del diccionario, hay que indicar la clave.
print("El diccionario actualizado es: ")
print(numeros)
#ITERAR UN DICCIONARIO solo las claves
for numero in numeros:
    print(numero)
#ITERAR UN DICCIONARIO solo los datos
for numero1 in numeros.values():
    print(numero1)
#ITERAR UN DICCIONARIO con clave y dato
for clave, numero2 in numeros.items():
    print(clave, numero2)



limpiar= numeros.clear()#Borrar todos los datos del diccionario
print(limpiar)
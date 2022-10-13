'''
5.1. Más sobre listas
El tipo de dato lista tiene algunos métodos más. Aquí están todos los métodos de los objetos lista:

list.append(x)
Agrega un ítem al final de la lista. Equivale a a[len(a):] = [x].

list.extend(iterable)
Extiende la lista agregándole todos los ítems del iterable. Equivale a a[len(a):] = iterable.

list.insert(i, x)
Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará, 
por lo tanto a.insert(0, x) inserta al principio de la lista y a.insert(len(a), x) equivale a a.append(x).

list.remove(x)
Quita el primer ítem de la lista cuyo valor sea x. Lanza un ValueError si no existe tal ítem.

list.pop([i])
Quita el ítem en la posición dada de la lista y lo retorna. Si no se especifica un índice, a.pop() quita 
y retorna el último elemento de la lista. (Los corchetes que encierran a i en la firma del método denotan 
que el parámetro es opcional, no que deberías escribir corchetes en esa posición. Verás esta notación con 
frecuencia en la Referencia de la Biblioteca de Python.)

list.clear()
Elimina todos los elementos de la lista. Equivalente a del a[:].

list.index(x[, start[, end]])
Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. Lanza una excepción 
ValueError si no existe tal elemento.

Los argumentos opcionales start y end son interpretados como la notación de rebanadas y se usan para 
limitar la búsqueda a un segmento particular de la lista. El índice retornado se calcula de manera relativa 
al inicio de la secuencia completa en lugar de con respecto al argumento start.

list.count(x)
Retorna el número de veces que x aparece en la lista.

list.sort(*, key=None, reverse=False)
Ordena los elementos de la lista in situ (los argumentos pueden ser usados para personalizar el orden de la lista, 
ver sorted() para su explicación).

list.reverse()
Invierte los elementos de la lista in situ.

list.copy()
Retorna una copia superficial de la lista. Equivalente a a[:].
'''
'''
DIFERENCIA ENTRE LISTA, TUPLA Y DICCIONARIO

LISTA: nombres = ["Ana","Juan","Sofía","Pablo","Tania"]
TUPLA: colores=("Azul","Verde","Rojo","Amarillo","Blanco","Negro","Gris")
DICCIONARIO: edades = {"Ana": 25, "David": 18, "Lucas": 35, "Ximena": 30, "Ale": 20}

'''


#-----------LISTAS---------------------

print("Datos 1")
datos=["felo", 33,"Robledo", True]
#Agregar datos a una lista
"""
Agrega un ítem al final de la lista. 
Equivale a a[len(a):] = [x].
"""
datos.append("INGENIERO DE SISTEMAS")
print(datos)

#extender datos a una lista
"""
Extiende la lista agregándole todos los ítems del iterable. 
Equivale a a[len(a):] = iterable.
"""

print("Datos 2")
datos2=["sura", "estrato 2","moto", True]
print(datos2)
print("Esto es una Lista extendida de Datos 1 y 2")
datos.extend(datos2)
print(datos)


#insertar datos en una lista en alguna posicion dada

"""
Inserta un ítem en una posición dada. El primer argumento
 es el índice del ítem delante del cual se insertará, por 
 lo tanto a.insert(0, x) inserta al principio de la lista y 
 a.insert(len(a), x) equivale a a.append(x).
"""
print("insertar datos en una lista en alguna posicion dada")
datos2.insert(2,"zmj47c")
print(datos2)
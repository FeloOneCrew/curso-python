'''
A continuación presentamos las instrucciones de esta revisión:
Acceder al contenido del siguiente sitio web mediante la biblioteca urllib: 
https://web.archive.org/web/20210422170527/https://en.wikipedia.org/wiki/Wikipedia

El acceso a los datos puedes hacerlo utilizando el módulo urllib.request. Ten cuidado, 
fíjate muy bien en los ejemplos proporcionados para evitar errores.

Usar la función findall, con la expresión regular adecuada en cada caso, para construir:
atleast3_found: Lista de todas las coincidencias de palabras que empiezan con al menos 3 letras, 
ya sean minúsculas o mayúsculas.
wiki_found: Lista de todas las coincidencias de palabras que empiezan con ‘wiki’.
Wiki_found: Lista de todas las coincidencias de palabras que empiezan con ‘Wiki’.

Recuerda que la función findall devuelve una lista con todas las coincidencias encontradas.

Anteriormente obtuviste tres listas con las coincidencias (atleast3_found, wiki_found, Wiki_found). 
Observa que hay palabras que se repiten varias veces en esas listas. Por ello en esta sección crearás un 
diccionario de frecuencias para cada uno.

Crear una función, freq_dict(), que reciba una lista de palabras y que regrese el diccionario que tiene 
como keys las palabras distintas de la lista y como values las respectivas frecuencias de éstas.
'''

from urllib import response
import re
import urllib.request

dicc = dict()
dicc2 = dict()
dicc3 = dict()
Cont = 0
Cont2 = 0
Cont3= 0


url = 'https://web.archive.org/web/20210422170527/https://en.wikipedia.org/wiki/Wikipedia'
response = urllib.request.urlopen(url)
felo = response.read()
atleast3_found = re.findall(r'\w{3,}', str(felo))
wiki_found =  re.findall(r'wiki[a-z]+', str(felo))
Wiki_found =  re.findall(r'Wiki\w+', str(felo))
for linea in atleast3_found:
    Cont += 1
    dicc[linea]=dicc.get(linea,0) + 1

for linea2 in wiki_found:
    Cont2 += 1
    dicc2[linea2]=dicc2.get(linea2,0) + 1

for linea3 in Wiki_found:
    Cont3 += 1
    dicc3[linea3]=dicc3.get(linea2,0) + 1


print("*"*10,"Diccionario 1","*"*10)
print(Cont,len(dicc), dicc)
print("*"*10,"Diccionario 2","*"*10)
print(Cont2,len(dicc2),dicc2)
print("*"*10,"Diccionario 3","*"*10)
print(Cont3,len(dicc3),dicc3)
#print(type(response))
#print(response.read[a-zA-Z0-9])

#Leer cada letra de la palabras e imprimirla
fruta='banana'
for letter in fruta:
 print (letter)

#Contar la palabra que yo le indique e imprimirla
count= 0
for letter in fruta:
    if letter == 'a':
       count += 1
print(count)

Palabra= input("Por favor ingrese la palabra: ")
count2= 0
for letter in Palabra:
    if letter == 'a':
       count2 += 1
print(count2)


pos= fruta.find('na')
print(pos)

text = "X-DSPAM-Confidence:    0.8475";
felo =text.find(" ")
print(float(text[felo+3:]))

#Poner un salto de linea con \n
x= "La Pelota"
y= "es ROJA"
z= x+'\n'+y
z= z.rstrip()#Borrar los espacion del lado izquierdo.
print(x,'\n',y)
print(z)
print('\n')
print(len(z))
c=0

x= int(input("Ingresar un número para el bucle: "))

while c < x:
    c+=1
    print(c)
    if c == 5:
        #print("FIN DEL BUCLE") # para el break
        print("Salta a la siguiente iteracion")
        #break #Se rompe el bucle segun la condicion
        continue
    print("continue")
else:
    print("FIN DEL While")

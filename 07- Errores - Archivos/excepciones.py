c=0
suma=0

while c<3:
    try:
        n= int(input(f"Ingrese el numero {c+1}:"))
        suma+=n
        c+=1
    
    except:
        print("Error: Por favor ingrese un numero BRUTO")


print("La suma total es:",suma)

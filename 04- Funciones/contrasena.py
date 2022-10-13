import random

def generar_contrasena():
    minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Mayus= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Simbolos= ['/','*','-','+','%','&','°','¬','~','=','¿','|']
    num=[1,2,3,4,5,6,7,8,9,0]

    caracteres = minus + Mayus + Simbolos + num
    contrasena = []

    for i in range(15):
        contra_ramdon = random.choice(caracteres)
        #felo =  "".join(contra_ramdon)
        contrasena.append(contra_ramdon)
    

    #contrasena = " ".join(contrasena) #Convertir en una cadena de caracteres
    contrasena = ''.join(str(v) for v in contrasena)
    return contrasena

#Funcion principal
def main():
    contrasena1= generar_contrasena()
    #contrasena1=contrasena1.replace(" ","")
    print("Tu contraseña generada es ", contrasena1)


if __name__ == "__main__":
    main()
    
    


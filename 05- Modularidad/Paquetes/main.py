import my_paquete.aritmetica as a

def main():
    suma= a.sumar(1,2,3,4)
    resta= a.restar(50,38)
    potencia= a.potencia(3,7)

    print("La suma es: ",suma )
    print("La resta es: ",resta )
    print("La potencia es: ",potencia )

if __name__ =="__main__":
    main()
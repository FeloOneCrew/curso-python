def conversor(valorDolar,pais):
    cantidadMoneda= float(input(f"Ingrese cantidad de {pais}: "))
    dolares= cantidadMoneda / valorDolar
    dolares= round(dolares,2)
    print(f"tienes tantos ${dolares} dolares")


def main():
    while True:
        menu= """
        1-Peso Colombiano
        2-Peso Mexicano
        3-Sol Peruano
        4-Lira Turca
        5-Salir

        Ingrese una de las opciones anteriores:"""

        opcion= input(menu)

        if opcion =="1":
            conversor(3710.01, "Peso colombiano")
        elif opcion =="2":
            conversor(20.56, "Peso Mexicano")
        elif opcion =="3":
            conversor(3.99, "Soles Peruanos")
        elif opcion =="4":
            conversor(9.15, "Lira Turca")
        elif opcion =="5":
            print("Cerrando conversor de monedas")
            break
        else:
            print("Opcion incorrecta, ingrese una opcion:")
        


#Punto inicio de la aplicación
if __name__=="__main__":
    main()


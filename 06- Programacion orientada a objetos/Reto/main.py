from figuras import Rectangulo, Circulo,Cuadrado, probar_figura

def main():
    while True:
        menu = """
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
        
        1 - Rectangurlo
        2 - Circulo
        3 - Cuadrado
        4 - Salir 
        Ingrese una Opcion: """

        opcion = input(menu)

        if opcion == '1':
            base = float(input('Ingrese Base:'))
            altura = float(input('Ingrese Altura: '))
            r = Rectangulo(base, altura)
            probar_figura(r)

        elif opcion == '2':
            radio = float(input('Ingrese Radio:'))
            c = Circulo(radio)
            probar_figura(c)

        elif opcion == '3':
            lado= float(input('Ingresar el valor de un lado del cuadrado: '))
            l= Cuadrado(lado)
            probar_figura(l)

        elif opcion == '4':
            print('Cerrando sistema')
            break

        else:
            print('Opción incorrecta')

if __name__ == '__main__': #El interprete inicia el proceso desde aqui
    main()
def hacer_tabla(num):

    tabla=[]
    for i in range(1,11):
        mult= num * i
        tabla.append(mult)
        
    return tabla



def main():
    while True:

        menu="""
        Para salir del generador indique S o s


        Ingrese el numero de la tabla: """
        n= input(menu)
        if n == 's' or n == 'S':
            print("Saliendo del generador de tablas de multiplicar")
            break
        else:
            n=int(n)
            t= hacer_tabla(n)
            contar= 1
            print(f"Tabla de Multiplicar del {n}")
            for i in t:
                print(f"{n} * {contar} = {i}")
                contar+=1

    
if __name__== "__main__":
    main()

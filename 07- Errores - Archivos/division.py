Div=0

try:
    a= int(input('Ingrese el Dividendo: '))
    b= int(input('Ingrese el Divisor: '))

    Div= a/b

except ValueError:
    print('Error: Ingrese solo numeros enteros')

except ZeroDivisionError:
    print('Error: No se puede dividir por 0')

except Exception as error:
    print('Ha ocurrido un error no previsto', type(error).__name__)

print('La Division es: ', Div)
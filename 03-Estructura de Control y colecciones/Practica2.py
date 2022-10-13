"""
Enunciado: debido a los excelentes resultados, el restaurante decide ampliar 
sus ofertas de acuerdo a la siguiente escala de consumo, ver la tabla. 
Determinar el monto del descuento, el importe del impuesto y el importe a pagar.
•	Consumo (S/.)       Descuento (%)
•	Hasta 100                 10
•	Mayor a 100             20
•	Mayor a 200             30

Análisis: para la solución de este problema, se requiere que el usuario ingrese 
el consumo y el sistema verifica y calcula el monto del descuento, el impuesto 
y el importe a pagar.

"""

#ENTRADA
n= float(input("Ingresar el valor del consumo: $"))

#PROCESO
inp= n*0.19
ps= n+inp
if n>0:
    if n<=100000:
        d= n*0.1
        des= "10%"     
    elif n>100000 and n<=200000:
        d= n*0.2
        des= "20%"
    else:
        d= n*0.3
        des= "30%"  

    Pagar= n+inp-d  

    #SALIDA
    print("="*53)
    print("-"*22,"Factura","-"*22)
    print("El porcentaje de descuento es: $",des)
    print("="*53)
    print("El valor del consumo es: $",n)
    print("El valor del descuento es: $",d)
    print("El valor del impuesto es: $",inp)
    print("El valor a pagar sin descuento es: ",ps)
    print("EL VALOR TOTAL A PAGAR ES: $",Pagar)
    print("-"*53)
else:
     print("DATO INVÁLIDO,Por favor ingresar un numero mayor a cero")
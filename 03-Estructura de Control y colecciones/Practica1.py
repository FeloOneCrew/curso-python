#Descuento del restaurante
"""
un restaurante ofrece un descuento del 10% para consumo 
de hasta s/. 100.00 y un descuento del 20 % para consumos 
mayores, para ambos casos se aplica un impuesto del 19%. 
Determinar el monto del descuento, el impuesto y el importe a pagar.

Análisis: para la solución de este problema, se requiere que el usuario
ingrese el consumo y el sistema verifica y calcula el monto del descuento,
el impuesto y el importe a pagar.
•	monto del descuento
•	impuesto
•	importe a pagar

"""

#ENTRADA
n= float(input("Ingresar el valor del consumo: $"))

#PROCESO
inp= n*0.19
ps= n+inp

if n<=100000 and n>0:
    d= n*0.1
    des= "10%"
elif n<=0:
    print("Por favor ingresar un numero mayor a cero")
    d= 0
    des= "0%"
else:
    d= n*0.2
    des= "20%"
    

Pagar= n+inp-d  

#SALIDA
print("="*53)
print("-"*22,"Factura","-"*22)
print("El porcentaje de descuento es: $",des)
print("="*53)
print("El valor del descuento es: $",d)
print("El valor del impuesto es: $",inp)
print("El valor a pagar sin descuento es: ",ps)
print("El valor a pagar es: $",Pagar)
print("-"*53)
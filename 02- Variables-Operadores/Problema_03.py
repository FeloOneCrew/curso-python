"""
Ver la imagen del problema_03 en la carpeta 
C:\workspace\curso-python\02- Variables-Operadores
"""

#Entrada de datos
print("Hallar el IGV y el precio de venta")
vv = float(input("Ingrese el valor de venta del producto: "))
b = float(input("Ingrese el porcentaje de IGV (%): "))

#Operacion

igv= vv * (b/100)
pv= vv + igv

#Salida
print("="*25)
print("-------- FACTURA---------")
print(f"VALOR DE VENTA: {vv}")
print(f"IGV: {igv}")
print(f"PRECIO DE VENTA: {pv}")
print("="*25)



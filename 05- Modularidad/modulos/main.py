#Para importar todo el modulo o las clases de ese modulo

#import fibonnaci
#from fibonnaci import fibo,fibo2
#from fibonnaci import * # hace lo mismo que el anterior
#import fibonnaci as fb
from fibonnaci import fibo as f1
from fibonnaci import fibo2 as f2

n= int(input("Ingrese un valor para el fibonnaci: "))

#fibo(n)
#print(fibo2(n))
#fb.fibo(n)
#print(fb.fibo2(n))
f1(n)
print(f2(n))

'''
Enunciado: Determinar la suma de los N primeros números enteros positivos (? +) use la siguiente formula.

S <== (n * (n + 1)) / 2

Análisis: Para la solución de este problema, se requiere que el usuario
ingrese un número entero positivo n, luego el sistema procesa y obtiene 
la suma de los primeros números enteros positivos hasta n.
'''

n  = input("Ingrese un número entero positivo: ")

try:
  if int(n) < 1:
      print('Por favor ingrese un número mayor a 0')
  else:
      
      felo = (int(n) * (int(n) + 1)) / 2
      print('La sumatoria de los numero sucesivos hasta', n, 'es:', felo)
        
except:
  print("El valor",n,"no es un número. Por favor ingrese un número")

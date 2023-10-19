"""1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos."""

x = 5
if x > 0:
  print('x es positivo')


x = 5
if x % 2 == 0:
  print('es par')
else: 
  print('es impar')
  
a = 3
b = 10
c = 5
if a > b and a > c:
  print('El número mayor es 3')
elif b > a and b > c:
  print ('El número mayor es 10')
elif c > a and c > b:
  print('El número mayor es 5')
  

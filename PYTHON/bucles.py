"""1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100."""

for n in range(1, 11):
  print(n)

numero = 1
while numero <= 20:
  if numero % 2 == 0:
    print(numero)
  numero += 1

numero = 1
suma = 0
while numero <= 100:
  suma += numero
  numero += 1 
print('La suma de los números del 1 al 100 es:', suma)

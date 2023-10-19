"""1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci."""
def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
fibonacci(10) 
print(fibonacci)

""" 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores."""
def divisores(n):
  lista_divisores = []
  for i in range(1, n + 1):
    if n % i == 0:
      lista_divisores.append(i)
  return lista_divisores
n = 12
lista_de_numeros = divisores(n)
print("Los divisores de", n, "son:", lista_de_numeros)

""" 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original."""
def unicos(lista):
  return list(set(lista))
print(unicos([2,2,5,6,4,4]))

""" 4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos."""
def suma_digitos(n):
  return sum(int(digito) for digito in str(n))
print(suma_digitos(465))

""" 5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena."""
def contar_vocales(cadena):
  return sum(1 for letra in cadena if letra.lower() in 'aeiou')
print(contar_vocales('Hola Mundo'))

""" 6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista."""
def primeros_n_elementos(lista,n):
  return lista[:n]
print(primeros_n_elementos([1,2,3,4],5))

"""7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena."""
def cantidad_mayusculas_minusculas(cadena):
  mayusculas = sum(1 for letra in cadena if letra.isupper())
  minusculas = sum(1 for letra in cadena if letra.islower())
  return mayusculas, minusculas
print(cantidad_mayusculas_minusculas('Hola Mundo'))

"""8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3"""
def es_perfecto(num):
  return num == sum(divisor for divisor in range(1, num) if num % divisor == 0)
print(es_perfecto(6))

"""9. Ejercicio: Define una función que reciba un número y retorne su representación en binario."""
def a_binario(n):
  return bin(n).replace("0b", "")
print(a_binario(5))

"""10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas)."""
def interseccion(list1, list2):
  return list(set(list1) & set(list2))
print(interseccion([1,2,3,4], [4,3,7,8]))

""" 11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""
def es_palindromo(cadena):
  return cadena == cadena [::-1]
print(es_palindromo("reconocer"))

"""12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”"""
for  i in range(1, 51):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

"""13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente."""
def ordenar_lista(lista):
  return sorted(lista)
print(ordenar_lista([3,1,5,4,2,6,7]))

"""14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n."""
def filtrar_palabras(lista_palabras, n):
  return [palabra for palabra in lista_palabras if len(palabra) > n]
print(filtrar_palabras(['hola', 'mundo', 'cerebro'], 5))

"""15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci"""
def serie_fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  fib = [0, 1]
  while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
  return fib
print(serie_fibonacci(10))
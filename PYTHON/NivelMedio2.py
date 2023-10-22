"""16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista."""
def maximo(lista):
  return max(lista)
print(maximo([1,5,52,16]))

"""17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo."""
def suma_al_cubo_digitos(n):
  return sum(int(digit)**3 for digit in str(n))
print(suma_al_cubo_digitos(448))

"""18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista."""
def segundo_maximo(lista):
  return sorted(set(lista), reverse=True) [1]
print(segundo_maximo([1,3,4,8,9,2]))

"""19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False."""
def tienen_comun(lista1, lista2):
  return bool(set(lista1) & set(lista2))
print(tienen_comun([1,2,3,4], [3,4,5,6]))

"""20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso."""
def invertir_lista(lista):
  return lista[::-1]
print(invertir_lista([1,2,3,4,5]))

"""21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene."""
def contar_digitos_letras(cadena):
  digitos = sum(c.isdigit() for c in cadena)
  letras = sum(c.isalpha() for c in cadena)
  return digitos, letras
print(contar_digitos_letras("Hola 56"))

"""22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números"""
def suma_acumulada(lista):
  total = 0
  suma_acumulada = []
  for numero in lista:
    total += numero
    suma_acumulada.append(total)
  return suma_acumulada
print(suma_acumulada([1,2,3,4,5]))

"""23. Ejercicio: Define una función que encuentre el elemento más común en una lista."""
from collections import Counter
def elemento_mas_comun(lista):
  contador = Counter(lista)
  elemento_mas_comun = contador.most_common(1)[0][0]
  return elemento_mas_comun
print(elemento_mas_comun([1,2,2,3,4,5]))

"""24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10."""
def tabla_de_multiplicar(numero):
  return {i: numero * i for i in range(1, 11)}
print(tabla_de_multiplicar(3))

"""25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena."""
def contar_caracteres(cadena):
  return {caracter: cadena.count(caracter) for caracter in cadena}
print(contar_caracteres("hola mundo"))

"""26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas."""
def elementos_no_comunes(lista1, lista2):
  return list(set(lista1) ^ set(lista2))
print(elementos_no_comunes([1,2,3,4],[3,4,5,6]))

"""27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados."""
def sin_duplicados(lista):
  return list(set(lista))
print(sin_duplicados([1,2,2,3,4,4,5]))

"""28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese número."""
def suma_cuadrados_pares(n):
  return sum(i**2 for i in range(2, n+1, 2))
print(suma_cuadrados_pares(6))

"""29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista."""
def promedio(lista):
  return sum(lista) / len(lista)
print(promedio([1,2,3,4,5]))

"""30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista."""
def cadena_mas_larga(lista):
  return max(lista, key=len)
print(cadena_mas_larga(['Hola', 'mundo', 'python']))

"""31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos."""
def es_primo(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
     return False
    return True
def primeros_n_primos(n):
  primos = []
  numero = 2
  while len(primos) < n:
    if es_primo(numero):
      primos.append(numero)
    numero += 1
print(primeros_n_primos(5))

"""32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso."""
def invertir_palabras(cadena):
  return ' '.join(cadena.split()[::-1])
print(invertir_palabras("Hola, que tal"))

"""33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla."""
def ordenar_por_ultimo_elemento(tuplas):
  return sorted(tuplas, key=lambda x: x[-1])
print(ordenar_por_ultimo_elemento([(1,2), (3,1), (4,5)]))

"""34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena"""
def contar_vocales(cadena):
  return sum(1 for c in cadena.lower() if c in 'aeiou')
print(contar_vocales("Hola Mundo"))

"""35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False."""
def es_primo(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
    return True
print(es_primo(17))
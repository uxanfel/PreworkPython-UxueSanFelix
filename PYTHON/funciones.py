"""1. Ejercicio: Define una función que tome dos números y retorne su suma."""
def suma(a, b):
  return a + b
resultado = suma(4, 2)
print(resultado)

"""2. Ejercicio: Define una función que tome un número y retorne su factorial."""
def factorial(n):
  if n < 0:
    return "El factorial no está definido para números negativos"
  elif n == 0:
    return 1
  else:
    resultado = 1
    for i in range(1, n + 1):
      resultado *= i 
    return resultado
numero = 5 
print (f"El factorial de {numero} es {factorial(numero)}")

"""3. Ejercicio: Define una función que tome un número y determine si es primo."""
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = 17
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")

"""4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos."""
def suma_lista(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma
lista_numeros = [1,2,4,6] 
print(suma_lista(lista_numeros))

"""5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa."""
def cadena_en_reversa(cadena):
  return cadena[::-1]
texto = 'Hola Mundo'
texto_en_reversa = cadena_en_reversa(texto)
print(texto_en_reversa) 

''' Un número es un cuadrado perfecto si su raíz cuadrada es un número exacto (sin decimales). Por ejemplo, 
el 4 es un cuadrado perfecto (2²), al igual que lo son el 36 (6²) y el 3.500.641 (1871²).
 Todos los números que no son cuadrados perfectos pueden multiplicarse por otros para conseguir serlo. Por 
ejemplo, el número 8 no es un cuadrado perfecto, pero al multiplicarlo por 2 se obtiene el 16, que sí lo es. 
Entradas del programa: La entrada comienza con un número que indica cuántos casos de prueba tendrán que 
procesarse.  Cada caso de prueba consiste en un número mayor que 0 y menor que 231. 
Salidas: Para cada caso de prueba, el programa escribirá por la salida estándar, en una línea independiente, el 
número más pequeño que al ser multiplicado por el número del caso de prueba da como resultado un 
cuadrado perfecto. '''

#Desarrollo

import string
import math


def cifrar_palabra(palabra, salto):
    """
    Función que aplica el cifrado de César a una palabra con un salto específico.
    """
    alfabeto = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    cifrado = ""
    
    for letra in palabra:
        if letra.lower() in alfabeto:  # Ignorar signos de puntuación y espacios
            nueva_posicion = (alfabeto.index(letra.lower()) + salto) % 26
            nueva_letra = alfabeto[nueva_posicion]
            cifrado += nueva_letra.upper() if letra.isupper() else nueva_letra
        else:
            cifrado += letra  # Mantener caracteres especiales

    return cifrado

def cifrar_frase(frase):
    """
    Función que divide la frase en palabras y aplica el cifrado de César con saltos diferentes.
    """
    palabras = frase.split()
    resultado = []

    for i, palabra in enumerate(palabras):
        salto = 3 if i % 2 == 0 else 4  # Saltos diferentes según posición de la palabra
        resultado.append(cifrar_palabra(palabra, salto))
    
    return " ".join(resultado)

def descifrar_palabra(palabra, salto):
    """
    Función que descifra una palabra usando el cifrado de César con un salto específico.
    """
    alfabeto = string.ascii_lowercase
    descifrado = ""
    
    for letra in palabra:
        if letra.lower() in alfabeto:
            nueva_posicion = (alfabeto.index(letra.lower()) - salto) % 26
            nueva_letra = alfabeto[nueva_posicion]
            descifrado += nueva_letra.upper() if letra.isupper() else nueva_letra
        else:
            descifrado += letra

    return descifrado

def descifrar_frase(frase):
    """
    Función que descifra una frase siguiendo la misma lógica que el cifrado.
    """
    palabras = frase.split()
    resultado = []

    for i, palabra in enumerate(palabras):
        salto = 3 if i % 2 == 0 else 4  # Usar los mismos saltos para descifrado
        resultado.append(descifrar_palabra(palabra, salto))
    
    return " ".join(resultado)



def encontrar_factor(n):
    """
    Función que encuentra el menor número por el cual multiplicar n para que sea un cuadrado perfecto.
    """
    factor = 2
    while True:
        if math.sqrt(n * factor).is_integer():
            return factor
        factor += 1


print("Programa de Cifrado y Descifrado de César + Cuadrado Perfecto\n")
opcion = input("Por favor, elija una opción:\n1: Cifrar una frase\n2: Descifrar una frase\n3: Calcular factor mínimo para cuadrado perfecto\n")

if opcion == "1":
    frase = input("Ingrese la frase a cifrar: ")
    resultado = cifrar_frase(frase)
    print("\nFrase cifrada:", resultado)

elif opcion == "2":
    frase = input("Ingrese la frase a descifrar: ")
    resultado = descifrar_frase(frase)
    print("\nFrase descifrada:", resultado)

elif opcion == "3":
    casos = int(input("Ingrese la cantidad de casos de prueba: "))
    for _ in range(casos):
        numero = int(input("Ingrese un número mayor a 0: "))
        print("Factor mínimo para cuadrado perfecto:", encontrar_factor(numero))

else:
    print("\nOpción no válida, por favor ingrese '1', '2' o '3'.")
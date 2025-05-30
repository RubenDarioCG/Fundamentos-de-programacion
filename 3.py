
""" Construir un programa que permita cifrar y descifrar una frase usando el cifrado conocido coloquialmente 
como el cifrado de César.  Este cifrado consiste en reemplazar cada letra de un texto por la letra que está tres 
posiciones adelante en el alssfabeto, por ejemplo cambiar todas las “A” por “D”; este valor de tres, para tres 
posiciones del alfabeto, lo llamaremos valor de salto, y puede variar.  Este programa debe hacer algo más: 
usar el valor de salto de 3 para las palabras en posiciones pares y el valor de salto de 4 para las que estén en 
posiciones impares.  El programa naturalmente tomará los espacios en blanco como separador de palabras y 
los ignorará para el proceso de reemplazo, al igual que los signos de puntuación."""

#Desarrollo

import string

def cifrar_palabra(palabra, salto):
    """Cifra una palabra utilizando el cifrado de César con un salto específico."""
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
    """Divide la frase en palabras y aplica el cifrado de César con saltos diferentes."""
    palabras = frase.split()
    resultado = []

    for i, palabra in enumerate(palabras):
        salto = 3 if i % 2 == 0 else 4  # Saltos diferentes según posición de la palabra
        resultado.append(cifrar_palabra(palabra, salto))
    
    return " ".join(resultado)

def descifrar_palabra(palabra, salto):
    """Descifra una palabra usando el cifrado de César con un salto específico."""
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
    """Descifra una frase siguiendo la misma lógica que el cifrado."""
    palabras = frase.split()
    resultado = []

    for i, palabra in enumerate(palabras):
        salto = 3 if i % 2 == 0 else 4  # Usar los mismos saltos para descifrado
        resultado.append(descifrar_palabra(palabra, salto))
    
    return " ".join(resultado)

# Interacción con el usuario
print("Programa de cifrado y descifrado de César\n")
opcion = input("Elija una opción (1: Cifrar, 2: Descifrar): ")

if opcion == "1":
    frase = input("Ingrese la frase a cifrar: ")
    resultado = cifrar_frase(frase)
    print("Frase cifrada:", resultado)
elif opcion == "2":
    frase = input("Ingrese la frase a descifrar: ")
    resultado = descifrar_frase(frase)
    print("Frase descifrada:", resultado)
else:
    print("Opción no válida, por favor ingrese '1' o '2'.")
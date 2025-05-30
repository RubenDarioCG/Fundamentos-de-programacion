
""". Construir un programa que tome una cadena de caracteres e imprima todas la posibles permutaciones de los 
mismos.  Antes de construirlas, el programa deberá limpiar posibles caracteres repetidos de la cadena.  Se 
deberá obtener un número N de elementos que se toman, y se debe tener en cuenta el número M de posibles 
valores, es decir, el número de caracteres diferentes en la cadena dada.  Por ejemplo:
 cadena de entrada: abcfga
 elementos que se tienen en cuenta: abcfg
 permutaciones:
 abcfg
 abcgf
 abgfc
 …
 El programa deberá imprimir todas las posibles permutaciones, que se entienden como todos los posibles 
ordenamientos del conjunto de caracteres que resulta de la limpieza de la cadena dada. Cada permutación se 
debe convertir en una cadena de texto a la hora de presentar los resultados."""

#Desarrollo

from itertools import permutations

def limpiar_cadena(cadena):
    """
    Función que elimina caracteres repetidos de la cadena y los ordena alfabéticamente.
    """
    caracteres_unicos = sorted(set(cadena))  # Eliminamos duplicados y ordenamos
    cadena_limpia = "".join(caracteres_unicos)
    return cadena_limpia

def generar_permutaciones(cadena):
    """
    Función que genera todas las permutaciones posibles de la cadena ya limpia.
    """
    permutaciones_lista = ["".join(p) for p in permutations(cadena)]  # Generamos permutaciones
    return permutaciones_lista

# Interacción con el usuario
print("Programa para generar todas las permutaciones únicas de una cadena.\n")

cadena_entrada = input("Por favor, ingrese una cadena de caracteres: ")

# Limpiar la cadena de caracteres repetidos
cadena_limpia = limpiar_cadena(cadena_entrada)

print("\nElementos que se tienen en cuenta después de limpiar caracteres repetidos:", cadena_limpia)

# Generar todas las permutaciones de los caracteres únicos
permutaciones_generadas = generar_permutaciones(cadena_limpia)

print("\nPermutaciones posibles:")
for perm in permutaciones_generadas:
    print(perm)
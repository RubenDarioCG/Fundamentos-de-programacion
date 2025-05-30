
''' Dada una lista de enteros y una suma objetivo, escriba una función que imprima todos los pares únicos de 
elementos de la lista que suman la cantidad objetivo. Cada par debe imprimirse en una línea nueva en el 
formato a, b, y no deben contarse pares duplicados. La entrada consiste en una lista de enteros (por ejemplo, 
[1, 2, 3, 4, 3, 5, 6]), y un número entero que representa la suma objetivo (por ejemplo, 7).  La salida debe ser 
todos los pares únicos de números que suman el valor objetivo. Cada par se debe imprimir en una línea nueva 
en el formato a, b. Los mismos dos números en un orden diferente no deben aparecer nuevamente, por 
ejemplo:
 1, 6
 3, 4
 2, 5'''
 
 #Desarrollo

def encontrar_pares(lista, objetivo):
    """
    Encuentra todos los pares únicos de elementos en la lista que suman la cantidad objetivo.
    """
    pares = set()  # Usamos un conjunto para evitar duplicados
    numeros_vistos = set()  # Almacena los números ya procesados

    for num in lista:
        complemento = objetivo - num  # Calculamos el complemento necesario para la suma objetivo
        if complemento in numeros_vistos:
            pares.add(tuple(sorted((num, complemento))))  # Asegurar orden único del par
        numeros_vistos.add(num)  # Agregar el número procesado para futuras comparaciones

    return pares

# Interacción con el usuario
print("Programa para encontrar pares únicos que suman la cantidad objetivo.\n")

try:
    lista = list(map(int, input("Por favor, ingrese una lista de números separados por espacio: ").split()))
    objetivo = int(input("Por favor, ingrese la suma objetivo: "))

    resultados = encontrar_pares(lista, objetivo)

    print("\nPares únicos que suman la cantidad objetivo:")
    for par in resultados:
        print(f"{par[0]}, {par[1]}")

except ValueError:
    print("Error: Por favor, ingrese una lista de números válidos y una suma objetivo correcta.")
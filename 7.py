
''' Matrices triangulares – https://aceptaelreto.com/problem/statement.php?id=160&cat=14'''
#Desarrollo

def es_triangular(matriz, n):
    """
    Función que verifica si una matriz cuadrada es triangular superior, inferior o ambas.
    """
    triangular_superior = True
    triangular_inferior = True

    for i in range(n):
        for j in range(n):
            if j > i and matriz[i][j] != 0:  # Elementos por encima de la diagonal
                triangular_superior = False
            if j < i and matriz[i][j] != 0:  # Elementos por debajo de la diagonal
                triangular_inferior = False

    return triangular_superior or triangular_inferior

# Interacción con el usuario
print("Programa para verificar si una matriz cuadrada es triangular.\n")

while True:
    try:
        n = int(input("Ingrese el número de filas/columnas de la matriz (0 para salir): "))
        if n == 0:
            break
        if n < 1 or n > 50:
            print("El tamaño de la matriz debe estar entre 1 y 50.")
            continue

        matriz = []
        print(f"Ingrese los {n*n} elementos de la matriz fila por fila:")
        for i in range(n):
            fila = list(map(int, input(f"Fila {i+1}: ").split()))
            if len(fila) != n:
                print("Error: La cantidad de elementos no coincide con el tamaño de la matriz.")
                break
            matriz.append(fila)

        if es_triangular(matriz, n):
            print("SI, la matriz es triangular.")
        else:
            print("NO, la matriz no es triangular.")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese valores numéricos correctamente.")

    continuar = input("\n¿Desea ingresar otra matriz? (Sí = 's', No = cualquier otra tecla): ").lower()
    if continuar != 's':
        break
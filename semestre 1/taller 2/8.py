
'''Escribir un programa que pida números enteros positivos y los convierta en romanos. El programa debe 
pedir números enteros hasta que se introduzca un 0, lo que detiene el ciclo.'''

#Desarrollo

def entero_a_romano(n):
    """
    Convierte un número entero positivo en su equivalente en números romanos.
    """
    valores_romanos = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    resultado = ""
    for valor, simbolo in valores_romanos:
        while n >= valor:
            resultado += simbolo
            n -= valor
    
    return resultado

# Interacción con el usuario
print("Programa de conversión de números enteros a romanos.\n")
print("Ingrese números enteros positivos para convertirlos a romanos.")
print("Ingrese '0' para salir.\n")

while True:
    try:
        num = int(input("Por favor, ingrese un número entero positivo: "))
        if num == 0:
            print("Fin del programa.")
            break
        elif num < 0:
            print("Por favor, ingrese un número positivo.")
        else:
            print(f"Número en romano: {entero_a_romano(num)}\n")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero correctamente.\n")
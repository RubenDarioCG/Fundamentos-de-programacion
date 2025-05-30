
"""Problemas de Herencia – https://aceptaelreto.com/problem/statement.php?id=103&cat=13"""
#Desarrollo

import numpy as np

def evaluar_polinomio(coeficientes, x):
    """
    Evalúa un polinomio en un punto x dado.
    """
    return sum(coef * (x ** i) for i, coef in enumerate(reversed(coeficientes)))

def calcular_area(coeficientes, n):
    """
    Calcula el área bajo la curva del polinomio usando la suma de Riemann.
    """
    base = 1 / n  # Ancho de cada rectángulo
    area = 0

    for i in range(n):
        x = i * base
        altura = evaluar_polinomio(coeficientes, x)
        
        # Ajustar valores fuera del rango [0,1]
        if altura < 0:
            altura = 0
        elif altura > 1:
            altura = 1
        
        area += base * altura

    return area

# Interacción con el usuario
print("Programa para calcular la división de tierras entre Caín y Abel.\n")

while True:
    try:
        grado = int(input("Ingrese el grado del polinomio (0-19): "))
        if grado < 0 or grado > 19:
            print("El grado debe estar entre 0 y 19.")
            continue

        coeficientes = list(map(float, input(f"Ingrese {grado + 1} coeficientes en orden decreciente: ").split()))
        n = int(input("Ingrese el número de rectángulos para la aproximación: "))

        area_cain = calcular_area(coeficientes, n)
        area_abel = 1 - area_cain  # El terreno total es 1 hectárea

        print(f"\nÁrea de Caín: {area_cain:.6f} hm²")
        print(f"Área de Abel: {area_abel:.6f} hm²")

        if abs(area_cain - area_abel) <= 0.001:
            print("La división es justa.")
        elif area_cain > area_abel:
            print("Caín recibe más tierra.")
        else:
            print("Abel recibe más tierra.")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese valores numéricos correctamente.")

    continuar = input("\n¿Desea ingresar otro caso? (Sí = 's', No = cualquier otra tecla): ").lower()
    if continuar != 's':
        break
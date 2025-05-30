

'''' Construir un programa que reciba las componentes en x y y de un vector y calcule una proyección del 
mismo sobre un par de vectores unitarios al azar.  El programa de permitir recibir más de un vector, pero uno 
a la vez. Para cada caso graficar el punto inicial y los puntos que representan las proyecciones.
'''

#Desarrollo

import numpy as np
import matplotlib.pyplot as plt

def generar_vector_unitario():
    """
    Genera un vector unitario aleatorio en R².
    """
    v = np.random.rand(2)  # Vector aleatorio
    v_unitario = v / np.linalg.norm(v)  # Normalización para que sea unitario
    return v_unitario

def proyectar_vector(vector, base):
    """
    Calcula la proyección del vector sobre otro vector unitario.
    """
    return (np.dot(vector, base) / np.dot(base, base)) * base

# Interacción con el usuario
print("Programa de proyección de vectores sobre dos vectores unitarios aleatorios.\n")

while True:
    try:
        vx = float(input("Ingrese la componente x del vector: "))
        vy = float(input("Ingrese la componente y del vector: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        continue

    vector = np.array([vx, vy])
    
    # Generar dos vectores unitarios aleatorios
    u1 = generar_vector_unitario()
    u2 = generar_vector_unitario()

    # Calcular las proyecciones
    proy1 = proyectar_vector(vector, u1)
    proy2 = proyectar_vector(vector, u2)

    # Graficar los vectores y sus proyecciones
    plt.figure(figsize=(6, 6))

    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r', label="Vector Original")
    plt.quiver(0, 0, proy1[0], proy1[1], angles='xy', scale_units='xy', scale=1, color='b', label="Proyección sobre U1")
    plt.quiver(0, 0, proy2[0], proy2[1], angles='xy', scale_units='xy', scale=1, color='g', label="Proyección sobre U2")

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.title("Proyección de un vector sobre dos vectores unitarios")
    plt.show()

    continuar = input("\n¿Desea ingresar otro vector? (Sí = 's', No = cualquier otra tecla): ").lower()
    if continuar != 's':
        break
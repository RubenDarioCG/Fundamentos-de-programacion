'''
Construir un programa que muestre los términos de la serie de Fibonacci que sean menores o iguales a
un valor entero dado por el usuario.
'''
#Solicitar el entero
n = int(input("Ingresa un número entero: "))

#Inicializar los primeros digitos de la sucesion y la lista donde van a guardarse.
a = 0
b = 1
lista = "0, 1"

#Empezar con i en 2 para empezar por el 3er elemento
i = 2

#Recorrer n posiciones
while i < n:
    suma = a + b
    a = b
    b = suma
    if b < n:
        lista = lista + ", " + str(b) #Agregar b a la lista cuando sea menor que n
    i = i + 1

print(lista) #Dar la lista de numeros de la sucecion menores que n
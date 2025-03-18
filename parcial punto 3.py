'''
Escribir un programa que lea un número entero y determine cuales de sus
cifras son pares y cuales son impares. Además, el programa debe contar cuantas
cifras tiene el número en total.
'''
n = int(input("Ingrese un número")) #se pide el numero a evaluar
m= str(n) #convertimos el numero n a cadena y lo almacenamos en m
cifras= len(m) #se usa len para obtener la cantidad de cifras, y se almacena en "cifras"
for i in m: 
    if int(i)%2==0: #se determina si el residuo de la division entre 2 es 0 en cada cifra del numero para saber que cifra es par e impar
        print(f"El número {i} es par")
    else:
        print(f"El número {i} es impar")
print(f"La cantidad de cifras del número ingresado es de:",cifras) #se imprime si es par o impar, y cuantas cifras tiene
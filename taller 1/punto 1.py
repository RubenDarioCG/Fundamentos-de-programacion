'''
 Construir un programa que lea un número variable de valores enteros. El resultado que entregara el
 programa es la media de los números pares de entre los leídos, es decir, la suma de todos los valores
 pares dividida por el número de estos.
'''

#Numero de elementos que se promedian
n = int(input("¿Cuántos valores numéricos desea ingresar? "))

suma = 0
a = 0

#Recorrer la cantidad de elementos elegida
for i in range(1,n+1):
    
    #Definir el valor en la posición i y guardarlo temporalmente
    m = int(input(f"valor {i}: "))
    
    #Si m es par se agrega a la suma y el numero de pares sube 1
    if m % 2 == 0:
        suma = suma + m
        a = a + 1

promedio = suma / a
print ("El promedio de los números pares que ingresaste es: " + str(promedio))
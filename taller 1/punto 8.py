'''
Escribir un programa que lea un entero positivo y escriba el mismo número conformado por las cifras
del número leído más 1. Si al sumar uno a una cifra da 10 se debe poner 0. Por ejemplo:
12345 → 23456.
987654 → 098765.
'''

#Pedir un numero entero
n = int(input("Ingresa un número entero: "))

#Guardar la forma en texto de n
m = str(n)
#Inicializar donde se va a guardar el nuevo numero
num = ""

#Recorrer cada caracter de n
for i in m:
    if int(i)+1 > 9: #En caso de que i+1 sea mas de 10, agregar un 0
        num = num + "0"
    else: #Si no, agregar i+1
        num = num + str(int(i)+1)

print(num) #Imprimir finalmente el nuevo numero
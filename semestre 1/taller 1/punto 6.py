'''
Escribir un programa que reciba una entrada n, que es un número entero. El programa devolverá una
lista de números enteros hasta n, incluyéndolo, y especificando si el número es divisible por 2, 3 o por
5, o si es divisible por ambos. Por ejemplo, asumiendo una entrada n=18:
'''

#Preguntar por la cantidad de elementos de la lista
n = int(input("Ingresa un número entero: "))

#Inicializar los comprobantes de divisibilidad
div2 = False
div3 = False
div5 = False

for i in range(1, n+1):
    
    #Comprobar si el elemento actual es divisible entre 2, 3 o 5
    if i % 2 == 0:
        div2 = True
    if i % 3 == 0:
        div3 = True
    if i % 5 == 0:
        div5 = True
    
    #Dependiendo de los casos, imprimir en que numeros es divisble es el elemento i
    if div2:
        if div3 and div5:
            print(str(i) + ". Divisible entre 2, 3 y 5")
        elif div3:
            print(str(i) + ". Divisible entre 2 y 3")
        elif div5:
            print(str(i) + ". Divisible entre 2 y 5")
        else:
            print(str(i) + ". Divisible entre 2")
            
    elif div3:
        if div5:
            print(str(i) + ". Divisible entre 3 y 5")
        else:
            print(str(i) + ". Divisible entre 3")
            
    elif div5:
        print(str(i) + ". Divisible entre 5")
        
    else: 
        print(str(i) + ". ")
    
    div2 = False
    div3 = False
    div5 = False
'''
Escribir un programa que lea un número entero y determine si este es un
palíndromo, es decir, que se lee igual de izquierda a derecha que de derecha a
izquierda. Estos números se conocen como como capicúas.
'''
n= int(input("ingrese un número: ")) #se pide el numero a evaluar
m= "" #valor para el numero leido al reves
cadena= str(n) #convertimos n a cadena y la almacenamos en "cadena"
for i in cadena:
    m= i+m #se lee el numero al reves y se almacena en m
if int(m)==n: #se evalua si el numero leido al reves es o no capicua
    #se imprime el numero y si es o no capicua:
    print(f"el número ingresado {n} es capicúa") 
else:
    print(f"El número ingresado {n} no es capicúa")
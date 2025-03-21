'''
Construir un programa que permita escoger entre dos operaciones, usando un
menú. La primera, leer un número n y determinar si es par o impar.  La segunda,
leer un número n y determinar si es primo o no. n debe ser un número entero
positivo. El programa debe detectar si la opción escogida es o no válida.
'''
#se pide al usuario escoger una operacion:
print("Escoja una de las siguiente operaciones:")
print("Operación 1: Comprobar si el número es par o impar")
print("Operación 2: comprobar si el número es primo o no")
p= int(input())
if p==1: #el usuario elige la operacion 1, comprobar si es par o impar
    n = int(input("Ingrese un número: "))
    if n%2==0: #si el residuo del numero dado dividido en 2 es 0, es par, si no es impar
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")
elif p==2: #el usuario elige la operacion 2, comprobar si es primo o no
    n = int(input("Ingrese un número: ")) 
    div = 0 #div (cantidad de divisores) se inicializa en 0
    z=n #se guarda el valor del numero n en z para distinguir la variable mejor
    for i in range(1,z+1): #se evaluan la cantidad de divisores, empezando desde el numero 1
      if z % i == 0: 
             div= div +1 #si el resudio de z entre i es 0, se aumenta el numero de divisores en 1
    if div>2: #si el numero dado tiene mas de 2 divisores, no es primo, si tiene 2 o menos, es primo
         print(f"El número {n} ingresado no es primo")
    else:
            print(f"El número {n} ingresado es primo")
else:
    print("Ingrese una operación valida") #si el usuario ingresa una operacion diferente a 1 o 2, se le pide ingresar una operacion disponible
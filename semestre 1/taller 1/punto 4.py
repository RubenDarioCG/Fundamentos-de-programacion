'''
Construir un programa que lea dos números y si son ambos pares o ambos impares, halle el máximo 
común divisor de dos números; si uno es par y el otro impar, el programa debe hallar el mínimo común 
múltiplo.
'''

#pide al usuario ingresar un numero entero y lo convierte a tipo entero
n1 = int(input("Digite un numero entero: "))
#pide al usuario ingresar un segundo numero entero y lo convierte a tipo entero
n2 = int(input("Digite otro numero entero: "))
#Verifica si ambos numeros son pares o impares
if (n1 % 2 == 0 and n2 % 2 == 0) or (n1 % 2 != 0 and n2 % 2 != 0):
    #Si alguno de los numeros es cero, se establece el mcd (maximo comun divisor) en 0
    if n1 == 0 or n2 == 0:
        mcd = 0
    # Si el primer numero es mayor que el segundo, se usara un ciclo while
    elif n1 > n2:
        i = 1
        # Se itera desde 1 hasta n2 para encontrar todos los divisores comunes
        while i <= n2:
            # Si i es divisor de ambos numeros
            if n1 % i == 0 and n2 % i == 0:
                mcd = i  # Se actualiza mcd con el divisor actual (el mayor encontrado hasta el momento)
            i = i + 1
    #Si el primer numero es menor que el segundo, se utiliza un ciclo for
    elif n1 < n2:
        # Se itera desde 1 hasta n1 (inclusive) para hallar divisores comunes
        for i in range(1, n1 + 1, 1):
           if n1 % i == 0 and n2 % i == 0:
                mcd = i  # Se actualiza mcd con el divisor actual encontrado
    #Si ambos numeros son iguales, el mcd es el mismo numero
    else:
        mcd = n1
    #Si mcd es 0, significa que al menos uno de los numeros era 0 y no se puede definir un mcd convencional
    if mcd == 0:
        print(f"{n1} y {n2} no poseen máximo comun divisor")
    else:
        print(f"El maximo comun divisor entre {n1} y {n2} es {mcd}")
#Caso en el que uno de los numeros es par y el otro impar
else:
    #Si alguno de los numeros es 0, se establece el mcm (minimo comun multiplo) en 0
    if n1 == 0 or n2 == 0:
        mcm = 0
    #Si los numeros son diferentes
    elif n1 != n2:
        #Se determina cual de los dos numeros es mayor y se asigna a la variable 'max'
        if n1 > n2:
            max = n1
        else:
            max = n2
        #Se recorre desde el producto de n1 y n2 hasta el mayor de ellos, en orden descendente
        for i in range(n1 * n2, max - 1, -1):
            #Si i es multiplo de ambos numeros
            if i % n1 == 0 and i % n2 == 0:
                mcm = i  #Se actualiza mcm con el multiplo comun actual encontrado
    #Si ambos numeros son iguales, el mcm es el mismo número
    else:
        mcm = n1
    #Se imprime el resultado del minimo comun multiplo
    print(f"El minimo comun multiplo entre {n1} y {n2} es {mcm}")
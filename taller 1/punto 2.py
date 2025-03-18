'''
Construir un programa que lea un número entero mayor que 2 y devuelva como resultado el
número primo de valor más cercano, en este caso menor o igual, al número leído.
'''

#n es el numero, p el numero primo y div el numero de divisores
n = int(input("numero a revisar:"))
p = n
div = 3 #div inicia en 3 para que entre directamente al bucle while de más adelante

if n > 2:

    #Comprobar si el numero es primo o no
    while div > 2:
        div = 0 #Reinicializar el div una vez iniciado el bucle

        #Combrobar si p es primo o no
        for i in range(1,p+1):
            if p%i == 0:
                div=div+1
        #Restarle 1 a p en caso de que no sea primo
        if div > 2:
            p = p-1
    #Dar la respuesta cuando p sea primo

    print(f"El numero primo más cercano a {n} es {p}")
else:
    print("Debes ingresar un valor mayor a 2")
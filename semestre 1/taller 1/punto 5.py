''' Escribir un programa que permita convertir un entero dado en base 2, 4, 8, 16.'''

#pedir un valor
n = int(input("Número a representar: "))

#pedir la base
print("Seleccione una base para hacer la representación del número")
print("OPCIONES: 2 - 4 - 8 - 16")
b = int(input("Base: "))

#Inicializar variables
m = 0 #Valor para los números en base 2, 4 u 8
fact = 1 #factor para recorrer los dígitos para las bases 2, 4, 8
hexa = "" #Valor para los números en hexadecimal

if b == 2 or b == 4 or b == 8:
    
    while n > 0:
        
        z = int(n // 1) #Definir z como la parte entera de n
        r = z % b #Definir r como el residuo entre z y b
        n = z / b #Dividir a z entre b y guardarlo en n
        m = m + (fact * r) #Colocar el residuo en la posición con base en fact
        fact = fact * 10 #Mover la posición del residuo que se está evaluando
    print (m) #Imprimir el valor con la base cambiada
    
#En caso de que la base sea Hexadecimal    
elif b == 16:
    print("Hexadecimal")
    #Mientras n sea mayor a 0
    while n > 0:
        
        z = int(n // 1) #Definir z como la parte entera de n
        r = z % b #Definir r como el residuo entre z y 16
        
        #Si el modulo es menor a 10, agregar el número a la izquierda de lo que llevamos
        if r < 10:
            hexa = str(r) + hexa
        #Si el modulo es de 10 hasta 15, agregar las letras A hasta F respectivamente
        elif r == 10:
            hexa = "A" + hexa
        elif r == 11:
            hexa = "B" + hexa
        elif r == 12:
            hexa = "C" + hexa
        elif r == 13:
            hexa = "D" + hexa
        elif r == 14:
            hexa = "E" + hexa
        elif r == 15:
            hexa = "F" + hexa
        n = z // b # ividir z entre b y guardar el valor en n
        
    print (hexa) #Imprimir el valor en Hexadecimal
    
#Si la base no coincide con los valores, notificar
else:
    print("La base debe ser 2, 4, 8 o 16")
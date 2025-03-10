#buscamos que el usuario introduzca un numero, para luego introducir la base en la que sera representado

n = int(input("Número a representar: "))
b = int(input("Base nueva en la que representarlo: "))
i = 0
fact = 1
if 2 <= b & b < 10:
    print(n)
    while n > 0:
        m = int(n // 1)
        r = m % b
        print(r)
        n = m / b
        i = i + (fact * r)
        fact = fact * 10
    print (i)
else:
    print("La base debe ser un número entre 2 y 9")
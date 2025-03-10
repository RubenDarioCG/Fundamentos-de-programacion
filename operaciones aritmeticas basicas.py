#se busca hacer un menu en el que se pueda elegir una operacion aritmetica a realizar introduciendo los valores de la operacion

salir = False

while salir == False:
    
    print("elija una operacion")
    print("Suma: +")
    print("Resta: -")
    print("Producto: *")
    print("Division: /")
    print("Salir: x")
    operacion = input()
    
    if operacion == "+":
        n1 = float(input("Primer numero: "))
        n2 = float(input("Segundo numero: "))
        print(n1 + n2)
    elif operacion == "-":
        n1 = float(input("Primer numero: "))
        n2 = float(input("Segundo numero: "))
        print(n1 - n2)
    elif operacion == "*":
        n1 = float(input("Primer numero: "))
        n2 = float(input("Segundo numero: "))
        print(n1 * n2)
    elif operacion == "/":
        n1 = float(input("Primer numero: "))
        n2 = float(input("Segundo numero: "))
        print(n1 / n2)
    elif operacion == "x" or operacion == "X":
        salir = True
    else:
        print("Seleccion erronea, no se encontro la operacion")
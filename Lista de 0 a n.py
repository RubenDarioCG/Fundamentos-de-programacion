#se busca hacer una lista que vaya desde el 0, hasta el numero dado por el usuario (n), arrojando los valores que sean divisibles entre: 2, 3 y/o 5

n = int(input("número hasta el que llegara la lista: "))

for i in range (n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        print(i)
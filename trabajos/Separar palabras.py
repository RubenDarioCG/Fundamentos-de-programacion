#se busca separar las palabras de la frase dada por el usuario en lineas diferentes

frase = input("Ingrese una frase: ")

n = len(frase)
separador = " "
palabra = ""

for f in range(n):
    if frase[f] == separador:
        print(palabra)
        palabra = ""
    else:
        palabra = palabra + frase[f]
print(palabra)
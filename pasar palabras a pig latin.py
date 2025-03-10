#se busca convertir una palabra dada por el usuario al sistema pig latin

palabra = input("Palabra a convertir: ")
n = len(palabra)
piglatin = ""

for p in range(n):
    if p == 0:
        l1 = palabra[p]
    else:
        piglatin = piglatin + palabra[p]

print(piglatin + l1 + "ay")
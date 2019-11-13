#!/usr/bin/python3

def procesar(numero):
    contador = 0
    while numero != "6174":
        contador += 1

        max = minuendo(numero)
        min = sustraendo(numero)

        numero = str(max - min)
    return contador

# Construimos el número mayor
def minuendo(numero):
    size = len(numero)
    arr = [
        numero[0],
        numero[1],
        numero[2],
        numero[3] if (size == 4) else "0",
    ]
    arr.sort()
    arr.reverse()
    return int("".join(str(e) for e in arr))

# Construimos el número menor
def sustraendo(numero):
    size = len(numero)
    arr = [
        numero[0],
        numero[1],
        numero[2],
        numero[3] if (size == 4) else "0",
    ]
    arr.sort()

    return int("".join(str(e) for e in arr))


print("")
print("CONSTANTE DE KAPREKAR")
print("=====================")
print("")

exclusiones = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]

for x in range(1000, 10000):
    if not x in exclusiones:
        print(x, "=", procesar(str(x)))
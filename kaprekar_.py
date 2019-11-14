#!/usr/bin/python3

def procesar(numero):
    contador = 0
    while numero != "6174":
        contador += 1

        mayor = minuendo(numero)
        menor = sustraendo(numero)

        numero = str(mayor - menor)
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

exclusiones = [1111, 2222, 3333, 4444, 5555, 6174, 6666, 7777, 8888, 9999]
minimo = 100
maximo = 0
lista_min = []
lista_max = []

for x in range(1000, 10000):
    if not x in exclusiones:
        intentos = procesar(str(x))
        if minimo > intentos: 
            lista_min.clear()
            minimo = intentos
            lista_min.append(x)
        if minimo == intentos: 
            lista_min.append(x)
        if maximo < intentos:
            lista_max.clear()
            maximo = intentos
            lista_max.append(x)
        if maximo == intentos:
            lista_max.append(x)

print("Cantidad de Intentos menor:", minimo)
print(lista_min)
print("Cantidad de Intentos mayor:", maximo)
print(lista_max)
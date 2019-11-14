#!/usr/bin/python3

def procesar(numero):
    contador = 0
    while numero != "6174":
        contador += 1

        mayor = minuendo(numero)
        menor = sustraendo(numero)

        numero = str(mayor - menor)
        print( str(contador) + '.- (', mayor, "-", menor, ")\t=\t", numero)

    print("================================================")
    print("Constante de Kaprekar encontrada en ("+ str(contador) +") intentos.")
    print("================================================")
    print("")

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
# Pedimos que ingresen un número de 4 dígitos
numero = input("Introduce un número de cuatro dígitos: ")


exclusiones = [1111, 2222, 3333, 4444, 5555, 6174, 6666, 7777, 8888, 9999]

# Evaluamos que el valor introducido sea un número y que sea de cuatro dígitos
if numero.isnumeric() and len(numero) == 4:
    if not int(numero) in exclusiones:
        print("Procesando el número:", numero, " para llegar a la constante de Kaprekar:")
        procesar(numero)
    else:
        print("No se permiten número de cuatro dígitos iguales (Ej. 1111), ni el 6174.")
else:
    print("No es un número de 4 dígitos.")

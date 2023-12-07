"""Generar de forma aleatoria un vector de 10 elementos enteros, los números aleatorios
serán del 1 al 10 y se tiene que controlar que los números no se repitan."""

import random

def generarnumeros():
    numeros = []
    try:
        while len(numeros) < 10:
            numero = random.randint(1, 10)
            if numero not in numeros:
                numeros.append(numero)
        print(f"La lista desordenada es: {numeros}")
    except FileNotFoundError:
        print("Error")
    return numeros

def listadesordenada(numeros):
    try:
        with open("listadesornedada.txt", "w") as archivo:
            archivo.write(str(numeros))
        print(f"Lista desordenada: {numeros}")
    except FileNotFoundError:
        print("Error")
    return numeros



"""Generar de forma aleatoria un vector de 10 elementos enteros, los números aleatorios
serán del 1 al 10 y se tiene que controlar que los números no se repitan."""

import random

def generar_vector():
    vector = []
    while len(vector) < 10:
        numero = random.randint(1, 10)
        if numero not in vector:
            vector.append(numero)
    return vector

def listadesordenada(vector):
    with open("listadesordenada.txt", "w") as archivo:
        for numero in vector:
            archivo.write(str(numero))
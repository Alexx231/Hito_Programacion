""" Generar de forma aleatoria un vector de 10 elementos enteros, los números aleatorios
serán del 1 al 10 y se tiene que controlar que los números no se repitan. """

import random

def generarVector():
    vector = []
    for i in range(10):
        num = random.randint(1, 10)
        while num in vector:
            num = random.randint(1, 10)
        vector.append(num)
    return vector

def listadesordenada(vector):
    try:
        with open("listadesordenada.txt", "w") as archivo:
            archivo.write(str(vector))
    except FileNotFoundError:
        print("No se ha podido guardar el vector en el archivo")

vector = generarVector()
listadesordenada(vector)

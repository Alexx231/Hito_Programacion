""" Aplicar el algoritmo de ordenación de Bubblesort: se debe mostrar información por pantalla para indicar
los distintos pasos que realiza el algoritmo. Mostrar el vector antes de la ordenación. y después de la ordenación. Imprimir el vector ordenado en una lista llamada listaordenada"""

from ordenacionnumeros import *

def bubble_sort(vector):
    n = len(vector)
    paso = 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                print(f"Paso {paso} de la ordenación: {vector}")
                paso += 1
    return vector
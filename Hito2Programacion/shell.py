""" Aplicar el algoritmo de ordenación de Shellsort: se debe mostrar información por pantalla para indicar
los distintos pasos que realiza el algoritmo. Mostrar el vector antes de la ordenación. y después de la ordenación. """

from ordenacionnumeros import *

def shell_sort(vector):
    gap = len(vector) // 2
    while gap > 0:
        for i in range(gap, len(vector)):
            temp = vector[i]
            j = i
            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j -= gap
            vector[j] = temp
            print(f"Paso a paso de la ordenación por el metodo shell: {vector}")
        gap //= 2
    return vector
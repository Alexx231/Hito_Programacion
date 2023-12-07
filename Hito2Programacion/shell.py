""" Aplicar el algoritmo de ordenación de Shellsort: se debe mostrar información por pantalla para indicar
los distintos pasos que realiza el algoritmo. Mostrar el vector antes de la ordenación. y después de la ordenación. """

from ordenacionnumeros import *

def shellSort(vector):
    gap = len(vector) // 2
    while gap > 0:
        for i in range(gap, len(vector)):
            aux = vector[i]
            j = i
            while j >= gap and vector[j-gap] > aux:
                vector[j] = vector[j-gap]
                j -= gap
            vector[j] = aux
        print(vector)
        gap //= 2
    return vector

def listaordenada(vector):
    try:
        with open("listaordenada.txt", "w") as archivo:
            archivo.write(str(shellSort(vector)))
        print(f"La lista ordenada por el metodo shell es:{shellSort(vector)}")
    except FileNotFoundError:
        print("No se ha podido guardar el vector en el archivo")

vector = generarVector()
print(vector)
vector = shellSort(vector)
print(vector)
listaordenada(vector)

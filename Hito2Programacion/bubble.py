""" Aplicar el algoritmo de ordenación de Bubblesort: se debe mostrar información por pantalla para indicar
los distintos pasos que realiza el algoritmo. Mostrar el vector antes de la ordenación. y después de la ordenación. Imprimir el vector ordenado en una lista llamada listaordenada"""

from ordenacionnumeros import *

def bubbleSort(vector):
    try:
        for i in range(len(vector)):
            for j in range(len(vector)-i-1):
                if vector[j] > vector[j+1]:
                    vector[j], vector[j+1] = vector[j+1], vector[j]
            print(vector)
    except FileNotFoundError:
        print("Error")
    return vector

def listaordenada(vector):
    try:
        with open("listaordenadabubble.txt", "a") as archivo:
            archivo.write(str(bubbleSort(vector)))
        print(f"La lista ordenada por el metodo bubble es:{bubbleSort(vector)}")
    except FileNotFoundError:
        print("No se ha podido guardar el vector en el archivo")

vector = generarVector()
print(vector)
vector = bubbleSort(vector)
print(vector)
listaordenada(vector)

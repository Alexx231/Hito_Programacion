""" Aplicar el algoritmo de ordenación de Shellsort: se debe mostrar información por pantalla para indicar
los distintos pasos que realiza el algoritmo. Mostrar el vector antes de la ordenación. y después de la ordenación. """

from ordenacionnumeros import *

def shell_sort(vector):
    gap = len(vector) // 2
    paso = 1
    while gap > 0:
        for i in range(gap, len(vector)):
            temp = vector[i]
            j = i
            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j -= gap
            vector[j] = temp
            print(f"Paso {paso} de la ordenación: {vector}")
            paso += 1
        gap //= 2
    return vector

def listaordenada_shell(vector):
    try:
        with open("listaordenada_shell.txt", "w") as archivo:
                archivo.write(str(vector))
        print("Archivo creado correctamente")
    except FileNotFoundError:
        print("No se ha podido crear el archivo")
    return vector
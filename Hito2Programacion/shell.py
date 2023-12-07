""" Aplicar el algoritmo de ordenación de Shellsort: se debe mostrar información por pantalla para indicar
los distintos pasos que realiza el algoritmo. Mostrar el vector antes de la ordenación. y después de la ordenación. """

from ordenacionnumeros import *

def shellSort(numeros):
    try:
        n = len(numeros)
        intervalo = n // 2
        while intervalo > 0:
            for i in range(intervalo, n):
                temp = numeros[i]
                j = i
                while j >= intervalo and numeros[j - intervalo] > temp:
                    numeros[j] = numeros[j - intervalo]
                    j -= intervalo
                numeros[j] = temp
            intervalo //= 2
        print(numeros)
    except FileNotFoundError:
        print("Error")
    return numeros

def listaordenada(numeros):
    try:
        with open("listaordenadashell.txt", "a") as archivo:
            archivo.write(str(shellSort(numeros)))
        print(f"La lista ordenada por el metodo shell es:{shellSort(numeros)}")
    except FileNotFoundError:
        print("No se ha podido guardar el vector en el archivo")

numeros = generarnumerosdesordenados()
print(numeros)
numeros_ordenados = shellSort(numeros)
print(numeros_ordenados)
listaordenada(numeros_ordenados)
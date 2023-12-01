from ordenacionnumeros import *

def bubbleSort(numeros_desordenados):
    n = len(numeros_desordenados)
    for i in range(n):
        for j in range(0, n-i-1):
            if numeros_desordenados[j] > numeros_desordenados[j+1] :
                numeros_desordenados[j], numeros_desordenados[j+1] = numeros_desordenados[j+1], numeros_desordenados[j]
                print(f"La lista ordenada por el metodo Bubble: {numeros_desordenados}")
    return numeros_desordenados

from ordenacionnumeros import *

def shellSort(numeros_desordenados):
    n = len(numeros_desordenados)
    intervalo = n // 2

    while intervalo > 0:
        for i in range(intervalo, n):
            temp = numeros_desordenados[i]
            j = i
            while j >= intervalo and numeros_desordenados[j - intervalo] > temp:
                numeros_desordenados[j] = numeros_desordenados[j - intervalo]
                j -= intervalo
            numeros_desordenados[j] = temp
            print(f"La lista ordenada por el metodo Shell: {numeros_desordenados}")
        intervalo //= 2

    return numeros_desordenados

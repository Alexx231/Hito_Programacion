import random

def generar_vector():
    vector = []
    while len(vector) < 10:
        numero = random.randint(1, 10)
        if numero not in vector:
            vector.append(numero)
    return vector

def bubble_sort(vector):
    n = len(vector)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                print(f"Paso a paso de la ordenación por el metodo bubble: {vector}")
    return vector

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

def main():
    vector = generar_vector()
    print(f"Vector antes de la ordenación: {vector}")
    vector = bubble_sort(vector)
    print(f"Vector después de la ordenación Bubble Sort: {vector}")
    vector = generar_vector()
    print(f"Vector antes de la ordenación: {vector}")
    vector = shell_sort(vector)
    print(f"Vector después de la ordenación Shell Sort: {vector}")

main()
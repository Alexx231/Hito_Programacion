

import random

numeros_desordenados= []

def generarnumeros(numeros_desordenados):
    try:
        with open("listadesordenada.txt", "a") as archivo:
            while len(numeros_desordenados) < 10:
                numero = random.randint(1, 10)
                if numero not in numeros_desordenados:
                    numeros_desordenados.append(numero)
                archivo.write(f"{numeros_desordenados}" + ",")
            print(f"La lista de numeros desordenada es: {numeros_desordenados}")
    except FileNotFoundError:
        print("La lista no ha podido ser generada")

    return numeros_desordenados


generarnumeros(numeros_desordenados)
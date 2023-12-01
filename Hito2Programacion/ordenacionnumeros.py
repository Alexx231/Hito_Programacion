
import random

numeros_desordenados = []

numeros_ordenados = []

def generarnumeros():
    try:
        while len(numeros_desordenados) < 10:
            numero = random.randint(1, 10)
            if numero not in numeros_desordenados:
                numeros_desordenados.append(numero)
        with open("listadesordenada.txt", "w") as archivo:
            archivo.write(str(numeros_desordenados))
        print(f"La lista aleatoria es : {numeros_desordenados}")
    except FileNotFoundError:
        print("La lista no ha podido ser generada")
    return numeros_desordenados

def listaordenada():
    try:
        with open("listaordenada.txt", "w") as archivo:
            archivo.write(str(numeros_ordenados))
    except FileNotFoundError:
        print("La lista ordenada no pudo ser guardada")
    return numeros_ordenados
from ordenacionnumeros import generarnumeros
from bubble import *
from shell import *

def menu():
    print(f"BIENVENIDO\n")
    print(f"1. Generar lista de números aleatorios")
    print(f"2. Ordenar lista con BubbleSort")
    print(f"3. Ordenar lista con ShellSort")
    print(f"4. Salir")
    opcion = input("\nSeleccione una opción: ")
    return (int(opcion))

while True:
    opcion = menu()
    
    if opcion == 1:
        generarnumeros()
    elif opcion == 2:
        bubbleSort(numeros_desordenados)
    elif opcion == 3:
        shellSort(numeros_desordenados)
    elif opcion == 4:
        print(f"\nGracias por utilizar nuestro programa")
        break
    
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
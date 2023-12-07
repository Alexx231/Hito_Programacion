from ordenacionnumeros import *
from bubble import *
from shell import *

def menu():
    print("BIENVENIDO AL PROGRAMA DE ORDENACIÓN DE NÚMEROS\n")
    print("1. Generar vector")
    print("2. Ordenación por el método Bubble Sort")
    print("3. Ordenación por el método Shell Sort")
    print("4. Salir")
    opcion = int(input("Introduce una opción: "))
    return opcion


while True:
    opcion = menu()
    
    if opcion == 1:
        vector = generar_vector()
        listadesordenada(vector)
        print(f"\nVector generado: {vector}\n")
    elif opcion == 2:
        vector = bubble_sort(vector)
        listaordenada_bubble(vector)
        print(f"\nVector después de la ordenación Bubble Sort: {vector}\n")
    elif opcion == 3:
        vector = shell_sort(vector)
        listaordenada_shell(vector)
        print(f"\nVector después de la ordenación Shell Sort: {vector}\n")
    elif opcion == 4:
        print("\nGracias por usar el programa\n")
        break
    else:
        print("Opción incorrecta")
        
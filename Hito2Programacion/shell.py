""" 
El sistema importa todas las funciones y variables del módulo ordenacionnumeros.

El sistema define la función shell_sort:

Establece una brecha inicial como la mitad de la longitud del vector.
Mientras la brecha sea mayor que 0, realiza lo siguiente:
Para cada elemento del vector desde la posición de la brecha hasta el final:
Guarda el valor del elemento actual en una variable temporal.
Mueve los elementos que son mayores que el valor temporal hacia la derecha.
Coloca el valor temporal en su posición correcta.
Imprime el paso actual de la ordenación y el estado actual del vector.
Reduce la brecha a la mitad.
Devuelve el vector ordenado.
El sistema define la función listaordenada_shell:

Intenta hacer lo siguiente:
Abre un archivo llamado "listaordenada_shell.txt" en modo de escritura.
Escribe el vector en el archivo.
Cierra el archivo.
Imprime un mensaje indicando que el archivo se creó correctamente.
Si no puede crear el archivo, imprime un mensaje de error.
Devuelve el vector. 
"""

from ordenacionnumeros import * #El sistema importa todas las funciones y variables del módulo ordenacionnumeros.

def shell_sort(vector): #El sistema define la función shell_sort con el parámetro vector.
    try:
        gap = len(vector) // 2 #Establece una brecha inicial como la mitad de la longitud del vector.
        paso = 1 #Inicializa la variable paso con el valor 1.
        while gap > 0: #Mientras la brecha sea mayor que 0, realiza lo siguiente:
            for i in range(gap, len(vector)): #Para cada elemento del vector desde la posición de la brecha hasta el final:
                temp = vector[i] #Guarda el valor del elemento actual en una variable temporal.
                j = i #Inicializa la variable j con el valor de i.
                while j >= gap and vector[j - gap] > temp: #Mueve los elementos que son mayores que el valor temporal hacia la derecha.
                    vector[j] = vector[j - gap] #Coloca el valor temporal en su posición correcta.
                    j -= gap #Reduce la brecha a la mitad.
                vector[j] = temp #Coloca el valor temporal en su posición correcta.
                print(f"Paso {paso} de la ordenación: {vector}") #Imprime el paso actual de la ordenación y el estado actual del vector.
                paso += 1 #Incrementa la variable paso en 1.
            gap //= 2 #Reduce la brecha a la mitad.
    except ValueError: #Si ocurre un error ValueError, realiza lo siguiente:
        print("El vector no puede ser ordenado por el metodo de Shell Sort") #Imprime un mensaje de error.
    return vector #Devuelve el vector ordenado.

def listaordenada_shell(vector): #El sistema define la función listaordenada_shell con el parámetro vector.
    try: #Intenta hacer lo siguiente:
        with open("listaordenada_shell.txt", "w") as archivo: #Abre un archivo llamado "listaordenada_shell.txt" en modo de escritura. 
                archivo.write(str(vector)) #Escribe el vector en el archivo.
        print("Archivo creado correctamente") #Imprime un mensaje indicando que el archivo se creó correctamente.
    except FileNotFoundError: #Si no puede crear el archivo, realiza lo siguiente:
        print("No se ha podido crear el archivo") #Imprime un mensaje de error.
    return vector #Devuelve el vector.
"""
CRITERIOS DE EVALUACIÓN

(0,75 Parte 1) Inicialmente se pedirá al usuario dos números que serán el número de filas y de columnas
de una matriz.

Función GenerarMatriz:
- Genera una matriz con números aleatorios entre 0 y filas*columnas.
- No se repiten salvo el 0.

(0,75 Parte 2)
Se piden coordenadas hasta que sean válidas.
Se guardan en un diccionario con claves fila y columna.
Se llama a SumarVecinos para sumar la casilla y sus alrededores.
"""

import random


def generar_matriz(numero_filas, numero_columnas):
    # Calculamos cuántas casillas tendrá la matriz completa
    numero_casillas = numero_filas * numero_columnas

    # Creamos una lista con todos los números posibles EXCEPTO el 0
    # Estos se usarán para colocarlos sin repetición
    numeros_no_cero_disponibles = list(range(1, numero_casillas + 1))

    # Creamos la matriz vacía
    matriz = []

    # Recorremos las filas usando i
    for i in range(numero_filas):

        # Añadimos una fila vacía a la matriz
        matriz.append([])

        # Recorremos las columnas usando j
        for j in range(numero_columnas):

            # Elegimos aleatoriamente si en esta posición pondremos un 0
            poner_cero = random.choice([True, False])

            if poner_cero:
                # Si sale True, colocamos un 0 directamente
                matriz[i].append(0)

            else:
                # Elegimos un índice aleatorio dentro de la lista de números disponibles
                indice = random.randrange(len(numeros_no_cero_disponibles))

                # Tomamos el valor que está en esa posición
                valor = numeros_no_cero_disponibles[indice]

                # Eliminamos ese número para que no pueda repetirse más
                numeros_no_cero_disponibles.pop(indice)

                # Insertamos el valor en la posición (i, j)
                matriz[i].append(valor)

    # Devolvemos la matriz completa ya generada
    return matriz


def mostrar_matriz(matriz):
    # Recorremos cada fila por índice
    for i in range(len(matriz)):

        # Recorremos cada columna por índice
        for j in range(len(matriz[0])):

            # Imprimimos cada valor separado por tabulador para formar columnas
            print(matriz[i][j], end="\t")

        # Al terminar la fila saltamos de línea
        print()


def sumar_vecinos(matriz, coordenada):
    # Extraemos del diccionario la fila seleccionada
    fila = coordenada["fila"]

    # Extraemos del diccionario la columna seleccionada
    columna = coordenada["columna"]

    # Guardamos los límites máximos de la matriz
    total_filas = len(matriz)
    total_columnas = len(matriz[0])

    # Variable acumuladora donde iremos sumando todas las casillas válidas
    suma = 0

    # Recorremos TODA la matriz con dos bucles
    for i in range(total_filas):
        for j in range(total_columnas):

            # Leemos el valor actual de la posición (i, j)
            valor_central = matriz[i][j]

            # Solo entramos cuando la posición actual coincide
            # con la coordenada pedida por el usuario
            if i == fila and j == columna:

                # Sumamos primero la casilla central
                suma = suma + valor_central

                # ---------------- DIAGONAL ARRIBA-IZQUIERDA ----------------
                # Para acceder a (i-1, j-1) comprobamos:
                # - que i > 0 (no estamos en la primera fila)
                # - que j > 0 (no estamos en la primera columna)
                if i > 0 and j > 0:
                    valor = matriz[i - 1][j - 1]
                    suma = suma + valor

                # ---------------- DIAGONAL ARRIBA-DERECHA ----------------
                # Subimos fila (i-1) y avanzamos columna (j+1),
                # pero solo si j no está en el borde derecho
                if i > 0 and j < total_columnas - 1:
                    valor = matriz[i - 1][j + 1]
                    suma = suma + valor

                # ---------------- DIAGONAL ABAJO-IZQUIERDA ----------------
                # Bajamos fila (i+1) y retrocedemos columna (j-1),
                # comprobando que no estemos en el borde inferior ni izquierdo
                if i < total_filas - 1 and j > 0:
                    valor = matriz[i + 1][j - 1]
                    suma = suma + valor

                # ---------------- DIAGONAL ABAJO-DERECHA ----------------
                # Bajamos fila y avanzamos columna,
                # sin salirnos del límite máximo
                if i < total_filas - 1 and j < total_columnas - 1:
                    valor = matriz[i + 1][j + 1]
                    suma = suma + valor

                # ---------------- ARRIBA ----------------
                # Solo subimos fila comprobando que no estemos en la primera
                if i > 0:
                    valor = matriz[i - 1][j]
                    suma = suma + valor

                # ---------------- ABAJO ----------------
                # Solo bajamos fila comprobando que no estemos en la última
                if i < total_filas - 1:
                    valor = matriz[i + 1][j]
                    suma = suma + valor

                # ---------------- IZQUIERDA ----------------
                # Retrocedemos columna si no estamos en la primera
                if j > 0:
                    valor = matriz[i][j - 1]
                    suma = suma + valor

                # ---------------- DERECHA ----------------
                # Avanzamos columna si no estamos en la última
                if j < total_columnas - 1:
                    valor = matriz[i][j + 1]
                    suma = suma + valor

    # Devolvemos la suma total calculada
    return suma


print("0.- Salir")
print("1.- Generar matriz")
print("2.- Mostrar matriz")
print("3.- Pedir coordenada y sumar vecinos")

opcion = int(input("Teclee opción: "))

while opcion != 0:

    if opcion == 1:
        numero_filas = int(input("Filas: "))
        numero_columnas = int(input("Columnas: "))

        # Generamos la matriz usando la función anterior
        matriz = generar_matriz(numero_filas, numero_columnas)

    elif opcion == 2:
        # Llamamos a la función que imprime la matriz
        mostrar_matriz(matriz)

    elif opcion == 3:
        # Inicializamos fila y columna fuera de rango para entrar en el bucle
        fila = -1
        columna = -1

        # Repetimos mientras los valores no estén dentro de los límites válidos
        while fila < 0 or fila >= len(matriz) or columna < 0 or columna >= len(matriz[0]):
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))

        # Guardamos las coordenadas en un diccionario con dos claves
        coordenada = {"fila": fila, "columna": columna}

        # Llamamos a la función que calcula la suma
        resultado = sumar_vecinos(matriz, coordenada)

        # Mostramos la suma final
        print(resultado)

    opcion = int(input("Teclee opción: "))

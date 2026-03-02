#IMPORTANTE: Gran parte del ejercicio está realizado en clase.

"""
Ejercicio clase Funciones - Listas - Diccionarios - Tuplas
- Función Se piden los nombres de personas hasta pulsar enter y devuelve lista
- Función que genera una matriz cuadrada según el número de personas y coloca aleatoriamente los nombres de las personas y la devuelve la matriz
- Función mostrar matriz
- Función que se le manda la matriz y la lista y te devuelve un diccionario con clave el nombre de las personas y contenido una lista de tuplas de posiciones de las personas.
- Función mostrar diccionario
- Función a partir del diccionario determinar si hay alguna persona que no está
- Función que se le pasa el diccionario y el tamaño de la lista de personas. A partir de esta información muestra los nombres de las personas en un menú numerado y pide el número (comprueba si es correcto) y finalmente a partir del diccionario pasado muestre en forma de matriz las posiciones en las que está la persona seleccionada, siendo el resto de posiciones "------"
- Función comer a partir de la matriz pasado como parámetro, si un jugador está entre dos iguales (arriba - abajo - derecha - izquierda) es comido por este. Irá en orden. Acaba cuando nadie es comido.
"""

import random

def pedir_nombres():
    lista_nombres = []
    nombre = input("Introduce un nombre: ")
    while nombre != "":
        lista_nombres.append(nombre)
        nombre = input("Introduce un nombre: ")
    return lista_nombres

def generar_matriz_cuadrada(lista_nombres):
    dimension = len(lista_nombres)
    matriz = []
    for i in range(dimension):
        matriz.append([])
        for j in range(dimension):
            matriz[i].append(random.choice(lista_nombres))
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\t")
        print()



def generar_diccionario_posiciones(matriz, lista_nombres):
    diccionario_posiciones = {}

    for nombre in lista_nombres:
        diccionario_posiciones[nombre] = []

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            nombre_actual = matriz[i][j]
            diccionario_posiciones[nombre_actual].append((i, j))

    return diccionario_posiciones


def mostrar_diccionario(diccionario):

    for nombre, posiciones in diccionario.items():
        print(f"{nombre}: {posiciones}")

    print()


def mostrar_ausentes(diccionario):

    for nombre in diccionario:
        posiciones = diccionario[nombre]
        print(f"{nombre}: {posiciones}")

    print()


def mostrar_posiciones_persona(diccionario, tam_lista):
    lista_personas = list(diccionario.keys())

    for i in range(len(lista_personas)):
        print(f"{i + 1}. {lista_personas[i]}")

    opcion = int(input("Elige número: "))
    while opcion < 1 or opcion > len(lista_personas):
        opcion = int(input("Elige número: "))

    nombre_elegido = lista_personas[opcion - 1]

    for i in range(tam_lista):
        for j in range(tam_lista):
            if (i, j) in diccionario[nombre_elegido]:
                print(nombre_elegido, end="\t")
            else:
                print("------", end="\t")
        print()


def comer(matriz):
    dimension = len(matriz)
    alguien_comido = True

    while alguien_comido:
        alguien_comido = False

        for i in range(dimension):
            for j in range(dimension):
                actual = matriz[i][j]

                if 0 < j < dimension - 1:
                    if matriz[i][j - 1] == matriz[i][j + 1] and actual != matriz[i][j - 1]:
                        matriz[i][j] = matriz[i][j - 1]
                        alguien_comido = True

                if 0 < i < dimension - 1:
                    if matriz[i - 1][j] == matriz[i + 1][j] and actual != matriz[i - 1][j]:
                        matriz[i][j] = matriz[i - 1][j]
                        alguien_comido = True


lista_nombres = []
matriz = []
diccionario = {}

print("0.- Salir")
print("1.- Pedir nombres")
print("2.- Generar matriz")
print("3.- Mostrar matriz")
print("4.- Generar diccionario posiciones")
print("5.- Mostrar diccionario")
print("6.- Mostrar ausentes")
print("7.- Mostrar posiciones  persona")
print("8.- Comer")

opcion = int(input("Teclee opción: "))

while opcion != 0:
    if opcion == 1:
        lista_nombres = pedir_nombres()

    elif opcion == 2:
        matriz = generar_matriz_cuadrada(lista_nombres)

    elif opcion == 3:
        mostrar_matriz(matriz)

    elif opcion == 4:
        diccionario = generar_diccionario_posiciones(matriz, lista_nombres)

    elif opcion == 5:
        mostrar_diccionario(diccionario)

    elif opcion == 6:
        mostrar_ausentes(diccionario)

    elif opcion == 7:
        mostrar_posiciones_persona(diccionario, len(lista_nombres))

    elif opcion == 8:
        comer(matriz)

    opcion = int(input("Teclee opción: "))

"""
CRITERIOS DE EVALUACIÓN

(0,75 Parte 1) Inicialmente se pedirá al usuario dos números que serán el número de filas y de columnas
de una matriz (Se supone que los números introducidos son correctos).

Una vez pedidos se llamará a la función GenerarMatriz.

Función GenerarMatriz. Esta función recibirá como parámetros el número de filas y columnas que
previamente se le han pedido al usuario:
- Generar una matriz (lista de listas) de las dimensión indicada por los parámetros. Como contenido
  estará formada por números comprendidos entre 0 y el número de casillas de la matriz, que se obtiene
  de multiplicar filas*columnas. Estos números se obtienen aleatoriamente.
- Los números no se pueden repetir en la matriz, excepto el 0.
- Devolver la matriz generada.

(0,75 Parte 2) Finalmente, se le estará pidiendo al usuario coordenadas de la matriz (Fila y columna)
hasta que la coordenada introducida no sea válida (los valores introducidos estén fuera del rango de la
matriz, Ejemplo: números negativos o mayores que las filas o las columnas…).
Una vez que la coordenada es correcta, es decir, está dentro del rango de la matriz, se guardará en un
diccionario llamado coordenada con dos claves: fila y columna, y se llamará a la función SumarVecinos.

Función SumarVecinos. Esta función recibirá como parámetros la matriz y el diccionario:
- Calculará la suma de la casilla que coincide con el punto y de todas las casillas que la rodean. En total
  son 9 casillas como máximo las que hay que sumar, teniendo en cuenta que puede ser que el punto esté
  en un borde.
"""

import random


# Se define la función GenerarMatriz que recibe filas y columnas
def GenerarMatriz(filas, columnas):

    # Se crea una lista vacía para construir la matriz
    # Se usa lista de listas porque así se representan matrices en Python
    matriz = []

    # Se calcula el valor máximo permitido dentro de la matriz
    # filas * columnas da el número total de casillas
    maximo = filas * columnas

    # Se crea una lista de números posibles desde 1 hasta maximo
    # El 0 no se mete aquí porque ese sí se puede repetir
    numeros = list(range(1, maximo + 1))

    # Se recorre fila a fila para rellenar la matriz
    for i in range(filas):

        # Se añade una fila vacía
        matriz.append([])

        # Se recorren las columnas de esa fila
        for j in range(columnas):

            # Se decide aleatoriamente si se coloca un 0 o un número no repetido
            # random.choice elige un elemento al azar de una lista
            poner_cero = random.choice([True, False])

            if poner_cero:

                # Si se decide poner 0, se añade directamente
                matriz[i].append(0)

            else:

                # Si no se pone 0, se saca un número de la lista de disponibles
                # random.randrange elige una posición válida dentro de la lista
                indice = random.randrange(len(numeros))

                valor = numeros[indice]

                # Se elimina ese número para que no vuelva a salir
                numeros.pop(indice)

                # Se añade a la matriz
                matriz[i].append(valor)

    # Se devuelve la matriz completa
    return matriz


# Se define la función SumarVecinos que recibe la matriz y el diccionario coordenada
def SumarVecinos(matriz, coordenada):

    # Se extraen la fila y la columna del diccionario usando sus claves
    fila = coordenada["fila"]
    columna = coordenada["columna"]

    # Se crea una variable acumuladora para la suma
    suma = 0

    # Se recorren las filas vecinas: fila-1, fila y fila+1
    # range(fila-1, fila+2) genera esos tres valores posibles
    for i in range(fila - 1, fila + 2):

        # Se comprueba que la fila está dentro de la matriz
        # Esto evita acceder a posiciones fuera del rango
        if i >= 0 and i < len(matriz):

            # Se recorren las columnas vecinas: columna-1, columna y columna+1
            for j in range(columna - 1, columna + 2):

                # Se comprueba que la columna está dentro del rango de la fila
                if j >= 0 and j < len(matriz[0]):

                    # Se suma el valor de esa casilla
                    suma = suma + matriz[i][j]

    # Se devuelve la suma final
    return suma


# Se pide al usuario el número de filas
filas = int(input("Filas: "))

# Se pide al usuario el número de columnas
columnas = int(input("Columnas: "))

# Se genera la matriz llamando a la función GenerarMatriz
matriz = GenerarMatriz(filas, columnas)

# Se muestra la matriz generada
print(matriz)


# Se inicializan fila y columna con valores inválidos para entrar en el bucle
fila = -1
columna = -1

# Se repite mientras las coordenadas estén fuera del rango de la matriz
# Se usa while con condición lógica, no while True
while fila < 0 or fila >= filas or columna < 0 or columna >= columnas:

    fila = int(input("Fila: "))
    columna = int(input("Columna: "))


# Se crea el diccionario coordenada con las dos claves exigidas
coordenada = {"fila": fila, "columna": columna}

# Se llama a la función SumarVecinos con la matriz y el diccionario
resultado = SumarVecinos(matriz, coordenada)

# Se muestra la suma obtenida
print(resultado)

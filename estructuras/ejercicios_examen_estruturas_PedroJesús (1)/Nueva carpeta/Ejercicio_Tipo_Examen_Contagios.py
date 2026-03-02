import random


def generar_ciudad(numero_filas, numero_columnas):
    # Creamos la matriz completa de la ciudad empezando vacía
    # La construimos añadiendo filas (listas) dentro de una lista principal
    ciudad = []

    # Recorremos las filas que tendrá la ciudad
    # range(numero_filas) crea índices 0..numero_filas-1 para construir fila a fila
    for i in range(numero_filas):

        # Creamos una fila nueva
        # Es una lista vacía que iremos llenando con las columnas
        fila = []

        # Recorremos las columnas de esa fila
        # range(numero_columnas) crea índices 0..numero_columnas-1 para añadir "SANO" en orden
        for j in range(numero_columnas):

            # Metemos una persona sana en cada casilla
            # append añade al final de la lista fila, así se respeta el orden de columnas
            fila.append("SANO")

        # Añadimos la fila completa a la ciudad
        # append mete la lista 'fila' como un elemento dentro de la lista 'ciudad'
        ciudad.append(fila)

    # Elegimos una fila al azar dentro del rango válido
    # randint incluye extremos, por eso usamos numero_filas - 1 como límite superior
    fila_aleatoria = random.randint(0, numero_filas - 1)

    # Elegimos una columna al azar dentro del rango válido
    # se aplica el mismo patrón que con las filas
    columna_aleatoria = random.randint(0, numero_columnas - 1)

    # Colocamos el primer contagiado inicial
    # accedemos con dos índices ciudad[fila][columna] y sustituimos el "SANO" por "CONT"
    ciudad[fila_aleatoria][columna_aleatoria] = "CONT"

    # Devolvemos la matriz construida para usarla en el menú
    # return entrega la referencia de la lista de listas
    return ciudad


def mostrar_ciudad(ciudad, dia_actual):
    # Mostramos el día actual antes de imprimir la matriz
    # f-string inserta el valor de dia_actual dentro del texto
    print(f"\nDia: {dia_actual}\n")

    # Recorremos cada fila por índice
    # len(ciudad) da cuántas filas hay en la matriz
    for i in range(len(ciudad)):

        # Construimos una línea completa de texto para esa fila
        # concatenamos para imprimir una sola vez al final de la fila
        linea = ""

        # Recorremos las columnas de la fila i
        # len(ciudad[i]) da cuántas columnas tiene esa fila
        for j in range(len(ciudad[i])):

            # Añadimos el contenido de la celda y un tabulador para separar columnas
            # como "SANO" y "CONT" miden 4 caracteres, el tabulador mantiene la alineación
            linea = linea + ciudad[i][j] + "\t"

        # Imprimimos la fila completa
        # print añade salto de línea automáticamente tras imprimir 'linea'
        print(linea)


def contagiar_un_dia(ciudad, dia_actual):
    # Guardamos el tamaño de la matriz para usarlo en condiciones de borde
    # len(ciudad) es el número de filas y len(ciudad[0]) el de columnas en una matriz regular
    total_filas = len(ciudad)
    total_columnas = len(ciudad[0])

    # Creamos una nueva matriz para el resultado del día siguiente
    # esto evita que un contagio nuevo de este día contagie a otros en el mismo recorrido
    nueva_ciudad = []

    # Recorremos todas las filas con i
    # i va de 0 a total_filas-1
    for i in range(total_filas):

        # Creamos la nueva fila i
        # iremos añadiendo cada casilla ya calculada con append
        nueva_fila = []

        # Recorremos todas las columnas con j
        # j va de 0 a total_columnas-1
        for j in range(total_columnas):

            # Si la casilla está sana, decidimos si se contagia mirando vecinos
            # si no está sana, se conserva el estado tal cual
            if ciudad[i][j] == "SANO":

                # Variable para marcar si algún vecino contagia
                # empezamos en False y cambiamos a True si se cumple alguna condición
                se_contagia = False

                # Miramos ARRIBA (i-1, j) solo si i > 0 para no salirnos por arriba
                # accedemos a ciudad[i-1][j] y comprobamos si es "CONT"
                if i > 0 and ciudad[i - 1][j] == "CONT":
                    se_contagia = True

                # Miramos ABAJO (i+1, j) solo si i < total_filas-1 para no salirnos por abajo
                if i < total_filas - 1 and ciudad[i + 1][j] == "CONT":
                    se_contagia = True

                # Miramos IZQUIERDA (i, j-1) solo si j > 0 para no salirnos por la izquierda
                if j > 0 and ciudad[i][j - 1] == "CONT":
                    se_contagia = True

                # Miramos DERECHA (i, j+1) solo si j < total_columnas-1 para no salirnos por la derecha
                if j < total_columnas - 1 and ciudad[i][j + 1] == "CONT":
                    se_contagia = True

                # Si algún vecino era "CONT", esta persona pasa a contagiada en el día siguiente
                # añadimos "CONT" a nueva_fila para construir la nueva matriz sin tocar la original
                if se_contagia:
                    nueva_fila.append("CONT")
                else:
                    nueva_fila.append("SANO")

            else:
                # Si ya estaba contagiado, lo copiamos tal cual al día siguiente
                # añadimos el mismo texto que había en ciudad[i][j]
                nueva_fila.append(ciudad[i][j])

        # Añadimos la fila ya calculada a la nueva ciudad
        # append mete la lista nueva_fila dentro de nueva_ciudad
        nueva_ciudad.append(nueva_fila)

    # Devolvemos la ciudad actualizada de un día a otro
    # el menú guardará este return en la variable ciudad
    return nueva_ciudad


print("0.- Salir")
print("1.- Generar ciudad")
print("2.- Mostrar ciudad")
print("3.- Avanzar un dia")

opcion = int(input("Teclee opción: "))

ciudad = []
dia_actual = 0

while opcion != 0:

    if opcion == 1:
        numero_filas = int(input("Filas: "))
        numero_columnas = int(input("Columnas: "))

        ciudad = generar_ciudad(numero_filas, numero_columnas)
        dia_actual = 0

    elif opcion == 2:
        mostrar_ciudad(ciudad, dia_actual)

    elif opcion == 3:
        queda_alguno_sano = False

        for i in range(len(ciudad)):
            for j in range(len(ciudad[0])):
                if ciudad[i][j] == "SANO":
                    queda_alguno_sano = True

        if queda_alguno_sano:
            dia_actual = dia_actual + 1
            ciudad = contagiar_un_dia(ciudad, dia_actual)
            mostrar_ciudad(ciudad, dia_actual)
        else:
            print("\nDesde el dia", dia_actual, "ya no quedan sanos\n")

    opcion = int(input("Teclee opción: "))

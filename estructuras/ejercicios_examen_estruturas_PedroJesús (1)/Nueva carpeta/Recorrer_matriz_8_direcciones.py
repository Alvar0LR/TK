def recorrer_matriz_8_direcciones(matriz):
    # Número total de filas
    total_filas = len(matriz)

    # Número total de columnas (se asume matriz rectangular)
    total_columnas = len(matriz[0])

    # Recorremos filas con i
    for i in range(total_filas):

        # Recorremos columnas con j
        for j in range(total_columnas):

            # Valor de la posición central (i, j)
            valor_central = matriz[i][j]

            # Aquí se hace lo que pida el ejercicio con la posición (i, j)

            # Diagonal arriba-izquierda
            if i > 0 and j > 0:
                valor = matriz[i - 1][j - 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Diagonal arriba-derecha
            if i > 0 and j < total_columnas - 1:
                valor = matriz[i - 1][j + 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Diagonal abajo-izquierda
            if i < total_filas - 1 and j > 0:
                valor = matriz[i + 1][j - 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Diagonal abajo-derecha
            if i < total_filas - 1 and j < total_columnas - 1:
                valor = matriz[i + 1][j + 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Arriba
            if i > 0:
                valor = matriz[i - 1][j]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Abajo
            if i < total_filas - 1:
                valor = matriz[i + 1][j]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Izquierda
            if j > 0:
                valor = matriz[i][j - 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Derecha
            if j < total_columnas - 1:
                valor = matriz[i][j + 1]
                # Aquí se hace lo que pida el ejercicio con este valor

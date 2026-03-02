def recorrer_matriz_irregular_8_direcciones(matriz):
    # Número total de filas de la matriz
    total_filas = len(matriz)

    # Recorremos cada fila usando i
    for i in range(total_filas):

        # Número de columnas de ESTA fila concreta
        total_columnas_fila = len(matriz[i])

        # Recorremos cada columna usando j
        for j in range(total_columnas_fila):

            # Valor almacenado en la posición central (i, j)
            valor_central = matriz[i][j]

            # Aquí se hace lo que pida el ejercicio con la posición (i, j)

            # Diagonal arriba-izquierda
            if i > 0 and j > 0 and j - 1 < len(matriz[i - 1]):
                valor = matriz[i - 1][j - 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Diagonal arriba-derecha
            if i > 0 and j + 1 < len(matriz[i - 1]):
                valor = matriz[i - 1][j + 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Diagonal abajo-izquierda
            if i + 1 < total_filas and j > 0 and j - 1 < len(matriz[i + 1]):
                valor = matriz[i + 1][j - 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Diagonal abajo-derecha
            if i + 1 < total_filas and j + 1 < len(matriz[i + 1]):
                valor = matriz[i + 1][j + 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Arriba
            if i > 0 and j < len(matriz[i - 1]):
                valor = matriz[i - 1][j]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Abajo
            if i + 1 < total_filas and j < len(matriz[i + 1]):
                valor = matriz[i + 1][j]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Izquierda
            if j > 0:
                valor = matriz[i][j - 1]
                # Aquí se hace lo que pida el ejercicio con este valor

            # Derecha
            if j + 1 < len(matriz[i]):
                valor = matriz[i][j + 1]
                # Aquí se hace lo que pida el ejercicio con este valor


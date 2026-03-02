import random
def generar_matriz_letras(lista_letras,n):
    M = []
    for i in range(n):
        M.append([])
        for j in range(n):
            letra_aleatoria = random.choice(lista_letras)
            M[i].append(letra_aleatoria)
    return M

def mostrar_matriz(M):
    for i in M:
        for j in i:
            print(j, end="\t")
        print()

def generar_mapa_calor(M):
    n = len(M)
    M_numeros = []
    for i in range(n):
        fila_numeros = []
        for j in range(n):
            contador = 0
            nombre_actual = M[i][j]

            if i > 0 and M[i-1][j] == nombre_actual:
                contador += 1 #mirar arriba
            if i < n - 1 and M[i+1][j] == nombre_actual:
                contador += 1 #mirar abajo
            if j > 0 and M[i][j-1] == nombre_actual:
                contador += 1 #mirar izquierda
            if j < n - 1 and M[i][j+1] == nombre_actual:
                contador += 1


            fila_numeros.append(contador)
        M_numeros.append(fila_numeros)
    return M_numeros




if __name__ == '__main__':

    print("0.- Salir")
    print("1.- Generar y mostrar Matriz letras")
    print("2.- Generar mapa calor")

    opcion = int(input("Teclee opción: "))
    while opcion != 0:
        if opcion == 1:
            numero = int(input("Numero de filas y columnas:"))
            lista_letras = ["A", "B", "C", "D"]
            matriz_letras = generar_matriz_letras(lista_letras, numero)
            mostrar_matriz(matriz_letras)
        elif opcion == 2:
            mapa = generar_mapa_calor(matriz_letras)
            mostrar_matriz(mapa)

        opcion = int(input("Teclee opción: "))

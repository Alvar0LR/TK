import random


def configurar_radar():
    tupla = ("Basico", "Avanzado")
    D = {}

    #campo 1
    nombre = input("Nombre: ")
    D['nombre'] = nombre

    #campo 2 y 3
    filas = int(input("filas: "))
    while filas < 4 or filas > 8:
        filas = int(input("filas: "))
    D['filas'] = filas

    columnas = int(input("columnas: "))
    while columnas < 4 or columnas > 8:
        columnas = int(input("columnas: "))
    D['columnas'] = columnas

    #campo 4
    dificultad = input("Dificultad: ")
    while dificultad not in tupla:
        dificultad = input("Dificultad: ")
    D['dificultad'] = dificultad

    return D


def generar_dic(D):
    M = []
    filas = D['filas']
    columnas = D['columnas']
    for i in range(filas):
        M.append([])
        for j in range(columnas):
            M[i].append(0)

    bancos_peces = max(filas, columnas)
    while bancos_peces > 0:
        fila_a = random.randint(0, filas - 1)
        columna_a = random.randint(0, columnas - 1)

        if M[fila_a][columna_a] == 0:
            M[fila_a][columna_a] = "P"
            bancos_peces -= 1

    return M


def visualizar_tabla(M):
    for i in M:
        print("\t", end="")
        for j in i:
            if j == 0 or j == "P":
                C = "~"
            elif j == "E":
                C = "><>"
            else:
                C = "X"
            print(C, end="\t")
        print()


def jugar(M, combustible):
    banco_peces = max(len(M)-1, len(M[0])-1)
    peces = banco_peces + 1
    while combustible > 0 and peces > 0:
        filas = int(input("filas: "))
        columnas = int(input("columnas: "))
        while filas < 0 or filas > (len(M) - 1) or columnas < 0 or columnas > (len(M[0])-1):
            print("te has pasado")
            filas = int(input("filas: "))
            columnas = int(input("columnas: "))

        if M[filas][columnas] == 0:
            combustible -= 1
        if M[filas][columnas] == "P":
            M[filas][columnas] = "E"
            peces -= 1
        if peces == 0 or combustible == 0:
            print("Game Over")
        visualizar_tabla(M)




if __name__ == '__main__':

    print("0.- Salir")
    print("1.- Configuracion de juego")
    print("2.- Generar isla de tesoros")
    print("3.- Mostrar isla de tesoros")
    print("4.- Calcular intentos")
    print("5.- Jugar")

    opcion = int(input("Teclee opción: "))
    while opcion != 0:
        if opcion == 1:
            #dic = configurar_radar()
            #print(dic)
            dic = {'nombre': 'alvaro', 'filas': 4, 'columnas': 4, 'dificultad': 'Avanzado'}
        elif opcion == 2:
            #matriz = generar_dic(dic)
            #print(matriz)
            matriz = [[0, 'P', 0, 0], [0, 0, 'P', 0], ['P', 'P', 0, 0], [0, 0, 0, 0]]
        elif opcion == 3:
            fl=lambda x: x['filas'] * x['columnas'] if x['dificultad'] == "Basico"  else  (x['filas'] * x['columnas']) // 2
            combustible = fl(dic)
        elif opcion == 4:
            jugar(matriz, combustible)
        opcion = int(input("Teclee opción: "))

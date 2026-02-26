import random


def configurar_juego():
    nivel = ("Facil", "Dificil")

    filas = int(input("Filas"))
    while filas < 3 or filas > 10:
        filas = int(input("Filas"))

    Columnas = int(input("Columnas"))
    while Columnas < 3 or Columnas > 10:
        Columnas = int(input("Columnas"))

    D = {"Filas": filas, "Columnas": Columnas}
    return D


def mostrar_dic(D):
    for i , j in D.items():
        print(i,j)

def isla_tesoro(D):
    M = []
    numero_filas = int(D['Filas'])
    numero_columnas = int(D['Columnas'])

    for i in range(numero_filas):
        M.append([])
        for j in range(numero_columnas):
            numero_selecionado = 0
            M[i].append(numero_selecionado)

    numero_tesoros = max(numero_filas, numero_columnas)
    while numero_tesoros > 0 :
        filas_a = random.randint(0, numero_filas -1)
        columnas_a = random.randint(0, numero_columnas - 1)

        if M[filas_a][columnas_a] == 0:
            M[filas_a][columnas_a] = "X"
            numero_tesoros -= 1

    return M

def visualizar_tabla(D, M, I="TODOS"):
    nombre_jugador = "Alvaro" # Aqui se deberia usar el diccionario para mostrar el nombre aun que esta a modo de ejmplo para ir mas rapido
    x = f"Jugador: {nombre_jugador} - Intentos Restantes: {I}"
    print(x)
    print("="*len(x))
    for i in M:
        print("\t", end="")
        for j in i:
            if j == 0 or j == "X":
                C = "-"
            elif j == "E":
                C = "X"
            else:
                C = 0
            print(C, end="\t")
        print()

def lambd(D):
    nivel = D['Nivel']
    numero_filas = int(D['Filas'])
    numero_columnas = int(D['Columnas'])
    if nivel == "facil":
        x1=lambda x: numero_filas * numero_columnas
        print(x1)

def jugar(M, Nombre, Intentos):
    Tesoros = 0
    while Intentos > 0 and Tesoros > 0:
        F = int(input("Filas: "))
        C = int(input("Columna: "))
        while F < 0 or F > (len(M)-1) or C < 0 or C > (len(M[0])-1):
            print("Fuera de rango")
            F = int(input("Fila: "))
            C = int(input("Columna: "))

        if M[F][C] == 0:
            M[F][C] = "V"
        if M[F][C] == "X":
            M[F][C] = "E"
            Tesoros -= 1
        Intentos -= 1
        visualizar_tabla(M, Nombre, Intentos)

def funcionL(D):
    if D['Dificultad'] == "Facil":
        V = D['Filas'] * D["Columnas"]
    else:
        V = D['Filas'] * D["Columnas"] // 2

    fl = lambda X: (X['Filas'] * X['Columna']) if X['Dificultad'] == "Facil" else (X['Filas'] * X['Columna']) // 2
    

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
            #dic = configurar_juego()
            #print(dic)
            dic= {'Filas': 3, 'Columnas': 3}
            #mostrar_dic(dic)
        elif opcion == 2:
            #matriz = isla_tesoro(dic)
            #print(matriz)
            matriz=[['X', 0, 0], ['X', 0, 'X'], [0, 0, 0]]
        elif opcion == 3:
            visualizar_tabla(dic, matriz, I="TODOS")
        elif opcion == 4:
            print()
        opcion = int(input("Teclee opción: "))

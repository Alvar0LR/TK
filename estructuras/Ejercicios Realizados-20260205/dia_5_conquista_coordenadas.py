import random

def generar_lista_jugadores():
    Lnombres = []
    nombre = input("Nombre: ")
    while nombre != "":
        Lnombres.append(nombre)
        nombre = input("Nombre: ")
    return Lnombres

def generar_matriz_territorio(L):
    M = []
    n = len(L)
    for i in range(n):
      M.append([])
      for j in range(n):
          nombre_aleatorio = random.choice(L)
          M[i].append(nombre_aleatorio)
    return M

def mostrar_matriz(M):
    for i in M:
        for j in i:
            print(j, end="\t")
        print()

def generar_diccionario_posiciones(M):
    D = {}
    n = len(M)
    for i in range(n):
        for j in range(n):
            actual = M[i][j]

            if actual not in D:
                D[actual] = []
            D[actual].append((i,j))

    return D

def mostrar_dic(D):
    for i , j in D.items():
        print(i,j)

def verificar_jugadores_ausentes(D,L):
    for i in L:
        if i not in D:
            print(f"El jugador {i} no aparece en la lista")

def menu_posiciones_individuales(M,L):
    for i, nombre in enumerate(L):
        print(f"[{i}]- {nombre}")
    numero = input("Elija un numero: ")

    if numero.isdigit():
        n = int(numero)
        if 0 <= n < len(L):
            nombre_buscado = L[n]
            print(f"Visualizando posiciones de: {nombre_buscado}")

            print("El nombre que se ha seleccionado es: ", nombre_buscado)
            for x in M:
                for y in x:
                    if y.lower() == nombre_buscado.lower():
                        print(y, end="\t")
                    else:
                        print("*", end="\t")
                print()
        else:
            print("Numero fuera de rango")
    else:
        print("El numero elegido no esta")


def aplicar_conquista(M):
    n = len(M)
    hubo_cambios = True

    while hubo_cambios:
        hubo_cambios = False

        for i in range(n):
            for j in range(n):
                actual = M[i][j]

                if 0 < j < n - 1:
                    izq = M[i][j - 1]
                    der = M[i][j + 1]

                    if izq == der and izq != actual:
                        M[i][j] = izq
                        hubo_cambios = True

                if 0 < i < n - 1:
                    arriba = M[i - 1][j]
                    abajo = M[i + 1][j]

                    if arriba == abajo and arriba != actual:
                        M[i][j] = arriba
                        hubo_cambios = True

    return M

def rellenar_diagonal_derecha(M):
    n = len(M)
    for i in range(n):
        # Fila i, Columna (Tamaño - 1 - i)
        # Posiciones (si n=4): (0,3), (1,2), (2,1), (3,0)
        M[i][n - 1 - i] = 1
    return M

print("0.- Salir")
print("1.- Generar Lista Jugadores")
print("2.- Generar Matriz territorio")
print("3.- Mostrar matriz")
print("4.- Mostrar matriz 2")
print("5.- Generar Diccionaro personas - posición")

opcion = int(input("Teclee opción: "))
while opcion != 0:
    if opcion == 1:
        jugadores = generar_lista_jugadores()
    elif opcion == 2:
       matriz = generar_matriz_territorio(jugadores)
       mostrar_matriz(matriz)
    elif opcion == 3:
       dic = generar_diccionario_posiciones(matriz)
    elif opcion == 4:
        mostrar_dic(dic)
        verificar_jugadores_ausentes(dic,jugadores)
    elif opcion == 5:
        menu_posiciones_individuales(matriz, jugadores)
        matriz2 = aplicar_conquista(matriz)
        mostrar_matriz(matriz2)
    elif opcion == 6:
        m = rellenar_diagonal_derecha(matriz)
        mostrar_matriz(m)
    opcion = int(input("Teclee opción: "))
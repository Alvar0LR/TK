import random


def pedir_nombres():
    N = []
    nombre = input("Introduce un nombre: ")
    while nombre != "":
        N.append(nombre)
        nombre = input("Introduce un nombre: ")
    return N


def generar_matriz(lista_nombres):
    long = len(lista_nombres)
    matriz = []
    for x in range(long):
        fila = []
        for y in range(long):
            nombre_azar = random.choice(lista_nombres)
            fila.append(nombre_azar)
        matriz.append(fila)

    return matriz


def diccionario_posiciones(matriz, lista_nombres: list):
    Dic = {}
    for nombre in lista_nombres:
        Dic[nombre] = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            nombre_actual = matriz[i][j]
            Dic[nombre_actual].append((i, j))
    return Dic


def comprobar_asuentes(diccionario):
    for i, j in diccionario.items():
        if not j:
            print(f"la lista esta vacia, para la persona {i}")


def mostrar_posciones_personas(matriz, nombre_elegido):
    print("El nombre que se ha seleccionado es: ", nombre_elegido)
    for i in matriz:
        for j in i:
            if j.lower() == nombre_elegido.lower():
                print(j, end="\t")
            else:
                print("---", end="\t")
        print()


def mostrar_matriz(titulo, matriz):
    print(f"---{titulo}---")
    for i in matriz:
        for j in i:
            print(j, end="\t")
        print()


def mostrar_diccionario_matriz(diccionario):
    for i, j in diccionario.items():
        print(f"Persona: {i}, Posiciones: {j}")
    print()


def menu_y_visualizacion(matriz, lista_nombres):
    print("\n--- menu  ---")
    for i, nombre in enumerate(lista_nombres):
        print(f"{i + 1}. {nombre}")

    opcion = int(input("Elige el numero de la persona para ver sus posiciones: "))

    if 1 <= opcion <= len(lista_nombres):
        nombre_elegido = lista_nombres[opcion - 1]
        mostrar_posciones_personas(matriz, nombre_elegido)
    else:
        print("opc no válida")


def comer(matriz):
    n = len(matriz)
    while True:
        alguien_comido = False
        for i in range(n):
            for j in range(n):
                actual = matriz[i][j]
                if actual == "---":
                    continue

                if 0 < j < n - 1:
                    if matriz[i][j - 1] == matriz[i][j + 1] and matriz[i][j - 1] != "---" and actual != matriz[i][
                        j - 1]:
                        print(f"{actual} ha sido comido por {matriz[i][j - 1]}")
                        matriz[i][j] = "---"
                        alguien_comido = True
                        continue

                if 0 < i < n - 1:
                    if matriz[i - 1][j] == matriz[i + 1][j] and matriz[i - 1][j] != "---" and actual != matriz[i - 1][
                        j]:
                        print(f"{actual} ha sido comido por {matriz[i - 1][j]}")
                        matriz[i][j] = "---"
                        alguien_comido = True


        if not alguien_comido:
            break


if __name__ == '__main__':
    lista_nombre = pedir_nombres()
    if not lista_nombre:
        print("No hay nombres")
    else:
        matriz = generar_matriz(lista_nombre)

        mostrar_matriz("matriz", matriz)
        dicc = diccionario_posiciones(matriz, lista_nombre)
        mostrar_diccionario_matriz(dicc)
        comprobar_asuentes(dicc)

        menu_y_visualizacion(matriz, lista_nombre)

        print("\n--- proceso de comer ---")
        comer(matriz)
        mostrar_matriz("matriz despues de comer", matriz)
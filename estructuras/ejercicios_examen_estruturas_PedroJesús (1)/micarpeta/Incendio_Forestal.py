from datetime import datetime
import random
import time

from estructuras.examen.examen_alvaro import mostrar_dic


def generar_ciudad(filas, columnas):
    M = []
    for i in range(filas):
        M.append([])
        for j in range(columnas):
            M[i].append("A")

    numero_fuegos = max(filas, columnas)
    while numero_fuegos > 0:
        fila_a = random.randint(0, filas - 1)
        columna_a = random.randint(0, columnas - 1)

        if M[fila_a][columna_a] == "A":
            M[fila_a][columna_a] = "F"
            numero_fuegos -= 1

    return M


def MostrarBosque(matriz):
    tiempo = datetime.now()
    for i in matriz:
        for j in i:
            print(j, end="\t" )
        print()
    time.sleep(0.5)
    fin = datetime.now()
    tiempo_f = fin - tiempo
    print(f"\n[+] tiempo: {tiempo_f}")


def SimularIncendio(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    arboles_sanos = 0
    dia = 0
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == "A":
                arboles_sanos += 1

    while arboles_sanos > 0:
        dia += 1
        matriz2 = []
        for i in range(filas):
            nueva_fila = []
            for j in range(columnas):
                if matriz[i][j] == "A":
                    # Verificar si algún vecino está infectado
                    contagiado = False
                    # Arriba
                    if i > 0 and matriz[i - 1][j] == "F":
                        contagiado = True
                    # Abajo
                    if i < filas - 1 and matriz[i + 1][j] == "F":
                        contagiado = True
                    # Izquierda
                    if j > 0 and matriz[i][j - 1] == "F":
                        contagiado = True
                    # Derecha
                    if j < columnas - 1 and matriz[i][j + 1] == "F":
                        contagiado = True

                    if contagiado:
                        nueva_fila.append("F")
                    else:
                        nueva_fila.append("A")
                elif matriz[i][j] == "F":
                    nueva_fila.append("C")
                else:
                    nueva_fila.append(matriz[i][j])
            matriz2.append(nueva_fila)

        matriz = matriz2


        arboles_sanos = 0
        for fila in matriz:
            for celda in fila:
                if celda == "F": contagiado = True
                if celda == "A": arboles_sanos += 1

        MostrarBosque(matriz)
        print(f"Día {dia} - Árboles sanos restantes: {arboles_sanos}")

        if not contagiado:
            print("--- El incendio se ha extinguido ---")

    return dia






matriz = generar_ciudad(4, 4)
MostrarBosque(matriz)
SimularIncendio(matriz)



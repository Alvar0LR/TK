"""
Este ejercicio se ha iniciado en clase el día 17/12 y su realización es muy aconsejable.
El enunciado es el siguiente:

Ejercicio

- Función Se piden los nombres de personas hasta pulsar enter y devuelve lista
- Función que genera una matriz cuadrada según el número de personas y coloca aleatoriamente los nombres de las personas y la devuelve la matriz
- Función mostrar matriz
- Función que se le manda la matriz y la lista y te devuelve un diccionario con clave el nombre de las personas y contenido una lista de tuplas de posiciones de las personas.
- Función mostrar diccionario
- Función a partir del diccionario determinar si hay alguna persona que no está
- Función que se le pasa el diccionario y el tamaño de la lista de personas. A partir de esta información muestra los nombres de las personas en un menú numerado y pide el número (comprueba si es correcto) y finalmente a partir del diccionario pasado muestre en forma de matriz las posiciones en las que está la persona seleccionada, siendo el resto de posiciones "------"
- Función comer a partir de la matriz pasado como parámetro, si un jugador está entre dos iguales (arriba - abajo - derecha - izquierda) es comido por este. Irá en orden. Acaba cuando nadie es comido.
"""
import random


# ------------------------------------------------------------
# Función: Se piden nombres hasta pulsar Enter y devuelve lista
# (Tu nombre de variable: L)
# ------------------------------------------------------------
def generar_lista():
    L = list()
    nombre = input("Ingrese nombre (Enter para terminar): ").strip()

    while nombre != "":
        L.append(nombre)
        nombre = input("Ingrese nombre (Enter para terminar): ").strip()

    return L


# -------------------------------------------------------------------
# Función: genera una matriz cuadrada según número de personas (len(L))
# y coloca aleatoriamente nombres. Devuelve matriz M
# -------------------------------------------------------------------
def Generar_Matriz_Cuadrada(L):
    M = list()

    for i in range(len(L)):
        F = ["---"] * len(L)
        M.append(F)

    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = random.choice(L)

    return M


# -------------------------
# Función: mostrar matriz M
# -------------------------
def mostrar_matriz(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end="\t")
        print()


# -------------------------------------------------------------
# Función: matriz M + lista L -> diccionario D (clave: nombre,
# valor: lista de tuplas (fila, columna) donde aparece)
# -------------------------------------------------------------
def Generar_Diccionario(M, L):
    D = {}

    for nombre in L:
        D[nombre] = []

    for i in range(len(M)):
        for j in range(len(M[i])):
            nombre_en_celda = M[i][j]
            if nombre_en_celda in D:
                D[nombre_en_celda].append((i, j))
            else:
                # Por si hubiese un nombre en M que no estuviese en L (poco probable)
                D[nombre_en_celda] = [(i, j)]

    return D


# --------------------------------
# Función: mostrar diccionario D
# --------------------------------
def mostrar_diccionario(D):
    for nombre in D:
        print(nombre, ":", D[nombre])


# ---------------------------------------------------------
# Función: a partir del diccionario determinar si hay alguien
# que no está (devuelve lista de nombres que NO aparecen)
# ---------------------------------------------------------
def personas_que_no_estan(D):
    lista_no_estan = []

    for nombre in D:
        if len(D[nombre]) == 0:
            lista_no_estan.append(nombre)

    return lista_no_estan


# -------------------------------------------------------------------------
# Función: se le pasa D y el tamaño de la lista de personas (len(L))
# - muestra nombres en menú numerado
# - pide número (comprueba correcto)
# - muestra en forma de matriz las posiciones de esa persona
#   y el resto "------"
# -------------------------------------------------------------------------
def mostrar_posiciones_persona(D, L):
    for i in range(len(L)):
        print(i + 1, "-", L[i])

    n = int(input("Teclee número: "))

    while n < 1 or n > len(L):
        n = int(input("Número incorrecto. Teclee número: "))

    nombre = L[n - 1]

    tamano = len(L)
    matriz_posiciones = []

    for i in range(tamano):
        fila = []
        for j in range(tamano):
            if (i, j) in D[nombre]:
                fila.append(nombre)
            else:
                fila.append("-----")
        matriz_posiciones.append(fila)

    mostrar_matriz(matriz_posiciones)


# -------------------------------------------------------------------------
# Función comer:
# si un jugador está entre dos iguales (arriba/abajo o izquierda/derecha)
# es "comido" por ese nombre.
# Va en orden (recorrido fila-columna).
# Acaba cuando en una pasada completa nadie es comido.
# -------------------------------------------------------------------------
def comer(M):
    hubo_cambios = True
    tamano = len(M)

    while hubo_cambios:
        hubo_cambios = False

        for i in range(tamano):
            for j in range(tamano):
                nombre_actual = M[i][j]

                # Arriba-Abajo
                if i - 1 >= 0 and i + 1 < tamano:
                    nombre_arriba = M[i - 1][j]
                    nombre_abajo = M[i + 1][j]
                    if nombre_arriba == nombre_abajo and nombre_arriba != nombre_actual:
                        M[i][j] = nombre_arriba
                        hubo_cambios = True
                        nombre_actual = M[i][j]

                # Izquierda-Derecha
                if j - 1 >= 0 and j + 1 < tamano:
                    nombre_izquierda = M[i][j - 1]
                    nombre_derecha = M[i][j + 1]
                    if nombre_izquierda == nombre_derecha and nombre_izquierda != nombre_actual:
                        M[i][j] = nombre_izquierda
                        hubo_cambios = True

    return M


# -------------------------
# PROGRAMA PRINCIPAL (tu menú)
# -------------------------
print("0. - Salir")
print("1. - Generar Lista de Nombre")
print("2. - Generar Matriz de Nombres")
print("3. - Mostrar Matriz")
print("4. - Generar Diccionario")
print("5. - Mostrar Diccionario")
print("6. - Ver personas que no están")
print("7. - Elegir persona y mostrar posiciones")
print("8. - Comer")

opcion = int(input("Teclee opción: "))

# Inicializaciones con tus nombres
L = []
M = []
D = {}

while opcion != 0:
    if opcion == 1:
        L = generar_lista()
        print(L)

    elif opcion == 2:
        M = Generar_Matriz_Cuadrada(L)
        print("Matriz generada.")

    elif opcion == 3:
        mostrar_matriz(M)

    elif opcion == 4:
        D = Generar_Diccionario(M, L)
        print("Diccionario generado.")

    elif opcion == 5:
        mostrar_diccionario(D)

    elif opcion == 6:
        lista_no_estan = personas_que_no_estan(D)
        print("No están:", lista_no_estan)

    elif opcion == 7:
        mostrar_posiciones_persona(D, L)

    elif opcion == 8:
        M = comer(M)
        print("Resultado tras comer:")
        mostrar_matriz(M)

        # Si cambia M, D ya no refleja posiciones, así que lo vaciamos
        D = {}

    opcion = int(input("Teclee opción: "))

print("Fin")


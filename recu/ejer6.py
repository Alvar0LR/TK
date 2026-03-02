import random


def validacion():
    D = {}
    nombre = input("Nombre: ")
    while not (4 <= len(nombre) <= 10):
        nombre = input("Nombre: ")
    D['Nombre'] = nombre

    return D

def diccionarios():
    puntuaciones = {"Alvaro": 50, "IA": 70}
    nombre = input("Nombre: ")
    if nombre in puntuaciones:
        puntuaciones[nombre] += 10
    else:
        puntuaciones[nombre] = 10
    print(puntuaciones)
def matrices():
    M = []
    fila = 5
    columna = 5
    numeros_aleatorios = []
    for x in range(11):
        numeros_aleatorios.append(x)
    for i in range(fila):
        M.append([])
        for j in range(columna):
            numero_seleccionado = random.choice(numeros_aleatorios)
            M[i].append(numero_seleccionado)

    for i in M:
        for j in i:
            print(j, end="\t")
        print()
    numeros_mayores = []
    for i in M:
        for j in i:
            if j > 5:
                numeros_mayores.append(j)
    print()
    print("Lista --> ", numeros_mayores)
    print("Conteo de los numeros grandes --> ", len(numeros_mayores))

def matriz2():
    M = []
    fila = 4
    columna = 4
    for i in range(fila):
        M.append([])
        for j in range(columna):
            M[i].append(0)
    for i in range(fila):
        for j in range(columna):
            if i == j:
                M[i][j] = 1
    for i in M:
        for j in i:
            print(j, end="\t")
        print()
#print(validacion())
#diccionarios()
matrices()
matriz2()
#notas = [3, 8, 5, 2, 9, 4]
#mayores_cinco = list(filter(lambda x: x >= 5, notas))
#print(mayores_cinco)
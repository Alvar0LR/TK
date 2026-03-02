import random
def validacion():
    D = {}
    filas = input("Filas: ")
    while not (filas.isdigit()) or not (4 >= int(filas) >= 0):
        filas = input("Filas: ")
    D['Filas'] = int(filas)

    columnas = input("Columnas: ")
    while not (columnas.isdigit()) or not (4 >= int(columnas) >= 0):
        columnas = input("Columnas: ")
    D['Columnas'] = int(columnas)

    return D

def diccionarios():
    puntos = {"jugador1": 100}
    numero = input("Puntos a Añadir: ")
    while not (numero.isdigit()):
        numero = input("Puntos a Añadir: ")
    puntos['jugador1'] += int(numero)

    return puntos

def matrices():
    M = []
    nfilas = 5
    ncolumnas = 5
    contador = 0
    for i in range(nfilas):
        M.append([])
        for j in range(ncolumnas):
            numero_seleccionado = 0
            M[i].append(numero_seleccionado)

    while contador < 1:
        fila_a = random.randint(0, nfilas -1)
        columna_a = random.randint(0, ncolumnas - 1)

        if M[fila_a][columna_a] == 0:
            M[fila_a][columna_a] = "X"
            contador += 1

    for i in M:
        for j in i:
            print(j, end="\t")
        print()



#print(validacion())
#print(diccionarios())
#matrices()
vidas = 5
a_triangulo = lambda v: 'Vas bien' if v >= 3 else 'Cuidado'
print(a_triangulo(vidas))
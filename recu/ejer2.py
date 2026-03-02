def validacion():
    jugador = {}

    nombre = input("Nombre: ").strip()
    while nombre == "":
        nombre = input("Nombre: ").strip()
    jugador['nombre'] = nombre

    edad = input("Edad: ")
    while not (edad.isdigit()) or not(5 <= int(edad) <= 80)  :
        edad = input("Edad: ")
    jugador['edad'] = int(edad)

    return jugador


def diccionarios(D):
    dificultad = input("Facil / Dificil: ").lower().strip()

    while not (dificultad.lower() == "Facil".lower()) and not (dificultad.lower() == "Dificil".lower()):
        dificultad = input("Facil / Dificil: ").lower().strip()

    D['Dificultad'] = dificultad

    if D['Dificultad'] == "facil" :
        D['Vidas'] = 5
    if D['Dificultad'] == "dificil":
        D['Vidas'] = 2

    return D

def matrices():
    M = []
    nfilas = 4
    ncolumnas = 4
    for i in range(nfilas):
        M.append([])
        for j in range(ncolumnas):
            numero_seleccionado = "."
            M[i].append(numero_seleccionado)

    for x in range(nfilas):
        M[0][x] = 1
        M[3][x] = 1

    for i in M:
        for j in i:
            print(j, end=" \t")
        print()


print(validacion())
#D = {}
#print(diccionarios(D))
matrices()
dic = {"intentos": 0}
nota_final = lambda i: 'sigue jugando' if i['intentos'] > 0 else 'Game Over'
print(nota_final(dic))
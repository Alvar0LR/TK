def validacion():
    D = {}
    email = input("Email: ").strip()
    while '@' not in email or email == "":
        email = input("Email: ").strip()

    D['Email'] = email

    return D


def diccionarios():
    D = {"equipo": []}
    contador = 0
    while contador < 3:
        nombre = input("Nombre: ")
        D['equipo'].append(nombre)
        contador += 1

    return D

def matrices():
    M = []
    nfilas = 5
    ncolumnas = 5
    for i in range(nfilas):
        M.append([])
        for j in range(ncolumnas):
            numero_seleccionado = 0
            M[i].append(numero_seleccionado)

    for x in range(ncolumnas):
        M[x][2] = 8
        M[1][x] = 8

    for i in M:
        for j in i:
            print(j, end=" \t")
        print()


#print(validacion())

print(diccionarios())
#matrices()
triangulo = {"base": 10, "altura": 5}
a_triangulo = lambda b: (b['base'] * b['altura']) / 2
print(a_triangulo(triangulo))
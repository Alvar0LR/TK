def agenda_contactos():
    agenda = {"amigos":[], "trabajo":[]}
    nombre = input("Nombre: ")
    while not (nombre.isalnum()):
        nombre = input("Nombre: ")

    categoria = input("Amigos / Trabajo: ").lower().strip()
    while categoria not in agenda:
        categoria = input("Amigos / Trabajo: ").lower().strip

    agenda[categoria].append(nombre)

    return agenda


def diccionarios():
    productos = [{"nombre": "pan", "precio": 1}, {"nombre": "leche", "precio": 2}]
    producto = input("que producto quieres buscar: ")
    encontrado = False
    for i in productos:
        if producto == i['nombre']:
            print(i['nombre'], i['precio'])
            encontrado = True

    if not encontrado:
        print("Ese producto no existe")


def matrices():
    M = []
    nfilas = 4
    ncolumnas = 4
    for i in range(nfilas):
        M.append([])
        for j in range(ncolumnas):
            M[i].append(".")
    f = 0
    c = 0
    M[f][c] = "J"
    while True:
        contestacion = input("derecha/abajo: ")
        while not (contestacion == "derecha") and not (contestacion == "abajo"):
            contestacion = input("derecha/abajo: ")

        if contestacion == "derecha":
            if c <= 3 and f <= 3:
                M[f][c] = "."
                c += 1
                if c <= 3:
                    M[f][c] = "J"
                else:
                    c -= 1
                    M[f][c] = "J"
                    print("nosepuede")
            else:
                print("nosepuede")

        if contestacion == "abajo":
            if c <= 3 and f <= 3:
                M[f][c] = "."
                f += 1
                if f <= 3:
                    M[f][c] = "J"
                else:
                    f -= 1
                    M[f][c] = "J"
                    print("nosepuede")
            else:
                print("nosepuede")


        for i in M:
            for j in i:
                print(j, end="\t")
            print()

#print(agenda_contactos())
#diccionarios()
#matrices()
notas = [3, 8, 5, 2, 9, 4]
mayores_cinco = list(filter(lambda x: x >= 5, notas))
print(mayores_cinco)
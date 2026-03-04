import random

def configurar_mision():
    Dic = dict()
    tupla = ('Alto', 'Bajo')

    nombre = input("Nombre: ")
    while not nombre.isalnum():
        nombre = input("Nombre: ")
    Dic['Nombre'] = nombre

    filas = int(input("filas: "))
    while filas < 5 or filas > 10:
        filas = int(input("filas: "))
    Dic['filas'] = filas

    columnas = int(input("columnas: "))
    while columnas < 5 or columnas > 10:
        columnas = int(input("columnas: "))
    Dic['columnas'] = columnas

    energia = input("energia: ")
    while energia not in tupla:
        energia = input("energia: ")
    Dic['energia'] = energia

    return Dic



def desplegar_satelites(D):
    M = []
    filas = D['filas']
    columnas = D['columnas']

    for i in range(filas):
        M.append([])
        for j in range(columnas):
            M[i].append(0)

    numero_satelites = (filas + columnas) // 2
    while numero_satelites > 0:
        filas_a = random.randint(0, filas - 1)
        columnas_a = random.randint( 0, columnas - 1)

        if M[filas_a][columnas_a] == 0:
            M[filas_a][columnas_a] = "S"
            numero_satelites -= 1

    return M


def mostrar_matriz(matriz):
    C = ""
    for i in matriz:
        print("\t", end="")
        for j in i:
            if j == "0" or j == "S":
                C = "."
            elif j == "R":
                C = "[S]"
            elif j == "X":
                C = "[X]"
            print(C, end="\t")
        print()


def iniciar_rescate(M, bateria):
    # Contamos cuántos satélites hay en total al inicio
    satelites_pendientes = sum(fila.count('S') for fila in M)

    while bateria > 0 and satelites_pendientes > 0:
        print(f"\nEnergía restante: {bateria}  "
              f"Satélites por rescatar: {satelites_pendientes}")
        f_user = int(input(f"Introduce fila (0-{len(M) - 1}): "))
        c_user = int(input(f"Introduce col (0-{len(M[0]) - 1}): "))

        # Validar límites
        if 0 <= f_user < len(M) and 0 <= c_user < len(M[0]):
            if M[f_user][c_user] == "S":
                print("satelite encontrado")
                M[f_user][c_user] = "R"
                satelites_pendientes -= 1
            elif M[f_user][c_user] == 0:
                print("Espacio vacío... Energía perdida.")
                M[f_user][c_user] = "X"
                bateria -= 1
            else:
                print("Ya has escaneado esa zona")
        else:
            print("Coordenadas fuera de rang.")

        mostrar_matriz(M)

    if satelites_pendientes == 0:
        print("\nMISION COMPLETADA")
    else:
        print("\nMISION FALLIDA")





#dic = configurar_mision()
#print(dic)
dic = {'Nombre': 'alvaro', 'filas': 5, 'columnas': 5, 'energia': 'Alto'}
fl = lambda x: x['filas'] * x['columnas'] if x['energia'] == "Alto" else (x['filas'] * x['columnas']) // 2
bateria = fl(dic)
matriz = desplegar_satelites(dic)
print(matriz)
mostrar_matriz(matriz)
iniciar_rescate(matriz, bateria)


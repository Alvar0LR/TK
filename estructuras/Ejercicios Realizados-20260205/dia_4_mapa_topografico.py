import random
def generar_terreno(n):
    M = []
    for i in range(n):
        M.append([])
        for j in range(n):
            numero = random.randint(1,50)
            M[i].append(numero)
    return M

def mostrar_matriz(M):
    for i in M:
        for j in i:
            print(j, end="\t")
        print()

def detectar_cimas(M):
    D = {}
    n = len(M)
    for i in range(n):
        for j in range(n):
            actual = M[i][j]
            es_cima = True

            #Mirar Arriba
            if i > 0 and M[i-1][j] > actual:
                es_cima = False

            #Mirar Abajo
            if i < n - 1 and M[i + 1][j] > actual:
                es_cima = False

            #Mirar a la izquierda
            if j > 0 and M[i][j-1] > actual:
                es_cima = False

            #Mirar a la derecha
            if j < n - 1 and M[i][j+1] > actual:
                es_cima = False


            if es_cima:
                tupla_topo = f"({i},{j})"
                D[tupla_topo] = actual
    return D

def mostrar_dic(D:dict):
    for i,j in D.items():
        print(i,j)



print("0.- Salir")
print("1.- Generar Lista Nombres")
print("2.- Generar Matriz Nombres")
print("3.- Mostrar matriz")
print("4.- Mostrar matriz 2")
print("5.- Generar Diccionaro personas - posición")

opcion = int(input("Teclee opción: "))
while opcion != 0:
    if opcion == 1:
        terreno = generar_terreno(4)
        mostrar_matriz(terreno)
    elif opcion == 2:
        cimas = detectar_cimas(terreno)
        mostrar_dic(cimas)
    opcion = int(input("Teclee opción: "))

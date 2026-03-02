import random

# Función Se piden los nombres de personas 
# hasta pulsar enter devuelve lista
def Generar_Lista():
    L = list()
    nombre = input("Nombre: ")
    while nombre != "":
        L.append(nombre)
        nombre = input("Nombre: ")
    return L

# Función que genera una matriz cuadrada 
# según el número de personas y coloca 
# aleatoriamente los nombres de las personas y la devuelve
def Generar_Matriz_Cuadrada(ListaN):
    M = list()
    for i in range(len(ListaN)):
        M.append([])
        for j in range(len(ListaN)):
           M[i].append(random.choice(ListaN))
    return M

# Función mostrar matriz
def Mostrar_Matriz(M):
    for i in range(len(M)):
        for j in range(len(M)):
           print(M[i][j], end="\t")
        print()

def Mostrar_Matriz2(M):
    matriz = ""
    for i in range(len(M)):
        fila =""
        for j in range(len(M)):
            fila += M[i][j] + " - "
        matriz += fila[:-2] + "\n"
    return matriz





# Función que se le manda la matriz y la lista 
# y te devuelve un diccionario con clave el 
# nombre de las personas y contenido una 
# lista de tuplas de posiciones de las personas. 
def Generar_Diccionario(M, L):
    D = dict()
    for e in L:
        D[e] = []
    for i in range(len(M)):
        for j in range(len(M)):
            D[M[i][j]].append((i,j))
            
    return D

print("0.- Salir")
print("1.- Generar Lista Nombres")
print("2.- Generar Matriz Nombres")
print("3.- Mostrar matriz")
print("4.- Mostrar matriz 2")
print("5.- Generar Diccionaro personas - posición")

opcion = int(input("Teclee opción: "))
while opcion != 0:
    if opcion == 1:
        L = Generar_Lista()
        print(L)         
    elif opcion == 2:
        M = Generar_Matriz_Cuadrada(L)
        print(M)
    elif opcion == 3:
        Mostrar_Matriz(M)
    elif opcion == 4:
       print(Mostrar_Matriz2(M))
    elif opcion == 5:
        Mi_D = Generar_Diccionario(M, L)
        print(Mi_D)
    opcion = int(input("Teclee opción: "))
    
    
    


# ########################
# Opciones generar sumar_matriz
    
#     for i in range(len(ListaN)):
#         F = ["---"] * len(ListaN)
#         M.append(F)    
        
#     for i in range(len(ListaN)):
#         for j in range(len(ListaN)):
#     #        M[i][j] = ListaN[random.randint(0, len(ListaN)-1)]
#             M[i][j] = random.choice(ListaN)

# ##############
        
#     for i in range(len(ListaN)):
#         F = [""] * len(ListaN)
#         M.append(F)
#         for j in range(len(ListaN)):
#             M[i][j] = random.choice(ListaN)


    # for i in range(len(M)):
    #     for j in range(len(M)-1):
    #         print(M[i][j], end=" - ")
    #     print(M[i][j])  
        
    # for i in range(len(M)):
    #     for j in range(len(M)):
    #         if j < (len(M)-1):
    #             print(M[i][j], end=" - ")
    #         else:
    #             print(M[i][j])            

    # for i in range(len(M)):
    #     for j in range(len(M)):
    #         print(f"{M[i][j] + ' - ' if j < (len(M)-1) else M[i][j]}", end="")
    #     print()

##############
#           print(f"{M[i][j]}\t", end="")

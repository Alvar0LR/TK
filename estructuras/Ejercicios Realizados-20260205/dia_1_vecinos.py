import random

def generar_lista_nombres():
    L =[]
    nombre = input("Nombre: ")
    while nombre != "": 
        L.append(nombre)
        nombre = input("Nombre: ")
    return L

def generar_matriz_nombres(L):
    M = []
    n = len(L)
    for i in range(n):
        M.append([])
        for j in range(n):
            nombre_seleccionado = random.choice(L)
            M[i].append(nombre_seleccionado)
    return M

def mostrar_matriz(M):
    for i in M:
        for j in i:
            print(j, end="\t") 
        print()

def detectar_gemelos_diagonales(M):
    D = {}
    n = len(M)

    for i in range(n):
        for j in range(n):
            nombre_actual = str(M[i][j])

            if i > 0 and j > 0:
                vecino = M[i-1][j-1]
                if vecino == nombre_actual:
                    mensaje = f"{nombre_actual} tiene un vecino en la posicion {(i-1,j-1)}"
                    if nombre_actual not in D:
                        D[nombre_actual] = []
                    D[nombre_actual].append(mensaje)

           
            if i > 0 and j < n - 1:
                vecino = M[i-1][j+1]
                if vecino == nombre_actual:
                    mensaje = f"En ({i},{j}) tiene gemelo en ({i-1},{j+1})"
                    if nombre_actual not in D:
                        D[nombre_actual] = []
                    D[nombre_actual].append(mensaje)

          
            if i < n - 1 and j > 0:
                vecino = M[i+1][j-1]
                if vecino == nombre_actual:
                    mensaje = f"En ({i},{j}) tiene gemelo en ({i+1},{j-1})"
                    if nombre_actual not in D:
                        D[nombre_actual] = []
                    D[nombre_actual].append(mensaje)

           
            if i < n - 1 and j < n - 1:
                vecino = M[i+1][j+1]
                if vecino == nombre_actual:
                    mensaje = f"En ({i},{j}) tiene gemelo en ({i+1},{j+1})"
                    if nombre_actual not in D:
                        D[nombre_actual] = []
                    D[nombre_actual].append(mensaje)
    return D    

def mostrar_gemelos(D):
    for i in D.keys():
        print(f"{i}:")
        for j in D[i]:
            print(j)
        print()    

print("0.- Salir")
print("1.- Generar Lista Nombres")
print("2.- Generar Matriz Nombres")
print("3.- Mostrar matriz")
print("4.- Mostrar matriz 2")
print("5.- Generar Diccionaro personas - posición")

opcion = int(input("Teclee opción: "))
while opcion != 0:
    if opcion == 1:
        nombres = generar_lista_nombres()
    elif opcion == 2:
        if nombres:
            M = generar_matriz_nombres(nombres)
            mostrar_matriz(M)
        else:
            print("Pulsa primero la opcion 1")
    elif opcion == 3:
      D = detectar_gemelos_diagonales(M)
      mostrar_gemelos(D)
    opcion = int(input("Teclee opción: "))
import random
def crearMatriz():
    matriz = []
    filas = random.randint(2,5)
    for i in range(filas):
        matriz.append([])
        columnas = random.randint(2,5)
        for j in range(0, columnas):
            matriz[i].append(random.randint(0, 10))   

    return matriz

def MostrarMatriz(M):
    for i in range(0, len(M)):
        for j in range(0,len(M[i])):
            print(M[i][j], end="\t")
        print()
    
   
def Recortes(matriz):
    #minimo = min(len(matriz), len(matriz[0]))
    filas = len(matriz)
    minimo = len(matriz[0])
    for fila in matriz:
        if len(fila) < minimo:
            minimo = len(fila)
    rango = min(filas, minimo)




print("0-Salir")
print("1- Crear Matriz")
print("2- Mostrar Matriz")
print("3- Recortes")

opc = int(input("Opcion: "))
while opc != 0:
    if opc == 1:
        m = crearMatriz()
        print(m)
    elif opc == 2:
        MostrarMatriz(m)
    elif opc == 3:
        Recortes(m)
    opc = int(input("Opcion: "))
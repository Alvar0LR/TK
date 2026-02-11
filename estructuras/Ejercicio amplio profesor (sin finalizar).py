"""
Este ejercicio se ha iniciado en clase el día 17/12 y su realización es muy aconsejable.
El enunciado es el siguiente:

Ejercicio

- Función Se piden los nombres de personas hasta pulsar enter y devuelve lista
- Función que genera una matriz cuadrada según el número de personas y coloca aleatoriamente los nombres de las personas y la devuelve la matriz
- Función mostrar matriz
- Función que se le manda la matriz y la lista y te devuelve un diccionario con clave el nombre de las personas y contenido una lista de tuplas de posiciones de las personas.
- Función mostrar diccionario
- Función a partir del diccionario determinar si hay alguna persona que no está
- Función que se le pasa el diccionario y el tamaño de la lista de personas. A partir de esta información muestra los nombres de las personas en un menú numerado y pide el número (comprueba si es correcto) y finalmente a partir del diccionario pasado muestre en forma de matriz las posiciones en las que está la persona seleccionada, siendo el resto de posiciones "------"
- Función comer a partir de la matriz pasado como parámetro, si un jugador está entre dos iguales (arriba - abajo - derecha - izquierda) es comido por este. Irá en orden. Acaba cuando nadie es comido.
"""


import random

#Función Se piden los nombres de personas hasta pulsar enter devuelve lista
def generar_lista():
    L = list()
    nombre = input("ingrese nombre: ")
    while nombre != '':
        L.append(nombre)
        nombre = input("ingrese nombre: ")
    return L

#Función que genera una matriz cuadrada según el número de personas y coloca
# aleatoriamente los nombres de las personas y la devuelve.

def Generar_Matriz_Cuadrada(L):
    M = list() #

    for i in range(len(L)):
        F=["---"] * len(L)
        M.append(F)

    for i in range(len(M)):
        #Se podria hacer con len(L), ya que es la misma dimensión al ser cuadrada
        # aqui estamos en M[i]
        """ Se podria meter el FOR anterior aqui dentro:
          F=["---"] * len(L)
        M.append(F)
        """
        for j in range(len(M[i])): #Se podria poner range(len(M)), ya que es cuadrada.
            # aqui estamos en M[i][j]
            M[i][j] =L[random.randint(0, len(L)-1)]
            #M[i][j] =random.choice(L)
    """ 
    #Metodo profesor:
    for in range(len(L)):
        M.append([])
         for j in range(len(L)):
            M[i].append(random.choice(L)) 
    """
    return M

#Función mostrar matriz.
def mostrar_matriz(M):
    for i in range(len(M)):
        for j in range(len(M)):
            print(M[i][j], end="\t")
        print()


def mostrar_matriz2(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if j < len(M[i]) - 1:
                print(M[i][j], end=" - ")
            else:
                print(M[i][j])


def mostrar_matriz3(M):
    matriz_mostrar = " "
    for i in range(len(M)):
        fila=""
        for j in range(len(M)):
            fila += M[i][j] + " - "
        #print(fila[:-2])
        matriz_mostrar+=fila[:-2] + "\n"
    return matriz_mostrar

"""
Función que se le manda la matriz y la lista y te devuelve un diccionario con clave
el nombre de las personas y contenido una lista de tuplas de posiciones de las personas.
"""
def Generar_Diccionario(M,L):
    D = {}  # diccionario vacío

    for i in L:  # se inicializa una lista vacía para cada nombre
        D[i] = []

    for i in range(len(M)):  # se recorren las filas
        for j in range(len(M)):  # se recorren las columnas
            # se añade la posición donde aparece cada nombre
            D[M[i][j]].append((i, j))
    return D  # se devuelve el diccionario

def mostrar_diccionario(M, D):
    for nombre in D:  # se recorre cada persona
        print("\nPosiciones de:", nombre)
        for i in range(len(M)):  # se recorren filas
            for j in range(len(M)):  # se recorren columnas
                if (i, j) in D[nombre]:  # si esa posición pertenece a la persona
                    print(nombre, end="\t")
                else:
                    print("-----", end="\t")

    return D


print("0. - Salir")
print("1. - Generar Lista de Nombre")
print("2. - Generar Matriz de Nombres")
print("3. - Mostrar Matriz")
print("4. - Generar Diccionario")
print("5. - Mostrar Diccionario")


opcion = int(input("Teclee opción: "))

while opcion != 0:
    if opcion == 1:
        L = generar_lista()
        print(L)

    elif opcion == 2:
        M = Generar_Matriz_Cuadrada(L)
        print(M)

    elif opcion == 3:
        mostrar_matriz2(M)

    elif opcion == 4:
        Dic = Generar_Diccionario(M, L)
        print(Dic)

    elif opcion == 5:
        mostrar_diccionario(M, Dic)


    opcion = int(input("Teclee opción: "))

print("Fin")
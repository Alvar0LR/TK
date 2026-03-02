def crear_almacen(filas, columnas):
    M = []
    D = {"estado": "libre", "peso": 0, "id": "VACIO"}
    for i in range(filas):
        M.append([])
        for j in range(columnas):
            M[i].append(D)

    return M

def filtrar_pesos(lista_pesos):
    evens2 = filter(lambda x: x > 20, lista_pesos)
    return list(evens2)

def validar_nombre():
    nombre_producto = input("Producto: ")
    while not (3 <= len(nombre_producto) <= 9):
        nombre_producto = input("Producto: ")
    return nombre_producto

def llenar_almacen_matriz(matriz, pesos_filtrados):
    contador = 0

    for i in pesos_filtrados:

        nombre = validar_nombre()
        hueco_encontrado = False

        while not hueco_encontrado:
            fila = input("Fila: ")
            while not (fila.isdigit()) or not(0 <= int(fila) <= 1):
                   fila = input("Fila: ")
            filav = int(fila)

            columna = input("Columna: ")
            while not (fila.isdigit() or not (0 <= int(columna) <= 1)):
               columna = input("Columna: ")
            columnav = int(columna)

            if matriz[filav][columnav]['estado'] == 'libre':
                matriz[filav][columnav] = {'nombre': nombre,'estado': 'ocupado', 'peso': i, 'id': contador}
                hueco_encontrado = True
                contador += 1
            else:
                print("Esta ocupado, vuelve a elegir, fila y columna")

    for i in matriz:
        for j in i:
            print(j, end="\t")
        print()

m = crear_almacen(2,2)
pesos = filtrar_pesos(lista_pesos=[1,2,4,5,6,20,21])
print(validar_nombre())
llenar_almacen_matriz(m,pesos)
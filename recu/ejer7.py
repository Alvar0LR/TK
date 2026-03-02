def mapa():
    M = []
    for i in range(4):
        M.append([])
        for j in range(4):
            M[i].append(0)
    for i in M:
        for j in i:
            print(j, end="\t")
        print()
    return M

def contenedor():
    D = {}

    id = input("id:")
    while not (id.isdigit()):
        id = input("id:")
    D['id'] = int(id)

    producto = input("producto:")
    D['producto'] = producto

    cantidad = input("cantidad:")
    while not (cantidad.isdigit()):
        cantidad = input("cantidad:")
    D['cantidad'] = int(cantidad)

    return D

def ubicarMercancias(M):

    filas = input("Filas: (0 <= y <=3): ")
    while not (filas.isdigit()) or not(0 <= int(filas) <= 3):
        filas = input("Filas: (0 <= y <=3): ")
    nfilas = int(filas)

    columnas = input("Columnas: (0 <= y <=3): ")
    while not (columnas.isdigit()) or not (0 <= int(columnas) <= 3):
        columnas = input("Columnas: (0 <= y <=3): ")
    ncolumnas = int(columnas)

    dic = contenedor()

    if M[nfilas][ncolumnas] == 0:
        M[nfilas][ncolumnas] = dic
    else:
        guardar = input("Sobreescribir/Sumar:").lower().strip()
        while not (guardar.lower() == "Sobreescribir".lower()) and not(guardar.lower() == "Sumar".lower()):
            guardar = input("Sobreescribir/Sumar:").lower().strip()
        if guardar == "sobreescribir":
            M[nfilas][ncolumnas] = dic
        if guardar == "sumar":
            M[nfilas][ncolumnas]['cantidad'] += dic['cantidad']

    for i in range(nfilas):
        for j in range(ncolumnas):
            if j == 0:
                print("Vacio")
            else:
                print(j)


    print(M)



m = mapa()
#print(contenedor())
print(ubicarMercancias(m))
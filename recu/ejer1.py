import random


def validacion_datos():
    D = {}
    vueltas = int(input("Numero vueltas (>=5 x <=20): "))
    while not (20 >= vueltas >= 5):
        vueltas = int(input("Numero vueltas (>=5 x <=20): "))
    D['vueltas'] = vueltas

    return D

def el_almacen():
    stock = {"balones": 15, "raquetas": 8, "camisetas": 20}
    cantidad_articulo = 0
    print("stock del almacen")
    for i,j in stock.items():
        print(i, j)

    articulo_solicitado = input("Articulo a solicitar")

    if articulo_solicitado in stock:

        cantidad = input("Cuantos quiere comprar: ")
        while not(cantidad.isdigit()):
            cantidad = input("Cuantos quiere comprar: ")
        cantidad_articulo = int(cantidad)
        if stock[articulo_solicitado] < cantidad_articulo or cantidad_articulo <= 0:
            print("El articulo no tiene esa cantidad ")
        else:
            stock[articulo_solicitado] -= cantidad_articulo
            print(f"{articulo_solicitado} -> Quedan: {stock[articulo_solicitado]}")
    else:
        print("Este articulo no exite")


def el_topografo():
    M = []
    nfilas = 3
    ncolumnas = 5
    for i in range(nfilas):
        M.append([])
        for j in range(ncolumnas):
            numero_seleccionado = 0
            M[i].append(numero_seleccionado)

    tesoros_puestos = 0
    while tesoros_puestos < 3:
        f_random = random.randint(0, nfilas - 1)
        c_random = random.randint(0, ncolumnas - 1)

        if M[f_random][c_random] == 0:
            M[f_random][c_random] = "X"
            tesoros_puestos += 1


    for i in M:
        for j in i:
            print(j, end="\t")
        print()

    return M

examen = {"teoria": 4, "practica": 6}
nota_final = lambda d: d['teoria'] + d['practica']
print(nota_final(examen))

#print(validacion_datos())
#el_almacen()
print(el_topografo())

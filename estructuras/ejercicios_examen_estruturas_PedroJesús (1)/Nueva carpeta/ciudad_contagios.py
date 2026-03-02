def GenerarCiudad(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("SANO")
        matriz.append(fila)
    
    import random
    fila_aleatoria = random.randint(0, filas - 1)
    columna_aleatoria = random.randint(0, columnas - 1)
    matriz[fila_aleatoria][columna_aleatoria] = "I-0"
    
    return matriz

def MostrarCiudad(matriz, dia):
    print(f"\nDia: {dia}\n")
    for i in range(len(matriz)):
        linea = ""
        for j in range(len(matriz[i])):
            linea += matriz[i][j] + "\t"
        print(linea)


def Contagiar(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    dia = 0
    
    # Contar cuántas personas sanas hay inicialmente
    sanas = 0
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == "SANO":
                sanas += 1
    
    # Continuar mientras haya personas sanas
    while sanas > 0:
        # Incrementar día
        dia += 1
        
        # Crear nueva matriz para el siguiente día
        nueva_matriz = []
        for i in range(filas):
            nueva_fila = []
            for j in range(columnas):
                if matriz[i][j] == "SANO":
                    # Verificar si algún vecino está infectado
                    contagiado = False
                    # Arriba
                    if i > 0 and matriz[i-1][j] != "SANO":
                        contagiado = True
                    # Abajo
                    if i < filas-1 and matriz[i+1][j] != "SANO":
                        contagiado = True
                    # Izquierda
                    if j > 0 and matriz[i][j-1] != "SANO" :
                        contagiado = True
                    # Derecha
                    if j < columnas-1 and matriz[i][j+1] != "SANO" :
                        contagiado = True
                    
                    if contagiado:
                        nueva_fila.append("I-" + str(dia))
                    else:
                        nueva_fila.append(matriz[i][j])
                else:
                    nueva_fila.append(matriz[i][j])
            nueva_matriz.append(nueva_fila)
        
        matriz = nueva_matriz
    
        MostrarCiudad(matriz, dia)
        
        sanas = 0
        for i in range(filas):
            for j in range(columnas):
                if matriz[i][j] == "SANO":
                    sanas += 1
    
    print(f"\nDías Totales: {dia}")
    return dia


# Programa principal
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

ciudad = GenerarCiudad(filas, columnas)

# Mostrar ciudad inicial (día 0)
MostrarCiudad(ciudad, 0)

dias_totales= Contagiar(ciudad)


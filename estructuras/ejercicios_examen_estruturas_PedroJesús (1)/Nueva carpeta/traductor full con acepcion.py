def Introducir_Palabra(D, P):
    resultado = ""
    if P in D:
        resultado = f"Ya existe {P} en diccionario"
    else:
        D[P] = []
        resultado = f"Insertada {P} en diccionario"
    return resultado


def Introducir_Acepción(D, P, A):
    resultado = ""
    if P in D:
        D[P].append(A)
        resultado = f"Acepción introducida en {P}"
    else:
        resultado = f"No existe {P} en diccionario"
    return resultado


def Mostrar_Diccionario(D):
    resultado = "Diccionario\n===========\n"
    PDic = list(D.keys())
    PDic.sort()
    for e in PDic:
        resultado += f"{e}:\n"
        for a in D[e]:
            resultado += f"\t- {a}\n"
        resultado += f"\n"
    return resultado


def Mostrar_Diccionario_letra(D, L):
    resultado = f"Diccionario enpieza por {L}\n===========\n"
    PDic = list(D.keys())
    PDic.sort()
    i = 0
    while i < len(PDic) and PDic[i][0] < L:
        i += 1

    while i < len(PDic) and PDic[i][0] == L:
        resultado += f"{PDic[i]}:\n"
        for a in D[PDic[i]]:
            resultado += f"\t- {a}\n"
        resultado += f"\n"
        i += 1

    return resultado


def Traducir_Texto_Ingles(D, texto_espanol):
    lista_palabras_espanol = texto_espanol.split()
    traduccion = ""

    for palabra_espanol in lista_palabras_espanol:
        if not palabra_espanol in D:
            print(Introducir_Palabra(D, palabra_espanol))
            acepcion_ingles = input(f"Traducción de {palabra_espanol}: ")
            print(Introducir_Acepción(D, palabra_espanol, acepcion_ingles))

        traduccion += f"{D[palabra_espanol][0]} "

    return traduccion


def Traducir_Texto_Espanol(D, texto_ingles):
    lista_palabras_ingles = texto_ingles.split()
    traduccion = ""

    for palabra_ingles in lista_palabras_ingles:
        palabra_espanol_encontrada = ""
        indice_clave = 0
        lista_claves = list(D.keys())

        while indice_clave < len(lista_claves) and palabra_espanol_encontrada == "":
            clave_espanol = lista_claves[indice_clave]
            if palabra_ingles in D[clave_espanol]:
                palabra_espanol_encontrada = clave_espanol
            indice_clave += 1

        if palabra_espanol_encontrada == "":
            palabra_espanol_nueva = input(f"Traducción de {palabra_ingles} a español: ")
            if not palabra_espanol_nueva in D:
                print(Introducir_Palabra(D, palabra_espanol_nueva))
            print(Introducir_Acepción(D, palabra_espanol_nueva, palabra_ingles))
            palabra_espanol_encontrada = palabra_espanol_nueva

        traduccion += f"{palabra_espanol_encontrada} "

    return traduccion


MiDic = dict()

print("0.- Salir")
print("1.- Introducir Palabra")
print("2.- Introducir Acepción")
print("3.- Mostrar Diccionario")
print("4.- Mostrar Diccionario Palabra")
print("5.- Traducir texto a inglés")
print("6.- Traducir texto a español")

opcion = int(input("Opción: "))

while opcion != 0:
    if opcion == 1:
        Palabra = input("Palabra: ")
        print(Introducir_Palabra(MiDic, Palabra))
        print(MiDic)

    elif opcion == 2:
        Palabra = input("Palabra: ")
        Acepción = input("Acepción: ")
        print(Introducir_Acepción(MiDic, Palabra, Acepción))
        print(MiDic)

    elif opcion == 3:
        print(Mostrar_Diccionario(MiDic))

    elif opcion == 4:
        Letra = input("Letra: ")
        print(Mostrar_Diccionario_letra(MiDic, Letra))

    elif opcion == 5:
        Texto = input("Texto en español: ")
        print(Traducir_Texto_Ingles(MiDic, Texto))

    elif opcion == 6:
        Texto = input("Texto en inglés: ")
        print(Traducir_Texto_Espanol(MiDic, Texto))

    opcion = int(input("Opción: "))

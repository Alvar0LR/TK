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

MiDic = dict()
print("0.- Salir")
print("1.- Introducir Palabra")
print("2.- Introducir Acepción")
print("3.- Mostrar Diccionario")
print("4.- Mostrar Diccionario Palabra")
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
    opcion = int(input("Opción: "))

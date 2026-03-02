def Introducir_Palabra_traducción(D, P, T):
    resultado = ""
    D[P] = T
    if P in D:
        resultado = f"Actualizada {P} en diccionario"
    else:
        resultado = f"Insertada {P} en diccionario"
    return resultado

def Mostrar_Diccionario(D):
    resultado = "Diccionario\n===========\n"
    PDic = list(D.keys())
    PDic.sort()
    for e in PDic:
        resultado += f"{e}: {D[e]}\n"
    return resultado


def Traducir_Texto_Inglés(D, T):
    L = T.split()
    traducción = ""
    for p in L:
        if not p in D:
            Trad = input(f"Traducción de {p}: ")
            D[p] = Trad
        traducción += f"{D[p]} "
    return traducción
            
def Traducir_Texto_Español(D, T):       
    L = T.split()
    traducción = ""
    TIngles = list(D.values())
    Lpalabras = list(D.keys())
    for p in L:
        if not p in TIngles:
            Trad = input(f"Traducción de {p} a español: ")
            D[Trad] = p
        else:
            i = 0
            while p != D[Lpalabras[i]]:
                i += 1
            Trad = Lpalabras[i]
        traducción += f"{Trad} "
    return traducción
                


MiDic = dict()
print("0.- Salir")
print("1.- Introducir Palabra Traducción")
print("2.- Mostrar Diccionario")
print("3.- Traducir texto a inglés")
print("4.- Traducir texto a español")
opcion = int(input("Opción: "))
while opcion != 0:
    if opcion == 1:
        Palabra = input("Palabra: ")
        Traducción = input(f"Traducción de {Palabra}: ")
        print(Introducir_Palabra_traducción(MiDic, Palabra, Traducción))
        print(MiDic)
    elif opcion == 2:
        print(Mostrar_Diccionario(MiDic))
    elif opcion == 3:
        Texto = input("Texto en español: ")
        print(Traducir_Texto_Inglés(MiDic, Texto))
     #   print(MiDic)
    elif opcion == 4:
        Texto = input("Texto en inglés: ")
        print(Traducir_Texto_Español(MiDic, Texto))
    opcion = int(input("Opción: "))
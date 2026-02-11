def insertar_palabra(dic, palabra):
    if palabra in dic:
        print("La palabra ya se encuentra en el diccionario")
    else:
        dic[palabra] = []
        print("palabra insertada con lista")

def introducir_acepcion(dic,palabra, acepcion):
    if palabra in dic:
        dic[palabra].append(acepcion)
        print("Acepcion introducida en el diccionario")
    else:
        print("No existe esta palabra en el diccionario")

def mostrar_diccionario(dic: dict):
    for i in dic:
        print(f"+ {i}")
        for j in dic[i]:
            print(f"-{j}", end="\n")
        print()


def mostrar_diccionario_letra(dic, letra):
    resultado = ""
    list_dic_palabras = list(dic.keys())
    list_dic_palabras.sort()
    i = 0
    while i < len(list_dic_palabras) and list_dic_palabras[i][0] < letra:
        i += 1

    while i < len(list_dic_palabras) and list_dic_palabras[i][0] == letra:
        resultado += f" - {list_dic_palabras[i]}:\n"
        for x in dic[list_dic_palabras[i]]:
            resultado += f"+ {x}\n"
        resultado += f"\n"
        i += 1

    return resultado



if __name__ == '__main__':

    print("0.- Salir")
    print("1.- Generar y mostrar Matriz letras")
    print("2.- Generar mapa calor")

    opcion = int(input("Teclee opción: "))
    while opcion != 0:
        if opcion == 1:
            dic = {"banco": ["Finanza", "Economia"] , "Silla":["Taburente"]}
            palabra = input("Palabra:")
            insertar_palabra(dic, palabra)
        elif opcion == 2:
            acepcion = input("Acepcion: ")
            palabra = input("palabra")
            introducir_acepcion(dic, palabra,acepcion)
        elif opcion == 3:
            mostrar_diccionario(dic)
        elif opcion == 4:
            letra = input("letra:")
            res = mostrar_diccionario_letra(dic,letra )
            print(res)
        opcion = int(input("Teclee opción: "))

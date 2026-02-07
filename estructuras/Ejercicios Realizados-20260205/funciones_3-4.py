def es_nif(N):
    LETRA = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
    Numero = int(N[:-1])
    L = N[-1]
    print(Numero)
    print(L)
    return LETRA[(Numero % 23)] == L

def letra_nif():
    pass

print("0.- Salir")
print("1.- Comprobar NIF")
print("2.- Obtener letra NIF")
opcion = int(input("Teclee opción: "))
while opcion != 0:
    if opcion == 1:
        NIF = input("Teclee NIF: ")
        if es_nif(NIF):
            print("NIF correcto")
        else:
            print("NIF incorrecto")
    elif opcion == 2:
        pass
    opcion = int(input("Teclee opción: "))
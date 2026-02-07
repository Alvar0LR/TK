def introducir_cadenas():
    pass

def cadenas_largas(L):
    R = list()
    Max = 0
    for e in L:
        if len(e) > Max:
            R = [e]
            Max = len(e)
        elif len(e) == Max:
            R.append(e)
    return R

L = list()
print("0.- Salir")
print("1.- Introducir datos")
print("2.- Cadenas más largas")
opcion = int(input("Teclee opción: "))
while opcion != 0:
    if opcion == 1:
        L=["Pepe", "Ana", "Juan", "Antonio", "Paz"]           
    elif opcion == 2:
        print(cadenas_largas(L))
    opcion = int(input("Teclee opción: "))
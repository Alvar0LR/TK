def CrearDiccionario():
    D = {}
    curso = input("Curso: ")
    D["Curso"] = curso
    NAlumnos = int(input("Numero de alumnos: "))
    D["NAlumnos"] = NAlumnos
    D["Mayores"] = []
    D["Menores"] = []
    for i in range(D["NAlumnos"]):
        Nombre = input("Introduce el nombre: ")
        Edad = int(input("Introduce la edad: "))
        if Edad >= 18:
            D["Mayores"].append(Nombre)
        else:
            D["Menores"].append(Nombre) 
    return D


def Mostrar(Dic: dict):
    print("Curso: ", Dic["Curso"])
    print("NAlumnos: ", Dic["NAlumnos"])

    ListaMenores = Dic["Menores"]
    ListaMayores = Dic["Mayores"]
    ListaMayores.sort()
    ListaMenores.sort()

    print("Mayores")
    for lM in ListaMayores:
        print(lM)
    print("Menores")
    for lm in ListaMenores:
        print(lm)

def Trabaja(D):
    DT = dict()
    for e in D["Mayores"]:
        R = input(f"{e} Trabaja (s/n)")
        if R == "s":
            DT[e] = True
        else:
            DT[e] = False
    return DT 

def mostrar_nombres_trabajan(quien, dic):
    if quien == "T":
        print("Alumnos que trabajan")
        for i in dic:
            if dic[i]:
                print(i)
    else:
        print("Alumnos que no trabajan")
        for i in dic:
            if not dic[i]:
                print(i)
    


print("0-Salir")
print("1- Crear Matriz")
print("2- Mostrar Matriz")
print("3- Recortes")

opc = int(input("Opcion: "))
while opc != 0:
    if opc == 1:
        #m = CrearDiccionario()
        #print(m)
       m = {'Curso': '4', 'NAlumnos': 6, 'Mayores': ['C', 'D', 'E', 'F'], 'Menores': ['A', 'B']}
    elif opc == 2:
       Mostrar(m)
    elif opc == 3:
       t = Trabaja(m)
       R = input("Quieres sacar (T)rabaja o (N)o trabaja")
       mostrar_nombres_trabajan(R, t)
    opc = int(input("Opcion: "))
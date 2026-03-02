def CrearDiccionario():
    # Se crea un diccionario vacío donde se irá guardando toda la información
    D = {}

    # Se pide al usuario el curso
    curso = input("Curso: ")

    # Se guarda el curso en el diccionario con la clave "Curso"
    D["Curso"] = curso

    # Se pide el número total de alumnos
    NAlumnos = int(input("Numero de alumnos: "))

    # Se guarda ese número en el diccionario
    D["NAlumnos"] = NAlumnos

    # Se crea una lista vacía para almacenar los mayores de edad
    D["Mayores"] = []

    # Se crea una lista vacía para almacenar los menores de edad
    D["Menores"] = []

    # Se repite tantas veces como alumnos haya
    for i in range(D["NAlumnos"]):
        # Se pide el nombre del alumno
        Nombre = input("Introduce el nombre: ")

        # Se pide la edad del alumno
        Edad = int(input("Introduce la edad: "))

        # Si la edad es mayor o igual que 18 se añade a la lista de mayores
        if Edad >= 18:
            D["Mayores"].append(Nombre)
        # En caso contrario se añade a la lista de menores
        else:
            D["Menores"].append(Nombre)

    # Se devuelve el diccionario completo
    return D


def Mostrar(Dic: dict):
    # Se muestra el curso guardado en el diccionario
    print("Curso: ", Dic["Curso"])

    # Se muestra el número de alumnos
    print("NAlumnos: ", Dic["NAlumnos"])

    # Se guardan en variables las listas de menores y mayores
    ListaMenores = Dic["Menores"]
    ListaMayores = Dic["Mayores"]

    # Se ordenan alfabéticamente las dos listas
    ListaMayores.sort()
    ListaMenores.sort()

    # Se muestran los alumnos mayores
    print("Mayores")
    for lM in ListaMayores:
        print(lM)

    # Se muestran los alumnos menores
    print("Menores")
    for lm in ListaMenores:
        print(lm)


def Trabaja(D):
    # Se crea un nuevo diccionario donde se guardará si cada mayor trabaja o no
    DT = dict()

    # Se recorre la lista de alumnos mayores
    for e in D["Mayores"]:
        # Se pregunta si ese alumno trabaja
        R = input(f"{e} Trabaja (s/n)")

        # Si responde "s", se guarda True en el diccionario
        if R == "s":
            DT[e] = True
        # En caso contrario se guarda False
        else:
            DT[e] = False

    # Se devuelve el diccionario con la información laboral
    return DT


def mostrar_nombres_trabajan(quien, dic):
    # Si el usuario pide los que trabajan
    if quien == "T":
        print("Alumnos que trabajan")

        # Se recorren las claves del diccionario
        for i in dic:
            # Si el valor es True significa que ese alumno trabaja
            if dic[i]:
                print(i)
    # Si el usuario pide los que no trabajan
    else:
        print("Alumnos que no trabajan")

        # Se recorren las claves del diccionario
        for i in dic:
            # Si el valor es False significa que ese alumno no trabaja
            if not dic[i]:
                print(i)


print("0-Salir")
print("1- Crear Matriz")
print("2- Mostrar Matriz")
print("3- Recortes")

# Se pide al usuario la opción del menú
opc = int(input("Opcion: "))

# Bucle principal que se repite mientras no se pulse 0
while opc != 0:

    # Si se elige la opción 1
    if opc == 1:
        # Estas dos líneas están comentadas para no pedir datos al usuario
        # m = CrearDiccionario()
        # print(m)

        # Se carga un diccionario de ejemplo directamente
        m = {
            'Curso': '4',
            'NAlumnos': 6,
            'Mayores': ['C', 'D', 'E', 'F'],
            'Menores': ['A', 'B']
        }

    # Si se elige la opción 2 se muestran los datos del diccionario
    elif opc == 2:
        Mostrar(m)

    # Si se elige la opción 3 se pregunta quién trabaja
    elif opc == 3:
        # Se genera el diccionario de trabajo
        t = Trabaja(m)

        # Se pregunta si se quieren mostrar los que trabajan o no
        R = input("Quieres sacar (T)rabaja o (N)o trabaja")

        # Se muestran según la elección
        mostrar_nombres_trabajan(R, t)

    # Se vuelve a pedir una opción
    opc = int(input("Opcion: "))

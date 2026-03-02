def Introducir_Palabra_traducción(D, P, T):
    # Se crea una variable donde se guardará el mensaje que devolverá la función
    resultado = ""

    # Comprobamos ANTES de modificar el diccionario si la palabra ya existía
    if P in D:
        # Si ya existía, el mensaje correcto es de actualización
        resultado = f"Actualizada {P} en diccionario"
    else:
        # Si no existía, el mensaje correcto es de inserción
        resultado = f"Insertada {P} en diccionario"

    # Ahora sí, se modifica el diccionario (se inserta o se actualiza la traducción)
    D[P] = T

    # Se devuelve el mensaje al programa principal (para que lo imprima con print)
    return resultado



def Mostrar_Diccionario(D):
    # Se construye un texto grande en vez de hacer prints dentro del bucle
    # luego el programa lo imprime de golpe con print(Mostrar_Diccionario(MiDic))
    resultado = "Diccionario\n===========\n"

    # keys() devuelve una “vista” de claves, se pasa a lista para poder ordenar
    PDic = list(D.keys())

    # Ordena alfabéticamente las claves (palabras en español)
    PDic.sort()

    # Recorre cada clave ya ordenada
    for e in PDic:
        # D[e] es el valor asociado a esa clave (la traducción en inglés)
        # Se va concatenando al string resultado
        resultado += f"{e}: {D[e]}\n"

    # Devuelve el bloque de texto ya preparado
    return resultado


def Traducir_Texto_Inglés(D, T):
    # split() separa el texto por espacios y devuelve una lista de palabras
    # ejemplo: "hola que tal" -> ["hola", "que", "tal"]
    L = T.split()

    # Se empieza con una traducción vacía y se irá construyendo palabra a palabra
    traducción = ""

    # Se recorre cada palabra p del texto original en español
    for p in L:
        # Si la palabra española p NO está como clave en el diccionario
        if not p in D:
            # Se le pide al usuario la traducción de esa palabra
            Trad = input(f"Traducción de {p}: ")

            # Se guarda en el diccionario: clave española p, valor inglés Trad
            # Así la próxima vez ya no volverá a preguntar por esa palabra
            D[p] = Trad

        # Aquí ya seguro existe D[p]:
        # - o ya existía antes
        # - o se acaba de añadir en el if de arriba
        # Se concatena la traducción al string final, y se añade un espacio
        traducción += f"{D[p]} "

    # Se devuelve el texto traducido completo (con un espacio final)
    return traducción


def Traducir_Texto_Español(D, T):
    # Igual que antes: separa el texto inglés en palabras
    L = T.split()

    # Aquí se irá construyendo la traducción al español
    traducción = ""

    # Se crea una lista con TODOS los valores del diccionario
    # es decir, todas las traducciones en inglés conocidas
    # ejemplo: si D = {"casa":"house", "perro":"dog"} -> TIngles = ["house", "dog"]
    TIngles = list(D.values())

    # Se crea una lista con TODAS las claves (palabras en español)
    # ejemplo: Lpalabras = ["casa", "perro"]
    Lpalabras = list(D.keys())

    # Se recorre cada palabra inglesa p del texto
    for p in L:
        # Si esa palabra inglesa p NO está dentro de la lista de valores ingleses
        # significa que el diccionario no sabe traducirla todavía (inglés -> español)
        if not p in TIngles:
            # Se pregunta al usuario la traducción al español
            Trad = input(f"Traducción de {p} a español: ")

            # Y aquí viene lo “especial”:
            # para poder traducir inglés->español usando el MISMO diccionario,
            # se añade una entrada invertida:
            #   clave = Trad (español)
            #   valor = p    (inglés)
            # En realidad es el mismo formato que siempre: español -> inglés
            # pero lo añadimos porque justo nos falta ese par en el diccionario
            D[Trad] = p

        else:
            # Si p SI está en los valores ingleses, entonces sabemos que existe
            # alguna clave española cuyo valor es exactamente p
            # pero como el diccionario está en español->inglés, no hay acceso directo
            # así que hay que BUSCAR qué clave tiene ese valor

            # i empieza en 0 para recorrer la lista de claves Lpalabras
            i = 0

            # Mientras la palabra inglesa p NO sea igual al valor de la clave actual,
            # seguimos avanzando i
            # D[Lpalabras[i]] es: "valor inglés asociado a la clave española Lpalabras[i]"
            while p != D[Lpalabras[i]]:
                i += 1

            # Cuando el while termina, significa que hemos encontrado el índice i
            # donde D[Lpalabras[i]] == p
            # Por tanto, la palabra española buscada es Lpalabras[i]
            Trad = Lpalabras[i]

        # Se añade la palabra española Trad a la traducción final con un espacio
        traducción += f"{Trad} "

    # Se devuelve la frase traducida al español (con un espacio final)
    return traducción


MiDic = dict()

print("0.- Salir")
print("1.- Introducir Palabra Traducción")
print("2.- Mostrar Diccionario")
print("3.- Traducir texto a inglés")
print("4.- Traducir texto a español")

# Se lee la opción del usuario (un número)
opcion = int(input("Opción: "))

# Bucle del menú: se repite mientras la opción no sea 0
while opcion != 0:

    # OPCIÓN 1: añadir/actualizar una palabra y su traducción
    if opcion == 1:
        # Se pide una palabra en español
        Palabra = input("Palabra: ")

        # Se pide la traducción en inglés de esa palabra
        Traducción = input(f"Traducción de {Palabra}: ")

        # Se llama a la función con (MiDic, Palabra, Traducción)
        # O sea: D = MiDic, P = Palabra, T = Traducción
        # La función modifica MiDic por dentro porque los diccionarios se pasan por referencia
        # y devuelve un texto (resultado) que aquí se imprime
        print(Introducir_Palabra_traducción(MiDic, Palabra, Traducción))

        # Se imprime el diccionario entero para ver cómo quedó tras la modificación
        print(MiDic)

    # OPCIÓN 2: mostrar  el diccionario ordenado
    elif opcion == 2:
        # Mostrar_Diccionario devuelve un string ya formateado
        # print lo imprime tal cual
        print(Mostrar_Diccionario(MiDic))

    # OPCIÓN 3: traducir una frase de español a inglés
    elif opcion == 3:
        # Se pide el texto en español
        Texto = input("Texto en español: ")

        # Se traduce usando el diccionario (y si faltan palabras, se van pidiendo)
        # La función devuelve la frase traducida y aquí se imprime
        print(Traducir_Texto_Inglés(MiDic, Texto))

        # Esta línea está comentada en tu archivo original, la dejo igual
        # print(MiDic)

    # OPCIÓN 4: traducir una frase de inglés a español
    elif opcion == 4:
        # Se pide el texto en inglés
        Texto = input("Texto en inglés: ")

        # Se traduce “a la inversa” buscando en los valores del diccionario
        # y si falta una palabra inglesa, se pide su equivalente en español
        print(Traducir_Texto_Español(MiDic, Texto))

    # Se vuelve a pedir la opción para seguir en el menú
    opcion = int(input("Opción: "))

    """
    
    """

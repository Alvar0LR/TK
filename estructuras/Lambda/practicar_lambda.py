
#Dado un número, calcula su cuadrado.

x1=lambda x: x**2
print(x1(5))

#Dados dos números, encuentra el mayor.

x2=lambda x, y: max(x,y)
x22=lambda x, y: x if x > y else y
print(x2(5,6))
print(x2(5,6))

#Dado un número, comprueba si es impar.

x3=lambda x: x % 2 !=0
print(x3(5))

# Dada una lista de números enteros positivos, filtra todos los números impares.

x4 = lambda lista_numeros: list(filter(lambda numero: numero % 2 != 0, lista_numeros))
print(x4([1, 2, 3, 4, 5, 6, 7]))


# Ordena una lista de tuplas de 3 elementos utilizando su tercer elemento.

x5 = lambda lista_tuplas: sorted(lista_tuplas, key=lambda tupla_actual: tupla_actual[2])
print(x5([(1, 2, 3), (4, 5, 1), (7, 8, 2)]))


# Extrae el dominio de una dirección de correo electrónico.
# Por ejemplo: user@example.com -> example.com

x6 = lambda correo: correo.split("@")[1]
print(x6("user@example.com"))
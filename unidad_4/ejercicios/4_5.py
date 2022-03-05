"""
Cree un programa que utilizando una función, solicite la edad de la persona e imprima
todos los años que la persona ha cumplido según el siguiente formato de ejemplo.

1, 2, 3, 4, 5
Y
5, 4, 3, 2, 1
"""


def imprimir_anios(edad):
    con_formato1 = ""
    con_formato2 = ""

    for x in range(1, edad + 1):
        if x == edad:
            con_formato1 += str(x)
        else:
            con_formato1 += str(x) + ", "

    for y in range(edad, 0, -1):
        if y == 1:
            con_formato2 += str(y)
        else:
            con_formato2 += str(y) + ", "

    print(con_formato1 + "\nY\n" + con_formato2)


edad = int(input("Digita tu edad: "))

print("Los años que la persona cumplio son:")
imprimir_anios(edad)

# Escriba un programa que consulte al usuario por una oración y comente
# al usuario cuantas veces aparecen todas las vocales considerando
# minúsculas, mayúsculas y acentos.

oracion = input("Escriba una oracion: ")
vocales = [
    "a",
    "A",
    "á",
    "Á",
    "e",
    "E",
    "é",
    "É",
    "i",
    "I",
    "í",
    "Í",
    "o",
    "O",
    "ó",
    "Ó",
    "u",
    "U",
    "ú",
    "Ú",
]
cant_vocales = 0

for x in oracion:

    if x in vocales:
        cant_vocales += 1

print(f"La cantidad vocales es {cant_vocales}")

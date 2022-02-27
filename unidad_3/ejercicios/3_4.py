# Escriba un programa que solicite la edad de la persona
# e imprima todos los años que la persona ha cumplido.

edad = int(input("Digita tu edad: "))

print("Los años que la persona cumplio son:")
for x in range(1, edad):
    print(x)

# Escriba un programa que consulte al usuario por una oración y
# comente al usuario cuantas veces aparece la letra “a”.

oracion = input("Escriba una oracion: ").lower()
cant_repet = 0

for x in oracion:

    if x == "a":
        cant_repet += 1

print(f"La cantidad de veces que aparece la letra 'a' es {cant_repet} veces")

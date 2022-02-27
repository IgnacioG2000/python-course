# Tome el ejercicio de cálculo de números pares e impares de la unidad 2
# y agréguele un bucle al código de forma de simplificarlo.

import sys

for x in range(3):

    num = int(sys.argv[x + 1])
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")

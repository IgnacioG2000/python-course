# Cree un programa que incorpore el módulo sys, al cual desde la terminal
# se le puedan pasar tres parámetros. El programa debe tomar los parámetros
# e indicar en la terminal si son múltiplos de dos.

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
    print("Los 3 numeros son multiplos de 2")
elif num1 % 2 != 0 and num2 % 2 == 0 and num3 % 2 == 0:
    print(f"{num1} no es multiplo de 2")
elif num1 % 2 == 0 and num2 % 2 != 0 and num3 % 2 == 0:
    print(f"{num2} no es multiplo de 2")
elif num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 != 0:
    print(f"{num3} no es multiplo de 2")
elif num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 == 0:
    print(f"{num1} y {num2} no son multiplos de 2")
elif num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 != 0:
    print(f"{num1} y {num3} no son multiplos de 2")
elif num1 % 2 == 0 and num2 % 2 != 0 and num3 % 2 != 0:
    print(f"{num2} y {num3} no son multiplos de 2")
else:
    print("Ningun numero es multiplo de 2")

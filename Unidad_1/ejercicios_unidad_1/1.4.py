# Escriba un programa que solicite el radio de una circunferencia y
# permita calcular el área. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# A = pi * radio^2
# A = Área
# π = Número pi igual a 3.1416
# r = Radio

radio = float(input("Digita el radio de la circunferencia: "))

area = 3.1416 * radio**2

print(f"El area de la circunferencia es: {area}")

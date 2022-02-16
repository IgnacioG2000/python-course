# Escriba un programa que solicite el radio de una circunferencia y permita
# calcular el perímetro. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# L = 2 · π · r
# L = Longitud de perímetro
# π = Número pí igual a 3.1416
# r = Radio


radio = float((input("Digita el radio de la circunferencia: ")))

longitud_circunferencia = 2 * 3.1416 * radio

print(f"La longitud de la circunferencia es: {longitud_circunferencia}")

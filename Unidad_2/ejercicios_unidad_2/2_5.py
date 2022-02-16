# Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de
# utilizar una función, de forma que la operacion se realice dentro de la misma
# Presente el resultado en la terminal del editor.


def area_circunferencia(radio):

    pi = 3.1416

    area = pi * radio**2

    return area


def valor_incrementado(valor):

    valor_aumentado = valor * 1.10

    return valor_aumentado


def longitud_circ(radio):

    pi = 3.1416
    longitud = 2 * pi * radio

    return longitud


radio = float(input("Ingresa el radio del circulo: "))

longitud_circunferencia = longitud_circ(radio)

print(f"La longitud del circulo es: {longitud_circunferencia} ")

area_circunferencia = area_circunferencia(radio)

print(f"El area del circulo es: {area_circunferencia} ")

print("--------------------------------------------------")

valor = float(input("Digita un valor: "))

valor_aumentado = valor_incrementado(valor)

print(f"El valor incrementado en un 10 por ciento es: {valor_aumentado} ")

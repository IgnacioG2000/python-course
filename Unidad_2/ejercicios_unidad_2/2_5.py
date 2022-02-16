# Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de
# utilizar una función, de forma que la operacion se realice dentro de la misma
# Presente el resultado en la terminal del editor.


def area_circunferencia(radio):

    pi = 3.1416

    area = pi * radio**2

    print(area)


def valor_incrementado(valor):

    valor_aumentado = valor * 1.10

    print(valor_aumentado)


def longitud_circ(radio):

    pi = 3.1416
    longitud = 2 * pi * radio

    print(longitud)


radio = float(input("Ingresa el radio del circulo: "))

longitud_circunferencia = longitud_circ(radio)

print("La longitud del circulo es: " + longitud_circunferencia)

area_circunferencia = area_circunferencia(radio)

print("El area del circulo es: " + area_circunferencia)

print("--------------------------------------------------")

valor = int(input("Digita un valor: "))

print("El valor incrementado en un 10 por ciento es: ")

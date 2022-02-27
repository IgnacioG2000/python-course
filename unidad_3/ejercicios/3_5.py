# Suponga que tiene una verdulería y carga la cantidad y el precio de lo
# comprado por un cliente. Realice un programa que tome de a uno la cantidad
# y el precio comprado por el cliente y al finalizar la compra
# retorne el monto total gastado.

valor = input(
    "Para agregar productos, presione i; sino presione cualquier tecla: "
).lower()
total = 0

while valor == "i":
    nombre = input("Digite el nombre de la fruta o verdura: ")
    cantidad = int(input("Digite la cantidad en kg de la fruta o verdura: "))
    precio = int(input("Digite el precio por kg de la fruta o verdura: "))

    total += cantidad * precio

    valor = input(
        "Si quiere agregar mas productos, presione la tecla i;"
        "sino presione cualquier tecla: "
    ).lower()

print(f"El monto total gastado es: {total}")

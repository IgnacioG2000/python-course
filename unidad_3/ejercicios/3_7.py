# A partir del ejercicio 5 cree un programa que vaya agregando en un
# diccionario las compras realizadas.

valor = input(
    "Para agregar productos, presione i; sino presione cualquier tecla: "
).lower()
total = 0
compras = {}

while valor == "i":
    nombre = input("Digite el nombre de la fruta o verdura: ")
    cantidad = int(input("Digite la cantidad en kg de la fruta o verdura: "))
    precio = int(input("Digite el precio por kg de la fruta o verdura: "))

    total += cantidad * precio

    valor = input(
        "Si quiere agregar mas productos, presione la tecla i;"
        "sino presione cualquier tecla: "
    ).lower()

    compras = {
        "nombre": nombre,
        "cantidad_en_kg": cantidad,
        "precio_cada_kg": precio,
    }

print(f"El monto total gastado es: {total}")
print(f"Las compras realizadas son: {compras}")

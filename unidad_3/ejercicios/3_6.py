# A partir del ejercicio 5 cree un programa que vaya agregando en una
# lista las compras realizadas.

valor = input(
    "Para agregar productos, presione i; sino presione cualquier tecla: "
).lower()
total = 0
compras = []

while valor == "i":
    nombre = input("Digite el nombre de la fruta o verdura: ")
    cantidad = int(input("Digite la cantidad en kg de la fruta o verdura: "))
    precio = int(input("Digite el precio por kg de la fruta o verdura: "))

    total += cantidad * precio

    valor = input(
        "Si quiere agregar mas productos, presione la tecla i;"
        "sino presione cualquier tecla: "
    ).lower()

    compras.append([nombre, cantidad, precio])

for x in compras:
    print(f"Producto:{x[0]},Cantidad en kg:{x[1]},Precio por c/ kg:{x[2]}")

print(f"El monto total gastado es: {total}")
print(f"Las compras realizadas son: {compras}")

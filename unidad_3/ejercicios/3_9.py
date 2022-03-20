"""
A partir del ejercicio 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra 
"""

import sys as s
import pprint as pp

iniciar_compra = ""
continuar_comprando = ""
compras = {}
total_gastado = 0
indice = 1


def alta(compras_realizadas, total):

    nombre = input("Digite el nombre de la fruta o verdura: ")
    cantidad = int(input("Digite la cantidad en kg de la fruta o verdura: "))
    precio = int(input("Digite el precio por kg de la fruta o verdura: "))

    total += cantidad * precio

    global indice

    compras_realizadas[indice] = {
        "Producto": nombre,
        "Cantidad": cantidad,
        "Precio": precio,
    }

    indice += 1

    return total


def baja(compras_realizadas, total):  # TODO: poner el id en vez del producto
    index_producto_a_quitar = int(input("Ingresa el indice del producto a eliminar: "))

    if len(compras_realizadas) == 0:
        print("El carrito esta vacio")

    else:
        for compra in compras_realizadas.items():
            if compra[0] == index_producto_a_quitar:
                total -= compra[1]["Precio"]

                del compras_realizadas[1]["Producto"]
                del compras_realizadas[1]["Cantidad"]
                del compras_realizadas[1]["Precio"]
            else:
                print("No esta ese producto en el changuito")

        print(f"Las compras hasta el momento son las siguientes: {compras_realizadas}")

    return total


def consultar(compras_realizadas_local):

    if len(compras_realizadas_local) == 0:
        print("No hay compras hasta el momento")

    else:
        pp.pprint(
            f"Las compras hasta el momento son las siguientes: {compras_realizadas_local}"
        )


def modificar(compras_realizadas_local, total):
    id_producto_a_modificar = int(input("Ingrese el producto a modificar: "))

    if len(compras_realizadas_local) == 0:
        print("El carrito esta vacio")

    else:
        for compra in compras_realizadas_local.items():
            if compra[0] == id_producto_a_modificar:
                producto_nuevo = input("Ingrese el nuevo producto: ")
                cantidad_nueva = int(input("Ingrese la cantidad en kg nueva: "))
                precio_nuevo = int(input("Ingrese el precio por kg: "))

                total = cantidad_nueva * precio_nuevo
                compra[0] = id_producto_a_modificar
                compra[1]["Producto"] = producto_nuevo
                compra[1]["Cantidad"] = cantidad_nueva
                compra[1]["Precio"] = precio_nuevo

            else:
                print("Ese producto no se encuentra en el changuito.")

    return total


def menu():

    print("\t\t\t\t\t******** MENU **********")
    print("\t\t\t\t\t1. Dar de alta una nueva compra")
    print("\t\t\t\t\t2. Dar de baja una compra")
    print("\t\t\t\t\t3. Consultar todas las compras")
    print("\t\t\t\t\t4. Modificar una compra")
    print("\t\t\t\t\t5. Salir")


# -------------------------------------------------------------------------------------#
while iniciar_compra != "Y" and iniciar_compra != "N":
    iniciar_compra = input("Desea iniciar una compra (Y/N): ").upper()

if iniciar_compra == "Y":
    while continuar_comprando != "N":
        menu()
        opcion = int(input("Ingresa la opcion deseada: "))
        if opcion == 1:
            aux = alta(compras, total_gastado)
            total_gastado = aux
        elif opcion == 2:
            aux = baja(compras, total_gastado)
            total_gastado = aux
        elif opcion == 3:
            consultar(compras)
        elif opcion == 4:
            aux = modificar(compras, total_gastado)
            total_gastado = aux
        elif opcion == 5:
            print("Gracias por usar nuestra verduleria")
            continuar_comprando = "N"

    print(f"El total gastado en la compra es de $ {total_gastado}")
    s.exit()
else:
    print("Gracias. Vuelva pronto")
    s.exit()

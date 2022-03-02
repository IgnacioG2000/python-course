"""
A partir del ejercicio 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra 
"""
import sys as s

iniciar_compra = ""
continuar_comprando = ""
compras = []
total_gastado = 0


def alta(compras_realizadas, total):

    nombre = input("Digite el nombre de la fruta o verdura: ")
    cantidad = int(input("Digite la cantidad en kg de la fruta o verdura: "))
    precio = int(input("Digite el precio por kg de la fruta o verdura: "))

    total += cantidad * precio

    compra = [nombre, cantidad, total]
    compras_realizadas.append(compra)

    return total


def baja(compras_realizadas, total):
    producto_a_quitar = input("Ingresa el producto a eliminar: ")

    if compras_realizadas is None:
        print("El carrito esta vacio")

    else:
        for compra in compras_realizadas:
            if compra[0] == producto_a_quitar:
                total -= compra[2]
                compras_realizadas.remove([compra[0], compra[1], compra[2]])
            else:
                print("No esta ese producto en el changuito")

        print("Las compras hasta el momento son las siguientes:")
        index = 0
        for compra in compras_realizadas:
            index += 1
            print(
                f"El producto numero {index} es {compra[0]}, la cantidad es {compra[1]} kg y el precio es $ {compra[2]}\n"
            )

    return total_gastado_local


def consultar(compras_realizadas_local):
    index = 0
    if compras_realizadas_local is None:
        print("No hay compras hasta el momento")

    else:
        print("Las compras hasta el momento son las siguientes:")
        for compra in compras_realizadas_local:
            index += 1
            print(
                f"El producto numero {index} es {compra[0]}, la cantidad es {compra[1]} kg y el precio es $ {compra[2]}\n"
            )


def modificar(compras_realizadas_local, total):
    producto_a_modificar = input("Ingrese el producto a modificar: ")

    if compras_realizadas_local is None:
        print("El carrito esta vacio")

    else:
        for compra in compras_realizadas_local:
            if compra[0] == producto_a_modificar:
                producto_nuevo = input("Ingrese el nuevo producto: ")
                cantidad_nueva = int(input("Ingrese la cantidad en kg nueva: "))
                precio_nuevo = int(input("Ingrese el precio por kg: "))

                total = cantidad_nueva * precio_nuevo
                compra[0] = producto_nuevo
                compra[1] = cantidad_nueva
                compra[2] = total

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

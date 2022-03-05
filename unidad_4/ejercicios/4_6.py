# Cree una función que tome la siguiente lista y reordene de menor a mayor sus
# componentes

# Ordenamiento burbuja
def ordenar_lista(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


lista_numeros = [3, 44, 21, 78, 5, 56, 9]
print("La lista ordenada es:")
print(ordenar_lista(lista_numeros))

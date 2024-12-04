def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    lista = []

    num = input('Nuevo número: ')

    while len(num) != 0:
        lista.append(int(num))
        num = input('Nuevo número: ')

    return lista


def posición_menor(lista, inicio):
    posición_mínimo = inicio

    for i in range(inicio, len(lista)):
        if lista[i] < lista[posición_mínimo]:
            posición_mínimo = i

    return posición_mínimo


def intercambiar(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_lista(lista):
    for i in range(len(lista)):
        índice_menor = posición_menor(lista, i)

        intercambiar(lista, i, índice_menor)


lista = leer_lista_enteros()

print(f'Lista leída: {lista}')
ordenar_lista(lista)
print(f'Lista ordenada: {lista}')

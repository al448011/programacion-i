def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    lista = []

    num = input('Nuevo número: ')

    while len(num) != 0:
        lista.append(int(num))
        num = input('Nuevo número: ')

    return lista


def posición_menor(lista):
    posición_mínimo = 0

    for i in range(len(lista)):
        if lista[i] < lista[posición_mínimo]:
            posición_mínimo = i

    return posición_mínimo


def intercambiar(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


lista = leer_lista_enteros()

if len(lista) == 0:
    print(f'Lista leída: []')
    print(f'Modificada: []')
else:
    posición_menor = posición_menor(lista)
    print(f'Lista leída: {lista}')
    intercambiar(lista, 0, posición_menor)
    print(f'Modificada: {lista}')

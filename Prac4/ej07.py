def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    lista = []

    num = input('Nuevo número: ')

    while len(num) != 0:
        lista.append(int(num))
        num = input('Nuevo número: ')

    return lista


def borrar_elemento(lista, elemento):

    for posición in range(len(lista)-1,-1,-1):
        if lista[posición] == elemento:
            del lista[posición]
            return True

    return False


lista = leer_lista_enteros()

while len(lista) > 0:
    elemento_a_borrar = int(input(f'¿Qué número debo eliminar de {lista}? '))

    if borrar_elemento(lista, elemento_a_borrar) is False:
        print('Número no encontrado')

print('La lista ha quedado vacía')
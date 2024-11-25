def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    lista = []

    num = input('Nuevo número: ')

    while len(num) != 0:
        lista.append(int(num))
        num = input('Nuevo número: ')

    return lista


def borrar_elemento(lista, posición):
    if len(lista) > posición >= 0:
        del lista[posición]
        return True
    else:
        return False


lista = leer_lista_enteros()

while len(lista) > 0:
    posición = int(input(f'¿Qué posición debo eliminar de {lista}? '))

    if borrar_elemento(lista,posición) is False:
        print('Posición incorrecta')

print('La lista ha quedado vacía')
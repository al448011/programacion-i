def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    lista = []

    num = input('Nuevo número: ')

    while len(num) != 0:
        lista.append(int(num))
        num = input('Nuevo número: ')

    return lista

def repetidos_lista(lista):

    veces_repetido = 0
    lista_repetidos = []

    for elemento in lista:
        veces_repetido = 0
        for i in range(len(lista)):
            if elemento == lista[i]:
                veces_repetido += 1
        if veces_repetido >= 2 and elemento not in lista_repetidos:
            lista_repetidos += [elemento]

    return lista_repetidos

def suma_lista(lista):
    suma = 0

    for elemtento in lista:
        suma += elemtento

    return suma

lista = leer_lista_enteros()
lista_repetidos = repetidos_lista(lista)
suma_repetidos = suma_lista(lista_repetidos)

print(f'Números leídos más de una vez (suman {suma_repetidos}): {lista_repetidos}')
print(f'Todos los números leídos: {lista}')

def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    lista = []

    num = input('Nuevo número: ')

    while len(num) != 0:
        lista.append(int(num))
        num = input('Nuevo número: ')

    return lista


lista = leer_lista_enteros()
lista_cuadrados = []

for elemento in lista:
    cuadrado = elemento ** 2
    lista_cuadrados.append(cuadrado)

print(f'Cuadrados de los números leídos: {lista_cuadrados}')
print(f'Números leídos: {lista}')
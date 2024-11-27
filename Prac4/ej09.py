def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    lista = []

    num = input('Nuevo número: ')

    while len(num) != 0:
        lista.append(int(num))
        num = input('Nuevo número: ')

    return lista


lista = leer_lista_enteros()
print(f'Lista leída: {lista}')

print('Ve contestando con números enteros, o con una cadena vacía para acabar...')
buscar_suma = input('¿Qué suma he de buscar en dos posiciones consecutivas? ')

while len(buscar_suma) != 0:

    for i in range(len(lista) - 1):
        if lista[i] + lista[i + 1] == int(buscar_suma):
            print(f'{lista[i]} + {lista[i + 1]} = {buscar_suma}')

    buscar_suma = input('¿Qué suma he de buscar en dos posiciones consecutivas? ')

print('¡Adiós!')
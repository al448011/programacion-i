def leer_alturas():
    print('Ve introduciendo alturas sobre el nivel del mar, o una cadena vacía para acabar...')

    lista_alturas = []
    km = 0
    altura = input(f'Altura en metros en el punto kilométrico {km}: ')

    while len(altura) != 0:
        lista_alturas += [int(altura)]
        km += 1

        altura = input(f'Altura en metros en el punto kilométrico {km}: ')

    return lista_alturas


def mostrar_tramos_subida(lista_alturas):
    desniveles = []

    for i in range(1, len(lista_alturas)):
        dif_alturas = lista_alturas[i] - lista_alturas[i - 1]
        desniveles += [dif_alturas]

    desnivel_max = desniveles[0]

    for i in range(len(desniveles)):
        if desniveles[i] >= desnivel_max:
            desnivel_max = desniveles[i]

    longitud = 0
    comienzo = 0
    tramo = 0
    desnivel = 0

    for i in range(len(desniveles)):
        if desniveles[i] > 0:
            longitud += 1
            desnivel += desniveles[i]
        else:
            if longitud > 0:
                tramo += 1
                mostrar_tramos(tramo, comienzo, longitud, desnivel)
            comienzo = i + 1
            longitud = 0
            desnivel = 0

    if desnivel_max <= 0:
        print('Ningún kilómetro es de subida')
    if longitud > 0:
        tramo += 1
        mostrar_tramos(tramo, comienzo, longitud, desnivel)


def mostrar_tramos(num_tramo, inicio, longitud, desnivel):
    print(f'Tramo de subida número {num_tramo}:')
    print(f'\tEntre los puntos kilométricos {inicio} y {inicio + longitud}')
    print(f'\tLongitud de {longitud} km')
    print(f'\tDesnivel de {desnivel} m')


lista_alturas = leer_alturas()

if len(lista_alturas) <= 1:
    print('Recorrido no válido, con menos de dos puntos')
else:
    print(f'Lista de alturas: {lista_alturas}')
    mostrar_tramos_subida(lista_alturas)

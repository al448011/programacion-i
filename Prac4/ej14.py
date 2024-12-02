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


def calcular_desniveles(lista_alturas):
    lista_dif_alturas = []

    for i in range(1, len(lista_alturas)):
        dif_alturas = lista_alturas[i] - lista_alturas[i - 1]
        lista_dif_alturas += [dif_alturas]

    return lista_dif_alturas


def posición_máximo(lista):
    desnivel_max = lista[0]
    km = 0

    for i in range(len(lista)):
        if lista[i] >= desnivel_max:
            desnivel_max = lista[i]
            km = i

    if desnivel_max <= 0:
        return None

    return km


lista_alturas = leer_alturas()

if len(lista_alturas) > 1:

    lista_desniveles = calcular_desniveles(lista_alturas)
    desnivel_max = posición_máximo(lista_desniveles)

    print(f'Lista de alturas: {lista_alturas}')
    print(f'Lista de desniveles: {lista_desniveles}')

    if desnivel_max is None:
        print('Ningún kilómetro es de subida')
    else:
        print('Kilómetro con mayor desnivel de subida:')
        print(f'Entre los puntos kilométricos {desnivel_max} y {desnivel_max + 1}')
        print(f'Desnivel de {lista_desniveles[desnivel_max]} m')
else:
    print('Recorrido no válido, con menos de dos puntos')
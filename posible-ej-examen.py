# ola_de_frio.py

# Almacenamos en una lista las temperaturas medias de cada dia durante un
# periodo de tiempo. Se considera una ola de frio a una secuencia de dias en
# Los que la temperatura media es negativa. Contamos los días asi: 8, 1, 2, ...
# Pretendemos encontrar el día en el que comienza la ola de fria más larga A
# y su duración en días.

def ola_frio_mas_larga(temperaturas):

    comienzo = 0
    longitud = 0

    comienzo_max = 0
    longitud_max = 0

    for i in range(len(temperaturas)):
        if temperaturas[i] < 0:
            longitud += 1
        else:
#            if longitud > 0:
#                print(f'{comienzo = }, {longitud = }')  # es equivalente a --> print(f'comienzo = {comienzo}')
            comienzo = i + 1
            longitud = 0

            if longitud > longitud_max:
                longitud_max = longitud
                comienzo_max = comienzo

#    if longitud > 0:
#       print(f'{comienzo = }, {longitud = }')  # es equivalente a --> print(f'comienzo = {comienzo}')

    if longitud > longitud_max:
        longitud_max = longitud
        comienzo_max = comienzo

    return [comienzo_max, longitud_max]

enero = [8, -5, -3, -1, 2, -1, -1, -3, -5, 2, 3, -1, -5, -7]

[dia, longitud] = ola_frio_mas_larga(enero)

print(f'La ola de frío más larga empezó el día {dia} y duró {longitud} días.')
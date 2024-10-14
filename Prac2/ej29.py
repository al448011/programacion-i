n = float(input('Introduce un número: '))

minimo = n

if n < 0:
    print('No se han introducido datos')
else:
    while n >= 0:
        n = float(input('Introduce otro número: '))
        if (n >= 0) and n < minimo:
            minimo = n

    print(f'Mínimo: {minimo}')
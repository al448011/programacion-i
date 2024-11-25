n = float(input('Introduce un número: '))

cont = 0
suma = n

if n < 0:
    print('No se han introducido datos')
else:
    while n >= 0:
        n = float(input('Introduce otro número: '))
        cont += 1
        if n > 0:
            suma += n

    print(f'Media: {suma/cont}')
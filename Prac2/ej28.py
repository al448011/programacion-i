n = float(input('Introduce un número: '))

maximo = n

if n < 0:
    print('No se han introducido datos')
else:
    while n >= 0:
        n = float(input('Introduce otro número: '))
        if n > maximo:
            maximo = n

    print(f'Máximo: {maximo}')
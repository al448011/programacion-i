n = float(input('Introduce un número: '))

suma = n
cont = 1
minimo = n
maximo = n

if n < 0:
    print('No se han introducido datos')
else:
    while n >= 0:
        n = float(input('Introduce otro número: '))
        if n >= 0:
            suma += n
            cont += 1
            if n > maximo:
                maximo = n
            if n < minimo:
                minimo = n

    print(f'Media: {suma/cont}\nMínimo: {minimo}\nMáximo: {maximo}')
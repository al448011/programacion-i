n = int(input('Introduce un número entero: '))

print(f'Los {n} primeros números primos son: ', end=' ')

cont_n = 1
contNumeros = 1

while cont_n <= n:
    cont = 1
    cont_divisores = 0

    while cont <= contNumeros:
        if contNumeros % cont == 0:
            cont_divisores += 1
        cont += 1

    if cont_divisores == 2:
        print(f'{contNumeros}', end=' ')
        cont_n += 1

    contNumeros += 1
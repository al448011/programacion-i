n = int(input('Introduce un número entero: '))

print(f'Los números primos menores que {n} son: ', end=' ')

for i in range(1,n):

    cont = 1
    cont_divisores = 0

    while cont <= i:
        if i % cont == 0:
            cont_divisores += 1
        cont += 1

    if cont_divisores == 2:
        print(f'{i}', end=' ')
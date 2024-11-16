n = int(input('Introduce un número entero: '))

print(f'Los {n} primeros números abundantes son:', end=' ')

cont_abundantes = 0
cont = 0

while cont_abundantes < n:
    suma_divisores = 0

    for divisor in range(1,cont):
        if cont % divisor == 0:
            suma_divisores += divisor

    if suma_divisores > cont:
        print(f'{cont}', end=' ')
        cont_abundantes += 1

    cont += 1
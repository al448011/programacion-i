def sumar_divisores_propios(n):
    suma_divisores = 0

    for divisor in range(1, n):
        if n % divisor == 0:
            suma_divisores += divisor

    return suma_divisores

def es_abundante(n):
    return sumar_divisores_propios(n) > n

n = int(input('Introduce un número entero: '))

print(f'Los {n} primeros números abundantes son:', end=' ')

cont_abundantes = 0
cont = 0

while cont_abundantes < n:
    if es_abundante(cont):
        print(f'{cont}', end=' ')
        cont_abundantes += 1

    cont += 1
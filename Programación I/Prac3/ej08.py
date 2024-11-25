def sumar_divisores_propios(n):
    suma_divisores = 0

    for divisor in range(1, n):
        if n % divisor == 0:
            suma_divisores += divisor

    return suma_divisores

def es_abundante(n):
    """
    if sumar_divisores_propios(n) > n:
        return True
    else:
        return False
    """
    return sumar_divisores_propios(n) > n


n = int(input('Introduce un número entero: '))
print(f'Los números abundantes menores que {n} son:', end=' ')

for i in range(1, n):
    sumar_divisores_propios(i)

    if es_abundante(i):
        print(f'{i}', end=' ')
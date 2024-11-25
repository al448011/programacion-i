n = int(input('Introduce un número entero: '))

print(f'Los números abundantes menores que {n} son: ', end=' ')
contNumAbundante = 0
cont = 0

for i in range(1, n):
    sumaDivisores = 0

    for divisores in range(1,i):
        if i % divisores == 0:
            sumaDivisores += divisores

    if sumaDivisores > i:
        print(f'{i}',end=' ')
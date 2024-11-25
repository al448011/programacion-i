n = int(input('Introduce un número entero: '))

num_mayor = 0
num_divisores_mayor = 0

for i in range(1, n+1):
    cont = 1
    num_divisores = 0

    while cont <= n:
        if i % cont == 0:
            num_divisores += 1
        cont += 1
    if num_divisores >= num_divisores_mayor:
        num_divisores_mayor = num_divisores
        num_mayor = i

print(f'El número con más divisores es {num_mayor} ({num_divisores_mayor} divisores)')
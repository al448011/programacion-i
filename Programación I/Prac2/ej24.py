n = int(input('Introduce un número entero: '))

cont = 1
divisores = 0

while cont <= n:
    if n % cont == 0:
        divisores += 1
    cont += 1

print(f'El número {n} tiene {divisores} divisores')
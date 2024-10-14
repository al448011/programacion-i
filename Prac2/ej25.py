n = int(input('Introduce un número entero: '))

cont = 1
sumaDivisores = 0

while cont <= n:
    if n % cont == 0:
        sumaDivisores += cont
    cont += 1

print(f'La suma de los divisores de {n} es {sumaDivisores}')
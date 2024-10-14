n = int(input('Introduce un número entero: '))

cont = 1

while cont <= n:
    factorial = 1
    for i in range(1, cont+1):
        factorial = factorial * i

    print(f'{cont}! = {factorial}')
    cont += 1
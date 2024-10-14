n = int(input('Introduce un número entero: '))

if n%2 != 0:
    n -= 1

cont = 2

while cont <= n:
    print(cont)
    cont += 2
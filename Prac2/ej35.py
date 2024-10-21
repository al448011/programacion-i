n = int(input('Introduce un número entero: '))

factorial = 1
i = 1

while True:
    factorial *= i

    if factorial > n:
        break

    i += 1

print(f'El número buscado es {i} ({i-1}! <= {n} < {i}!)')
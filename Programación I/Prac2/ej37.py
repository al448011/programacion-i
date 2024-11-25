n = int(input('Introduce un número entero: '))

print(f'Los {n} primeros números de Fibonacci son: 1 1', end=' ')

num1 = 1
num2 = 1
suma = 1

for i in range(2,n):
    suma = num1 + num2
    num1 = num2
    num2 = suma
    print(f'{suma}', end=' ')
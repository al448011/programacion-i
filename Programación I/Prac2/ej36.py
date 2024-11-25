n = int(input('Introduce un número entero: '))

num1 = 1
num2 = 1
suma = 1

if n != 1 or n != 2:
    for i in range(2,n):
        suma = num1 + num2
        num1 = num2
        num2 = suma

print(f'Fibonacci({n}) = {suma}')
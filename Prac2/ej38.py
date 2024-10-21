n = int(input('Introduce un número entero: '))

num1 = 1
num2 = 1
suma = 1
cont = 2

while suma <= n-1:
    suma = num1 + num2
    num1 = num2
    num2 = suma

    cont +=1

if suma == n:
    print(f'El número buscado es {cont}')
else:
    print('No es un número de Fibonacci')
num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))

menor = num1

if num1 < num2:
    print(f'El menor es: {menor}')
else:
    menor = num2
    print(f'El menor es: {menor}')

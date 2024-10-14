num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
num3 = int(input('Introduce el tercer número: '))

if num1 <= num2 and num1 <= num3:
    menor = num1

if num2 <= num1 and num2 <= num3:
    menor = num2

if num3 <= num2 and num3 <= num1:
    menor = num3

print(f'El menor es: {menor}')

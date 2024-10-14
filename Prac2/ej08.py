num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
num3 = int(input('Introduce el tercer número: '))
num4 = int(input('Introduce el cuarto número: '))

if num1 <= num2 and num1 <= num3 and num1 <= num4:
    menor = num1

if num2 <= num1 and num2 <= num3 and num2 <= num4:
    menor = num2

if num3 <= num2 and num3 <= num1 and num3 <= num4:
    menor = num3

if num4 <= num1 and num4 <= num2 and num4 <= num3:
    menor = num4

print(f'El menor es: {menor}')

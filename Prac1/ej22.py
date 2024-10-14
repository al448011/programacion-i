from math import sin

lado1 = int(input('Introduce el primer lado: '))
lado2 = int(input('Introduce el segundo lado: '))
angulo = float(input('Introduce el ángulo (en radianes): '))

area = ((lado1 * lado2) / 2) * sin(angulo)

print(f'El área del triángulo es: {area:.2f}')